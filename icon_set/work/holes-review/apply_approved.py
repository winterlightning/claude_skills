"""Promote user-approved geometry, preserving identity and recoverable source copies."""
import ast,json,sys,hashlib
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3];sys.path.insert(0,str(ROOT))
SOURCE_ICON_ID=None
SOURCE_PATH='icon_set/work/holes-review/mapping.json'
AUTHOR='gpt-6'
W=Path(__file__).parent;excluded=json.loads((W/'excluded.json').read_text());mapping=json.loads((W/'mapping.json').read_text());backup=W/'approved-source-backups';backup.mkdir(exist_ok=True)
changes=[]
for m in mapping:
 if m['original'] in excluded:continue
 path=ROOT/m['source'];original=path.read_text();candidate=ast.parse((ROOT/m['file']).read_text());t=ast.parse(original)
 def iconclass(tree,iconid):
  return next(c for c in tree.body if isinstance(c,ast.ClassDef) and any(isinstance(a,ast.Assign) and any(isinstance(v,ast.Name) and v.id=='icon_id' for v in a.targets) and isinstance(a.value,ast.Constant) and a.value.value==iconid for a in c.body))
 target=iconclass(t,m['original']);src=iconclass(candidate,m['candidate'])
 methods=[v for v in src.body if isinstance(v,(ast.FunctionDef,ast.AsyncFunctionDef))];names={v.name for v in methods}
 target.body=[v for v in target.body if not (isinstance(v,(ast.FunctionDef,ast.AsyncFunctionDef)) and v.name in names)]+methods
 key=next(a.value for a in src.body if isinstance(a,ast.Assign) and any(isinstance(v,ast.Name) and v.id=='keyshape' for v in a.targets))
 for a in target.body:
  if isinstance(a,ast.Assign) and any(isinstance(v,ast.Name) and v.id=='keyshape' for v in a.targets):a.value=key
 for a in t.body:
  if isinstance(a,ast.Assign) and any(isinstance(v,ast.Name) and v.id=='AUTHOR' for v in a.targets):a.value=ast.Constant(AUTHOR)
 ast.fix_missing_locations(t);new=ast.unparse(t)+'\n';compile(new,str(path),'exec')
 bp=backup/path.name
 if not bp.exists():bp.write_text(original)
 path.write_text(new)
 changes.append({**m,'backup':str(bp.relative_to(ROOT)),'before_sha256':hashlib.sha256(original.encode()).hexdigest(),'after_sha256':hashlib.sha256(new.encode()).hexdigest()})
(W/'approved-applied.json').write_text(json.dumps({'status':'geometry applied; rebuild pending','count':len(changes),'excluded':list(excluded),'changes':changes},indent=2))
print('Promoted',len(changes),'approved geometries; source identities and backups preserved.')
