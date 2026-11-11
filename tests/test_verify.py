"""Regression tests for the bilingual case/gallery publishing contract."""
import importlib.util
from pathlib import Path
import re
import shutil
import tempfile
import unittest

REPOSITORY = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("portfolio_verify", REPOSITORY / "verify.py")
verify = importlib.util.module_from_spec(spec)
spec.loader.exec_module(verify)


class PortfolioContractTests(unittest.TestCase):
    def setUp(self):
        self.directory = tempfile.TemporaryDirectory()
        self.addCleanup(self.directory.cleanup)
        self.fixture = Path(self.directory.name)
        for name in ("index.html", "en.html", "projects.json", "script.js", "style.css", "robots.txt", "sitemap.xml"):
            shutil.copy2(REPOSITORY / name, self.fixture / name)
        shutil.copytree(REPOSITORY / "screens", self.fixture / "screens")
        self.original_root = verify.ROOT
        verify.ROOT = self.fixture
        self.addCleanup(setattr, verify, "ROOT", self.original_root)

    def edit(self, name, change):
        path = self.fixture / name
        path.write_text(change(path.read_text(encoding="utf-8")), encoding="utf-8")

    def test_real_five_case_fixture_passes(self):
        verify.verify()


    def test_missing_escalas_spotlight_is_rejected(self):
        self.edit("index.html", lambda s: re.sub(
            r'<section class="repolens-spotlight escalas-spotlight".*?</section>', "", s, flags=re.S
        ))
        with self.assertRaises(AssertionError):
            verify.verify()

    def test_escalas_missing_admin_validation_disclaimer_is_rejected(self):
        self.edit("en.html", lambda s: s.replace("have not yet been confirmed", "are fully validated"))
        with self.assertRaises(AssertionError):
            verify.verify()

    def test_escalas_incorrect_password_status_is_rejected(self):
        self.edit("index.html", lambda s: s.replace("cadastrada", "não configurada"))
        with self.assertRaises(AssertionError):
            verify.verify()

    def test_escalas_public_app_link_is_rejected(self):
        self.edit("index.html", lambda s: s.replace(
            '<section class="repolens-spotlight escalas-spotlight" id="escalas-medicina"',
            '<section class="repolens-spotlight escalas-spotlight" id="escalas-medicina"'
        ).replace(
            '<h3 id="escalas-medicina-title">',
            '<a href="https://script.google.com/s/mock">Open app</a><h3 id="escalas-medicina-title">'
        ))
        with self.assertRaises(AssertionError):
            verify.verify()

    def test_missing_aulapulse_spotlight_is_rejected(self):
        self.edit("index.html", lambda s: re.sub(
            r'<section class="repolens-spotlight aulapulse-spotlight".*?</section>', "", s, flags=re.S
        ))
        with self.assertRaises(AssertionError):
            verify.verify()

    def test_wrong_aulapulse_live_url_is_rejected(self):
        self.edit("en.html", lambda s: s.replace("https://aulapulse-google-workspace.vercel.app/", "https://example.invalid/"))
        with self.assertRaises(AssertionError):
            verify.verify()

    def test_missing_repolens_spotlight_is_rejected(self):
        self.edit("en.html", lambda s: re.sub(
            r'<section class="repolens-spotlight".*?</section>', "", s, flags=re.S
        ))
        with self.assertRaises(AssertionError):
            verify.verify()

    def test_missing_repolens_evaluation_link_is_rejected(self):
        self.edit("index.html", lambda s: s.replace("GEMINI_RAG_EVALUATION.md", "missing-report.md"))
        with self.assertRaises(AssertionError):
            verify.verify()

    def test_gallery_manifest_mismatch_is_rejected(self):
        self.edit("script.js", lambda s: s.replace("orcaflow-budget.webp", "missing-screen.webp"))
        with self.assertRaises(AssertionError):
            verify.verify()

    def test_missing_english_case_is_rejected(self):
        self.edit("en.html", lambda s: re.sub(r'<article class="case" id="orcaflow">.*?</article>', "", s, flags=re.S))
        with self.assertRaises(AssertionError):
            verify.verify()

    def test_unsafe_new_tab_cta_is_rejected(self):
        self.edit("index.html", lambda s: s.replace('href="https://orcaflow-demo.vercel.app/" target="_blank" rel="noopener noreferrer"', 'href="https://orcaflow-demo.vercel.app/" target="_blank"'))
        with self.assertRaises(AssertionError):
            verify.verify()

    def test_orcaflow_code_link_is_rejected(self):
        self.edit("index.html", lambda s: s.replace('<article class="case" id="orcaflow">', '<article class="case" id="orcaflow"><a href="https://example.invalid/code">Code</a>'))
        with self.assertRaises(AssertionError):
            verify.verify()

    def test_screenshot_above_budget_is_rejected(self):
        path = self.fixture / "screens/orcaflow-landing.webp"
        path.write_bytes(path.read_bytes() + b"x" * 200_000)
        with self.assertRaises(AssertionError):
            verify.verify()


    # --- GoRelay showcase and ATS readability -------------------------------------------

    def reject(self):
        with self.assertRaises(AssertionError):
            verify.verify()

    def test_missing_gorelay_spotlight_is_rejected(self):
        self.edit("index.html", lambda s: re.sub(
            r'<section class="repolens-spotlight gorelay-spotlight".*?</section>', "", s, flags=re.S
        ))
        self.reject()

    def test_gorelay_non_repository_link_is_rejected(self):
        self.edit("en.html", lambda s: s.replace(
            '<h3 id="gorelay-title">', '<a href="https://example.invalid/demo">Demo</a><h3 id="gorelay-title">'
        ))
        self.reject()

    def test_gorelay_without_production_disclaimer_is_rejected(self):
        self.edit("en.html", lambda s: s.replace("not a production service", "ready for production"))
        self.reject()

    def test_gorelay_without_exactly_once_disclaimer_is_rejected(self):
        self.edit("index.html", lambda s: s.replace("Não há alegação de exactly-once, capacidade ou SLA", "Entrega exatamente uma vez garantida"))
        self.reject()

    def test_gorelay_missing_screenshot_is_rejected(self):
        (self.fixture / "screens/gorelay-dashboard.webp").unlink()
        with self.assertRaises((AssertionError, FileNotFoundError)):
            verify.verify()

    def test_gorelay_must_lead_the_showcases(self):
        def move_last(s):
            block = re.search(r'<section class="repolens-spotlight gorelay-spotlight".*?</section>\s*', s, flags=re.S).group(0)
            s = s.replace(block, "")
            return s.replace('<article class="case" id="orcaflow">', block + '<article class="case" id="orcaflow">')
        self.edit("index.html", move_last)
        self.reject()

    def test_word_gluing_line_break_is_rejected(self):
        self.edit("index.html", lambda s: s.replace("Ideias que viram <br>", "Ideias que viram<br>"))
        self.reject()

    def test_missing_go_skill_keyword_is_rejected(self):
        self.edit("en.html", lambda s: s.replace("Go (Golang), ", ""))
        self.reject()

    def test_decorative_arrow_in_contact_link_is_rejected(self):
        self.edit("index.html", lambda s: s.replace(
            '<li><a href="mailto:niskier.rodrigo@gmail.com">niskier.rodrigo@gmail.com</a></li>',
            '<li><a href="mailto:niskier.rodrigo@gmail.com">niskier.rodrigo@gmail.com ↗</a></li>'
        ))
        self.reject()

    def test_missing_social_metadata_is_rejected(self):
        self.edit("en.html", lambda s: s.replace('<meta name="twitter:title"', '<meta name="x-removed"'))
        self.reject()

    def test_json_ld_without_software_project_is_rejected(self):
        self.edit("index.html", lambda s: s.replace('"@type":"SoftwareSourceCode"', '"@type":"CreativeWork"'))
        self.reject()

    def test_sitemap_missing_english_page_is_rejected(self):
        self.edit("sitemap.xml", lambda s: s.replace("<loc>https://rn-dev-portfolio-orcin.vercel.app/en.html</loc>", ""))
        self.reject()

    def test_robots_without_sitemap_is_rejected(self):
        self.edit("robots.txt", lambda s: s.replace("Sitemap:", "# Sitemap:"))
        self.reject()

    def test_print_css_that_hides_spotlight_text_is_rejected(self):
        self.edit("style.css", lambda s: s.replace(".repolens-spotlight{display:block;background:#fff!important;", ".repolens-spotlight-x{display:block;"))
        self.reject()


if __name__ == "__main__":
    unittest.main()
