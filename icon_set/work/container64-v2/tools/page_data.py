"""Collect v1/v2 path data + report rows into page-data.json for the review page."""
import json, re, subprocess
from pathlib import Path
ROOT = Path('.')
W = ROOT / 'icon_set/work/container64-v2'
report = json.loads((W / 'report.json').read_text())
rows = []
def paths(svg):
    return [d for d in re.findall(r' d="([^"]+)"', svg)]
for iid, row in sorted(report.items()):
    v1 = subprocess.run(['git', 'show', f'HEAD:published/container64/{iid}.svg'], capture_output=True, text=True, check=True).stdout
    v2 = (ROOT / 'published/container64' / f'{iid}.svg').read_text()
    rows.append({'id': iid, 'from': row.get('from'), 'to': row.get('to'), 'status': row['status'],
                 'stage': row.get('stage', 'auto-fit'), 'repair': row.get('repair', ''),
                 'notes': row.get('notes', []), 'v1': paths(v1), 'v2': paths(v2)})
(W / 'page-data.json').write_text(json.dumps(rows, separators=(',', ':')))
print(len(rows), 'rows')
