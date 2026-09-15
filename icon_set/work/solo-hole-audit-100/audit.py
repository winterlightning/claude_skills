from pathlib import Path
import sys,json,tempfile
ROOT=Path(__file__).resolve().parents[3];sys.path.insert(0,str(ROOT))
from icon_set.model.icons.registry import create
from icon_set.validation import hole_geometry as engine
from icon_set.validation.library_qa import inspect_icon
SOURCE_ICON_ID=None
SOURCE_PATH='icon_set/work/solo-failed-batch-100/review-decisions.json'
AUTHOR='gpt-6'
W=Path(__file__).parent
rows=json.loads((ROOT/SOURCE_PATH).read_text());out=[]
for n,row in enumerate(rows,1):
 ident=row.get('replacement',row['icon_id']);icon=create(ident);qa=inspect_icon(icon)
 with tempfile.TemporaryDirectory() as t:
  p=Path(t)/'icon.svg';p.write_text(icon.to_svg());ink=engine.render_ink_mask(p,48,48,32,0)
  pinches=engine.find_pinches(p,ink,(0,0,48,48),32,1,0,48)
 out.append(dict(number=n,icon_id=ident,status=qa['status'],holes=qa['negative_space'],authored_pinches=pinches))
 if pinches or qa['negative_space']['status']!='pass':print(n,ident,'holes',qa['negative_space']['status'],'authored pinches',[(p['center_viewbox'],p['closure_margin_design_u']) for p in pinches],flush=True)
 (W/'audit.json').write_text(json.dumps(out,indent=2))
print('DONE',len(out),'icons; pinch failures',sum(bool(r['authored_pinches']) for r in out),flush=True)
