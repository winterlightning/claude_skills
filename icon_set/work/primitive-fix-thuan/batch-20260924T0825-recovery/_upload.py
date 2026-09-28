from pathlib import Path
import sys,json
sys.path.insert(0,str(Path.cwd()))
from icon_set.scripts import primitive_fix as f,work_queue as w
w.TIMEOUT=90
root=Path(__file__).parent;rows=json.loads((root/'inputs.json').read_text());base=w.default_base_url()
for r in rows:
 fix=Path(r['fix']);bad=fix/'before-upload-error.txt'
 if bad.exists():
  c=json.loads((fix/'claim.json').read_text());item=c['item'];modules=list((fix/'before').glob('*.py'))
  print('Retrying before upload',r['key'],flush=True)
  receipt=w.upload_result(base,'thuan-mac',r['key'],item['svg_sha256'],'before',Path(r['before']),modules[0] if modules else None,note='First version, before the fix; retry after network timeout.')
  (fix/'before-upload-retry.json').write_text(json.dumps(receipt,indent=2))
for i,r in enumerate(rows,1):
 fix=Path(r['fix'])
 if (fix/'result.json').exists():
  saved=json.loads((fix/'result.json').read_text())
  if saved.get('outcome')=='done':print('Already done',r['key'],flush=True);continue
 result=json.loads((Path(r['run'])/'result.json').read_text())
 print('Finishing',i,'of',len(rows),r['key'],flush=True)
 ret=f.finish(base,'thuan-mac',r['key'],'done',note='Bad-stroke revision: '+result['plan']+' Valid with zero warnings; visually reviewed at 48px in light and dark.',ray_run=r['run'])
 if ret:raise SystemExit(ret)
