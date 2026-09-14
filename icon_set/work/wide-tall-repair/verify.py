from pathlib import Path
import sys,json,hashlib,re
ROOT=Path(__file__).resolve().parents[3];sys.path.insert(0,str(ROOT))
from icon_set.model.icons.registry import create
from icon_set.validation.envelope import centerline_bounds
SOURCE_ICON_ID=None
SOURCE_PATH='icon_set/work/wide-tall-repair/results.json'
AUTHOR='gpt-6'
W=Path(__file__).parent;rows=json.loads((W/'results.json').read_text());targets=json.loads((W/'targets.json').read_text());splits=json.loads((W/'splits.json').read_text());manifest=json.loads((ROOT/'icon_set/dist/solo48/manifest.json').read_text());manifestids={i['icon_id'] for i in manifest['icons']};checks=[]
for r in rows:
 o=create(r['id']);f=ROOT/'icon_set/dist/solo48'/f"{r['id']}.svg";q=json.loads((ROOT/'icon_set/dist/qa/solo'/r['id']/'metrics.json').read_text());b=centerline_bounds(o.primitives);ink=[b[0]-2,b[1]-2,b[2]+2,b[3]+2];expected=list(o.keyshape_bounds());deltas=[a-b for a,b in zip(ink,expected)]
 assert q['status']=='pass' and not q['errors'] and not q['warnings'] and q['internal_spacing']['status']=='pass',r['id']
 assert r['id'] in manifestids,r['id'];assert f.read_text()==o.to_svg(),r['id']
 # Exact acceptance is asserted by the zero-tolerance model check; the following values retain raw floating arithmetic.
 v=o.validate_icon();assert v.status=='valid' and not v.warnings,(r['id'],v.describe())
 checks.append({'id':r['id'],'originals':r['originals'],'validation':v.describe(),'qa':q['status'],'internal_spacing':q['internal_spacing']['status'],'ink_bounds':ink,'expected_bounds':expected,'deltas':deltas,'manifest':True,'export_matches_model':True})
parents=json.loads((W/'parent-hashes.json').read_text());changed=[p for p,h in parents.items() if hashlib.sha256((ROOT/p).read_bytes()).hexdigest()!=h];assert not changed,changed
covered=[old for r in rows for old in r['originals']]+[s['original'] for s in splits];assert sorted(covered)==sorted(r['id'] for r in targets);assert all(s['exit_code']==0 for s in splits)
missing=[]
for link in re.findall(r'(?:src|href)="([^"]+)"',(W/'index.html').read_text()):
 if link.startswith(('http','#')) or link in ['README.md','verification.json']:continue
 if not (W/link).resolve().exists():missing.append(link)
assert not missing,missing
human=[]
for r in rows:
 if r['original'] not in {'baby-figure-v2','figure-with-outstretched-limbs','fortune-teller-reading','geisha-bust','two-stick-figures'}:continue
 q=json.loads((ROOT/'icon_set/dist/qa/solo'/r['id']/'metrics.json').read_text());pairs=[]
 for pair in q['spacing']['pairs']:
  for cp in pair.get('contourPairs',[pair]):
   ids=cp['closestContours']
   if any('head:' in i for i in ids) and abs(cp['centerlineDistance']-8)<1e-10:pairs.append({'contours':ids,'centerline_gap':cp['centerlineDistance'],'ink_gap':cp['inkClearance'],'nearest_points':cp['nearestPoints']})
 assert pairs,(r['id'],'Missing exact human gap')
 human.append({'id':r['id'],'measurements':pairs})
result={'targets':len(targets),'new_variants':sum(not r['reused'] for r in rows),'reused_variants':sum(r['reused'] for r in rows),'standalone_entries_covered':sum(len(r['originals']) for r in rows),'split_entries':len(splits),'component_briefs':2*len(splits),'all_parent_models_unchanged':not changed,'missing_gallery_links':missing,'human_head_body_gaps':human,'checks':checks,'browser_controls':'Not exercised: browser URL policy blocked local file navigation; static asset links checked.'}
(W/'verification.json').write_text(json.dumps(result,indent=2));print({k:v for k,v in result.items() if k not in ['checks','human_head_body_gaps']})
