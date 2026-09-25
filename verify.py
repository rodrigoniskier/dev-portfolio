"""Check the portfolio's published links and screenshot assets."""
from pathlib import Path
import json
root=Path(__file__).resolve().parent
projects=json.loads((root/'projects.json').read_text())
html=(root/'index.html').read_text()
assert len(projects)==4
for project in projects:
    assert project['demo'] in html
    assert len(project['screens'])==len(project['screenLabels'])
    for name in project['screens']:
        data=(root/'screens'/name).read_bytes()
        assert data[:4]==b'RIFF' and data[8:12]==b'WEBP', name
        assert len(data)<200_000, name
assert '<iframe' not in html
assert 'mailto:niskier.rodrigo@gmail.com' in html
assert 'og:image' in html and 'rel="canonical"' in html
assert 'em preparação' not in html
print('Four live demo links, ten WebP screenshots, metadata and contact verified.')
