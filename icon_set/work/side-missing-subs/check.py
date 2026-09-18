"""Read-only model and release QA for the source-linked side reference batch."""
import sys,json,importlib
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3];sys.path.insert(0,str(ROOT))
from icon_set.validation.library_qa import inspect_icon
from icon_set.renderers.svg import render_svg
out=Path(__file__).parent;results=[]
for r in json.loads((out/'solo-targets.json').read_text()):
 p=Path(r['path']);m=importlib.import_module('.'.join(p.with_suffix('').parts));c=next(c for c in vars(m).values() if isinstance(c,type) and getattr(c,'icon_id',None) and c.__module__==m.__name__);icon=c();v=icon.validate_icon();q=inspect_icon(icon); r.update(icon_id=icon.icon_id,keyshape=icon.keyshape.name,model_status=v.status,status=q['status'],errors=q['errors'],warnings=q['warnings']);results.append(r)
 (out/(icon.icon_id+'.svg')).write_text(q.get('_svg') or render_svg(icon))
 print(r['number'],q['status'],q['errors'],q['warnings'][:3],flush=True)
(out/'solo-results.json').write_text(json.dumps(results,indent=2))
