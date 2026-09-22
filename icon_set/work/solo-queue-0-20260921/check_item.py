import json,sys,urllib.request
from pathlib import Path
import cairosvg
w=Path(__file__).resolve().parent
u=json.loads((w/'worklist.json').read_text())['uuids'][int(sys.argv[1])]
for endpoint in ['status','briefs']:
 data=json.load(urllib.request.urlopen('http://localhost:8000/api/primitives/'+endpoint))
 saved=data.get(u)
 (w/(u+'-'+endpoint+'.json')).write_text(json.dumps(saved,indent=2))
 print(endpoint,json.dumps(saved))
p=next(Path('pictographic-primitives').rglob('*'+u+'*.svg'))
cairosvg.svg2png(url=str(p),write_to=str(w/'reference.png'),output_width=384,output_height=384,background_color='white')
print('SOURCE',p)
