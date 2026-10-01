# Rodrigo Niskier — developer portfolio

Public bilingual portfolio for software development, applied AI, automation, EdTech and HealthTech.

- Portuguese: https://rn-dev-portfolio-orcin.vercel.app/
- English: https://rn-dev-portfolio-orcin.vercel.app/en.html

## ATS / recruiter-friendly structure

The portfolio uses semantic HTML, standard headings, plain-text technical skills, education and professional background, static Portuguese and English pages, language-specific metadata, `hreflang`, JSON-LD Person markup and print-friendly CSS. Critical professional information is not stored only in images or generated dynamically by JavaScript.

## Selected demos

| Project | Demo | Code |
| --- | --- | --- |
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
