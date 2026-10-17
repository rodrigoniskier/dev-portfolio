"""Verify both static pages, the gallery registry and optimized screenshot assets."""
from html.parser import HTMLParser
from pathlib import Path
import json
import re
import subprocess

ROOT = Path(__file__).resolve().parent
EXPECTED_IDS = ("orcaflow", "examforge", "clinicaltrack", "serviceflow", "teammural")


class PortfolioPage(HTMLParser):
    def __init__(self, source):
        super().__init__()
        self.lang = None
        self.ids = set()
        self.links = []
        self.cases = []
        self.active = None
        self.in_number = False
        self.feed(source)

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == "html":
            self.lang = attrs.get("lang", "")
        if "id" in attrs:
            assert attrs["id"] not in self.ids, f"Duplicate ID: {attrs['id']}"
            self.ids.add(attrs["id"])
        if tag == "article" and "case" in attrs.get("class", "").split():
            self.active = {"id": attrs.get("id"), "links": [], "images": [], "buttons": [], "text": [], "number": None}
            self.cases.append(self.active)
        if tag == "a":
            self.links.append(attrs)
        if self.active is not None:
            if tag == "div" and "case-number" in attrs.get("class", "").split():
                self.in_number = True
            if tag in ("a", "img", "button"):
                self.active[{"a": "links", "img": "images", "button": "buttons"}[tag]].append(attrs)

    def handle_endtag(self, tag):
        if tag == "div" and self.in_number:
            self.in_number = False
        if tag == "article":
            self.active = None

    def handle_data(self, text):
        if self.active is not None:
            self.active["text"].append(text)
            if self.in_number:
                match = re.match(r"\s*(\d{2})", text)
                if match:
                    self.active["number"] = int(match.group(1))


def gallery_registry():
    # Execute the local registry with a minimal DOM stub; no browser or network.
    command = """
const fs = require('node:fs');
const vm = require('node:vm');
const source = fs.readFileSync('script.js', 'utf8');
const result = vm.runInNewContext(source + '\\nJSON.stringify(projects)', {
  document: {getElementById() { return null; }}
});
process.stdout.write(result);
"""
    return json.loads(subprocess.check_output(["node", "-e", command], cwd=ROOT, text=True))


def verify():
    projects = json.loads((ROOT / "projects.json").read_text(encoding="utf-8"))
    gallery = gallery_registry()
    assert tuple(p["id"] for p in projects) == EXPECTED_IDS, "Five ordered projects required"
    assert tuple(p["id"] for p in gallery) == EXPECTED_IDS, "Gallery IDs differ from projects.json"
    images = set()
    for project, registered in zip(projects, gallery):
        assert project["name"] == registered["name"], project["id"]
        assert project["screens"] == registered["screens"], project["id"]
        assert project["screenLabels"] == registered["pt"], project["id"]
        assert len(project["screens"]) == len(registered["en"]) > 0, project["id"]
        if "screenLabelsEn" in project:
            assert project["screenLabelsEn"] == registered["en"], project["id"]
        assert project["screen"] == project["screens"][0], project["id"]
        for name in project["screens"]:
            assert Path(name).name == name and name.endswith(".webp"), name
            data = (ROOT / "screens" / name).read_bytes()
            assert data[:4] == b"RIFF" and data[8:12] == b"WEBP", name
            assert len(data) < 200_000, f"Screenshot exceeds 200 KB: {name}"
            images.add(name)
    assert len(images) == 12, "Twelve referenced screenshots required"
    assert images == {p.name for p in (ROOT / "screens").glob("*.webp")}, "Unreferenced/missing screenshot"
    assert projects[0]["repo"] is None, "OrçaFlow has no public code repository link"
    for filename, language, cta in (("index.html", "pt", "Explorar demonstração"), ("en.html", "en", "Explore demo")):
        source = (ROOT / filename).read_text(encoding="utf-8")
        page = PortfolioPage(source)
        assert page.lang.startswith(language), filename
        assert tuple(case["id"] for case in page.cases) == EXPECTED_IDS, filename
        assert [case["number"] for case in page.cases] == list(range(1, 6)), filename
        for project, case in zip(projects, page.cases):
            assert any(link.get("href") == project["demo"] for link in case["links"]), project["id"]
            assert any(button.get("data-project") == project["id"] and button.get("aria-label") for button in case["buttons"]), project["id"]
            assert len(case["images"]) == 1, project["id"]
            image = case["images"][0]
            assert image["src"] == "screens/" + project["screen"], project["id"]
            assert image.get("alt") and int(image["width"]) > 0 and int(image["height"]) > 0, project["id"]
            assert image.get("loading") == "lazy", project["id"]
        # AulaPulse is a live, separate spotlight; the GitHub source repo is private.
        assert "aulapulse" in page.ids, f"Missing AulaPulse showcase in {filename}"
        aula_marker = '<section class="repolens-spotlight aulapulse-spotlight" id="aulapulse"'
        assert source.count(aula_marker) == 1, filename
        repolens_marker = '<section class="repolens-spotlight" id="repolens"'
        assert repolens_marker in source, f"Missing RepoLens showcase in {filename}"
        assert source.index(aula_marker) < source.index(repolens_marker), filename
        aula = source.split(aula_marker, 1)[1].split("</section>", 1)[0]
        assert 'aria-labelledby="aulapulse-title"' in aula and 'id="aulapulse-title"' in aula, filename
        for evidence in (
            "https://aulapulse-google-workspace.vercel.app/",
            "Google Forms", "Google Sheets", "Google Apps Script",
            "Node.js", "TypeScript", "Gemini API", "Vercel Functions", "22",
            "SHA-256",
        ):
            assert evidence in aula, f"AulaPulse evidence missing in {filename}: {evidence}"
        aula_links = re.findall(r'<a\s[^>]*href="([^"]+)"[^>]*>', aula)
        assert aula_links == ["https://aulapulse-google-workspace.vercel.app/"], filename
        assert "github.com/rodrigoniskier/aulapulse-google-workspace" not in aula, "Private source must not be linked publicly"
        # The RAG showcase is a separate text-first spotlight, not a fictitious live demo.
        assert "repolens" in page.ids, f"Missing RepoLens showcase in {filename}"
        marker = '<section class="repolens-spotlight" id="repolens"'
        assert source.count(marker) == 1, f"Missing/duplicate RepoLens showcase in {filename}"
        assert source.index(marker) < source.index('<article class="case" id="orcaflow">'), filename
        repolens = source.split(marker, 1)[1].split("</section>", 1)[0]
        for required in (
            "https://github.com/rodrigoniskier/repolens-ai",
            "https://github.com/rodrigoniskier/repolens-ai/tree/v0.2.0",
            "GEMINI_RAG_EVALUATION.md",
            "HashingEmbedder",
            "Gemini 3.5 Flash-Lite",
            "86",
        ):
            assert required in repolens, f"RepoLens evidence missing in {filename}: {required}"
        assert "repolens-demo" not in repolens.lower(), "No hosted RepoLens demo exists"
        assert 'aria-labelledby="repolens-title"' in repolens, filename
        assert 'id="repolens-title"' in repolens, filename
        spotlight_links = re.findall(r'<a\s[^>]*href="([^"]+)"[^>]*>', repolens)
        assert len(spotlight_links) == 3, f"Expected three evidence links in {filename}"
        for link in spotlight_links:
            assert link.startswith("https://github.com/rodrigoniskier/repolens-ai"), link

        orcaflow = page.cases[0]
        assert len(orcaflow["links"]) == 1, "OrçaFlow must link only to its public demo"
        link = orcaflow["links"][0]
        assert link["href"] == "https://orcaflow-demo.vercel.app/"
        assert link.get("target") == "_blank" and {"noopener", "noreferrer"} <= set(link.get("rel", "").split())
        text = " ".join(orcaflow["text"])
        assert cta in text and "Decimal/ROUND_HALF_UP" in text and "PostgreSQL 17" in text, filename
        assert "local" in text, filename
        for link in page.links:
            href = link.get("href", "")
            if href.startswith("#") and href != "#":
                assert href[1:] in page.ids, f"Broken anchor in {filename}: {href}"
        assert "<iframe" not in source and "em preparação" not in source, filename
        assert 'mailto:niskier.rodrigo@gmail.com' in source, filename
        assert 'og:image' in source and 'rel="canonical"' in source, filename
    print("Five bilingual gallery cases plus AulaPulse AI and RepoLens AI spotlights, twelve WebP screenshots, metadata, contact and links verified.")


if __name__ == "__main__":
    verify()
