"""Snapshot this batch and run the current unchanged family build against it."""
import json,shutil,subprocess
from pathlib import Path
OUT=Path(__file__).resolve().parent;ROOT=OUT.parents[2];snap=OUT/'centerline-build'
assert not snap.exists()
shutil.copytree(OUT/'isolated-build',snap,ignore=shutil.ignore_patterns('dist','__pycache__','*.pyc'))
# Use the current validation/rendering code without changing any rule.
for name in ('validation','renderers','scripts'):
 shutil.copytree(ROOT/'icon_set'/name,snap/'icon_set'/name,dirs_exist_ok=True,ignore=shutil.ignore_patterns('__pycache__','*.pyc'))
for p in (ROOT/'icon_set/model').glob('*.py'):shutil.copy2(p,snap/'icon_set/model'/p.name)
shutil.copytree(ROOT/'icon_set/model/contracts',snap/'icon_set/model/contracts',dirs_exist_ok=True)
rows=json.loads((OUT/'batch.json').read_text());args=['python3','icon_set/scripts/build.py','--family','solo']
for r in rows:
 draft=ROOT/r['variant_path'];dest=snap/'icon_set/model/icons/solo'/draft.name;shutil.copy2(draft,dest)
 args+=['--icon',str(dest.relative_to(snap))]
with (OUT/'centerline-build.log').open('w') as log:result=subprocess.run(args,cwd=snap,stdout=log,stderr=subprocess.STDOUT)
(OUT/'centerline-build-result.json').write_text(json.dumps({'exit_code':result.returncode,'scope':100,'isolated':True},indent=2))
print('Centerline batch build exit:',result.returncode)
