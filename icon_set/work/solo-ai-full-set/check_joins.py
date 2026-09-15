from pathlib import Path
import sys,json
ROOT=Path(__file__).resolve().parents[3];sys.path.insert(0,str(ROOT))
from icon_set.model.icons.registry import create
AUTHOR='gpt-6';SOURCE_ICON_ID=None;SOURCE_PATH='icon_set/work/solo-ai-full-set/batch.json'
w=Path(__file__).parent;bad=[]
for r in json.loads((w/'batch.json').read_text()):
 i=create(r['icon_id']);points={}
 for p in i.primitives:
  points[p.element_id]={(v.x,v.y) for v in [getattr(p,'start',None),getattr(p,'end',None)] if v is not None}
  if hasattr(p,'points'):points[p.element_id].update((v.x,v.y) for v in p.points)
 for c in i.contours:points[c.contour_id]=set().union(*(points[m] for m in c.members))
 for rel in i.relationships:
  if rel.kind=='connect':
   a,b=rel.members
   if not points.get(a,set())&points.get(b,set()):bad.append(dict(parent=r['parent'],a=a,b=b))
(w/'join-check.json').write_text(json.dumps(bad,indent=2))
for r in bad:print(r)
print(len(bad))
