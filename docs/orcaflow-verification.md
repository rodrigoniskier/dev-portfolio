# OrçaFlow case — Issue #1 verification

Date: 12/10/2026. Branch: `feat/orcaflow-case`, based on main `e22ba8a`.
The portfolio now has five static cases in Portuguese and English, with OrçaFlow
first. No merge or manual production deployment was performed.

## Executed checks

| Check | Result |
| --- | --- |
| `node --check script.js` | Passed |
| `python3 verify.py` | Five ordered bilingual cases, gallery metadata, twelve WebP images, links and accessibility attributes verified |
| `python3 -m unittest discover -s tests -v` | Six regression tests passed |
| `git diff --check` | Passed |
| Chromium responsive QA | Both pages checked at 320, 375, 768, 1366 and 1440 px; five cases and all primary images loaded; no horizontal overflow |
| Gallery regression | All five projects in PT/EN; 24 screen selections; images and localized labels loaded |
| Keyboard | Demo CTA → gallery button via Tab; gallery via Enter; Escape closes; focus returns to opener |
| OrçaFlow demo CTA | Opens https://orcaflow-demo.vercel.app/ in a new tab; public page and functional CTA visible; `noopener noreferrer` present |
| JavaScript errors | None detected in the portfolio pages |
| axe WCAG A/AA tags 2.0, 2.1 and 2.2 | No violations attributed to the new OrçaFlow case or its CTA in PT/EN at 375 and 1366 px |

## Actual screenshots

The public OrçaFlow overview and quote screenshots were captured in an isolated
Chromium context at 1363×936, without authentication or personal browser state.
Only the public simulation with fictional data was captured. No Django operational
screens, contact details, credentials or browser chrome were included.
The WebP encoding strips EXIF/ICC/XMP and preserves the captured content.

| Asset | Size | SHA-256 |
| --- | --- | --- |
| `screens/orcaflow-landing.webp` | 56,398 bytes | `a26461b6c41ed073d6bd322361f9be1fc42e0955d8e70e01e231babc32ce37d8` |
| `screens/orcaflow-budget.webp` | 44,078 bytes | `56b83b78082e3ba34ce86069a09f4de7e6b03f71804e83b408e2416f4d1b88a0` |

Both are below 200,000 bytes. The English case accurately identifies the captured
UI as Portuguese. The operational Django/PostgreSQL MVP stays local/private;
the public frontend has fictional data and temporary browser state.

Portfolio QA captures, taken from the local checkout:

- [Portuguese desktop](orcaflow-case-pt-desktop.webp)
- [English desktop](orcaflow-case-en-desktop.webp)
- [Portuguese mobile](orcaflow-case-pt-mobile.webp)
- [English mobile](orcaflow-case-en-mobile.webp)

## Scope and inherited findings

The four existing selected-case bodies and their JSON records are unchanged,
except for sequential renumbering from 02 through 05. Their screenshots, demo/code
links and gallery behavior are preserved. No private OrçaFlow repository link is
published. No runtime dependency, credential or Vercel/GitHub setting was added.

Two additive CSS rules were necessary: use one column for the existing “Other
projects” grid below 361 px (it previously overflowed by 6 px at 320), and use an
existing palette color for the new case's small metadata text to meet contrast.
The existing stylesheet rules, typography and palette were retained.

Full-page axe still reports nine inherited color-contrast nodes per page/profile,
all outside the new OrçaFlow case. The same nine nodes were confirmed against the
original main markup at 375 and 1366 px. They are not a new regression and were
not restyled in this focused change. These checks are not a complete WCAG audit;
human screen-reader testing and physical-device QA remain useful.

## Review and delivery

A Draft PR is prepared for owner review. A branch push can create an automatic
Vercel preview; its URL/status should be reported without promoting production.
The existing GitHub Actions workflow continues to check JavaScript syntax and
run the expanded standard-library verifier.

Final review: compare PT/EN copy, inspect the two real screenshots and new case,
exercise the gallery/CTA in the preview, and review the diff before any main merge.
