"""Activate only the accepted repairs; preserve unrelated profiles and manual state."""
import json,hashlib,shutil,sys
from pathlib import Path
W=Path(__file__).parent;ROOT=W.resolve().parents[2];sys.path.insert(0,str(ROOT))
from icon_set.model.icons.registry import create
from icon_set.validation.envelope import centerline_bounds,visible_bounds
from icon_set.scripts.workspace import development_dist,output_lock
accepted=json.loads((W/'accepted.json').read_text());release_by_number=json.loads((W/'release-qa.json').read_text());release={r['candidate']:release_by_number[str(r['number'])] for r in accepted};data=ROOT/'icon_set/data';dist=development_dist(ROOT);gallery=dist/'gallery'
paths={name:data/(name+'.json') for name in ('sub-profile-migration','icon-profile-links','sub-profile-aliases','canonical-sub32','combination-pairs')}
paths['roles']=ROOT/'icon_set/model/catalog/sub-usage-categories.json'
paths['qa']=ROOT/'icon_set/work/sub-profile-migration/qa.json'
backup=W/'activation-backup';backup.mkdir(exist_ok=True)
with output_lock(dist):
 docs={n:json.loads(p.read_text()) for n,p in paths.items()};before={n:hashlib.sha256(p.read_bytes()).hexdigest() for n,p in paths.items()}
 for n,p in paths.items():
  b=backup/(n+'.json')
  if not b.exists():shutil.copy2(p,b)
 mapping={r['icon']:r['candidate'] for r in accepted};records={};pair_count=0;link_count=0
 for r in accepted:
  old,new=r['icon'],r['candidate'];m=create(new);svg=m.to_svg();sha=hashlib.sha256(svg.encode()).hexdigest();qa=release[new]
  assert qa['status']=='pass' and qa['svg_sha256']==sha,new
  oldrec=docs['canonical-sub32'][old]
  assert oldrec['family']=='sub'
  record=dict(oldrec);drawing=m.draw();bounds=list(centerline_bounds(drawing.primitives));ink=list(visible_bounds(drawing.primitives,radius=2))
  target=ROOT/'icon_set/assets/sub-profiles'/f'{new}.svg';target.write_text(svg)
  public=gallery/'sub-profiles'/f'{new}.svg';public.parent.mkdir(parents=True,exist_ok=True);public.write_text(svg)
  record.update(icon=new,model_key='sub/'+new,python_source=r['candidate_python'],svg=str(target.relative_to(ROOT)),export_url='sub-profiles/'+new+'.svg',sha256=sha,bounds=bounds,model_validation='pass',sub32_status='native_sub32',sub32_reason='')
  from icon_set.model.icons.sub._text_base import canvas_dimensions
  width,height=canvas_dimensions(m)
  record.update(canvas_width=width,canvas_height=height,sizing_mode=getattr(m,'sizing_mode',None),side_only=getattr(m,'sizing_mode',None) in ('side-32x48','side-one-axis32','side-source-fit'))
  record['ink32']=dict(record['ink32'],bounds=bounds,ink_bounds=ink,ink_width=ink[2]-ink[0],ink_height=ink[3]-ink[1],canvas_width=width,canvas_height=height)
  if hasattr(m,'text_canvas_width'):
   record.update(canvas_width=m.text_canvas_width,sizing_kind='text')
   record['ink32'].update(canvas_width=m.text_canvas_width)
   record['typeface_glyph_ids']=list(__import__(m.__module__,fromlist=['TYPEFACE_GLYPH_IDS']).TYPEFACE_GLYPH_IDS)
  module=__import__(m.__module__,fromlist=['TYPEFACE_GLYPH_IDS'])
  for attr,key in [('TYPEFACE_GLYPH_IDS','typeface_glyph_ids'),('TYPEFACE_PROFILE_VARIANTS','typeface_profile_variants')]:
   if hasattr(module,attr):record[key]=list(getattr(module,attr))
  docs['canonical-sub32'].pop(old);docs['canonical-sub32'][new]=record;records[new]=dict(record,document=svg)
  qa=dict(qa,selected_for_build=True);docs['qa'][new]=qa
  matched=0
  for ent in docs['sub-profile-migration']['icons'].values():
   if ent['model_key']=='sub/'+old:
    prior=ent.setdefault('previous_model_keys',[])
    if ent['model_key'] not in prior:prior.append(ent['model_key'])
    ent['model_key']='sub/'+new;ent['python_source']=record['python_source'];matched+=1
  assert matched==1,(old,matched)
 for ent in docs['icon-profile-links']['links']:
  uid=ent['target'].split('/',1)[1]
  if uid in mapping:ent['target']='sub/'+mapping[uid];link_count+=1
 for key,value in list(docs['sub-profile-aliases'].items()):
  if value in mapping:docs['sub-profile-aliases'][key]=mapping[value]
 for old,new in mapping.items():docs['sub-profile-aliases'][old]=new;docs['sub-profile-aliases'][new]=new
 for row in docs['combination-pairs']['rows']:
  changed=False
  for i,sub in enumerate(row['subs']):
   if sub['icon'] in mapping:row['subs'][i]=records[mapping[sub['icon']]];changed=True
  if changed:pair_count+=1
 # Update only the side role. Independent container-symbol artwork stays untouched.
 from icon_set.scripts.sub_usage_categories import geometry
 side_versions_updated=0
 for ent in docs['roles']['icons']:
  v=ent['versions'].get('side')
  if not v:continue
  old=v['icon_id'];new=mapping.get(old)
  if not new:continue
  rec=records[new];svg=rec['document'];v.setdefault('previous_icon_ids',[]).append(old)
  v.update(icon_id=new,python_source=rec['python_source'],svg='icon_set/assets/sub-usage/side/'+new+'.svg',preview_url='sub-usage/side/'+new+'.svg',sha256=rec['sha256'],model_validation='pass',validated_geometry_sha256=hashlib.sha256(geometry(svg)).hexdigest())
  for dst in (ROOT/v['svg'],gallery/v['preview_url']):dst.parent.mkdir(parents=True,exist_ok=True);dst.write_text(svg)
  side_versions_updated+=1
 assert side_versions_updated==len(accepted),(side_versions_updated,len(accepted))
 # Refuse to clobber any concurrently edited inputs.
 for n,p in paths.items():assert hashlib.sha256(p.read_bytes()).hexdigest()==before[n],f'Concurrent change: {p}'
 for n,p in paths.items():
  payload=json.dumps(docs[n],indent=None if n in ('combination-pairs','qa') else 2)+'\n';temp=p.with_suffix('.repair-tmp');temp.write_text(payload);temp.replace(p)
 (gallery/'experiment-combination.json').write_text(json.dumps(docs['combination-pairs']))
 from icon_set.scripts.activate_sub_profiles import stage_catalog
 catalog=gallery/'combinations.json'
 if catalog.exists():
  d=json.loads(catalog.read_text());stage_catalog(d,ROOT);
  from icon_set.scripts.sub_usage_categories import stage_catalog as stage_roles
  stage_roles(d,ROOT);catalog.write_text(json.dumps(d,separators=(',',':'))+'\n')
 # A compact report, without touching caches or human review choices.
 from collections import Counter
 report=dict(activated=len(accepted),side_versions_updated=side_versions_updated,profile_links_updated=link_count,pair_rows_updated=pair_count,recorded_statuses=dict(Counter(x['model_validation'] for x in docs['canonical-sub32'].values())),recorded_sub_statuses=dict(Counter(x['model_validation'] for x in docs['canonical-sub32'].values() if x['family']=='sub')),manual_state_changed=False)
 (W/'publication.json').write_text(json.dumps(report,indent=2));print(report)
