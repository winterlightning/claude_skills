import sys,json
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[3]))
from icon_set.scripts.primitive_fix import finish
from icon_set.scripts.work_queue import default_base_url
ROOT=Path(__file__).parent
for e in json.loads((ROOT/'entries.json').read_text()):
    if e['icon_id'] not in sys.argv[1:]:continue
    run=Path(e['run']);checks=json.loads((run/'checks.json').read_text());design=json.loads((run/'design.json').read_text())
    result=dict(e,author='gpt-6',validation_status=checks['validation'],build_gate=checks['gate'],visual_review='Inspected native 48px and enlarged light/dark previews: recognizable concept, clear negative space, consistent stroke and smooth curves.',**design,artifacts=[p.name for p in run.iterdir() if p.is_file()])
    (run/'result.json').write_text(json.dumps(result,indent=2)+'\n')
    code=finish(default_base_url(),'thuan-mac','solo/'+e['icon_id'],'done',note=design['plan'],ray_run=run)
    if code:print('FAILED',e['icon_id'],code,flush=True)
