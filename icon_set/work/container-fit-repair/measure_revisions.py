from pathlib import Path
import json
from shapely.geometry import box
from icon_set.model.icons.registry import create
from icon_set.scripts.container_placement import Artwork,validate_padding
from icon_set.scripts.container_vector_geometry import VectorInk,read_art,check_pair,vector_zone
base=Path('icon_set');root=base/'work/container-fit-repair'
rows=json.loads((root/'variants.json').read_text());subs={n:Artwork.read((base/f'dist/sub32/{n}.svg').read_text(),32) for n in ['check-mark','add-sub32','heart-state-63']}
for r in rows:
 model=create(r['variant']);r['validation']=model.validate_icon().describe()
 document=model.to_svg();(root/(r['variant']+'.svg')).write_text(document)
 host=read_art(document);host_ink=VectorInk.from_art(host);x,y=r['center']
 # Identify the enclosed face using an interior seed independent of old raster geometry.
 summary,inner,outer=vector_zone(host_ink,{'kind':'safe-zone','method':'selected semantic enclosed face','polygon':[[x-1,y-1],[x+1,y-1],[x+1,y+1],[x-1,y+1]]})
 if inner is None:
  # Open webcam screen: an explicit local content rectangle for this fit test.
  # It is only the tested content footprint, not a claim of maximal empty area.
  inner=outer=box(x-17,y-17,x+17,y+17)
  summary={'status':'explicit-test-region','reason':'Bounded test rectangle inside the display; actual host clearance checked separately.'}
 r['area']=summary;r['pairs']={}
 for n,art in subs.items():
  transform=(1,x-16,y-16)
  ink=VectorInk.from_art(art,transform);p=check_pair(host_ink,ink,inner,outer)
  if p['gap_status']=='review':
   exact=validate_padding(host,art,transform,2)
   p['exact_gap_verification']=exact
   if exact['status']=='pass':p['gap_status']='pass'
  r['pairs'][n]=p
 print(r['variant'],r['validation'],[(n,p['gap_status'],p['containment_status'],round(p['ink_gap_lower_units'],5)) for n,p in r['pairs'].items()],flush=True)
(root/'revisions-measured.json').write_text(json.dumps(rows,indent=2))
