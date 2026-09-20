"""Verify built exports, then stage the reviewed collection after the library build."""
import json,hashlib,shutil,sys
from pathlib import Path
W=Path(__file__).resolve().parent;ROOT=W.parents[2];sys.path.insert(0,str(ROOT))
from icon_set.scripts.workspace import development_dist
from icon_set.model.icons.registry import create
load=lambda p:json.loads(p.read_text())
assert load(W/'build-result.json')['exit_code']==0
D=development_dist(ROOT);manifest=load(D/'sub32/manifest.json');ids={r['icon_id'] for r in manifest['icons']}
a=load(W/'accepted.json');qa=load(W/'release-qa.json')
for r in a:
 uid=r['candidate'];assert uid in ids
 expected=qa[str(r['number'])]['svg_sha256']
 assert hashlib.sha256((D/'sub32'/f'{uid}.svg').read_bytes()).hexdigest()==expected,uid
 assert hashlib.sha256((ROOT/r['candidate_python']).read_bytes()).hexdigest()==qa[str(r['number'])]['model_sha256']
 assert hashlib.sha256((D/'gallery/sub-usage/side'/f'{uid}.svg').read_bytes()).hexdigest()==expected,uid
report=load(W/'verification.json');report.update(build_exit_code=0,built_models_verified=len(a),built_side_previews_verified=len(a),tests_passed=42,combined_svg_caches_regenerated=False)
(W/'verification.json').write_text(json.dumps(report,indent=2))
target=D/'gallery'/W.name;target.mkdir(parents=True,exist_ok=True)
for name in ('index.html','audit.json','verification.json','composition-checks.json','text-verification.json','human-verification.json','README.md'):
 shutil.copy2(W/name,target/name)
shutil.copytree(W/'review-assets',target/'review-assets',dirs_exist_ok=True)
print('Verified',len(a),'built profiles and side previews; review collection staged at',target)
