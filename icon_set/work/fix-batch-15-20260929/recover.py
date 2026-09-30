from pathlib import Path
import sys,json,os,datetime
sys.path.insert(0,str(Path.cwd()))
from icon_set.scripts import primitive_fix as f,work_queue as w
B=Path(__file__).parent
worker=os.environ.get('PICTOGRAPHIC_WORKER','thuan-mac');base=w.default_base_url()
w.TIMEOUT=90
orig=w.call;claims=json.loads((B/'claims.json').read_text());cache={}
def logged(base,method,path,body=None,query=None):
 stamp=datetime.datetime.now(datetime.timezone.utc).isoformat()
 try:d=orig(base,method,path,body,query)
 except w.ApiError as e:
  if method=='POST' and path=='/api/work/claim' and e.status==0:
   s=orig(base,'GET','/api/work',query={'icon':body['icon']});work=s.get('work') or {}
   if work.get('worker')==worker and work.get('state')=='working' and work.get('claimed_at','')>=stamp:
    d={'item':dict(cache[body['icon']],work=work),'work':work}
   else:raise
  else:raise
 if path=='/api/work/queue':
  for i in d.get('items',[]):cache[i['key']]=i
 if path=='/api/work/claim':
  claims.append(d);(B/'claims.json').write_text(json.dumps(claims,indent=2));print('CLAIM',len(claims),d['item']['key'],flush=True)
 return d
w.call=logged
take=w.take_next
old=list(claims);rows=[]
for claim in old:
 w.take_next=lambda *a,c=claim,**kw:([c],{},None)
 rows+=f.start(base,worker,1,offset=0,max_disapprovals=1,family='solo')
 (B/'staged.json').write_text(json.dumps(rows,default=str,indent=2));print('STAGED',len(rows),flush=True)
w.take_next=take
rows+=f.start(base,worker,20-len(claims),offset=0,max_disapprovals=1,family='solo')
(B/'staged.json').write_text(json.dumps(rows,default=str,indent=2));print('STAGED',len(rows),flush=True)
