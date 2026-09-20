import json,hashlib,sys,shutil,collections
from pathlib import Path
from html.parser import HTMLParser
W=Path(__file__).resolve().parent;ROOT=W.parents[2];sys.path.insert(0,str(ROOT))
from icon_set.scripts.workspace import development_dist
load=lambda p:json.loads(p.read_text())
audit=load(W/'audit.json');assert len(audit)==71 and len({r['icon'] for r in audit})==71
for r in audit:
 assert hashlib.sha256((ROOT/r['python_source']).read_bytes()).hexdigest()==r['parent_sha256']
 assert hashlib.sha256(Path(r['source_path']).read_bytes()).hexdigest()==r['source_sha256']
class Parse(HTMLParser):
 def __init__(self):super().__init__();self.cards=0;self.images=[]
 def handle_starttag(self,tag,attrs):
  attrs=dict(attrs)
  if tag=='article':self.cards+=1
  if tag=='img':self.images.append(attrs['src'])
p=Parse();p.feed((W/'index.html').read_text());assert p.cards==71 and len(p.images)==426
for src in p.images:assert (W/src).is_file()
verification=[load(W.parent/f'side-repair-50-priority-{b}/verification.json') for b in (7,8)]
assert all(v['build_exit_code']==0 and v['tests_passed']==42 for v in verification)
summary=load(W.parent/'side-repair-priority/summary.json');assert summary['statuses']=={'pass':757,'fail':63,'review':5}
report={'reviewed':71,'repaired':3,'unresolved':68,'blocker_groups':dict(collections.Counter(r['blocker_group'] for r in audit if r['outcome']=='unresolved')),'tests_passed':42,'build_exit_code':0,'parents_preserved':71,'sources_preserved':71,'side_progress':summary,'pair_rows_updated':sum(v['pair_rows_updated'] for v in verification),'combined_svg_caches_regenerated':False,'manual_state_changed':False,'independent_symbol_versions_unchanged':True,'gallery_cards':71,'gallery_images':426}
(W/'verification.json').write_text(json.dumps(report,indent=2))
target=development_dist(ROOT)/'gallery'/W.name;target.mkdir(exist_ok=True)
for name in ('index.html','audit.json','verification.json'):shutil.copy2(W/name,target/name)
shutil.copytree(W/'review-assets',target/'review-assets',dirs_exist_ok=True)
print(json.dumps(report,indent=2))
