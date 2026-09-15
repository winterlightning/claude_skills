"""Anatomically reviewed head/body repairs; source parents remain unchanged."""
from audit import *
from dataclasses import replace
from copy import deepcopy
from icon_set.model.primitives import Point,Contour,Relationship,primitive_to_dict
from icon_set.validation.library_qa import inspect_icon
from icon_set.renderers.svg import build_paths
SOURCE_ICON_ID=None
SOURCE_PATH='icon_set/work/human-repair-review/audit.json'
AUTHOR='gpt-6'
source={x['row']['icon_id']:x for x in rows}
def move_joint(i,old,new):
 old,new=tuple(old),tuple(new);out=[]
 for p in i.primitives:
  a=tuple(p.start.as_tuple());b=tuple(p.end.as_tuple());kw={}
  if a==old:kw['start']=Point(*new)
  if b==old:kw['end']=Point(*new)
  if isinstance(p,Bezier):
   seg=list(p.segments)
   if a==old:
    c1,c2,k=seg[0];seg[0]=((c1[0]+new[0]-old[0],c1[1]+new[1]-old[1]),c2,k)
   if b==old:
    c1,c2,k=seg[-1];seg[-1]=(c1,(c2[0]+new[0]-old[0],c2[1]+new[1]-old[1]),new)
   kw['segments']=tuple(seg)
  out.append(replace(p,**kw) if kw else p)
 i.primitives=out

def move_head(i,fs,dx=0,dy=0):
 ids=fs['head_members'];out=[]
 for p in i.primitives:
  if p.element_id in ids:p=replace(p,start=Point(p.start.x+dx,p.start.y+dy),end=Point(p.end.x+dx,p.end.y+dy))
  out.append(p)
 i.primitives=out

def tangent(i,f):
 by=i.draw().by_id();t=by[f['torso_members'][0]];junction=f['torso_junction'];cx,cy,r=circle([by[z] for z in f['head_members']]);q=getattr(t,junction).as_tuple();other=getattr(t,'end' if junction=='start' else 'start').as_tuple()
 
 if isinstance(t,Line):
  v=(q[0]-other[0],q[1]-other[1]);w=(cx-q[0],cy-q[1])
  if abs(v[0]*w[1]-v[1]*w[0])<1e-8 and v[0]*w[0]+v[1]*w[1]>0:return
 dist=math.dist(q,other);length=min(3.0,dist/3);head_dist=math.hypot(cx-q[0],cy-q[1]);near=(q[0]+(q[0]-cx)/head_dist*length,q[1]+(q[1]-cy)/head_dist*length)
 if isinstance(t,Bezier):far=t.segments[-1][1] if junction=='start' else t.segments[0][0]
 else:far=(other[0]+(q[0]-other[0])/4,other[1]+(q[1]-other[1])/4)
 c1,c2=(near,far) if junction=='start' else (far,near)
 # Keep exact decimal controls on the same radial direction, avoiding output-rounding drift.
 v=(q[0]-cx,q[1]-cy);fac=.25 if dist>=5 else .125;near=(q[0]+v[0]*fac,q[1]+v[1]*fac)
 c1,c2=(near,far) if junction=='start' else (far,near)
 changed=Bezier(t.element_id,t.start,t.end,((c1,c2,t.end.as_tuple()),))
 i.primitives=[changed if p.element_id==t.element_id else p for p in i.primitives]

def split(i,name,at,newname=None):
 newname=newname or name+'-continued';by=i.draw().by_id();p=by[name];assert isinstance(p,Line)
 a=replace(p,end=Point(*at));b=Line(newname,Point(*at),p.end);out=[]
 for old in i.primitives:out.extend([a,b] if old.element_id==name else [old])
 i.primitives=out
 found=False;cts=[]
 for c in i.contours:
  if name in c.members:found=True;c=replace(c,members=tuple(z for m in c.members for z in ([name,newname] if m==name else [m])))
  cts.append(c)
 if not found:cts.append(Contour(name+'-path',(name,newname)))
 i.contours=cts
 return newname

def repair(i,a):
 n=a['number'];fs=a['figures'];reason=[]
 changes={1:((12,21),(12,20)),16:((24,21),(20,20)),26:((18,18),(20,20)),27:((35,28),(37,28)),30:((22,18),(28,22)),42:((18,21),(16,20)),104:((34,26),(34,25)),139:((24,24),(25,23)),173:((24,21),(24,20))}
 headmoves={16:(3,0),26:(-9,0),30:(-6,0)}
 if n in headmoves:move_head(i,fs[0],*headmoves[n]);reason.append('Reposition head over the anatomical shoulder.')
 if n in changes:move_joint(i,*changes[n]);reason.append('Set head-outline to shoulder centerline separation to exactly 8u.')
 if n==16:
  i.primitives=[p for p in i.primitives if p.element_id!='arms-2']
  i.contours=[replace(c,members=('arms-1',)) if c.contour_id=='arms' else c for c in i.contours]
  reason.append('Simplify to one visible balancing arm; omit the far raised arm that crowds the head and bent leg.')
 if n==27:split(i,'person-1',(25,28));reason.append('Keep the extended arm clear of the detached head.')
 if n==139:move_joint(i,(22,10),(19,10));reason.append('Rebalance raised hand to keep it clear of the head.')
 if n in {1,16,26,27,30,34,42,96,100,104,139,173}:
  for f in fs:
   if f['torso_junction'] and (f.get('needs_repair') or n in changes):tangent(i,f)
  reason.append('Align the upper torso tangent with its own head center.')
 if n==15:
  move_joint(i,(37,33),(35,33));i.primitives=[p for p in i.primitives if p.element_id!='gun-2'];i.contours=[replace(c,members=('gun-1',)) if c.contour_id=='gun' else c for c in i.contours];reason.append('Remove the short gun-stock overhang trapping a pinch against the bent arm.');reason.append('Rebalance outlined shoulders: nearest shoulder point is 8u below the head outline.')
 if n==77:
  move_joint(i,(24,18),(19,18));reason.append('Bring the top of the outlined body under the head with exact 4u ink clearance.')
 if n==66:
  i.primitives=[replace(p,radius_y=10) if p.element_id=='face' else replace(p,radius_y=7) if p.element_id=='shoulders' else p for p in i.primitives]
  i.relate('connect','face','shoulders');reason.append('Use a circular face and raise the shoulder arch to tangent ink contact for a bust (0u visible gap).')
 if n in {90,168,169}:
  ry=12 if n==90 else 8;i.primitives=[replace(p,radius_y=ry) if p.element_id=='front-shoulders' else p for p in i.primitives]
  reason.append('Raise front bust shoulder arch to an exact 4u detached ink gap; preserve the rear continuous neck.')
 if n==133:
  torso=next(c for c in i.contours if c.contour_id=='torso');remove=set(torso.members)
  i.primitives=[p for p in i.primitives if p.element_id not in remove];i.contours=[c for c in i.contours if c.contour_id!='torso']
  move_joint(i,(26,31),(26,34))
  i.add_line('torso-left',(26,42),(26,34));i.add_arc('shoulder-left',(26,34),(34,26),radius_x=8);i.add_arc('shoulder-right',(34,26),(42,34),radius_x=8);i.add_line('torso-right',(42,34),(42,42));i.add_line('torso-base',(42,42),(26,42));i.add_contour('torso','torso-left','shoulder-left','shoulder-right','torso-right','torso-base',closed=True)
  i.relate('connect','face','torso');reason.append('Replace pinched collar with smooth rounded shoulders touching the circular face ink; retain cap, raised arm and passport.')
 if n==180:
  move_joint(i,(13,27),(13,24));move_joint(i,(23,27),(23,24));move_joint(i,(8,20),(8,17));reason.append('Raise gown neckline to exactly 4u ink clearance below the head.')
 if n==101:
  split(i,'director-1',(36,32),'director-leg');reason.append('Separate the director torso from the leg at the hip without moving ink.')
 return reason

def record_report(i):
 r=inspect_icon(i);r.pop('_svg',None);return r
if __name__=='__main__':
 audits=json.loads((OUT/'audit.json').read_text());results=[]
 (OUT/'before').mkdir(exist_ok=True);(OUT/'after').mkdir(exist_ok=True)
 for a in audits:
  original=load(source[a['icon_id']]);i=deepcopy(original);reason=repair(i,a)
  if reason:
   # Only flag verified stick torso primitives; silhouette figures stay separately typed.
   for f in a['figures']:
    if f['torso_junction'] and isinstance(f['torso'],str):i.mark_human_figure(f['figure_id'],head=f['head'],torso=f['torso_members'][0],torso_junction=f['torso_junction'])
   before=record_report(original);after=record_report(i)
   after_fs=deepcopy(a['figures'])
   for f in after_fs:
    cs={c.contour_id:c.members for c in i.contours}
    if isinstance(f['torso'],str) and f['torso'] in cs:f['torso_members']=list(cs[f['torso']])

   (OUT/'before'/f'{i.icon_id}.svg').write_text(original.to_svg());(OUT/'after'/f'{i.icon_id}.svg').write_text(i.to_svg())
   result=dict(a,reasons=reason,before_qa=before,after_qa=after,after_record=i.to_record(),after_figures=evaluate(i,after_fs))
   results.append(result);(OUT/'repairs.json').write_text(json.dumps(results,indent=2));print(a['number'],i.icon_id,before['status'],'->',after['status'],after['errors'][:2],flush=True)
 (OUT/'repairs.json').write_text(json.dumps(results,indent=2))
