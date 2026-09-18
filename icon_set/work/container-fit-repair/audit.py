from pathlib import Path
import json
from shapely.geometry import shape
from icon_set.scripts.container_placement import Artwork
from icon_set.scripts.container_vector_geometry import VectorInk,read_art,check_pair
BASE=Path('icon_set')
v=json.loads((BASE/'work/container-vector-report/results.json').read_text())['containers']
a=json.loads((BASE/'data/container-content-areas.json').read_text())['areas']
subs={name:Artwork.read((BASE/f'dist/sub32/{name}.svg').read_text(),32) for name in ['check-mark','add-sub32','heart-state-63']}
results=[]
for c in v:
 name=c['container'];center=c.get('center_units') or a[name]['center']
 host=VectorInk.from_art(read_art((BASE/f'dist/container64/{name}.svg').read_text()))
 inner=shape(c['safe_zone_inner']) if 'safe_zone_inner' in c else None
 outer=shape(c['safe_zone_outer']) if 'safe_zone_outer' in c else None
 pairs={}
 for sub,art in subs.items():
  ink=VectorInk.from_art(art,(1,center[0]-16,center[1]-16))
  pairs[sub]=check_pair(host,ink,inner,outer)
 results.append({'container':name,'center':center,'pairs':pairs,'failed':[n for n,p in pairs.items() if p['gap_status']=='fail']})
Path('icon_set/work/container-fit-repair/before.json').write_text(json.dumps(results,indent=2))
from collections import Counter
print(Counter(len(r['failed']) for r in results))
print('\n'.join(r['container']+' '+','.join(r['failed']) for r in results if r['failed']))
