import json,sys,urllib.request,urllib.parse
from pathlib import Path
import cairosvg
W=Path(__file__).parent
IDS="52dc4cf2-c01c-479a-94a1-3ad9cbef9449 6bad0489-febc-4c6d-a02e-bb32765a3240 3bb8a803-55a9-4a2d-a6ac-2586a065ac7f 835a03b0-4d14-4e41-ac37-15d8f7325426 944d0ea3-f712-4093-a262-a9b150fbef6c 7ad20e87-7343-4347-8dd5-6c0cde10087e 5a6bc318-1415-407d-8cee-66dc95d8d15f 1c6d508d-38fb-4b6a-bfe9-e20ebd9e9bf4 29a5a818-9fcd-4062-843c-4ae6c6b33268 abff6337-b854-552e-afe3-b89605887cad".split()
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
