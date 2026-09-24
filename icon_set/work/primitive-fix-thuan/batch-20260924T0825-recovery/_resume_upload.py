from pathlib import Path
import json,sys,time
sys.path.insert(0,str(Path.cwd()))
from icon_set.scripts import primitive_fix as f,work_queue as w
ROOT=Path(__file__).parent;rows=json.loads((ROOT/'inputs.json').read_text());w.TIMEOUT=90
original=w.call
log=ROOT/'upload-recovery.jsonl'
def reliable(base,method,path,body=None,query=None):
 for attempt in range(2):
  try:
   result=original(base,method,path,body,query)
   with log.open('a') as out:out.write(json.dumps({'method':method,'path':path,'icon':(body or {}).get('icon'),'response':result})+'\n')
   return result
  except w.ApiError as err:
   work=err.payload.get('work',{}) if isinstance(err.payload,dict) else {}
   if path=='/api/work/done' and err.status==409 and work.get('state')=='done' and work.get('worker')=='thuan-mac' and work.get('svg_sha256')==body.get('svg_sha256') and work.get('note')==body.get('note'):
    # Production confirms that this exact earlier finish succeeded before its response timed out.
    with log.open('a') as out:out.write(json.dumps({'icon':body['icon'],'recovered_finish_receipt':err.payload})+'\n')
    print('Recovered confirmed done receipt',body['icon'],flush=True)
    return {'work':work,'status':'ready'}
   print('API attempt failed',path,(body or {}).get('icon'),err.status,str(err),flush=True)
   if err.status!=0 or attempt==1:raise
   time.sleep(2)
w.call=reliable
for r in rows[15:]:
 if (Path(r['fix'])/'result.json').exists():continue
 result=json.loads((Path(r['run'])/'result.json').read_text())
 print('Finishing',r['key'],flush=True)
 try:
  ret=f.finish(w.default_base_url(),'thuan-mac',r['key'],'done',note='Bad-stroke revision: '+result['plan']+' Valid with zero warnings; visually reviewed at 48px in light and dark.',ray_run=r['run'])
  if ret:print('Refused',r['key'],ret,flush=True)
 except w.ApiError as err:print('Still pending',r['key'],str(err),flush=True)
