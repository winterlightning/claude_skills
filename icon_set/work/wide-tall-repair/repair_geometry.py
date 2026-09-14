from pathlib import Path
import sys,json
ROOT=Path(__file__).resolve().parents[3];sys.path.insert(0,str(ROOT))
from icon_set.model.icons.registry import create
from icon_set.model.primitives import primitive_from_dict,Contour,Relationship
from icon_set.model.keyshapes import Keyshape
from icon_set.validation.library_qa import inspect_icon
SOURCE_ICON_ID=None
SOURCE_PATH='icon_set/work/wide-tall-repair/targets.json'
AUTHOR='gpt-6'
W=Path(__file__).parent

def model(ident,r):
 o=create(ident);o.keyshape=Keyshape[r['keyshape']];o.primitives=[primitive_from_dict(p) for p in r['primitives']];o.contours=[Contour(c['contour_id'],tuple(c['members']),c['closed']) for c in r['contours']];o.relationships=[Relationship(c['kind'],tuple(c['members'])) for c in r['relationships']];return o

def check(f,x):
 q=inspect_icon(model(f.stem,x['record']));q.pop('_svg',None);x['report']['validation']=q;f.write_text(json.dumps(x,indent=2));return q

if __name__=='__main__':
 for f in (W/'candidates').glob('*.json'):
  x=json.loads(f.read_text());o=create(f.stem);orig={p.element_id:p for p in o.primitives}
  if x['report']['validation']['status']=='pass':continue
  changed=False
  for p in x['record']['primitives']:
   a=orig.get(p['element_id'])
   if p['kind']!='arc' or not hasattr(a,'radius_x'):continue
   dx=abs(a.start.x-a.end.x);dy=abs(a.start.y-a.end.y)
   if dx==a.radius_x and dy==a.radius_y:
    nx=abs(p['start'][0]-p['end'][0]);ny=abs(p['start'][1]-p['end'][1])
    if nx and ny:p['radius_x']=nx;p['radius_y']=ny;changed=True
  if changed:q=check(f,x);print(f.stem,q['status'],flush=True)
