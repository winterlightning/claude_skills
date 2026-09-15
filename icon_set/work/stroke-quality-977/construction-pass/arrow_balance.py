import json,sys,re
from pathlib import Path
from collections import defaultdict
from dataclasses import replace
H=Path(__file__).resolve().parent;ROOT=H.parents[3];sys.path.insert(0,str(ROOT))
from icon_set.model.icons.registry import create
from icon_set.model.primitives import Line,Point
from icon_set.validation.library_qa import inspect_icon
from normalize import code
rows=json.loads((H/'baseline.json').read_text());accepted=[];declined=[]
for row in rows:
 id=row['id']
 if not any(s in id for s in ['arrow','direction','navigation','move-','angles-','side-road']):continue
 icon=create(id)
 if len(icon.primitives)!=3 or not all(isinstance(p,Line) for p in icon.primitives):continue
 ends=defaultdict(list)
 for p in icon.primitives:
  for side in ['start','end']:ends[getattr(p,side).as_tuple()].append((p,side))
 hubs=[(pt,parts) for pt,parts in ends.items() if len(parts)==3]
 if len(hubs)!=1:continue
 (x,y),parts=hubs[0];arms=[];stem=[]
 for p,side in parts:
  end=getattr(p,'end' if side=='start' else 'start').as_tuple();dx,dy=end[0]-x,end[1]-y
  (stem if dx==0 or dy==0 else arms).append((p,side,end))
 if len(stem)!=1 or len(arms)!=2:continue
 axis=0 if stem[0][2][1]==y else 1;other=1-axis;hub=(x,y)
 if (arms[0][2][other]-hub[other])*(arms[1][2][other]-hub[other])>=0:continue
 if (arms[0][2][axis]-hub[axis])*(arms[1][2][axis]-hub[axis])<=0:continue
 depth=max(abs(a[2][axis]-hub[axis]) for a in arms);width=max(abs(a[2][other]-hub[other]) for a in arms);moves={}
 for p,side,e in arms:
  ep=list(e);ep[axis]=hub[axis]+(depth if e[axis]>hub[axis] else -depth);ep[other]=hub[other]+(width if e[other]>hub[other] else -width)
  if tuple(ep)!=e:moves[p.element_id]=('end' if side=='start' else 'start',tuple(ep))
 if not moves:continue
 icon.primitives=[replace(p,**{moves[p.element_id][0]:Point(*moves[p.element_id][1])}) if p.element_id in moves else p for p in icon.primitives]
 q=inspect_icon(icon)
 if q['status']!='pass' or q['warnings']:declined.append(dict(id=id,validation=q));continue
 p=ROOT/row['source'];s=p.read_text();s=s[:s.index('    def build(')];s=re.sub(r'REVIEW_ACTION = .*',"REVIEW_ACTION = 'geometry-reconstructed'",s)
 s+='    def build(self):\n        # Plan: exact reflection of both arrowhead arms about the shaft.\n        # Reference: the existing directional symbol and shared dimensions.\n'+code(icon);p.write_text(s)
 accepted.append(dict(id=id,source=row['source'],plan='Equal arrowhead arms reflected exactly about the shaft; the original directional vocabulary is preserved.',reference='Original directional symbol; shared arm depth and spread.',details=moves))
(H/'arrow-balance.json').write_text(json.dumps(accepted,indent=2));(H/'arrow-balance-declined.json').write_text(json.dumps(declined,indent=2));print('Balanced',len(accepted),'Declined',len(declined));print(', '.join(r['id'] for r in accepted))
