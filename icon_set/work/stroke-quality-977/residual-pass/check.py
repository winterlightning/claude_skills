import json,sys
from pathlib import Path
H=Path(__file__).resolve().parent;sys.path.insert(0,str(H.parents[3]))
from icon_set.model.icons.registry import create
from icon_set.validation.library_qa import inspect_icon
rows=json.loads((H/'changes.json').read_text());out=[]
for r in rows:
 try:
  q=inspect_icon(create(r['id']));out.append(dict(id=r['id'],**q))
  if q['status']!='valid' or q['warnings']:print(r['id'],q['status'],q['errors'],q['warnings'],flush=True)
 except Exception as e:print(r['id'],repr(e),flush=True)
(H/'validation.json').write_text(json.dumps(out,indent=2,default=str))
print(len(out),'checked')
