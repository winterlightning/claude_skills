"""Run the unchanged family build on this batch in an isolated source snapshot."""
import inspect,json,shutil,subprocess
from pathlib import Path
from icon_set.model.icons.registry import factories
from icon_set.scripts.discard_icon import remove_class
OUT=Path(__file__).resolve().parent;ROOT=OUT.parents[2];SNAP=OUT/'isolated-build'
assert not SNAP.exists(),'Snapshot already exists; inspect before rebuilding.'
(SNAP/'icon_set').mkdir(parents=True)
for directory in ['model','renderers','validation','scripts']:
 shutil.copytree(ROOT/'icon_set'/directory,SNAP/'icon_set'/directory,ignore=shutil.ignore_patterns('__pycache__','*.pyc'))
shutil.copy2(ROOT/'icon_set/__init__.py',SNAP/'icon_set/__init__.py')
for p in ROOT.glob('*.py'):shutil.copy2(p,SNAP/p.name)
rows=json.loads((OUT/'batch.json').read_text());registered=factories()
for r in rows:
 f=registered[r['icon_id']];current=Path(inspect.getsourcefile(f));relative=current.relative_to(ROOT)
 p=SNAP/relative;p.write_text(remove_class(p.read_text(),f.__name__))
 original=ROOT/r['original_model'];dest=SNAP/r['python_source']['path'];dest.write_bytes(original.read_bytes())
 if r.get('variant_path'):
  draft=ROOT/r['variant_path'];dest=SNAP/'icon_set/model/icons/solo'/draft.name;dest.write_bytes(draft.read_bytes())
  r['isolated_source']=str(dest.relative_to(SNAP))
 else:r['isolated_source']=r['python_source']['path']
args=['python3','icon_set/scripts/build.py','--family','solo']
for r in rows:args+=['--icon',r['isolated_source']]
(OUT/'batch.json').write_text(json.dumps(rows,indent=2))
with (OUT/'isolated-build.log').open('w') as log:
 result=subprocess.run(args,cwd=SNAP,stdout=log,stderr=subprocess.STDOUT)
(OUT/'build-result.json').write_text(json.dumps({'exit_code':result.returncode,'command':args,'scope':100,'isolated':True},indent=2))
print('Isolated batch build exit:',result.returncode)
