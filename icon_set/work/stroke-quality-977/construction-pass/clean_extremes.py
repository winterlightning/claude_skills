"""Absorb microscopic contour knots into their neighboring cubic, retaining extremes."""
import sys,json,re,math,itertools
from pathlib import Path
from dataclasses import replace
H=Path(__file__).resolve().parent;ROOT=H.parents[3];sys.path.insert(0,str(ROOT))
from icon_set.model.icons.registry import create
from icon_set.model.primitives import Bezier
from icon_set.validation.library_qa import inspect_icon
from normalize import code
SOURCE_ICON_ID=None
SOURCE_PATH='icon_set/work/intersection-review-977/cohort.json'
AUTHOR='gpt-6'
rows={r['id']:r for r in json.loads((H/'baseline.json').read_text())};accepted=[];declined=[]
for row in json.loads((H/'cubic-declined.json').read_text()):
 id=row['id'];icon=create(id);new=[];details=[]
 for p in icon.primitives:
  if not isinstance(p,Bezier):new.append(p);continue
  pts=[p.start.as_tuple(),p.end.as_tuple(),*p.extrema()];limits=[(min(x[k] for x in pts),max(x[k] for x in pts)) for k in range(2)]
  segs=[];start=p.start.as_tuple();shift=(0,0)
  for j,(c1,c2,end) in enumerate(p.segments):
   diameter=max(math.dist(a,b) for a,b in itertools.combinations([start,c1,c2,end],2))
   if diameter<.2 and segs and j<len(p.segments)-1:
    point=list(end)
    for k,(lo,hi) in enumerate(limits):
     if min(abs(start[k]-lo),abs(end[k]-lo))<1e-8:point[k]=lo
     elif min(abs(start[k]-hi),abs(end[k]-hi))<1e-8:point[k]=hi
    a,b,old=segs[-1];delta=tuple(point[k]-old[k] for k in range(2))
    segs[-1]=(a,tuple(b[k]+delta[k] for k in range(2)),tuple(point));shift=tuple(point[k]-end[k] for k in range(2))
    details.append((p.element_id,j));start=end;continue
   segs.append((tuple(c1[k]+shift[k] for k in range(2)),c2,end));shift=(0,0);start=end
  new.append(replace(p,segments=tuple(segs)))
 if not details:continue
 icon.primitives=new;q=inspect_icon(icon)
 if q['status']!='pass' or q['warnings']:declined.append(dict(id=id,validation=q));continue
 p=ROOT/rows[id]['source'];s=p.read_text();s=s[:s.index('    def build(')];s=re.sub(r'REVIEW_ACTION = .*',"REVIEW_ACTION = 'geometry-reconstructed'",s)
 s+='    def build(self):\n        # Plan: absorb microscopic detours into neighboring cubics; retain the true extremes.\n        # Reference: original stroke graph and contour extremes.\n'+code(icon);p.write_text(s)
 accepted.append(dict(id=id,source=rows[id]['source'],plan=f'Absorb {len(details)} microscopic detours into their neighboring curves while preserving the exact contour extremes.',reference='Original subject; individual cubic and extreme-point inspection.',details=details))
(H/'cubic-extremes.json').write_text(json.dumps(accepted,indent=2));(H/'cubic-extremes-declined.json').write_text(json.dumps(declined,indent=2,default=str));print('Cleaned:',len(accepted),'Deferred:',len(declined));print(', '.join(r['id'] for r in accepted))
