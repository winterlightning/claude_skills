from pathlib import Path
import json,sys
ROOT=Path(__file__).resolve().parents[3];sys.path.insert(0,str(ROOT))
from icon_set.model.icons.registry import create
from icon_set.validation.library_qa import inspect_icon
W=Path(__file__).parent;out=[]
for r in json.loads((W/'mapping.json').read_text()):
 try:
  obj=create(r['id']);v=obj.validate_icon();q=inspect_icon(obj);q.pop('_svg',None);out.append(dict(r,qa=q,validation=v.describe()))
  print(r['id'],v.describe(),json.dumps({k:q.get(k) for k in ['status','needs_review','internal_spacing','negative_space']}),flush=True)
 except Exception as e:print(r['id'],repr(e),flush=True);out.append(dict(r,error=repr(e)))
(W/'results.json').write_text(json.dumps(out,indent=2,default=str))
