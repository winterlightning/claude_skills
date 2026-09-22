import json,sys
from pathlib import Path
from urllib.request import urlopen
import cairosvg
w=Path(__file__).parent
n=int(sys.argv[1]);u=json.loads((w/'worklist.json').read_text())['uuids'][n-1]
s=json.load(urlopen('http://localhost:8000/api/primitives/status'));b=json.load(urlopen('http://localhost:8000/api/primitives/briefs'))
x={'uuid':u,'status':s.get(u),'brief':b.get(u)}
(w/f'{n:02}-current.json').write_text(json.dumps(x,indent=2));print(json.dumps(x))
p=next(Path('pictographic-primitives').rglob('*'+u+'*.svg'))
cairosvg.svg2png(url=str(p),write_to=str(w/f'{n:02}-reference.png'),output_width=320,output_height=320,background_color='white')
print('Existing originals:',[str(p) for p in Path('icon_set/model/icons/solo').glob('*.py') if u in p.read_text() or u.replace('-','_') in p.name])
