import json,sys,urllib.request,urllib.parse
from pathlib import Path
import cairosvg
W=Path(__file__).parent
IDS="771cdf79-e59d-4541-bdff-a58073f629be f95af12b-a19b-4e5a-a6ec-10d5dae17560 9046ec78-1a6b-4029-a2e9-be0d10843436 54079a5b-25ea-4346-8fc4-d2b5f8239da0 5fba6994-83b3-4c8e-872d-6f2fc2d663b7 9c2120ce-007e-416d-a659-5f5577147e92 7d6d51d0-8bd7-4f12-a38b-3cc89d83a68b e978c911-6376-4c9f-a6c5-4de2b2acc0b1 97505a77-9794-4383-8806-61bbb128d83e 8f674c71-e41d-4766-9a9e-25a0eb335c94".split()
def get(path):
    with urllib.request.urlopen("http://localhost:8000"+path) as r:return r.read()
i=int(sys.argv[1]);uid=IDS[i]
s=json.loads(get('/api/primitives/status')).get(uid)
b=json.loads(get('/api/primitives/briefs')).get(uid)
rows=json.loads(get('/api/primitives'))
r=next(r for r in rows if r['uuid']==uid)
d={'uuid':uid,'status':s,'brief':b,'row':r}
(W/f'{i:02}-intake.json').write_text(json.dumps(d,indent=2))
print(json.dumps({'uuid':uid,'status':s,'effective':r.get('status'),'family':b.get('family') if b else None,'concept':r.get('concept'),'models':r.get('models')}))
if r.get('status')=='todo':
    raw=get('/primitives/'+urllib.parse.quote(r['path'],safe='/'))
    (W/f'{i:02}-reference.svg').write_bytes(raw)
    cairosvg.svg2png(bytestring=raw,write_to=str(W/f'{i:02}-reference.png'),output_width=288,output_height=288,background_color="white")
