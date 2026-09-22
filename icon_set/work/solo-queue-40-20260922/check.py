import json, sys
from pathlib import Path
from urllib.request import urlopen
import cairosvg

root = Path(__file__).parent
items = json.loads((root / 'queue.json').read_text())['briefs']
for n in map(int, sys.argv[1:]):
    item = items[n-1]
    uid = item['uuid']
    def get(path):
        with urlopen('http://localhost:8000' + path) as response:
            return response.read()
    status = json.loads(get('/api/primitives/status')).get(uid)
    brief = json.loads(get('/api/primitives/briefs')).get(uid)
    rows = json.loads(get('/api/primitives'))
    row = next(r for r in rows if r['uuid'] == uid)
    data = {'uuid': uid, 'status': status, 'brief': brief, 'row': row}
    (root / f'{n:02}-current.json').write_text(json.dumps(data, indent=2))
    print(json.dumps({'index': n, 'uuid':uid, 'status':status, 'family':brief.get('family'), 'effective':row.get('status'), 'models':row.get('models')}))
    if row.get('status') == 'todo' and brief.get('family') == 'solo':
        raw = get(item['reference_url'])
        (root / f'{n:02}-reference.svg').write_bytes(raw)
        cairosvg.svg2png(bytestring=raw, write_to=str(root / f'{n:02}-reference.png'), output_width=320, output_height=320, background_color='white')
