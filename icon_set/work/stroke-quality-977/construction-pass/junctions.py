import json,sys
from pathlib import Path
H=Path(__file__).resolve().parent;sys.path.insert(0,str(H.parents[3]))
from icon_set.model.icons.registry import create
from audit import samples
from shapely.geometry import LineString,Point
from shapely.ops import unary_union
rows=json.loads((H/'baseline.json').read_text());out=[]
for row in rows:
 icon=create(row['id']);prims={p.element_id:p for p in icon.primitives};owners={c.contour_id:c for c in icon.contours}
 groups={c.contour_id:list(c.members) for c in icon.contours};used={x for c in icon.contours for x in c.members}
 groups.update({id:[id] for id in prims if id not in used});lines={k:unary_union([LineString(samples(prims[id])) for id in ids]) for k,ids in groups.items()}
 closed={c.contour_id for c in icon.contours if c.closed};issues=[]
 for rel in icon.relationships:
  if rel.kind!='connect':continue
  for a in rel.members:
   for b in rel.members:
    if a==b or b not in closed or a not in groups or a in closed:continue
    ids=groups[a];ends=[prims[ids[0]].start.as_tuple(),prims[ids[-1]].end.as_tuple()]
    for p in set(ends):
     dist=Point(p).distance(lines[b])
     if .03<dist<2:issues.append(dict(stroke=a,target=b,endpoint=p,distance=round(dist,4)))
 if issues:out.append(dict(id=row['id'],issues=issues));print(row['id'],issues)
(H/'junction-findings.json').write_text(json.dumps(out,indent=2))
