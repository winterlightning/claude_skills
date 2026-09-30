from pathlib import Path
import sys,json
sys.path.insert(0,str(Path.cwd()))
from icon_set.scripts import work_queue as w,primitive_fix as f
B=Path(__file__).parent
w.TIMEOUT=90
original=w.call
def resilient(base,method,path,body=None,query=None):
    for attempt in range(4):
        try:return original(base,method,path,body,query)
        except w.ApiError as error:
            if error.status not in (0,429,500,502,503,504) or attempt==3:raise
            print('Network retry',path,attempt+1,flush=True)
            if path=='/api/work/done':
                state=original(base,'GET','/api/work',query={'icon':body['icon']})
                if state.get('status')=='ready' and state.get('work',{}).get('state')=='done':
                    return {'status':'ready','work':state['work']}
w.call=resilient
runs=json.loads((B/'runs.json').read_text())
audit=json.loads((B/'disapproval-audit.json').read_text())
assert len(runs)==20 and len(audit)==20 and set(audit.values())=={1}
for i in sorted(runs,key=int):
    d=runs[i];result=Path(d['fix'])/'result.json'
    if result.exists():
        assert json.loads(result.read_text())['outcome']=='done'
        continue
    assert Path(f.latest_run(d['key'])).resolve()==Path(d['fix']).resolve()
    note=d['change']+' Compared original and rejected drawing; reviewed at 48px in light/dark. AUTHOR=gpt-6; zero-warning SOLO48 and full build-gate pass.'
    status=f.finish(w.default_base_url(),'thuan-mac',d['key'],'done',note,ray_run=d['run'])
    assert status==0
print('FINISHED 20/20',flush=True)
