from pathlib import Path
import json,math
from shapely.geometry import shape,Polygon
from shapely.affinity import translate
from icon_set.scripts.container_placement import Artwork
from icon_set.scripts.container_vector_geometry import VectorInk
base=Path('icon_set');rows=json.loads((base/'work/container-fit-repair/before.json').read_text());v={c['container']:c for c in json.loads((base/'work/container-vector-report/results.json').read_text())['containers']}
subs={n:VectorInk.from_art(Artwork.read((base/f'dist/sub32/{n}.svg').read_text(),32)).envelope(2,True) for n in ['check-mark','add-sub32','heart-state-63']}
for r in rows:
 c=v[r['container']];r['shifted']={};r['unresolved']=[]
 if c['status']!='vector':
  r['unresolved']=r['failed'];continue
 zone=shape(c['safe_zone_inner']);x0,y0,x1,y1=zone.bounds
 for name in r['failed']:
  ink=subs[name];a,b,d,e=ink.bounds
  xmin,xmax=math.ceil((x0-a)*2)/2,math.floor((x1-d)*2)/2
  ymin,ymax=math.ceil((y0-b)*2)/2,math.floor((y1-e)*2)/2
  candidates=[(xmin+i*.5,ymin+j*.5) for i in range(max(0,round((xmax-xmin)*2)+1)) for j in range(max(0,round((ymax-ymin)*2)+1))]
  # Prioritize the content centerline before considering lateral movement.
  candidates.sort(key=lambda p:(round(abs(p[0]+16-r['center'][0]),6), round(abs(p[1]+16-r['center'][1]),6)))
  match=next((p for p in candidates if zone.covers(translate(ink,*p))),None)
  if match:r['shifted'][name]=[match[0]+16,match[1]+16]
  else:r['unresolved'].append(name)
# Optical placements retain native symbol dimensions and are revalidated by build_report.py.
preferences=json.loads((base/'data/container-placement-preferences.json').read_text())
for r in rows:
 for symbol,center in preferences['optical_overrides'].get(r['container'],{}).items():
  if symbol in r['shifted']:r['shifted'][symbol]=center
Path('icon_set/work/container-fit-repair/placement-search.json').write_text(json.dumps(rows,indent=2))
print('failed hosts',sum(bool(r['failed']) for r in rows),'still unresolved',sum(bool(r['unresolved']) for r in rows),'shifted pairs',sum(len(r['shifted']) for r in rows))
print('\n'.join(r['container']+' '+','.join(r['unresolved']) for r in rows if r['unresolved']))
