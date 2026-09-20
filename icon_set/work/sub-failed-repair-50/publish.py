"""Activate only the accepted repairs; preserve unrelated profiles and manual state."""
import json,hashlib,shutil,sys
from pathlib import Path
W=Path(__file__).parent;ROOT=W.resolve().parents[2];sys.path.insert(0,str(ROOT))
from icon_set.model.icons.registry import create
from icon_set.validation.envelope import centerline_bounds,visible_bounds
from icon_set.scripts.workspace import development_dist,output_lock
accepted=json.loads((W/'accepted.json').read_text());release=json.loads((W/'release-qa.json').read_text());data=ROOT/'icon_set/data';dist=development_dist(ROOT);gallery=dist/'gallery'
paths={name:data/(name+'.json') for name in ('sub-profile-migration','icon-profile-links','sub-profile-aliases','canonical-sub32','combination-pairs')}
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
  record.update(icon=new,model_key='sub/'+new,python_source=str(Path(r['candidate_python']).relative_to(ROOT)),svg=str(target.relative_to(ROOT)),export_url='sub-profiles/'+new+'.svg',sha256=sha,bounds=bounds,model_validation='pass',sub32_status='native_sub32',sub32_reason='')
  record['ink32']=dict(record['ink32'],bounds=bounds,ink_bounds=ink,ink_width=ink[2]-ink[0],ink_height=ink[3]-ink[1])
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
 # Refuse to clobber any concurrently edited inputs.
 for n,p in paths.items():assert hashlib.sha256(p.read_bytes()).hexdigest()==before[n],f'Concurrent change: {p}'
 for n,p in paths.items():
  payload=json.dumps(docs[n],indent=None if n=='combination-pairs' else 2)+'\n';temp=p.with_suffix('.repair-tmp');temp.write_text(payload);temp.replace(p)
 (gallery/'experiment-combination.json').write_text(json.dumps(docs['combination-pairs']))
 from icon_set.scripts.activate_sub_profiles import stage_catalog
 catalog=gallery/'combinations.json'
 if catalog.exists():
  d=json.loads(catalog.read_text());stage_catalog(d,ROOT);catalog.write_text(json.dumps(d,separators=(',',':'))+'\n')
 # A compact report, without touching caches or human review choices.
 from collections import Counter
 report=dict(activated=len(accepted),profile_links_updated=link_count,pair_rows_updated=pair_count,recorded_statuses=dict(Counter(x['model_validation'] for x in docs['canonical-sub32'].values())),recorded_sub_statuses=dict(Counter(x['model_validation'] for x in docs['canonical-sub32'].values() if x['family']=='sub')),manual_state_changed=False)
 (W/'publication.json').write_text(json.dumps(report,indent=2));print(report)
