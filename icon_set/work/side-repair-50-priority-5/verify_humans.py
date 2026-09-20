"""Verify actual detached head-to-shoulder gaps for repaired human busts."""
import json,sys
from pathlib import Path
W=Path(__file__).resolve().parent;sys.path.insert(0,str(W.parents[2]))
from icon_set.model.icons.registry import create
from icon_set.validation.envelope import centerline_bounds
c=json.loads((W/'candidates.json').read_text());out={}
pairs={2:[('head-l',('side-l','shoulder-l','back-tip')),('head-r',('front-l','front-top','front-r'))],3:[('left-head',('left-shoulders',)),('right-head',('right-shoulders',))],6:[('back-head',('back-l','back-r')),('front-head',('front-l','front-r'))],31:[('head',('left','right'))]}
for n,subjects in pairs.items():
 p=create(c[str(n)]['icon']).draw().primitives;checks=[]
 for name,body in subjects:
  head=[v for v in p if v.element_id.startswith(name+'-')];shoulder=[v for v in p if v.element_id in body]
  hb=centerline_bounds(head);sb=centerline_bounds(shoulder);gap=sb[1]-hb[3]-4
  assert abs(gap-4)<1e-7,(n,name,gap)
  assert abs((hb[2]-hb[0])-(hb[3]-hb[1]))<1e-7
  checks.append(dict(head=name,ink_gap=gap,circular_head=True))
 out[n]=checks
(W/'human-verification.json').write_text(json.dumps(out,indent=2));print('Seven circular heads have exactly 4px visible separation from their own shoulders.')
