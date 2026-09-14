"""Check authored connections against actual emitted paths, without declarations."""
import json,itertools
from pathlib import Path
from dataclasses import asdict
from icon_set.model.icons.registry import create
from icon_set.renderers.svg import build_paths
from icon_set.validation.path_commands import commands_for_path
from icon_set.validation.stroke_distance import analyze_paths
w=Path('icon_set/work/parallel-spacing-repair');names=json.loads((w/'notes.json').read_text());findings=[]
for name in names:
 icon=create(name);paths=build_paths(icon.draw());lookup={p['id']:{'id':p['id'],'commands':commands_for_path(p['primitives'],p['closed'])} for p in paths}
 owner={m:p['id'] for p in paths for m in p['members']}
 for relation in icon.relationships:
  if relation.kind!='connect':continue
  for first,second in itertools.combinations(relation.members,2):
   a=first if first in lookup else owner[first];b=second if second in lookup else owner[second]
   if a==b:continue
   result=analyze_paths([lookup[a],lookup[b]])
   if result['connectedPairs']:continue
   pairs=result['pairs']
   distance=min((p['centerlineDistance'] for p in pairs),default=999)
   # Actual curve intersections can be approximated by the distance routine.
   if distance>0.002:
    findings.append({'icon':name,'parts':[first,second],'distance':round(distance,5)})
    print(name,first,second,round(distance,5),flush=True)
(w/'contact-findings.json').write_text(json.dumps(findings,indent=2))
print('UNRESOLVED CONTACTS',len(findings))
