from pathlib import Path
import sys,json,datetime
ROOT=Path(__file__).resolve().parents[3];sys.path.insert(0,str(ROOT))
from icon_set.scripts import primitive_fix as f,work_queue as q
B=Path(__file__).parent
orig=q.call;take=q.take_next;cache={};new=[]
def logged(base,method,path,body=None,query=None):
 stamp=datetime.datetime.now(datetime.timezone.utc).isoformat()
 for retry in range(3 if method=='GET' else 1):
  try:
   d=orig(base,method,path,body,query)
   if path=='/api/work/queue':
    for i in d.get('items',[]):cache[i['key']]=i
   if path=='/api/work/claim':new.append(d);(B/'new-claims.json').write_text(json.dumps(new,indent=2));print('CLAIMED',d['icon'],flush=True)
   return d
  except q.ApiError as e:
   if method=='POST' and path=='/api/work/claim' and e.status==0:
    s=orig(base,'GET','/api/work',query={'icon':body['icon']})
    w=s.get('work') or {}
    if w.get('state')=='working' and w.get('worker')==body['worker'] and w.get('claimed_at','')>=stamp:
     i=dict(cache[body['icon']],work=w);d={'item':i,'work':w,'icon':body['icon'],'svg_sha256':body['svg_sha256'],'saved':True,'recovered_after_timeout':True};new.append(d);(B/'new-claims.json').write_text(json.dumps(new,indent=2));return d
   if method!='GET' or retry==2:raise
q.call=logged
old=json.loads((B/'recovered-claims.json').read_text())
q.take_next=lambda *args,**kw:(old,{},None)
a=f.start(q.default_base_url(),'thuan-mac',11,max_disapprovals=1,family='solo')
(B/'staged.json').write_text(json.dumps(a,default=str,indent=2));print('STAGED RECOVERED 11',flush=True)
q.take_next=take
b=f.start(q.default_base_url(),'thuan-mac',9,offset=0,max_disapprovals=1,family='solo')
a+=b
(B/'staged.json').write_text(json.dumps(a,default=str,indent=2))
assert len(a)==20
for x in a:print(f.describe_block(x['item'],Path(x['result_dir']),x['module'],x.get('reference')),flush=True)
print('STAGED 20 TOTAL',flush=True)
