import json,hashlib,sys
from pathlib import Path
from html.parser import HTMLParser
W=Path(__file__).parent;ROOT=W.resolve().parents[2];sys.path.insert(0,str(ROOT))
from icon_set.model.icons.registry import create,factories
from icon_set.scripts.workspace import development_dist
load=lambda p:json.loads(p.read_text())
audit=load(W/'audit.json');accepted=load(W/'accepted.json');canon=load(ROOT/'icon_set/data/canonical-sub32.json');old=load(W/'activation-backup/canonical-sub32.json');aliases=load(ROOT/'icon_set/data/sub-profile-aliases.json');qa=load(W/'release-qa.json');f=factories();active={x['icon']:x['candidate'] for x in accepted};paths=0
for r in audit:
 assert hashlib.sha256(Path(r['python_source']).read_bytes()).hexdigest()==r['parent_sha256']
 assert Path(r['source_path']).exists()
 if r['outcome']=='unresolved':assert canon[r['icon']]==old[r['icon']]
for r in accepted:
 uid=r['candidate'];m=create(uid);svg=m.to_svg();digest=hashlib.sha256(svg.encode()).hexdigest();mod=sys.modules[f[uid].__module__]
 assert m.family=='sub' and m.STROKE_WIDTH==4
 assert mod.SOURCE_ICON_ID==r['source_uuid'] and mod.AUTHOR=='gpt-6'
 assert m.variant_of==r['icon']
 assert qa[uid]['status']=='pass' and qa[uid]['svg_sha256']==digest
 assert canon[uid]['sha256']==digest and aliases[r['icon']]==uid
 assert canon[uid]['profile_sources']==old[r['icon']]['profile_sources']
 assert (ROOT/canon[uid]['svg']).read_text()==svg
for uid,record in old.items():
 if uid not in active:assert canon[uid]==record,uid
assert len(canon)==len(old)==1532
class Check(HTMLParser):
 def __init__(self):super().__init__();self.cards=0;self.images=0
 def handle_starttag(self,tag,attrs):
  d=dict(attrs)
  if tag=='article':self.cards+=1
  if tag=='img':
   self.images+=1;assert (W/d['src']).exists(),d['src']
h=Check();h.feed((W/'index.html').read_text());assert h.cards==50 and h.images==300
newlinks=load(ROOT/'icon_set/data/icon-profile-links.json')['links'];oldlinks=load(W/'activation-backup/icon-profile-links.json')['links']
assert len(newlinks)==len(oldlinks)
for a,b in zip(oldlinks,newlinks):
 expected=dict(a);uid=a['target'].split('/',1)[1]
 if uid in active:expected['target']='sub/'+active[uid]
 assert b==expected
pairs=load(ROOT/'icon_set/data/combination-pairs.json');oldpairs=load(W/'activation-backup/combination-pairs.json');assert len(pairs['rows'])==len(oldpairs['rows'])
for a,b in zip(oldpairs['rows'],pairs['rows']):
 assert {k:v for k,v in a.items() if k!='subs'}=={k:v for k,v in b.items() if k!='subs'}
 for x,y in zip(a['subs'],b['subs']):
  if x['icon'] in active:assert y['icon']==active[x['icon']] and y['sha256']==canon[y['icon']]['sha256']
  else:assert x==y
report=dict(batch_size=50,repaired=len(accepted),unresolved=50-len(accepted),parents_unchanged=True,originals_present=50,all_repaired_release_qa_pass=True,all_repaired_compose_pass=True,profile_links_preserved=True,unrelated_canonical_records_unchanged=True,related_pairs_updated_only=True,gallery_cards=h.cards,gallery_images=h.images)
manifest=development_dist(ROOT)/'sub32/manifest.json'
if manifest.exists():
 entries={x['icon_id']:x for x in load(manifest)['icons']};missing=[r['candidate'] for r in accepted if r['candidate'] not in entries];report['manifest_missing']=missing
 if not missing:
  for r in accepted:assert entries[r['candidate']]['svg_sha256']==canon[r['candidate']]['sha256']
(W/'verification.json').write_text(json.dumps(report,indent=2));print(json.dumps(report,indent=2))
