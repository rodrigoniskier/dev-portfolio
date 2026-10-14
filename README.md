# Rodrigo Niskier — developer portfolio

Public bilingual portfolio for software development, applied AI, automation, EdTech and HealthTech.

- Portuguese: https://rn-dev-portfolio-orcin.vercel.app/
- English: https://rn-dev-portfolio-orcin.vercel.app/en.html

## ATS / recruiter-friendly structure

The portfolio uses semantic HTML, standard headings, plain-text technical skills, education and professional background, static Portuguese and English pages, language-specific metadata, `hreflang`, JSON-LD Person markup and print-friendly CSS. Critical professional information is not stored only in images or generated dynamically by JavaScript.

## RepoLens AI — featured personal project (v0.2.0)

The bilingual homepages feature **RepoLens AI** as a dedicated text-first spotlight above the existing five gallery cases. No screenshot or online demo is claimed. The public, versioned [repository](https://github.com/rodrigoniskier/repolens-ai), [v0.2.0 source](https://github.com/rodrigoniskier/repolens-ai/tree/v0.2.0) and [generative RAG evaluation report](https://github.com/rodrigoniskier/repolens-ai/blob/v0.2.0/docs/reports/GEMINI_RAG_EVALUATION.md) provide inspectable evidence.

RepoLens AI combines Python/FastAPI, source-code ingestion, chunking, ChromaDB retrieval and Gemini-powered answer generation with references. The published v0.2.0 has 86 passing automated tests, two tagged versions, and eight successful Gemini API calls (one smoke test plus seven evaluation calls). The **live generative evaluation used a lexical HashingEmbedder**, not semantic embeddings; citation validity and lexical claim support are not semantic-accuracy claims.

The static spotlight is accessible in Portuguese and English and requires no external resources or browser JavaScript. The original five screenshot-based projects and their gallery remain unchanged. `verify.py` asserts the evidence links, bilingual wording and separation from hosted demos.

## Selected demos

| Project | Demo | Code |
| --- | --- | --- |
| OrçaFlow — Rodrigo Niskier Lab | https://orcaflow-demo.vercel.app/ | Not published; operational MVP remains local |
| ExamForge AI | https://rn-examforge-demo.vercel.app | https://github.com/rodrigoniskier/ExamForgeAI |
| ClinicalTrack | https://rn-clinicaltrack-demo.vercel.app | https://github.com/rodrigoniskier/ClinicalTrack |
| ServiceFlow | https://rn-serviceflow-demo.vercel.app | https://github.com/rodrigoniskier/ServiceFlow |
| TeamMural | https://rn-teammural-demo.vercel.app | https://github.com/rodrigoniskier/TeamMural |

All demo data is synthetic. ExamForge AI uses simulated AI generation/review in the public demo.

## Development

```bash
python -m http.server 8000
node --check script.js
python verify.py
```

Primary files: `index.html` (Portuguese), `en.html` (English), `style.css`, `script.js`, `projects.json`, and `screens/`.

The repository is intended for static deployment and requires no runtime secrets.

## OrçaFlow case — Issue #1

OrçaFlow — Rodrigo Niskier Lab is the first selected case in both languages.
Its public demo is https://orcaflow-demo.vercel.app/. No private repository link
or code CTA is provided. The other four cases, their images and their demo/code
links are preserved; numbering now runs from 01 to 05.

The **operational MVP is local**: Python/Django 5.2, PostgreSQL 17, per-item
Decimal/ROUND_HALF_UP arithmetic, transactions, relational integrity, tests and
GitHub Actions. The **public site is a separate React/TypeScript/Vite simulation**
with an eight-step tour, fictional data and temporary browser state. It does not
connect to Django or PostgreSQL, send email or persist business changes. Approved
quotes are proposals, not revenue. Vercel delivers the static frontend.

### Screenshot provenance

Two real captures were taken from the public OrçaFlow site on 12/10/2026 using
an isolated Chromium context, without authentication, browser chrome or personal
browser state. Only the fictional public showcase was captured; the operational
Django application was not accessed.

- `screens/orcaflow-landing.webp`: showcase overview, 1363×936, 56,398 bytes.
- `screens/orcaflow-budget.webp`: simulated ORC-01 quote, 1363×936, 44,078 bytes.

The PNG originals were encoded as WebP (quality 82, method 6), with no resizing,
compositing, invented UI or private metadata. Both stay below the verifier's
200,000-byte limit. The demo UI is Portuguese; the English portfolio provides
translated captions and alt text without claiming an English screenshot.

`projects.json`, the static PT/EN cases and the gallery registry in `script.js`
are synchronized. `verify.py` checks five ordered cases, twelve referenced WebP
images, gallery IDs/labels, accessible image/CTA attributes, internal anchors and
the absence of an OrçaFlow code link. It uses only Python's standard library and
Node; no runtime dependencies or credentials were added.

Use `python3 verify.py` on WSL installations without the `python` alias. The
GitHub Actions workflow retains its existing `python verify.py` command.

This change is reviewed through a **Draft PR**. No merge or manual production
deployment is authorized. A branch push may create an automatic Vercel preview;
record that URL/status for review and do not promote it to production.

Verifier regression tests (standard-library `unittest`, no additional packages):

```bash
python3 -m unittest discover -s tests -v
```

These cover bilingual inventory, gallery/manifest mismatches, unsafe demo CTAs,
unwanted OrçaFlow code links and oversized screenshots. The existing CI continues
to run the expanded `verify.py` and `node --check script.js`.

Detailed QA, screenshot provenance, inherited accessibility findings and visual
captures: [OrçaFlow verification](docs/orcaflow-verification.md).
