"""Build only the defined container combinations from combination_data.json."""
from pathlib import Path
import json,hashlib,xml.etree.ElementTree as ET
from collections import Counter
from shapely.geometry import shape
from icon_set.scripts.build_all_container_combinations import PreparedSub
from icon_set.scripts.container_placement import Artwork,root_svg,artwork_group
from icon_set.scripts.container_vector_geometry import VectorInk,read_art,reject_effects,check_pair,vector_zone
from icon_set.scripts.suggest_container_sub_size import transform,recommendation
BASE=Path(__file__).resolve().parents[1];ROOT=BASE.parent
OUT=BASE/'work/container-pair-combinations'

def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def main():
 OUT.mkdir(parents=True,exist_ok=True)
 definitions=json.loads((ROOT/'combination_data.json').read_text())['container']
 catalog={r['id']:r for r in json.loads((BASE/'dist/gallery/combinations.json').read_text())['rows'] if r['kind']=='container'}
 audit={r['container']:r for r in json.loads((BASE/'work/container-vector-report/results.json').read_text())['containers']}
 areas=json.loads((BASE/'data/container-content-areas.json').read_text())['areas']
 prefs=json.loads((BASE/'data/container-placement-preferences.json').read_text())
 fixes=json.loads((BASE/'work/container-fit-repair/fit-adjustments.json').read_text())
 hosts=[];subs=[];hi={};si={};hgeo={};sgeo={};rows=[];missing=[];labels=['keep-32','suggest-24','no-fit-at-center','review','blocked']
 for definition in definitions:
  cat=catalog.get(definition['id'])
  if cat is None:missing.append(dict(definition,reason='Pair not resolved in generated catalog'));continue
  mains=cat.get('main_generated',[]);children=cat.get('sub_generated',[])
  if not mains or not children:missing.append(dict(definition,reason='Missing mapped component'));continue
  for hg in mains:
   parent=hg['icon_id'];revision=fixes.get('revisions',{}).get(parent);hn=revision['variant'] if revision else parent;hp=(BASE/'work/container-fit-repair'/(hn+'.svg')) if revision else (BASE/'dist/gallery'/hg['preview_url']).resolve()
   if not hp.is_file():missing.append(dict(definition,reason='Container asset missing: '+hn));continue
   if hn not in hi:
    idx=len(hosts);hi[hn]=idx;doc=hp.read_text();digest=sha(hp);c=audit.get(hn,{});center=c.get('center_units') or areas.get(hn,{}).get('center') or [32,32]
    center=revision['center'] if revision else prefs.get('container_centers',{}).get(parent,center)
    h={'parent':parent,'revised':bool(revision),'repair_batch':revision.get('batch') if revision else None,'name':hn,'svg':doc,'sha256':digest,'center':center,'area_status':c.get('status','review')}
    try:
     ink=VectorInk.from_art(read_art(doc))
     if revision:
      if revision['variant_sha256']!=digest:raise ValueError('Stale revision')
      x,y=center
      zone,inner,outer=vector_zone(ink,{'kind':'safe-zone','method':'selected semantic enclosed face','polygon':[[x-1,y-1],[x+1,y-1],[x+1,y+1],[x-1,y+1]]})
      h['area_status']=zone['status']
     else:
      if c.get('source_sha256')!=digest:raise ValueError('Missing or stale interior audit')
      inner=shape(c['safe_zone_inner']) if 'safe_zone_inner' in c else None;outer=shape(c['safe_zone_outer']) if 'safe_zone_outer' in c else None
     hgeo[idx]=(ink,inner,outer)
    except (ValueError,KeyError) as e:h['error']=str(e)
    hosts.append(h)
   hx=hi[hn]
   seen_children=set()
   for sg in children:
    sub_revision=fixes.get('sub_revisions',{}).get(parent,{}).get(sg['icon_id'])
    sn=sub_revision['variant'] if sub_revision else sg['icon_id'];sp=Path(sub_revision['path']) if sub_revision else (BASE/'dist/gallery'/sg['preview_url']).resolve()
    if not sp.is_file():missing.append(dict(definition,reason='Sub asset missing: '+sn));continue
    key=(sn,str(sp))
    if key in seen_children:continue
    seen_children.add(key)
    if key not in si:
     sx=len(subs);si[key]=sx;doc=sp.read_text();root=ET.fromstring(doc);vb=[float(x) for x in root.get('viewBox','0 0 32 32').split()];s={'name':sn,'sha256':sha(sp),'svg32':doc,'width':vb[2],'height':vb[3],'model_validation':sub_revision['model_validation'] if sub_revision else sg.get('model_validation','unknown')}
     try:
      if vb!=[0,0,32,32]:raise ValueError('Wide or non-square profile: native dimensions retained; layout review required')
      reject_effects(doc);art=Artwork.read(doc,32)
      if min(art.bounds[:2])<2-1e-6 or max(art.bounds[2:])>30+1e-6:raise ValueError('Source exceeds SUB32 drafting extent')
      sgeo[sx]={size:PreparedSub(art,size) for size in (32,24)}
      root=root_svg();root.set('viewBox','0 0 32 32');root.append(artwork_group(art,'sub',*transform(24,[16,16]),stroke=4));s['svg24']=ET.tostring(root,encoding='unicode')
     except ValueError as e:s['error']=str(e)
     subs.append(s)
    sx=si[key];s=subs[sx];h=hosts[hx];center=prefs.get('optical_overrides',{}).get(hn,{}).get(sn)
    saved=fixes.get('placements',{}).get(hn,{}).get(sn,{})
    if center is None and saved.get('visual_status')=='centerline-priority' and saved.get('host_sha256')==h['sha256'] and saved.get('sub_sha256')==s['sha256']:center=saved['center']
    center=center or h['center'];center=[round(v) if abs(v-round(v))<1e-9 else v for v in center];gaps=[None,None];fits=[None,None]
    if hx not in hgeo or sx not in sgeo:status='blocked'
    else:
     ink,inner,outer=hgeo[hx]
     for k,size in enumerate((32,24)):
      m=check_pair(ink,sgeo[sx][size].at(center),inner,outer);fits[k]=m['status'];gaps[k]=[m['ink_gap_lower_units'],m['ink_gap_upper_units']]
     status=recommendation({'status':fits[0]},{'status':fits[1]}) if inner is not None else 'review'
     if s['model_validation']!='pass':status='review'
    rows.append([hx,sx,labels.index(status),*center,*gaps,*fits,definition['id'],definition['concept'],definition['main_id'],definition['sub_id']])
 # Recommendations describe future authored grid variants, never preview scaling.
 for row in rows:
  host=hosts[row[0]];sub=subs[row[1]];suggestion=''
  if row[7] in ('fail','review'):
   suggestion='Suggest a separately drawn 24 × 24 sub-icon; snap its construction to the grid and recheck fit.' if row[8]=='pass' else 'Suggest a 24 × 24 redraw first; fit is not yet verified and may need further shape changes.'
  elif row[7]=='pass' and row[0] in hgeo and hgeo[row[0]][1] is not None and row[1] in sgeo:
   zone=hgeo[row[0]][1];zx0,zy0,zx1,zy1=zone.bounds
   art=Artwork.read(sub['svg32'],32);ax0,ay0,ax1,ay1=art.bounds
   if any(word in host['name'] for word in ('monitor','screen','window','board','card','rectangular','rectangle')) and zx1-zx0>(zy1-zy0)*1.2 and ax1-ax0>(ay1-ay0)*1.2:
    suggestion='Suggest a wider grid-snapped redraw: target 32 units of visible height, allow width above 32 within the safe interior. Keep 4-unit strokes and recheck clearance.'
  if not suggestion and row[7] is None:suggestion='Size review needed before recommending a grid-snapped redraw.'
  row.append(suggestion)
  prototype=None
  if suggestion and row[1] in sgeo and row[0] in hgeo and (row[7] in ('fail','review') or suggestion.startswith('Suggest a wider')):
   art=Artwork.read(sub['svg32'],32);x0,y0,x1,y1=map(float,art.bounds);cx,cy=row[3:5]
   wide=suggestion.startswith('Suggest a wider');scale=28/(y1-y0) if wide else 20/28
   tx=cx-scale*(x0+x1)/2;ty=cy-scale*(y0+y1)/2
   root=root_svg();root.append(artwork_group(art,'prototype',scale,tx,ty,stroke=4))
   ink,inner,outer=hgeo[row[0]];metrics=check_pair(ink,VectorInk.from_art(art,(scale,tx,ty)),inner,outer)
   prototype={'svg':ET.tostring(root,encoding='unicode'),'label':'32-high wide prototype' if wide else '24 × 24 footprint prototype','width':scale*(x1-x0)+4,'height':scale*(y1-y0)+4,'fit':metrics['status'],'gap':metrics['ink_gap_lower_units']}
  if prototype and wide and prototype['fit']!='pass':
   row[13]='';prototype=None
  row.append(prototype)
 counts=dict(Counter(labels[r[2]] for r in rows));data={'hosts':hosts,'subs':subs,'statuses':labels,'counts':counts,'rows':rows,'defined_pairs':len(definitions),'resolved_pairs':len({r[9] for r in rows}),'missing':missing,'pair_source':'combination_data.json:container','policy':'Only mapped components for each defined pair. Multiple source variants are shown within their original pairing. Preserve centered placement and native wide-text dimensions. Failed source models and unsupported geometry remain review or blocked.'}
 from icon_set.scripts.container_repair_recommendations import apply
 apply(data,OUT)
 (OUT/'results.json').write_text(json.dumps(data,separators=(',',':')))
 template=(BASE/'scripts/templates/paired-container-combinations.html').read_text();page=template.replace('__DATA__',json.dumps(data,separators=(',',':')).replace('<','\\u003c'));(OUT/'index.html').write_text(page)
 # Correct the earlier shared URL too; no cross-product gallery remains at it.
 legacy=BASE/'work/all-container-combinations';(legacy/'results.json').write_text(json.dumps(data,separators=(',',':')));(legacy/'index.html').write_text(page.replace('href="results.json"','href="../container-pair-combinations/results.json"'))
 from icon_set.scripts.build_container_pair_summary import main as build_summary
 build_summary()
 print(json.dumps({'defined_pairs':len(definitions),'resolved_pairs':data['resolved_pairs'],'previews':len(rows),'missing':len(missing),'counts':counts,'report':str(OUT/'index.html')},indent=2))
if __name__=='__main__':main()
