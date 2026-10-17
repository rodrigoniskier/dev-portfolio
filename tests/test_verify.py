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
        for name in ("index.html", "en.html", "projects.json", "script.js"):
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


if __name__ == "__main__":
    unittest.main()
