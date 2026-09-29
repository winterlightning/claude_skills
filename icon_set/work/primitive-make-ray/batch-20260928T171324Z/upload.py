from author_batch import *
from icon_set.scripts import primitive_fix,work_queue
records=json.loads((Path(__file__).parent/'ready-runs.json').read_text())
for r in records:
    fix=ROOT/r['fix_dir']
    if (fix/'result.json').exists():
        prior=json.loads((fix/'result.json').read_text())
        assert prior['outcome']=='done' and prior['make_ray_run']==r['run']
        print('Already finished',r['key'],flush=True)
        continue
    code=primitive_fix.finish(work_queue.default_base_url(),'thuan-mac',r['key'],'done',r['spec']['change']+(' Exact-drawing visual exception authorized by user; automatic findings retained.' if r['accepted_exception'] else ' Full automatic gate passes.'),ray_run=ROOT/r['run'])
    if code:raise RuntimeError((r['key'],code))
    print(f"Finished {r['n']}/20",flush=True)
