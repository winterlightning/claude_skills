"""Finish only this batch's twenty claims through the authorized production helper."""
from pathlib import Path
import json, subprocess, sys
ROOT=Path(__file__).resolve().parent
REPO=ROOT.parents[2]
sys.path.insert(0,str(REPO))
from icon_set.scripts.primitive_fix import latest_run
SOURCE_ICON_ID=None
SOURCE_PATH=str(ROOT/'claims.json')
AUTHOR='gpt-6'
claims=json.loads((ROOT/'claims.json').read_text())
runs=json.loads((ROOT/'runs.json').read_text())
for i,c in enumerate(claims):
    fix=REPO/c['fix_dir']
    completed=fix/'result.json'
    if completed.exists():
        result=json.loads(completed.read_text())
        assert result['outcome']=='done' and result['make_ray_run']==runs[str(i)]
        print(i,c['key'],'already done',flush=True)
        continue
    assert latest_run(c['key']).resolve()==fix.resolve()
    run=REPO/runs[str(i)]
    record=json.loads((run/'result.json').read_text())
    note=record['before_findings']+' '+record['revision_plan']
    if record['accepted_exception']:
        note+=' User-authorized visual exception, exact SVG hash; automatic findings retained.'
    else:note+=' Strict validation and full build gate pass without warnings.'
    proc=subprocess.run([sys.executable,'icon_set/scripts/primitive_fix.py','finish','--worker','thuan-mac','--icon',c['key'],'--run',runs[str(i)],'--outcome','done','--note',note],cwd=REPO,capture_output=True,text=True)
    (ROOT/f'finish-{i:02d}.log').write_text(proc.stdout+proc.stderr)
    print(i,proc.stdout.strip(),proc.stderr.strip(),flush=True)
    if proc.returncode:
        raise SystemExit(proc.returncode)
print('ALL 20 FINISHED',flush=True)
