"""Correct stale keyshape declarations and sub-unit arc overshoots without stretching subjects."""
SOURCE_ICON_ID=None
SOURCE_PATH='icon_set/work/spacing-remaining/targets.json'
AUTHOR='gpt-6'
import sys,json,math,re
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[3]))
from icon_set.model.icons.registry import create
from icon_set.model.primitives import Arc,Bezier,Point,primitive_to_dict
from icon_set.validation.envelope import arc_geometry,centerline_bounds
w=Path(__file__).parent
rows=json.loads((w/'targets.json').read_text());done=set(json.loads((w/'notes.json').read_text()))|set(json.loads((w/'applied.json').read_text()))
ledger={}
for row in rows:
 n=row['id']
 if n in done:continue
 i=create(n);b=centerline_bounds(i.primitives)
 if max(abs(v-t) for v,t in zip(b,(6,6,42,42)))>.85:continue
 ends=[p.start.as_tuple() for p in i.primitives]+[p.end.as_tuple() for p in i.primitives]
 if (min(x for x,y in ends),min(y for x,y in ends),max(x for x,y in ends),max(y for x,y in ends))!=(6,6,42,42):continue
 s=Path(row['file']).read_text();s=re.sub(r'keyshape = Keyshape.\w+','keyshape = Keyshape.SQUARE',s)
 changes=[]
 for p in i.primitives:
  pb=centerline_bounds([p])
  if min(pb[:2])>=6-1e-10 and max(pb[2:])<=42+1e-10:continue
  if not isinstance(p,Arc):continue
  g=arc_geometry(p);steps=max(1,math.ceil(abs(g.delta_angle)/(math.pi/2)));segs=[]
  def clip(pt):return tuple(round(max(6,min(42,v)),8) for v in pt)
  for j in range(steps):
   a=g.start_angle+g.delta_angle*j/steps;b=a+g.delta_angle/steps;k=4/3*math.tan((b-a)/4)
   p0=g.point(a);p3=g.point(b)
   c1=(p0[0]-k*g.radius_x*math.sin(a),p0[1]+k*g.radius_y*math.cos(a))
   c2=(p3[0]+k*g.radius_x*math.sin(b),p3[1]-k*g.radius_y*math.cos(b))
   segs.append((clip(c1),clip(c2),clip(p3) if j<steps-1 else p.end.as_tuple()))
  pat=r'(?m)^        self\.add_arc\('+re.escape(repr(p.element_id))+r',.*$'
  line=f'        self.add_bezier({p.element_id!r}, {p.start.as_tuple()!r}, *{tuple(segs)!r})'
  ns,count=re.subn(pat,lambda _:line,s)
  if not count:
   pat=r'(?m)^        self\.add_arc\("'+re.escape(p.element_id)+r'",.*$';ns,count=re.subn(pat,lambda _:line,s)
  if count:s=ns;changes.append(p.element_id)
 s=re.sub(r'AUTHOR = .*',"AUTHOR = 'gpt-6'",s)
 Path(row['file']).write_text(s);ledger[n]={'keyshape':'SQUARE','corrected_curves':changes}
(w/'bounds-adjusted.json').write_text(json.dumps(ledger,indent=2));print('Preserved square proportions:',len(ledger))
