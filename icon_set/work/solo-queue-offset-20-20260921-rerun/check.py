import json,urllib.request,sys,cairosvg
from pathlib import Path
p=Path(__file__).parent
n=int(sys.argv[1]);u=json.loads((p/'source-uuids.json').read_text())[n]
a={k:json.load(urllib.request.urlopen('http://localhost:8000/api/primitives/'+k)).get(u) for k in ['status','briefs']}
(p/(u+'.json')).write_text(json.dumps(a,indent=2));print(json.dumps(a))
s=next(Path('pictographic-primitives').rglob('*'+u+'*.svg'))
cairosvg.svg2png(url=str(s),write_to=str(p/f'reference-{n}.png'),output_width=256,output_height=256,background_color='white')
