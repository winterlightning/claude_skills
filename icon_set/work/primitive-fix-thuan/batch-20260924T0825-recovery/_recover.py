from pathlib import Path
import json,sys
sys.path.insert(0,str(Path.cwd()))
from icon_set.scripts import work_queue as w,primitive_fix as f
ROOT=Path(__file__).parent
w.TIMEOUT=90
base=w.default_base_url()
print('Reading active claims...',flush=True)
page=w.call(base,'GET','/api/work/review',query={'family':'solo','state':'working','limit':500})
recovered=[{'item':i,'work':i['work']} for i in page['items'] if i['work'].get('worker')=='thuan-mac' and i['work'].get('claimed_at','')>='2026-09-24T08:24']
print('Recovered',len(recovered),[r['item']['key'] for r in recovered],flush=True)
(ROOT/'claim-receipts.json').write_text(json.dumps(recovered,indent=2))
original=w.call
all_claims=list(recovered)
def logged_call(base,method,path,body=None,query=None):
 result=original(base,method,path,body,query)
 if method=='POST' and path=='/api/work/claim':
  all_claims.append(result)
  (ROOT/'claim-receipts.json').write_text(json.dumps(all_claims,indent=2))
  print('Claimed',len(all_claims),result['item']['key'],flush=True)
 return result
w.call=logged_call
if len(recovered)<20:
 claimed,_,_=w.take_next(base,'thuan-mac',family='solo',limit=20-len(recovered),offset=0,reason='bad-stroke')
assert len(all_claims)<=20
# Stage the already-authorized, already-owned claims using the skill's exact staging workflow.
w.take_next=lambda *args,**kwargs:(all_claims,{},None)
started=f.start(base,'thuan-mac',len(all_claims),0,'bad-stroke')
for entry in started:print(f.describe_block(entry['item'],entry['result_dir'],entry['module'],entry['reference']),flush=True)
(ROOT/'staged.json').write_text(json.dumps([{'key':e['key'],'fix':str(e['result_dir']),'ref':str(e['reference']) if e['reference'] else None,'upload_error':e['upload_error']} for e in started],indent=2))
print('Staged',len(started),flush=True)
