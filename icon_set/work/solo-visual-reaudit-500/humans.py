from repair import *
from icon_set.model.icons.registry import create
from icon_set.model.primitives import Line,Arc,Bezier,Point
from dataclasses import replace
# Explicit per-pose shoulder, head and upper-torso choices after source review.
# n: (head contour, torso member, old shoulder, new shoulder, head center, radius)
specs={
7:('head','body-1',(24,23),(24,23),(29,11),5),
27:('present-head','present-body-1',(14,23),(14,24),(14,12),4),
43:('head','torso-1',(36,27),(36,26),(36,12),6),
44:('person-head','person-body-1',(24,21),(24,23),(29,11),5),
46:('head','body',(24,22),(24,23),(29,11),5),
47:('person-head','person-back-1',(16,23),(16,25),(21,13),5),
48:('head','body-1',(30,21),(30,23),(35,11),5),
49:('head','body-back-leg-1',(22,26),(22,26),(27,14),5),
50:('person-head','person-torso-1',(28,21),(28,23),(33,11),5),
51:('person-head','person-body-1',(23,30),(23,30),(23,18),4),
52:('person-head','person-torso-1',(26,20),(26,22),(26,10),4),
53:('head','body-leg-1',(24,22),(24,23),(29,11),5),
54:('person-head','person-body-1',(22,21),(22,23),(27,11),5),
60:('head','body-2',(24,23),(24,23),(36,18),5),
75:('head','back-1',(20,18),(23,16),(11,11),5),
86:('head','torso',(32,23),(32,24),(32,11),5),
89:('head','person-1',(14,25),(14,24),(14,11),5),
94:('head','rider-1',(12,21),(12,22),(12,10),4),
95:('head','torso-0',(24,20),(24,22),(24,10),4),
96:('head','torso-0',(24,21),(24,22),(24,10),4),
100:('head','body-1',(20,19),(20,23),(25,11),5),
110:('person-head','person-body-1',(24,19),(24,21),(29,9),5),
112:('head','body-1',(25,22),(25,25),(30,13),5),
118:('head','body-1',(16,20),(14,22),(14,10),4),
119:('head','body-1',(29,20),(30,22),(30,10),4),
126:('head','body-1',(24,24),(24,24),(24,11),5),
135:('person-head','person-body-1',(24,19),(24,21),(29,9),5),
138:('head','body-1',(13,23),(13,24),(13,12),4),
142:('head','person-1',(16,22),(16,23),(16,11),4),
146:('adult-head','adult-body-1',(12,23),(12,24),(12,12),4),
168:('head','paddler-1',(17,22),(17,24),(17,12),4),
186:('head','torso-0',(22,25),(24,24),(24,11),5),
204:('head','seated-body-0',(12,24),(12,24),(12,11),5),
230:('skier-head','skier-1',(8,21),(10,22),(10,10),4),
232:('head','torso-1',(25,19),(25,23),(30,11),5),
235:('head','back-1',(28,24),(28,24),(28,10),6),
263:('left-head','left-body-0',(14,22),(14,23),(14,11),4),
270:('person-head','person-body-1',(18,20),(18,22),(18,10),4),
273:('person-head','person-torso-1',(24,21),(24,23),(29,11),5),
303:('head','back-and-leg-1',(18,19),(18,20),(18,8),4),
340:('head','rider-2',(35,20),(35,22),(35,10),4),
342:('head','body-1',(15,23),(15,24),(15,12),4),
347:('head','rider-3',(12,24),(12,25),(12,13),4),
392:('head','torso',(24,22),(24,23),(29,11),5),
396:('head','rider-1',(19,19),(19,23),(24,11),5),
397:('head','body-1',(17,22),(17,24),(17,11),5),
421:('rider-head','rider-1',(18,19),(18,20),(18,8),4),
425:('person-head','person-body-1',(18,21),(18,23),(23,11),5),
426:('person-head','person-body-1',(16,23),(16,24),(16,12),4),
447:('head','rider-1',(19,20),(19,23),(24,11),5),
490:('head','rider-1',(25,18),(25,23),(30,11),5),
}
# Local limb adjustments preserve the same action while clearing the larger head.
moves={48:{(38,25):(38,29)},49:{(30,28):(30,30)},52:{(42,20):(42,22)},53:{(14,16):(14,20)},54:{(32,25):(32,28)},89:{(25,23):(25,24)},95:{(15,20):(15,22),(33,20):(33,22)},96:{(15,20):(15,22),(33,20):(33,22)},112:{(38,28):(38,31)},168:{(25,23):(25,25)},397:{(6,20):(6,24)},426:{(26,21):(26,24)}}

def emit(d,heads,replaced,pointmoves={}):
 out=[];skip=set()
 for name,(cx,cy,r) in heads.items():
  ct=next(c for c in d.contours if c.contour_id==name);skip.update(ct.members)
  out.append(f"self.ring({name!r},{cx},{cy},{r})")
 for p in d.primitives:
  if p.element_id in skip:continue
  p=replaced.get(p.element_id,p)
  def pt(a):return pointmoves.get(a.as_tuple(),a.as_tuple())
  if isinstance(p,Line):out.append(f'self.add_line({p.element_id!r},{pt(p.start)!r},{pt(p.end)!r})')
  elif isinstance(p,Arc):out.append(f'self.add_arc({p.element_id!r},{pt(p.start)!r},{pt(p.end)!r},radius_x={p.radius_x},radius_y={p.radius_y},large_arc={p.large_arc},sweep={p.sweep})')
  elif isinstance(p,Bezier):out.append(f'self.add_bezier({p.element_id!r},{pt(p.start)!r},*{p.segments!r})')
 for c in d.contours:
  if c.contour_id not in heads:out.append(f'self.add_contour({c.contour_id!r},*{c.members!r},closed={c.closed})')
 for rel in d.relationships:out.append(f'self.relate({rel.kind!r},*{rel.members!r})')
 return '\n'.join(out)

def repair_pose(n,spec):
 head,body,old,s,c,r=spec;icon=create(rows[n-1]['selected']);d=icon.draw();prim=next(p for p in d.primitives if p.element_id==body)
 assert old in [prim.start.as_tuple(),prim.end.as_tuple()],(n,body,prim)
 end=prim.end.as_tuple() if prim.start.as_tuple()==old else prim.start.as_tuple()
 vx,vy=(s[0]-c[0],s[1]-c[1]);assert vx*vx+vy*vy==(r+8)**2,(n,s,c,r)
 # Curved upper torso begins along the axis away from the head. Controls stay
 # on the far side of the shoulder support line; this is measured in QA.
 length=((end[0]-s[0])**2+(end[1]-s[1])**2)**.5
 t=min(0.28,length/(r+8)*.4)
 p1=(s[0]+vx*t,s[1]+vy*t);p2=(end[0]+(s[0]-end[0])*.25,end[1]+(s[1]-end[1])*.25)
 if prim.start.as_tuple()==old:b=Bezier(body,Point(*s),Point(*end),((p1,p2,end),))
 else:b=Bezier(body,Point(*end),Point(*s),((p2,p1,s),))
 mapping={old:s,**moves.get(n,{})};hs={head:(*c,r)};repl={body:b}
 if n==7:repl['pack-2']=replace(b,element_id='pack-2')
 # Repeated figures share head radius and exact gaps.
 if n==27:hs['missing-head']=(36,12,4);mapping[(36,23)]=(36,24)
 if n==263:hs['right-head']=(34,11,4);mapping[(34,22)]=(34,23)
 reason=f"Reconstruct {rows[n-1]['icon_id'].replace('-',' ')} using its inspected source pose and full_body_ref.png. Head radius {r}, center {c}, actual torso junction {s}: squared distance {(r+8)**2}, centerline clearance8 and painted clearance4. Upper torso tangent follows that axis; preserve the subject's limb action and equipment. Shared Lucide person-standing joints; updated approaching-ball example informs head/body balance."
 save(n,emit(d,hs,repl,mapping),reason)
if __name__=='__main__':
 for n,spec in specs.items():repair_pose(n,spec)
