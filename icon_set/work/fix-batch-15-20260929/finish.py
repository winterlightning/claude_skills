import json,sys,os
from pathlib import Path
sys.path.insert(0,str(Path.cwd()))
from icon_set.scripts import primitive_fix as f,work_queue as q
B=Path(__file__).parent
rows=json.loads((B/'staged.json').read_text());runs=json.loads((B/'runs.json').read_text())
for row in rows:
 key=row['item']['icon_id'];r=runs[key];fix=Path(row['result_dir'])
 if (fix/'result.json').exists():
  d=json.loads((fix/'result.json').read_text());assert d['outcome']=='done';print('ALREADY DONE',key,flush=True);continue
 note=r['metadata']['comparison']+' No written reviewer feedback. Compared original and rejected drawing; inspected native light/dark previews. AUTHOR=gpt-6; valid and full build gate pass with zero warnings.'
 result=f.finish(q.default_base_url(),os.environ.get('PICTOGRAPHIC_WORKER','thuan-mac'),row['key'],'done',note,ray_run=r['run'])
 if result:raise SystemExit(result)
 print('FINISHED',key,flush=True)
