import json,sys,urllib.request
from pathlib import Path
import cairosvg
p=Path(__file__).resolve().parent
ids=json.loads((p/'ids.json').read_text())
i=int(sys.argv[1]);u=ids[i]
data={k:json.load(urllib.request.urlopen('http://localhost:8000/api/primitives/'+k)).get(u) for k in ('status','briefs')}
rows=json.load(urllib.request.urlopen('http://localhost:8000/api/primitives'))
data['catalog']=next(r for r in rows if r['uuid']==u)
(p/f'{i+1:02}-current.json').write_text(json.dumps(data,indent=2))
src=next(Path('pictographic-primitives').rglob('*'+u+'.svg'))
cairosvg.svg2png(url=str(src),write_to=str(p/f'{i+1:02}-reference.png'),output_width=240,output_height=240,background_color="white")
print(json.dumps({'index':i,'uuid':u,'status':data['status'],'catalog':data['catalog'],'family':data['briefs']['family'],'brief':data['briefs']['brief']},indent=2))
