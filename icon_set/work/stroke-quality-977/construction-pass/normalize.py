"""Normalize exact straight runs and short corner artifacts in existing models.
Candidate plans are individually recorded and checked before publication.
"""
import sys,json,math,copy,re,itertools
from dataclasses import replace
from pathlib import Path
H=Path(__file__).resolve().parent;ROOT=H.parents[3];sys.path.insert(0,str(ROOT))
from icon_set.model.icons.registry import create
from icon_set.model.primitives import Line,Arc,Bezier,Point,Contour,Relationship
from icon_set.validation.library_qa import inspect_icon
from audit import samples
from shapely.geometry import LineString,Point as SPoint
SOURCE_ICON_ID=None
SOURCE_PATH='icon_set/work/intersection-review-977/cohort.json'
AUTHOR='gpt-6'
rows=json.loads((H/'baseline.json').read_text());manual={r['id'] for r in json.loads((H/'changes.json').read_text())}

def code(icon):
 out=[]
 for p in icon.primitives:
  if isinstance(p,Line):out.append(f"self.add_line({p.element_id!r}, {p.start.as_tuple()!r}, {p.end.as_tuple()!r})")
  elif isinstance(p,Arc):out.append(f"self.add_arc({p.element_id!r}, {p.start.as_tuple()!r}, {p.end.as_tuple()!r}, radius_x={p.radius_x}, radius_y={p.radius_y}, large_arc={p.large_arc}, sweep={p.sweep})")
  else:out.append(f"self.add_bezier({p.element_id!r}, {p.start.as_tuple()!r}, "+', '.join(repr(x) for x in p.segments)+')')
 for c in icon.contours:out.append(f"self.add_contour({c.contour_id!r}, "+', '.join(repr(x) for x in c.members)+f", closed={c.closed})")
 for r in icon.relationships:out.append(f"self.relate({r.kind!r}, "+', '.join(repr(x) for x in r.members)+')')
 return '\n'.join('        '+x for x in out)+'\n'

def simplify(icon):
 original={p.element_id:p for p in icon.primitives};updates={};remove=set();plans=[]
 # Only replace short transition chains between the owning contour's long lines.
 for c in icon.contours:
  members=list(c.members);long=[i for i,id in enumerate(members) if isinstance(original[id],Line) and math.dist(original[id].start.as_tuple(),original[id].end.as_tuple())>=5]
  if len(long)<2:continue
  pairs=list(zip(long,long[1:]))+([(long[-1],long[0]+len(members))] if c.closed else [])
  for ia,ib in pairs:
   mids=[members[i%len(members)] for i in range(ia+1,ib)]
   if not mids:continue
   if any(LineString(samples(original[id])).length>4.8 for id in mids):continue
   a=updates.get(members[ia],original[members[ia]]);b=updates.get(members[ib%len(members)],original[members[ib%len(members)]])
   x1,y1=a.start.as_tuple();x2,y2=a.end.as_tuple();x3,y3=b.start.as_tuple();x4,y4=b.end.as_tuple()
   den=(x1-x2)*(y3-y4)-(y1-y2)*(x3-x4)
   if abs(den)<1e-9:
    # Collinear consecutive lines can share one run without a tiny pseudo-arc.
    cross=(x2-x1)*(y3-y1)-(y2-y1)*(x3-x1)
    if abs(cross)>1e-9:continue
    pts=[q for id in mids for q in samples(original[id])]
    line=LineString([a.start.as_tuple(),b.end.as_tuple()])
    if max(SPoint(p).distance(line) for p in pts)>.035:continue
    # Keep the attachment node and remove only the intervening detour.
    if math.dist(a.end.as_tuple(),b.start.as_tuple())>3:continue
    knot=b.start
   else:
    f1=x1*y2-y1*x2;f2=x3*y4-y3*x4
    xx=(f1*(x3-x4)-(x1-x2)*f2)/den;yy=(f1*(y3-y4)-(y1-y2)*f2)/den
    if abs(xx-round(xx))>1e-9 or abs(yy-round(yy))>1e-9:continue
    knot=Point(round(xx),round(yy))
    if max(math.dist(knot.as_tuple(),a.end.as_tuple()),math.dist(knot.as_tuple(),b.start.as_tuple()))>3.1:continue
   if knot==a.start or knot==b.end:continue
   # A connector used as an attachment by a separate primitive is not discarded.
   attached=any(q.element_id not in c.members and (q.start in [original[id].start for id in mids] or q.end in [original[id].end for id in mids]) for q in icon.primitives)
   if attached:continue
   updates[a.element_id]=replace(a,end=knot);updates[b.element_id]=replace(b,start=knot);remove.update(mids)
   plans.append(dict(kind='coherent-straight-junction',a=a.element_id,b=b.element_id,node=knot.as_tuple(),removed=mids))
 if not plans:return []
 icon.primitives=[updates.get(p.element_id,p) for p in icon.primitives if p.element_id not in remove]
 icon.contours=[replace(c,members=tuple(id for id in c.members if id not in remove)) for c in icon.contours]
 # Remove duplicate relation declarations; preserve all actual surviving owners.
 refs={p.element_id for p in icon.primitives}|{c.contour_id for c in icon.contours};seen=set();rels=[]
 for r in icon.relationships:
  members=tuple(x for x in r.members if x in refs);key=(r.kind,tuple(sorted(members)))
  if len(members)>1 and key not in seen:seen.add(key);rels.append(Relationship(r.kind,members))
 icon.relationships=rels
 return plans

if __name__=='__main__':
 accepted=[];declined=[]
 for row in rows:
  if row['id'] in manual:continue
  icon=create(row['id']);plans=simplify(icon)
  if not plans:continue
  try:q=inspect_icon(icon)
  except Exception as e:q=dict(status='exception',errors=[str(e)],warnings=[])
  if q['status']!='pass' or q['warnings']:
   declined.append(dict(id=row['id'],plans=plans,validation=q));continue
  p=ROOT/row['source'];s=p.read_text();s=s[:s.index('    def build(')];s=re.sub(r'REVIEW_ACTION = .*',"REVIEW_ACTION = 'geometry-reconstructed'",s)
  s+='    def build(self):\n        # Plan: restore exact straight junctions; remove short fitted corner detours.\n        # Reference: existing subject and its ideal straight-edge intersections.\n'+code(icon)
  p.write_text(s);accepted.append(dict(id=row['id'],source=row['source'],plan='Restore exact straight-edge junctions and remove short fitted detours at '+', '.join(str(p['node']) for p in plans)+'.',reference='Original subject geometry; integer intersections of its straight edges.',details=plans))
 (H/'normalized.json').write_text(json.dumps(accepted,indent=2));(H/'normalize-declined.json').write_text(json.dumps(declined,indent=2,default=str))
 print('Straight junctions repaired:',len(accepted),'Deferred:',len(declined));print(', '.join(r['id'] for r in accepted))
