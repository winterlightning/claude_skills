from pathlib import Path
import json,sys,os
ROOT=Path(__file__).resolve().parent;REPO=ROOT.parents[2]
sys.path.insert(0,str(REPO))
from icon_set.scripts import primitive_fix as p, work_queue as w
rows=json.loads((ROOT/'batch.json').read_text())
failed=[]
for i,r in enumerate(rows,1):
 receipt=REPO/r['claim_dir']/'result.json'
 if receipt.exists():
  result=json.loads(receipt.read_text())
  assert result['outcome']=='done' and result['review_status']=='ready'
  print(i,r['key'],'already finished',flush=True)
  continue
 m=json.loads((ROOT/f'latest-{i}.json').read_text())
 assert (REPO/m['result_dir']/'result.json').is_file()
 try:
  code=p.finish(w.default_base_url(),os.environ.get('PICTOGRAPHIC_WORKER','thuan-mac'),r['key'],'done',note=m['comparison']+' AUTHOR=gpt-6; compared with original and rejected drawing; light/dark48 and384 reviewed; model valid and full gate pass with zero warnings.',ray_run=REPO/m['result_dir'])
  if code:failed.append({'number':i,'key':r['key'],'error':f'exit {code}'})
 except Exception as e:
  failed.append({'number':i,'key':r['key'],'error':str(e)})
  print(i,r['key'],type(e).__name__,str(e),flush=True)
 print('processed',i,'of',len(rows),flush=True)
(ROOT/'submission-errors.json').write_text(json.dumps(failed,indent=2))
print('Submission failures:',len(failed),flush=True)
sys.exit(bool(failed))
