"""Replace rounded-to-grid circle contacts with exact integer circle nodes."""
import json,sys,math,re
from pathlib import Path
from dataclasses import replace
H=Path(__file__).resolve().parent;ROOT=H.parents[3];sys.path.insert(0,str(ROOT))
from icon_set.model.icons.registry import create
from icon_set.model.primitives import Line,Arc,Bezier,Point
from icon_set.validation.envelope import arc_geometry
from icon_set.validation.library_qa import inspect_icon
from normalize import code
SOURCE_ICON_ID=None
SOURCE_PATH='icon_set/work/intersection-review-977/cohort.json'
AUTHOR='gpt-6'
rows={r['id']:r for r in json.loads((H/'baseline.json').read_text())};findings=json.loads((H/'junction-findings.json').read_text());accepted=[];deferred=[]
for row in findings:
 id=row['id'];icon=create(id);by={p.element_id:p for p in icon.primitives};groups={c.contour_id:c for c in icon.contours};moves={};contacts={};plans=[]
 for issue in row['issues']:
  target=groups.get(issue['target']);stroke=groups.get(issue['stroke'])
  if target is None or stroke is None:continue
  circle=[by[x] for x in target.members]
  if not all(isinstance(p,Arc) and p.radius_x==p.radius_y for p in circle):continue
  geos=[arc_geometry(p) for p in circle];g=geos[0];cx,cy,r=g.center_x,g.center_y,g.radius_x
  if abs(cx-round(cx))+abs(cy-round(cy))+abs(r-round(r))>1e-6:continue
  if any(math.hypot(a.center_x-cx,a.center_y-cy)>1e-6 or abs(a.radius_x-r)>1e-6 for a in geos):continue
  x,y=issue['endpoint'];candidates=[]
  for xx in range(round(cx-r),round(cx+r)+1):
   for yy in range(round(cy-r),round(cy+r)+1):
    if (xx-round(cx))**2+(yy-round(cy))**2==round(r)**2:candidates.append((xx,yy))
  # Ties use the more vertical point, consistently across reflections.
  point=min(candidates,key=lambda p:(round(math.dist((x,y),p),7),-abs(p[1]-cy)))
  if math.dist((x,y),point)>3:continue
  for pid in (stroke.members[0],stroke.members[-1]):
   p=by[pid]
   if isinstance(p,Arc):continue
   side='start' if p.start.as_tuple()==(x,y) else 'end' if p.end.as_tuple()==(x,y) else None
   if side:
    moves[(pid,side)]=point;contacts.setdefault(issue['target'],set()).add(point)
    plan=dict(stroke=issue['stroke'],target=issue['target'],before=(x,y),after=point)
    if plan not in plans:plans.append(plan)
 if not moves:continue
 new=[]
 for p in icon.primitives:
  for side in ['start','end']:
   if (p.element_id,side) not in moves:continue
   target=moves[(p.element_id,side)];old=getattr(p,side).as_tuple();delta=(target[0]-old[0],target[1]-old[1])
   if isinstance(p,Bezier):
    segs=list(p.segments)
    if side=='start':a,b,e=segs[0];segs[0]=((a[0]+delta[0],a[1]+delta[1]),b,e)
    else:a,b,e=segs[-1];segs[-1]=(a,(b[0]+delta[0],b[1]+delta[1]),target)
    p=replace(p,segments=tuple(segs),**{side:Point(*target)})
   else:p=replace(p,**{side:Point(*target)})
  new.append(p)
 icon.primitives=new;by={p.element_id:p for p in new};splits={}
 for cid,points in contacts.items():
  for pid in groups[cid].members:
   p=by[pid];g=arc_geometry(p);ordered=[]
   for pt in points:
    if pt in (p.start.as_tuple(),p.end.as_tuple()):continue
    a=math.atan2(pt[1]-g.center_y,pt[0]-g.center_x)
    progress=(a-g.start_angle)%(2*math.pi) if g.delta_angle>0 else (g.start_angle-a)%(2*math.pi)
    if 1e-6<progress<abs(g.delta_angle)-1e-6:ordered.append((progress,pt))
   if not ordered:continue
   seq=[(0,p.start.as_tuple())]+sorted(ordered)+[(abs(g.delta_angle),p.end.as_tuple())];parts=[]
   for k,((ta,a),(tb,b)) in enumerate(zip(seq,seq[1:])):parts.append(replace(p,element_id=f'{pid}-node-{k}',start=Point(*a),end=Point(*b),large_arc=tb-ta>math.pi+1e-8))
   splits[pid]=parts
 icon.primitives=[part for p in icon.primitives for part in splits.get(p.element_id,[p])]
 icon.contours=[replace(c,members=tuple(q.element_id for pid in c.members for q in splits.get(pid,[by[pid]]))) for c in icon.contours]
 try:q=inspect_icon(icon)
 except Exception as e:q=dict(status='exception',errors=[str(e)],warnings=[])
 if q['status']!='pass' or q['warnings']:deferred.append(dict(id=id,plans=plans,validation=q));continue
 p=ROOT/rows[id]['source'];s=p.read_text();s=s[:s.index('    def build(')];s=re.sub(r'REVIEW_ACTION = .*',"REVIEW_ACTION = 'geometry-reconstructed'",s)
 s+='    def build(self):\n        # Plan: exact integer circle attachments; split the receiving arcs at the real nodes.\n        # Reference: circle geometry and the supplied subject.\n'+code(icon);p.write_text(s)
 accepted.append(dict(id=id,source=rows[id]['source'],plan='Replace approximate circle attachments with exact integer boundary nodes, and expose each node in its receiving arc.',reference='Original subject; exact circle equation and shared junctions.',details=plans))
(H/'circle-contacts.json').write_text(json.dumps(accepted,indent=2));(H/'circle-contacts-deferred.json').write_text(json.dumps(deferred,indent=2,default=str));print('Exact circle contacts:',len(accepted),'Deferred:',len(deferred));print(', '.join(r['id'] for r in accepted))
