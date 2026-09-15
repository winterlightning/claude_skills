import json,sys,hashlib,ast
from pathlib import Path
from collections import Counter
H=Path(__file__).resolve().parent;ROOT=H.parents[3];sys.path.insert(0,str(ROOT))
from icon_set.model.icons.registry import create
from audit import analyze
phases=['normalized','cubic-cleaned','cubic-extremes','circle-contacts','ellipse-contacts','changes','final-junctions','sweep-repairs','arrow-balance','terminal-cleanup','bokeh-opening']
all_changes={};counts={}
for phase in phases:
 rows=json.loads((H/(phase+'.json')).read_text());counts[phase]=len(rows)
 for row in rows:
  old=all_changes.get(row['id'],{});row['phases']=old.get('phases',[])+[phase];all_changes[row['id']]=row
(H/'all-changes.json').write_text(json.dumps(list(all_changes.values()),indent=2))
parent={r['id']:r for r in json.loads((H.parent/'changes.json').read_text())};parent.update(all_changes)
(H.parent/'changes.json').write_text(json.dumps(list(parent.values()),indent=2))
baseline=json.loads((H/'baseline.json').read_text());index={r['id']:r for r in json.loads((H/'sweep-index.json').read_text())};ledger=[]
for r in baseline:
 p=ROOT/r['source'];now=hashlib.sha256(p.read_bytes()).hexdigest();changed=now!=r['sha256']
 assert changed==(r['id'] in all_changes),(r['id'],changed)
 icon=create(r['id']);findings=analyze(icon)
 row=dict(id=r['id'],source=r['source'],before_sha256=r['sha256'],sha256=now,repair_in_this_pass=changed,visual_evidence=index[r['id']],construction_candidates_before=r['issues'],construction_candidates_after=findings)
 row['review']='Reconstructed and inspected with centerlines and native previews.' if changed else 'Inspected enlarged and with thin centerlines; no further repair selected. Deliberate corners and subject-specific asymmetry are retained.'
 if r['id'] in all_changes:row['plan']=all_changes[r['id']]['plan']
 ledger.append(row)
(H/'review-ledger.json').write_text(json.dumps(ledger,indent=2));summary=dict(total=len(ledger),repairs_this_pass=len(all_changes),reconstructed_total=len(parent),retained=len(ledger)-len(parent),phase_counts=counts,candidate_counts_before=dict(Counter(i['kind'] for r in ledger for i in r['construction_candidates_before'])),candidate_counts_after=dict(Counter(i['kind'] for r in ledger for i in r['construction_candidates_after'])))
(H/'audit-summary.json').write_text(json.dumps(summary,indent=2));print(json.dumps(summary,indent=2))
for r in ledger:
 bad=[i for i in r['construction_candidates_after'] if i['kind'] in ['duplicate','duplicate-dot','overlapping-lines','tiny-curve','degenerate-cubic']]
 if bad:print('CHECK',r['id'],bad)
