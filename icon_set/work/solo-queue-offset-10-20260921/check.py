import json, sys
from pathlib import Path
from urllib.request import urlopen
import cairosvg

ROOT = Path(__file__).resolve().parents[3]
OUT = Path(__file__).resolve().parent
IDS = ['e89d9bcb-0e93-4a07-abd4-7740608fbbd7','566c0e57-a142-4e0c-b0fc-b66d54d9dee7','bacf81f7-d345-4811-883f-80c90e127362','8d2595e2-135f-48bd-8886-08c5da475869','c6d7f6d7-a700-4894-830b-9788ba0a2a17','3e406d94-3472-495a-b48a-7dc0d21a13ed','757a7e35-7ab6-4777-857e-44cd9f41831d','9c89e718-df3d-451b-808f-bb9daab2e5b2','e7e9a99a-f549-4a65-b8f6-bb7790c0aab4','d3d86e97-b873-48ff-bd6b-fc4456184a6e']
i = int(sys.argv[1]); uid = IDS[i]
data = {'uuid': uid}
for endpoint in ['status', 'briefs']:
    with urlopen('http://localhost:8000/api/primitives/' + endpoint) as response:
        data[endpoint] = json.load(response).get(uid)
paths = list((ROOT/'pictographic-primitives').glob('*/*' + uid + '.svg'))
data['source_path'] = str(paths[0].relative_to(ROOT)) if paths else None
data['originals'] = [str(p.relative_to(ROOT)) for p in (ROOT/'icon_set/model/icons').glob('**/*'+uid.replace('-','_')+'*.py')]
(OUT/f'{i:02}-state.json').write_text(json.dumps(data, indent=2))
print(json.dumps(data, indent=2))
if paths:
    for size in [48, 320]:
        cairosvg.svg2png(url=str(paths[0]), write_to=str(OUT/f'{i:02}-reference-{size}.png'), output_width=size, output_height=size, background_color="white")
