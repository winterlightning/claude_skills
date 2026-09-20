"""Freeze verified complete-source replacements; preserve original evidence."""
import json,hashlib,sys,shutil,subprocess
from pathlib import Path
W=Path(__file__).resolve().parent;ROOT=W.parents[2];sys.path.insert(0,str(ROOT))
from icon_set.model.icons.registry import create
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
rows=json.loads((W/'batch.json').read_text());cs=json.loads((W/'candidates.json').read_text());qa=json.loads((W/'release-qa.json').read_text());accepted=[]
for r in rows:
 c=cs[str(r['number'])];q=qa[str(r['number'])];m=create(c['icon'])
 assert sha(ROOT/r['python_source'])==r['model_sha256'],r['icon']
 assert sha(ROOT/r['source_path'])==r['source_sha256'],r['icon']
 assert q['status']=='pass' and q['svg_sha256']==hashlib.sha256(m.to_svg().encode()).hexdigest()
 assert q['model_sha256']==sha(ROOT/c['python_source'])
 accepted.append(dict(r,candidate=c['icon'],candidate_python=c['python_source'],parent_sha256=r['model_sha256'],reason=c['reason'],source_parts=c['parts'],status='pass',outcome='complete-redraw',source_parts_omitted=[],visual_review='Original and current compared enlarged and by centerline, with native light/dark review. Human feedback remains open.'))
assert len({r['candidate'] for r in accepted})==32
(W/'accepted.json').write_text(json.dumps(accepted,indent=2));(W/'audit.json').write_text(json.dumps(dict(checked=32,geometry_pass=32,parent_and_reference_hashes_preserved=True,human_approval=False),indent=2))
# Target only the independently authored replacements.
args=[sys.executable,'-m','icon_set','build','--no-png','--no-report']
for r in accepted:args+=['--icon',r['candidate_python']]
with (W/'build.log').open('w') as f:subprocess.run(args,cwd=ROOT,stdout=f,stderr=subprocess.STDOUT,check=True)
shutil.copy2(W.parent/'side-repair-priority/inventory.json',W/'inventory-before.json')
print('32 source/model hashes checked and targeted builds passed.')
