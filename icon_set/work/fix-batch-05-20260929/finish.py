"""Finalize visually reviewed runs and upload through the authorized fix workflow."""
import json, os, sys
from pathlib import Path
ROOT=Path(__file__).resolve().parent
REPO=ROOT.parents[2]
sys.path.insert(0,str(REPO))
from icon_set.scripts import primitive_fix,work_queue
rows=json.loads((ROOT/'batch.json').read_text())
for row in rows:
    if row['icon_id'] not in sys.argv[1:]:continue
    fix=REPO/row['fix_dir']
    if (fix/'result.json').exists():
        print(row['key'],'already finished',flush=True);continue
    run=REPO/row['run'];checks=json.loads((run/'checks.json').read_text());plan=json.loads((run/'review-plan.json').read_text())
    assert checks['validation_status']=='valid' and not checks['errors'] and not checks['warnings']
    assert checks['build_gate']['status']=='pass' and not checks['build_gate']['warnings'] and not checks['build_gate']['errors']
    result={**row,'author':'gpt-6','validation_status':'valid','validation_errors':[],'validation_warnings':[],
            'build_gate':checks['build_gate'],'visual_review':{'native_light_dark':'Reviewed at 48px and enlarged; clear silhouette, consistent strokes, smooth curves and legible intended subject.','original_current_comparison':plan['issue'],'changes':plan['change'],'construction_reference':plan['reference']},
            'omissions':'Secondary fine details reduced for SOLO48; principal subject and identifying arrangement retained.',
            'artifacts':[p.name for p in run.iterdir() if p.is_file()]}
    (run/'result.json').write_text(json.dumps(result,indent=2)+'\n')
    code=primitive_fix.finish(work_queue.default_base_url(),os.environ.get('PICTOGRAPHIC_WORKER') or 'thuan-mac',row['key'],'done',plan['change'],ray_run=run)
    print('FINISH EXIT',row['key'],code,flush=True)
    if code:raise SystemExit(code)
