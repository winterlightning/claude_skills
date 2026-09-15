"""Discard the six Pending text matches explicitly selected by the user."""
import base64, hashlib, json, sqlite3
from pathlib import Path
from icon_set.scripts.discard_icon import discard_many, plan_source_removal, _write_atomic
from icon_set.scripts.deploy import review_detail, record_activity
ROOT=Path(__file__).resolve().parents[3]
OUT=Path(__file__).resolve().parent
DIST=ROOT/'icon_set/dist'
DB=ROOT/'icon_set/data/feedback.sqlite3'
report=json.loads((OUT/'matches.json').read_text())['icons']
targets=[r for r in report if r['review_status']=='pending' and r['decision']=='review']
expected_ids={'circle-l','cpp-text','css-text','degrees-celsius','fahrenheit','podium-first-place'}
assert {r['icon_id'] for r in targets}==expected_ids and len(targets)==6
keep_keys={r['key'] for r in report if r['decision']=='keep'}
lookup={r['key']:r for r in json.loads((DIST/'gallery/icons.json').read_text())['icons']}
indexes={}
for r in targets:
 assert lookup[r['key']]['svg_sha256']==r['svg_sha256'],f"Changed: {r['key']}"
 plan_source_removal(ROOT,lookup[r['key']],indexes)
kept_files={}
for key in keep_keys:
 for p in [ROOT/lookup[key]['python_source']['path'],(DIST/'gallery'/lookup[key]['preview_url']).resolve()]:
  kept_files[str(p)]=hashlib.sha256(p.read_bytes()).hexdigest()
(OUT/'pending/kept-file-hashes.json').write_text(json.dumps(kept_files,indent=2))
cache=json.loads((OUT/'preview-snapshot.json').read_text())
for r in targets:
 p=(DIST/'gallery'/r['preview_url']).resolve()
 cache[r['key']]={'generated':'data:image/svg+xml;base64,'+base64.b64encode(p.read_bytes()).decode()}
(OUT/'preview-snapshot.json').write_text(json.dumps(cache))
backup=OUT/'pending/before-discard.sqlite3'
assert not backup.exists(),'Existing backup: inspect prior attempt before retrying.'
with sqlite3.connect(DB) as c, sqlite3.connect(backup) as b:c.backup(b)
with sqlite3.connect(DB,timeout=30) as c:
 c.execute('BEGIN IMMEDIATE')
 for r in targets:assert review_detail(c,r['key'],r['svg_sha256'])['status']=='pending',f"No longer Pending: {r['key']}"
 result=discard_many([lookup[r['key']] for r in targets],source_root=ROOT,dist=DIST,archive=DB.parent/'discarded-icons',connection=c,user='codex')
 for r in result['discarded']:
  record_activity(c,'codex','discard',r['icon'],svg_sha256=lookup[r['icon']]['svg_sha256'],source=r['source'],archive=r['archive'],reason='User requested discard of six Pending text/number report matches; Keep exceptions preserved')
 c.commit()
(OUT/'pending/discard-results.json').write_text(json.dumps(result,indent=2)+'\n')
removed={r['icon'] for r in result['discarded']}
preview=DIST/'gallery/preview-icons.json'
if preview.exists():
 data=json.loads(preview.read_text());data['icons']=[r for r in data['icons'] if r['family']+'/'+r['icon_id'] not in removed]
 _write_atomic(preview,json.dumps(data,ensure_ascii=False,indent=2)+'\n')
after={r['key'] for r in json.loads((DIST/'gallery/icons.json').read_text())['icons']}
assert not removed&after and keep_keys<=after
assert all(hashlib.sha256(Path(p).read_bytes()).hexdigest()==digest for p,digest in kept_files.items())
assert len(removed)==6 and not result['failed']
print(json.dumps({'discarded':len(removed),'kept_unchanged':len(keep_keys),'failed':result['failed']}))
