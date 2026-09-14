from fit_candidates import W
from icon_set.model.icons.registry import create
from icon_set.model.keyshapes import Keyshape
import json
SOURCE_ICON_ID=None
SOURCE_PATH='icon_set/work/wide-tall-repair/targets.json'
AUTHOR='gpt-6'
for f in sorted((W/'candidates').glob('*.json')):
 x=json.loads(f.read_text())
 if x['report']['validation']['status']=='pass':continue
 o=create(f.stem)
 for k in [Keyshape.SQUARE,Keyshape.VRECT_L,Keyshape.HRECT_L]:
  if k.name==x['record']['keyshape']:continue
  c=o.fit_to_keyshape(k,force_stretch=True);q=c.report['validation']
  if q['status']=='pass':
   f.write_text(json.dumps({'record':c.icon.to_record(),'report':c.report},indent=2));print(f.stem,k.name,flush=True);break
