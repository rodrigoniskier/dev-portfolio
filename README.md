# Rodrigo Niskier — developer portfolio

Public bilingual portfolio for software development, applied AI, automation, EdTech and HealthTech.

- Portuguese: https://rn-dev-portfolio-orcin.vercel.app/
- English: https://rn-dev-portfolio-orcin.vercel.app/en.html

## ATS / recruiter-friendly structure

The portfolio uses semantic HTML, standard headings, plain-text technical skills, education and professional background, static Portuguese and English pages, language-specific metadata, `hreflang`, JSON-LD Person markup and print-friendly CSS. Critical professional information is not stored only in images or generated dynamically by JavaScript.

## Escalas de Estágio – Medicina — Google Workspace workflow (2026)

A new Portuguese/English text-first showcase precedes AulaPulse AI and RepoLens AI. This is a real medical internship scheduling workflow developed with **Google Sheets, Google Drive and Google Apps Script**, backed by a private spreadsheet and published as a web app.

- **Problem:** students and coordination staff need a single structured workflow for medical rotation scheduling instead of disparate manual records.
- **Verified inventory:** eight schedules; 1,532 schedule slots imported and checked; four application screens installed; four spreadsheet tabs protected.
- **Architecture:** Google Sheets stores the scheduling matrix in Drive; Google Apps Script exposes a browser-based flow connected to the sheet for schedule reading and input. The application includes student entry fields and a coordination dashboard.
- **Observed checks on 19 Oct 2026:** published app loaded all eight schedules; student fields displayed and empty submissions were blocked. The sheet's Fortaleza time zone and protected tabs were configured.
- **Open acceptance point:** initial administrator password setup and the full admin authentication flow had **not yet been confirmed**. Do not describe this as independently security-audited or fully validated.
- **Privacy:** no spreadsheet identifier, web app deployment URL, student names, credentials, real-data screenshots or internal configuration values are committed or linked from this portfolio. App availability by link does not justify amplifying personal data via an indexed portfolio.
- **Positioning:** applied academic workflow project. No claim of commercial contract, public-source repository, artificial intelligence, automated QA suite or measured productivity gains.

The case demonstrates low-friction process digitization, native Google Workspace integration, application publishing, input validation, spreadsheet tab protection and clear separation of public project documentation from operational academic records. It is independent of the separate ClinicalTrack simulation.

## AulaPulse AI — live Google Workspace + Gemini integration (2026)

The bilingual homepages feature **AulaPulse AI** after Escalas de Estágio – Medicina, followed by RepoLens AI and the five existing screenshot-based gallery projects.

- **Live application:** https://aulapulse-google-workspace.vercel.app/ (public browser access verified by the project owner).
- **Problem:** academic feedback is frequently collected but not consolidated into actionable module-level indicators.
- **Event-driven integration:** Google Forms → Google Sheets → Google Apps Script (installable submission triggers, validation, SHA-256 deterministic deduplication and idempotent consolidation).
- **Full stack:** Node.js/TypeScript REST API with Vercel Functions, a responsive dashboard and a server-side Gemini API call for pedagogical synthesis. Demo mode uses synthetic data; live mode reads authenticated Apps Script data through the server.
- **Validation:** the owner manually verified an incognito browser visit, one fictional form submission reflected in the dashboard and a successful Gemini synthesis using the production API key. Separately, CI passes on Node.js 22/24 with 22 automated tests and a dependency audit reporting zero vulnerabilities.
- **Portfolio positioning:** independently developed personal MVP; not a client contract. The source repository remains **private**; no public code link is advertised. The private Google Sheets and API credentials are never embedded in the portfolio.

**New technologies emphasized relative to other featured projects:** Google Forms, Google Sheets, Apps Script triggers, cross-service event-driven automation and server-side Vercel Functions. React/TypeScript, GitHub Actions and Gemini API already appeared in OrçaFlow or RepoLens AI; AulaPulse demonstrates their integration with a working Google Workspace data pipeline.

## RepoLens AI — featured personal project (v0.2.0)

The bilingual homepages feature **RepoLens AI** as a dedicated text-first spotlight after AulaPulse AI and above the existing five gallery cases. No screenshot or online demo is claimed. The public, versioned [repository](https://github.com/rodrigoniskier/repolens-ai), [v0.2.0 source](https://github.com/rodrigoniskier/repolens-ai/tree/v0.2.0) and [generative RAG evaluation report](https://github.com/rodrigoniskier/repolens-ai/blob/v0.2.0/docs/reports/GEMINI_RAG_EVALUATION.md) provide inspectable evidence.

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
