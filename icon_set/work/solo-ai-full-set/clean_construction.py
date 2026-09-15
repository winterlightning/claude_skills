"""Coalesce exact straight runs and explicitly close already closed contours.
No snapping, smoothing, scaling, profile edits or clearance exemptions.
"""
from pathlib import Path
import sys,json,ast,copy,inspect,hashlib
from dataclasses import replace
from io import BytesIO
import numpy as np
from PIL import Image
ROOT=Path(__file__).resolve().parents[3];sys.path.insert(0,str(ROOT))
from icon_set.model.icons.registry import create,factories
from icon_set.model.primitives import Line,Arc,Bezier
from icon_set.validation.library_qa import inspect_icon
from icon_set.renderers.png import render_png
from icon_set.scripts.create_variant import prepare_variant
SOURCE_ICON_ID=None
SOURCE_PATH='icon_set/work/solo-ai-full-set/inventory.json'
AUTHOR='gpt-6'
w=Path(__file__).parent
excluded=set(json.loads((w/'prior-reviews.json').read_text()))|{r['parent'] for r in json.loads((w/'batch.json').read_text())}
prior=json.loads((w/'construction-cleanup.json').read_text()) if (w/'construction-cleanup.json').exists() else []
excluded|={r['parent'] for r in prior};out=list(prior)
for rec in json.loads((w/'pending.json').read_text()):
 name=rec['icon_id']
 if name in excluded:continue
 original=create(name);i=copy.deepcopy(original);changed=[];by={p.element_id:p for p in i.primitives};removed=set();used={m for r in i.relationships for m in r.members}
 contours=[]
 for c in i.contours:
  members=[]
  for mid in c.members:
   p=by[mid]
   if isinstance(p,Line) and p.start==p.end and mid not in used:removed.add(mid);changed.append('zero-length straight segment');continue
   if members:
    a=by[members[-1]]
    if isinstance(a,Line) and isinstance(p,Line) and a.end==p.start and a.element_id not in used and mid not in used:
     ax,ay=a.end.x-a.start.x,a.end.y-a.start.y;bx,byy=p.end.x-p.start.x,p.end.y-p.start.y
     if ax*byy==ay*bx and ax*bx+ay*byy>0:
      by[a.element_id]=replace(a,end=p.end);removed.add(mid);changed.append('exact collinear run');continue
   members.append(mid)
  closed=c.closed
  if len(members)>1 and by[members[-1]].end==by[members[0]].start and not closed:
   closed=True;changed.append('explicit existing contour closure')
  contours.append(replace(c,members=tuple(members),closed=closed))
 if not changed:continue
 i.primitives=[by[p.element_id] for p in i.primitives if p.element_id not in removed];i.contours=contours
 q=inspect_icon(i)
 if q['status']!='pass':continue
 alpha=[]
 for scale in [1,2]:
  a=np.asarray(Image.open(BytesIO(render_png(original,scale=scale))).convert('RGBA')).astype(float)
  b=np.asarray(Image.open(BytesIO(render_png(i,scale=scale))).convert('RGBA')).astype(float)
  alpha.append(float(np.abs(a-b).sum()/255))
 if max(alpha)>4:continue
 dest,new,source=prepare_variant(name,'solo','Clean continuous construction');tree=ast.parse(source)
 for n in tree.body:
  if isinstance(n,ast.Assign) and any(isinstance(t,ast.Name) and t.id=='AUTHOR' for t in n.targets):n.value=ast.Constant(AUTHOR)
 cls=next(n for n in tree.body if isinstance(n,ast.ClassDef));cls.body=[n for n in cls.body if not isinstance(n,ast.FunctionDef)]
 body=[]
 for p in i.primitives:
  s,e=p.start.as_tuple(),p.end.as_tuple()
  if isinstance(p,Line):body.append(f'self.add_line({p.element_id!r}, {s!r}, {e!r})')
  elif isinstance(p,Arc):body.append(f'self.add_arc({p.element_id!r}, {s!r}, {e!r}, radius_x={p.radius_x!r}, radius_y={p.radius_y!r}, large_arc={p.large_arc!r}, sweep={p.sweep!r})')
  elif isinstance(p,Bezier):body.append(f'self.add_bezier({p.element_id!r}, {s!r}, '+', '.join(repr(s) for s in p.segments)+')')
  else:raise TypeError(type(p))
 for c in i.contours:body.append(f'self.add_contour({c.contour_id!r}, '+', '.join(repr(m) for m in c.members)+f', closed={c.closed!r})')
 for r in i.relationships:body.append(f'self.relate({r.kind!r}, '+', '.join(repr(m) for m in r.members)+')')
 func='def build(self):\n    # Plan: Preserve every painted coordinate; coalesce exact straight runs and declare existing closed paths.\n    # Reference: Original subject, verified with pixel comparisons at 48 and 96 pixels.\n'+'\n'.join('    '+l for l in body)+'\n'
 cls.body.append(ast.parse(func).body[0]);ast.fix_missing_locations(tree)
 uuid=getattr(sys.modules[type(original).__module__],'SOURCE_ICON_ID');dest=dest.with_name(dest.stem+'_'+uuid.replace('-','_')+'.py');dest.write_text(ast.unparse(tree)+'\n')
 out.append(dict(parent=name,icon_id=new,path=str(dest.relative_to(ROOT)),label='Clean continuous construction',plan='Same painted shape; exact collinear runs consolidated and existing closed contours explicitly closed.',changes=changed,pixel_difference=alpha,report=q))
 (w/'construction-cleanup.json').write_text(json.dumps(out,indent=2));print(name,'->',new,len(changed),alpha,flush=True)
print('Cleaned',len(out),flush=True)
