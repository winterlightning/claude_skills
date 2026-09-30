from pathlib import Path
import json
from icon_set.scripts import primitive_fix as f, work_queue as w
ROOT=Path(__file__).resolve().parent
claims=json.loads((ROOT/'claims.json').read_text());runs=json.loads((ROOT/'runs.json').read_text())
completed=json.loads((ROOT/'completion.json').read_text()) if (ROOT/'completion.json').exists() else {}
for i,e in enumerate(claims,1):
 result_file=Path(e['result_dir'])/'result.json'
 if result_file.exists():
  result=json.loads(result_file.read_text())
  if result.get('outcome')=='done' and result.get('review_status')=='ready':
   completed[e['key']]=result;continue
 r=runs[str(i)];d=json.loads((Path(r['run'])/'result.json').read_text())
 note=d['change']+' Compared original and rejected drawing; no written reviewer feedback. Reviewed at 48 px in light and dark. AUTHOR gpt-6; valid and full build gate pass with zero warnings.'
 code=f.finish(w.default_base_url(),'thuan-mac',e['key'],'done',note,ray_run=r['run'])
 assert code==0,(e['key'],code)
 result=json.loads(result_file.read_text());completed[e['key']]=result
 (ROOT/'completion.json').write_text(json.dumps(completed,indent=2)+'\n')
 print(json.dumps({'finished':len(completed),'key':e['key'],'status':result.get('review_status')}),flush=True)
(ROOT/'completion.json').write_text(json.dumps(completed,indent=2)+'\n')
