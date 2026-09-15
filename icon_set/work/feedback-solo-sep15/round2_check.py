from pathlib import Path
import json,sys,traceback
W=Path(__file__).resolve().parent;sys.path.insert(0,str(W/'snapshot'))
from icon_set.model.icons.registry import create
from icon_set.validation.library_qa import inspect_icon
from icon_set.renderers.svg import render_svg
R=json.loads((W/'revisions.json').read_text());Q=json.loads((W/'release-validation.json').read_text());V=json.loads((W/'validation.json').read_text());nums=list(map(int,sys.argv[1:])) if len(sys.argv)>1 else json.loads((W/'round2-numbers.json').read_text())
for n in nums:
 r=R[str(n)];id=r['id']
 try:
  icon=create(id);qa=inspect_icon(icon);v=icon.validate_icon();V[id]={'status':v.status,'description':v.describe(),'keyshape':icon.keyshape.name,'svg':render_svg(icon)};Q[id]={k:qa.get(k) for k in ['status','errors','warnings']}
 except Exception as e:Q[id]={'status':'error','errors':[str(e)],'warnings':[]};traceback.print_exc()
 print(n,id,json.dumps(Q[id]),flush=True)
 (W/'release-validation.json').write_text(json.dumps(Q,indent=2));(W/'validation.json').write_text(json.dumps(V,indent=2))
