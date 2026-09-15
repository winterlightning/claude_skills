"""Apply the user's discard request to the report's 86 non-Keep icons."""
import hashlib,json,sqlite3
from pathlib import Path
from icon_set.scripts.discard_icon import discard_many,_write_atomic
from icon_set.scripts.deploy import review_detail,record_activity
ROOT=Path(__file__).resolve().parents[3]
OUT=Path(__file__).resolve().parent
DIST=ROOT/'icon_set/dist'
DB=ROOT/'icon_set/data/feedback.sqlite3'
report=json.loads((OUT/'matches.json').read_text())
preflight=json.loads((OUT/'discard-preflight.json').read_text())
assert not preflight['errors']
target_keys={r['key'] for r in report['icons'] if r['decision']=='review'}
keep_keys={r['key'] for r in report['icons'] if r['decision']=='keep'}
assert len(target_keys)==86 and len(keep_keys)==36 and not target_keys&keep_keys
catalog=json.loads((DIST/'gallery/icons.json').read_text())
lookup={r['key']:r for r in catalog['icons']}
expected={r['key']:r['svg_sha256'] for r in preflight['targets']}
assert set(expected)==target_keys
kept_files={}
for key in keep_keys:
 icon=lookup[key]
 for file in [ROOT/icon['python_source']['path'],(DIST/'gallery'/icon['preview_url']).resolve()]:
  kept_files[str(file)]=hashlib.sha256(file.read_bytes()).hexdigest()
(OUT/'kept-file-hashes.json').write_text(json.dumps(kept_files,indent=2))
backup=OUT/'before-discard.sqlite3'
assert not backup.exists(),'Discard backup already exists; inspect results before retrying.'
with sqlite3.connect(DB) as connection, sqlite3.connect(backup) as snapshot:
 connection.backup(snapshot)
with sqlite3.connect(DB,timeout=30) as connection:
 connection.execute('BEGIN IMMEDIATE')
 for key in sorted(target_keys):
  assert lookup[key]['svg_sha256']==expected[key],f'Icon changed: {key}'
  assert review_detail(connection,key,expected[key])['status']=='rejected',f'No longer rejected: {key}'
 result=discard_many([lookup[k] for k in sorted(target_keys)],source_root=ROOT,dist=DIST,
                     archive=DB.parent/'discarded-icons',connection=connection,user='codex')
 for r in result['discarded']:
  record_activity(connection,'codex','discard',r['icon'],svg_sha256=expected[r['icon']],
                  source=r['source'],archive=r['archive'],reason='User requested discard of the text/number report shortlist; Keep exceptions preserved')
 connection.commit()
(OUT/'discard-results.json').write_text(json.dumps(result,indent=2)+'\n')
removed={r['icon'] for r in result['discarded']}
# Keep the gallery's lightweight preview catalog aligned with its main catalog.
preview=DIST/'gallery/preview-icons.json'
if preview.exists():
 data=json.loads(preview.read_text());data['icons']=[r for r in data['icons'] if r['family']+'/'+r['icon_id'] not in removed]
 _write_atomic(preview,json.dumps(data,ensure_ascii=False,indent=2)+'\n')
after={r['key'] for r in json.loads((DIST/'gallery/icons.json').read_text())['icons']}
assert not removed&after
assert keep_keys<=after
assert all(hashlib.sha256(Path(p).read_bytes()).hexdigest()==digest for p,digest in kept_files.items())
print(json.dumps({'discarded':len(result['discarded']),'failed':result['failed'],'kept_unchanged':len(keep_keys)}))
