"""Remove subpixel cubic detours hidden inside traced strokes."""
import json,sys,re,math,itertools
from pathlib import Path
from dataclasses import replace
H=Path(__file__).resolve().parent;ROOT=H.parents[3];sys.path.insert(0,str(ROOT))
from icon_set.model.icons.registry import create
from icon_set.model.primitives import Bezier,Line
from icon_set.validation.library_qa import inspect_icon
from normalize import code
SOURCE_ICON_ID=None
SOURCE_PATH='icon_set/work/intersection-review-977/cohort.json'
AUTHOR='gpt-6'
rows=json.loads((H/'baseline.json').read_text());out=[];declined=[]
for row in rows:
 if not any(i['kind']=='degenerate-cubic' for i in row['issues']):continue
 icon=create(row['id']);prims=[];details=[]
 for p in icon.primitives:
  if not isinstance(p,Bezier):prims.append(p);continue
  segments=[];start=p.start.as_tuple()
  for j,(c1,c2,end) in enumerate(p.segments):
   diameter=max(math.dist(a,b) for a,b in itertools.combinations([start,c1,c2,end],2))
   if diameter<.2 and (start==end or j<len(p.segments)-1):
    details.append(dict(primitive=p.element_id,segment=j,diameter=diameter));continue
   segments.append((c1,c2,end));start=end
  # A standalone intentionally shaped point still emits one proper round dot.
  prims.append(replace(p,segments=tuple(segments)) if segments else Line(p.element_id,p.start,p.end))
 if not details:continue
 icon.primitives=prims
 q=inspect_icon(icon)
 if q['status']!='pass' or q['warnings']:declined.append(dict(id=row['id'],details=details,validation=q));continue
 p=ROOT/row['source'];s=p.read_text();s=s[:s.index('    def build(')];s=re.sub(r'REVIEW_ACTION = .*',"REVIEW_ACTION = 'geometry-reconstructed'",s)
 s+='    def build(self):\n        # Plan: remove subpixel cubic detours while preserving real contour nodes.\n        # Reference: supplied subject and its existing stroke graph.\n'+code(icon);p.write_text(s)
 out.append(dict(id=row['id'],source=row['source'],plan=f'Remove {len(details)} subpixel cubic detours inside the stroke; preserve the real contour and attachment nodes.',reference='Original subject; exact stroke graph inspection.',details=details))
(H/'cubic-cleaned.json').write_text(json.dumps(out,indent=2));(H/'cubic-declined.json').write_text(json.dumps(declined,indent=2,default=str))
print('Cleaned',len(out),'icons,',sum(len(r['details']) for r in out),'detours. Declined:',len(declined));print(', '.join(r['id'] for r in out))
