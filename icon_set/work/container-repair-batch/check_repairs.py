import json
from pathlib import Path
from collections import Counter
from icon_set.model.icons.registry import create
from icon_set.scripts.container_placement import Artwork
from icon_set.scripts.container_vector_geometry import VectorInk,read_art,vector_zone,check_pair
from icon_set.scripts.build_all_container_combinations import PreparedSub
OUT=Path(__file__).parent
baseline=json.loads((OUT/'baseline.json').read_text());variants=json.loads((OUT/'variants.json').read_text());cache={};results=[]
for variant in variants:
 model=create(variant['variant'] if Path(variant['module']).exists() else variant['parent']);doc=model.to_svg();(OUT/(variant['variant']+'.svg')).write_text(doc);validation=model.validate_icon().describe();x,y=variant['center'];ink=VectorInk.from_art(read_art(doc));zone,inner,outer=vector_zone(ink,{'kind':'safe-zone','method':'selected semantic enclosed face','polygon':[[x-1,y-1],[x+1,y-1],[x+1,y+1],[x-1,y+1]]});pairs=[]
 for idx,row in enumerate(baseline['rows']):
  if baseline['hosts'][row[0]]['name']!=variant['parent']:continue
  sub=baseline['subs'][row[1]]
  if row[1] not in cache:
   try:cache[row[1]]=PreparedSub(Artwork.read(sub['svg32'],32),32) if sub['width']==sub['height']==32 else None
   except ValueError:cache[row[1]]=None
  subink=cache[row[1]]
  if subink is None:continue
  result=check_pair(ink,subink.at([x,y]),inner,outer)
  small=check_pair(ink,PreparedSub(Artwork.read(sub['svg32'],32),24).at([x,y]),inner,outer)
  pairs.append({'small_after':small['status'],'small_gap':small['ink_gap_lower_units'],'row':idx,'sub':sub['name'],'before':row[7],'after':result['status'],'gap':result['ink_gap_lower_units'],'containment':result['containment_status']})
 record={**variant,'validation':validation,'zone':zone,'pairs':pairs};results.append(record)
 print(variant['variant'],validation.replace('\n',' | '),zone['status'],dict(Counter(p['after'] for p in pairs)),'regressions',sum(p['before']=='pass' and p['after']!='pass' for p in pairs),flush=True)
(OUT/'measured.json').write_text(json.dumps(results,indent=2))
