import json,sys,urllib.request,urllib.parse
from pathlib import Path
import cairosvg
W=Path(__file__).parent
IDS="f422872b-42cf-4b74-aa1f-bf870f557d7a c2caf72a-e028-4b0f-9d4f-ea1a841b97bb 602f9a81-4306-4859-94c6-dc6f92e2061c 407c218e-c29c-4f30-b87f-c44424fce8df 46622ecc-42b6-4d7f-b812-d85bb3ec076e 1a8ec40b-c5b8-4694-afaf-5baadb4972ad 1d983437-28d4-4d9e-8147-91158ea165bf f1449e0a-c5a1-4ede-806c-ca36de940e2c ed60c884-6e26-4a90-9170-23473b0ad667 79dff51d-7a09-497d-8df1-de4b77d03e31".split()
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
