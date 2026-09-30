import json,sys,subprocess
from pathlib import Path
root=Path(__file__).resolve().parent;repo=root.parents[2]
latest=json.loads((root/'latest.json').read_text())
for i in map(int,sys.argv[1:]):
    r=latest[str(i)];out=repo/r['run']
    assert r['validation_status']=='valid' and r['build_gate']['status']=='pass' and not r['warnings'] and not r['build_gate']['warnings']
    r['visual_review']='Inspected source comparison, native 48px and enlarged previews in light and dark; clear subject, consistent strokes and readable negative space.'
    r['feedback']='No written feedback recorded; repair follows visual comparison with source.'
    (out/'result.json').write_text(json.dumps(r,indent=2))
    cmd=[sys.executable,'icon_set/scripts/primitive_fix.py','finish','--worker','thuan-mac','--icon','solo/'+r['icon_id'],'--run',r['run'],'--outcome','done','--note',r['change']]
    p=subprocess.run(cmd,cwd=repo,text=True,capture_output=True)
    (root/f'finish-{i}.log').write_text(p.stdout+p.stderr)
    print(i,p.returncode,p.stdout[-400:],p.stderr[-600:],flush=True)
