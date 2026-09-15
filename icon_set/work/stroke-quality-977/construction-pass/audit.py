"""Inspect primitive geometry inside every stroke of the fixed cohort."""
import sys,json,math,hashlib,itertools
from pathlib import Path
H=Path(__file__).resolve().parent;ROOT=H.parents[3];sys.path.insert(0,str(ROOT))
from icon_set.model.icons.registry import create
from icon_set.model.primitives import Line,Arc,Bezier,primitive_to_dict
from icon_set.validation.envelope import arc_geometry
from shapely.geometry import LineString,Point

def samples(p):
 if isinstance(p,Line):return [p.start.as_tuple(),p.end.as_tuple()]
 if isinstance(p,Bezier):return p.sample(32)
 a=arc_geometry(p);return [a.point(a.start_angle+a.delta_angle*i/100) for i in range(101)]
def angle(a,b):
 na=math.hypot(*a);nb=math.hypot(*b)
 return math.degrees(math.acos(max(-1,min(1,sum(x*y for x,y in zip(a,b))/na/nb)))) if na*nb>1e-9 else 0

def analyze(icon):
 ps=icon.primitives;pts={p.element_id:samples(p) for p in ps};ls={id:LineString(v) for id,v in pts.items()};issues=[]
 # Exact duplicate strokes, including retraced edges in collapsed loops.
 for a,b in itertools.combinations(ps,2):
  aa,bb=ls[a.element_id],ls[b.element_id]
  if aa.length==bb.length==0:
   if a.start==b.start:issues.append(dict(kind='duplicate-dot',a=a.element_id,b=b.element_id))
  elif aa.length>0 and bb.length>0 and aa.hausdorff_distance(bb)<1e-7:
   issues.append(dict(kind='duplicate',a=a.element_id,b=b.element_id))
  elif isinstance(a,Line) and isinstance(b,Line):
   if aa.length>0 and bb.length>0 and aa.intersection(bb).length>.05:issues.append(dict(kind='overlapping-lines',a=a.element_id,b=b.element_id,length=aa.intersection(bb).length))
 # Dead/near-zero cubics hide inside an otherwise normal path.
 for p in ps:
  v=pts[p.element_id];length=ls[p.element_id].length
  if not isinstance(p,Line) and length<1:issues.append(dict(kind='tiny-curve',a=p.element_id,length=round(length,4)))
  if isinstance(p,Bezier):
   for j,c in enumerate(p.cubics()):
    diameter=max(math.dist(a,b) for a,b in itertools.combinations(c,2))
    if diameter<.2:issues.append(dict(kind='degenerate-cubic',a=p.element_id,segment=j,diameter=round(diameter,4)))
 # Compare continuous tangent vectors, including interior cubic knots.
 by={p.element_id:p for p in ps}
 for c in icon.contours:
  chain=[]
  for id in c.members:
   p=by[id]
   if isinstance(p,Bezier):
    for j,(v0,v1,v2,v3) in enumerate(p.cubics()):
     chain.append((id+':'+str(j),'curve',v0,v3,(v1[0]-v0[0],v1[1]-v0[1]),(v3[0]-v2[0],v3[1]-v2[1])))
   else:
    v=pts[id];chain.append((id,'line' if isinstance(p,Line) else 'curve',v[0],v[-1],(v[1][0]-v[0][0],v[1][1]-v[0][1]),(v[-1][0]-v[-2][0],v[-1][1]-v[-2][1])))
  pairs=list(zip(chain,chain[1:]))+([(chain[-1],chain[0])] if c.closed and len(chain)>1 else [])
  for a,b in pairs:
   turn=angle(a[-1],b[-2])
   if 'curve' in (a[1],b[1]) and 12<turn<168:issues.append(dict(kind='tangent-change',a=a[0],b=b[0],degrees=round(turn,1),point=a[3]))
 # Loose endpoints that terminate just inside a different primitive at a declared junction.
 for a in ps:
  for b in ps:
   if a==b:continue
   if isinstance(a,Line) and a.is_dot:continue
   for endpoint in (a.start,a.end):
    pt=endpoint.as_tuple()
    if endpoint in (b.start,b.end):continue
    dist=Point(pt).distance(ls[b.element_id])
    if .05<dist<1.6 and min(math.dist(pt,b.start.as_tuple()),math.dist(pt,b.end.as_tuple()))<3:
     issues.append(dict(kind='inexact-junction',a=a.element_id,b=b.element_id,point=pt,distance=round(dist,3)))
 return issues
if __name__=='__main__':
 rows=json.loads((H.parent/'report.json').read_text())['rows'];out=[]
 for r in rows:
  p=ROOT/r['source'];bk=H/'before'/p.name
  if not bk.exists():bk.write_bytes(p.read_bytes())
  icon=create(r['id']);issues=analyze(icon)
  out.append(dict(id=r['id'],source=r['source'],sha256=hashlib.sha256(p.read_bytes()).hexdigest(),svg=icon.to_svg(),keyshape=icon.keyshape.name,primitives=[primitive_to_dict(p) for p in icon.primitives],contours=[dict(id=c.contour_id,members=c.members,closed=c.closed) for c in icon.contours],issues=issues))
 (H/'baseline.json').write_text(json.dumps(out,indent=2))
 print('Audited',len(out),'icons;',sum(bool(r['issues']) for r in out),'with construction candidates')
 from collections import Counter
 print(Counter(i['kind'] for r in out for i in r['issues']))
 for r in out:
  if r['issues']:print(r['id'],dict(Counter(i['kind'] for i in r['issues'])))
