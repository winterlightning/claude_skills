import json,hashlib,sys,inspect
from pathlib import Path
from html.parser import HTMLParser
W=Path(__file__).resolve().parent;ROOT=W.parents[2];sys.path.insert(0,str(ROOT))
from icon_set.model.icons.registry import create,factories
from icon_set.scripts.workspace import development_dist
load=lambda p:json.loads(p.read_text())
audit=load(W/'audit.json');accepted=load(W/'accepted.json');qa=load(W/'release-qa.json');data=ROOT/'icon_set/data';backup=W/'activation-backup';roles=load(ROOT/'icon_set/model/catalog/sub-usage-categories.json');priorroles=load(backup/'roles.json');canon=load(data/'canonical-sub32.json');priorcanon=load(backup/'canonical-sub32.json');aliases=load(data/'sub-profile-aliases.json');mapping={r['icon']:r['candidate'] for r in accepted};f=factories()
for r in audit:
 assert hashlib.sha256((ROOT/r['python_source']).read_bytes()).hexdigest()==r['parent_sha256']
 assert hashlib.sha256(Path(r['source_path']).read_bytes()).hexdigest()==r['source_sha256']
for r in accepted:
 uid=r['candidate'];m=create(uid);svg=m.to_svg();sha=hashlib.sha256(svg.encode()).hexdigest();mod=inspect.getmodule(f[uid])
 assert mod.SOURCE_ICON_ID==r['source_uuid'] and mod.AUTHOR=='gpt-6'
 assert r['source_uuid'].replace('-','_') in r['candidate_python']
 assert qa[str(r['number'])]['status']=='pass' and qa[str(r['number'])]['svg_sha256']==sha
 assert aliases[r['icon']]==uid and aliases[uid]==uid and canon[uid]['sha256']==sha
 assert (ROOT/canon[uid]['svg']).read_text()==svg
for uid,v in priorcanon.items():
 if uid not in mapping:assert canon[uid]==v,uid
assert len(canon)==len(priorcanon)
for a,b in zip(priorroles['icons'],roles['icons']):
 assert a['original_icon_id']==b['original_icon_id']
 if 'symbol' in a['versions']:assert a['versions']['symbol']==b['versions']['symbol']
 old=a['versions'].get('side',{}).get('icon_id')
 if old in mapping:
  v=b['versions']['side'];assert v['icon_id']==mapping[old] and v['model_validation']=='pass'
  assert hashlib.sha256((ROOT/v['svg']).read_bytes()).hexdigest()==v['sha256']
 else:assert a==b
oldpairs=load(backup/'combination-pairs.json')['rows'];pairs=load(data/'combination-pairs.json')['rows'];changed=0
for a,b in zip(oldpairs,pairs):
 assert a['id']==b['id']
 assert {k:v for k,v in a.items() if k!='subs'}=={k:v for k,v in b.items() if k!='subs'}
 for x,y in zip(a['subs'],b['subs']):
  if x['icon'] in mapping:assert y['icon']==mapping[x['icon']]
  else:assert x==y
 changed+=a!=b
class Parser(HTMLParser):
 def __init__(self):super().__init__();self.cards=0;self.images=[]
 def handle_starttag(self,tag,attrs):
  d=dict(attrs)
  if tag=='article':self.cards+=1
  if tag=='img':self.images.append(d['src'])
p=Parser();p.feed((W/'index.html').read_text());assert p.cards==50 and len(p.images)==300
for src in p.images:assert (W/src).is_file(),src
summary=load(ROOT/'icon_set/work/side-repair-priority/summary.json');assert summary['statuses']=={'pass':628,'fail':187,'review':10}
report=dict(reviewed=50,repaired=len(accepted),unresolved=50-len(accepted),parents_unchanged=50,source_files_unchanged=50,export_qa_pass=len(accepted),container_composition_pass=len(load(W/'composition-checks.json')),pair_rows_updated=changed,independent_symbol_versions_unchanged=True,unrelated_canonical_records_unchanged=True,gallery_cards=p.cards,gallery_images=len(p.images),side_progress=summary)
(W/'verification.json').write_text(json.dumps(report,indent=2));print(json.dumps(report,indent=2))
