from pathlib import Path
import json,tarfile,shutil,hashlib,ast
R=Path.cwd();W=R/'icon_set/work/feedback-solo-sep15';S=W/'snapshot';S.mkdir(exist_ok=True)
for part in ['model','validation','renderers','scripts','tests']:
 shutil.copytree(R/'icon_set'/part,S/'icon_set'/part,dirs_exist_ok=True,ignore=shutil.ignore_patterns('__pycache__','*.png'))
for f in (R/'icon_set').glob('*.py'):shutil.copy2(f,S/'icon_set'/f.name)
archive=R/'icon_set/data/variant-consolidation-latest-20260915'
plan=json.loads((archive/'plan.json').read_text())
for g in plan:
 p=S/Path(g['target_file']).relative_to(R)
 if p.exists():p.unlink()
with tarfile.open(archive/'sources.tar.gz') as t:
 for m in t.getmembers():
  if m.isfile() and m.name.endswith('.py'):
   p=S/m.name;p.parent.mkdir(parents=True,exist_ok=True);p.write_bytes(t.extractfile(m).read())
rows=json.loads((W/'inventory.json').read_text())
for r in rows:
 if 'path' in r:
  p=S/Path(r['path']).relative_to(R)
  assert p.exists(),(r['parent'],p)
  assert hashlib.sha256(p.read_bytes()).hexdigest()==r['hash'],r['parent']
  r['original_workspace_path']=r['path'];r['path']=str(p)
(W/'inventory.json').write_text(json.dumps(rows,indent=2))
# Keep the reconstruction scripts pointed at the isolated source tree.
for name in ['edit_batch.py','check.py']:
 p=W/name;s=p.read_text();s=s.replace("ROOT=Path(__file__).resolve().parents[3]","ROOT=Path(__file__).resolve().parent/'snapshot'")
 p.write_text(s)
print('Recovered exact originals and draft variants in',S)
