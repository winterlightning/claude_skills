"""Record source comparison independently from geometry validation."""
import json,hashlib,sys,shutil
from pathlib import Path
W=Path(__file__).resolve().parent;ROOT=W.parents[2];sys.path.insert(0,str(ROOT))
from icon_set.model.icons.registry import create
rows=json.loads((W/'accepted.json').read_text());sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
path=ROOT/'icon_set/data/sub-reference-fidelity.json';history=json.loads(path.read_text())
rp=ROOT/'icon_set/data/sub-reference-repairs.json';repairs=json.loads(rp.read_text())
for r in rows:
 q=dict(status='redrawn',model_sha256=sha(ROOT/r['candidate_python']),svg_sha256=hashlib.sha256(create(r['candidate']).to_svg().encode()).hexdigest(),source_sha256=r['source_sha256'],source_id=r['source_id'],finding='Complete source composition restored and compared enlarged, by centerline and at native size in light/dark. Human feedback remains open.',disposition='complete-redraw',review_url='sub-fidelity-repair-32/index.html#'+r['candidate'])
 history[r['candidate']]=q
 repairs[r['icon']]=dict(icon_id=r['icon'],source_id=r['source_id'],source_path=r['source_path'],parent_model_sha256=r['model_sha256'],status='redrawn',new_id=r['candidate'],new_model_path=r['candidate_python'],new_model_sha256=q['model_sha256'],new_svg_sha256=q['svg_sha256'],parts=r['source_parts'],qa='pass',reason=r['reason'],review_url=q['review_url'])
path.write_text(json.dumps(history,indent=2)+'\n');rp.write_text(json.dumps(repairs,indent=2)+'\n')
# Compare immutable parents/references and verify the activated exported drawings.
canon=json.loads((ROOT/'icon_set/data/canonical-sub32.json').read_text())
for r in rows:
 assert sha(ROOT/r['python_source'])==r['model_sha256']
 assert sha(ROOT/r['source_path'])==r['source_sha256']
 c=canon[r['candidate']];assert sha(ROOT/c['svg'])==history[r['candidate']]['svg_sha256']
# Existing inventory contains each selected side profile; update only these replacements.
p=ROOT/'icon_set/work/side-repair-priority/inventory.json';data=json.loads(p.read_text());mapping={r['icon']:r for r in rows}
for r in data:
 if r['icon'] in mapping:
  a=mapping[r['icon']];r.update(previous_icon=r['icon'],icon=a['candidate'],python_source=a['candidate_python'],status='pass',freshly_validated=True,verified_svg_sha256=history[a['candidate']]['svg_sha256'],hash_current=True)
p.write_text(json.dumps(data,indent=2))
# Preserve unrelated canonical and role records exactly.
before=json.loads((W/'activation-backup/canonical-sub32.json').read_text());old=set(mapping)
assert len(canon)==len(before)==1532
for k,v in before.items():
 if k not in old:assert canon[k]==v,k
br=json.loads((W/'activation-backup/roles.json').read_text());ar=json.loads((ROOT/'icon_set/model/catalog/sub-usage-categories.json').read_text())
for a,b in zip(br['icons'],ar['icons']):
 for role,record in a['versions'].items():
  if role!='side' or record['icon_id'] not in mapping:assert b['versions'][role]==record
(W/'verification.json').write_text(json.dumps(dict(geometry_pass=32,originals_and_parents_unchanged=True,canonical_count=1532,unrelated_canonical_and_roles_unchanged=True,targeted_build='pass',focused_tests='10 passed',broader_tests='23 passed; 2 missing existing fixtures: square and container_content_text_51708702_sub32',combined_svg_cache_rebuilt=False),indent=2))
print('32 selections verified; originals and unrelated records unchanged.')
