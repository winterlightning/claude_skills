from pathlib import Path
import json,sys,time
ROOT=Path(__file__).resolve().parents[3];sys.path.insert(0,str(ROOT))
from icon_set.scripts import primitive_fix as p,work_queue as w
B=Path(__file__).parent;rows=json.loads((B/'staged.json').read_text());runs=json.loads((B/'runs.json').read_text());changes=json.loads((B/'changes.json').read_text())
for n,row in enumerate(rows,1):
 k=row['item']['icon_id'];folder=Path(row['result_dir'])
 if (folder/'result.json').exists():print(n,k,'already finished',flush=True);continue
 for attempt in range(3):
  try:
   rc=p.finish(w.default_base_url(),'thuan-mac',row['key'],'done',changes[k],ray_run=runs[k]['run'])
   if rc:raise RuntimeError('finish refused: '+str(rc))
   print(f'{n}/20 uploaded and done: {k}',flush=True);break
  except Exception as e:
   print(k,type(e).__name__,str(e),flush=True)
   if attempt==2:raise
   time.sleep(1)
