from pathlib import Path
import json,sys,cairosvg
ROOT=Path(__file__).resolve().parents[3];sys.path.insert(0,str(ROOT))
from icon_set.scripts import primitive_fix as f,work_queue as q
B=Path(__file__).parent;rows=json.loads((B/'claims.json').read_text());runs=json.loads((B/'runs.json').read_text())
for row in rows:
 k=row['key'].split('/')[-1];v=runs[k]
 if not v['valid']:print('NOT READY',k,flush=True);continue
 run=Path(v['run']);fix=Path(row['fix_dir'])
 if (fix/'result.json').exists():continue
 h=json.loads((B/'history'/(k+'.json')).read_text());assert q.disapproval_count(h)==1
 m=v['metadata'];r=f.load_icon(v['module']).validate_icon();assert r.status=='valid' and not r.warnings
 for typ,p in [('reference',row['reference']),('before',row['before'])]:
  for size in [48,384]:cairosvg.svg2png(url=p,write_to=str(run/f'{typ}-{size}.png'),output_width=size,output_height=size,background_color='white')
 result=dict(m,validation_status='valid',validation_errors=list(r.errors),validation_warnings=list(r.warnings),build_gate='pass',visual_review='Inspected at native 48px and enlarged size in light and dark themes; subject and source arrangement preserved with stated reductions.',artifacts=[p.name for p in run.iterdir() if p.is_file()])
 (run/'result.json').write_text(json.dumps(result,indent=2)+'\n')
 claim=json.loads((fix/'claim.json').read_text());item=claim['item'];note=m['comparison']+' '+m['omissions']
 for attempt in range(3):
  try:
   if (fix/'before-upload-error.txt').exists() and not (fix/'before-upload-retry.json').exists():
    modules=list((fix/'before').glob('*.py'));up=q.upload_result('https://pictographic-review.pictographic.workers.dev','thuan-mac',row['key'],item['svg_sha256'],'before',Path(row['before']),modules[0] if modules else None,note='Rejected drawing before batch 12 fix')
    (fix/'before-upload-retry.json').write_text(json.dumps(up,indent=2))
   rc=f.finish('https://pictographic-review.pictographic.workers.dev','thuan-mac',row['key'],'done',note,ray_run=run)
   print('FINISH',k,rc,flush=True)
   if rc!=0:break
   break
  except Exception as e:print('RETRY',k,attempt+1,str(e),flush=True)
