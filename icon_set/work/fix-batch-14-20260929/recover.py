from pathlib import Path
import json,sys,os
sys.path.insert(0,str(Path.cwd()))
from icon_set.scripts import primitive_fix as f,work_queue as q
B=Path(__file__).parent
worker=os.environ.get('PICTOGRAPHIC_WORKER','thuan-mac');base=q.default_base_url()
q.TIMEOUT=90
original=q.call
# Persist each acknowledged new claim so transport errors cannot lose batch membership.
new=[]
def logged(base,method,path,body=None,query=None):
 d=original(base,method,path,body,query)
 if path=='/api/work/claim':
  new.append(d);(B/'new-claims.json').write_text(json.dumps(new,indent=2));print('CLAIM',d['item']['key'],flush=True)
 return d
q.call=logged
old=json.loads((B/'recovered-claims.json').read_text())
take=q.take_next
rows=[]
for c in old:
 q.take_next=lambda *a, c=c, **kw:([c],{},None)
 staged=f.start(base,worker,1,max_disapprovals=1,family='solo')
 rows+=staged;(B/'staged.json').write_text(json.dumps(rows,default=str,indent=2));print('STAGED',c['item']['key'],flush=True)
q.take_next=take
rows+=f.start(base,worker,5,offset=0,max_disapprovals=1,family='solo')
(B/'staged.json').write_text(json.dumps(rows,default=str,indent=2))
print('TOTAL',len(rows),flush=True)
