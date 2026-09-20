"""Source coverage, native visual decisions, and composition verification for this batch."""
import json,sys,hashlib,sqlite3
from pathlib import Path
W=Path(__file__).resolve().parent;ROOT=W.parents[2];sys.path.insert(0,str(ROOT))
from icon_set.model.icons.registry import create
from icon_set.scripts.compose import compose
from icon_set.scripts.primitive_status import init_primitive_status,set_status
rows=json.loads((W/'batch.json').read_text());c=json.loads((W/'candidates.json').read_text());qa=json.loads((W/'release-qa.json').read_text())
from designs import SIMPLIFICATIONS
HOLD={44: ('Shield and five-point star.', 'The simplified five-ray mark reads as an asterisk at native size; preserve the original until a recognizable star fits.')}

audit=[];accepted=[];compositions={}
for r in rows:
 n=r['number'];assert Path(r['source_path']).is_file()
 assert hashlib.sha256(Path(r['source_path']).read_bytes()).hexdigest()==r['source_sha256']
 assert hashlib.sha256((ROOT/r['python_source']).read_bytes()).hexdigest()==r['parent_sha256']
 e=dict(r,parent_preserved=True,source_sha256=hashlib.sha256(Path(r['source_path']).read_bytes()).hexdigest())
 current=json.loads((W/'current-checks.json').read_text())[str(n)]
 e.update(current_status=current['status'],current_findings=current.get('errors',[])+current.get('warnings',[]),complete_source_reviewed=True)
 if str(n) in c:
  cand=c[str(n)];m=create(cand['icon']);sv=m.to_svg();q=qa[str(n)];assert q['svg_sha256']==hashlib.sha256(sv.encode()).hexdigest()
  e.update(candidate=cand['icon'],candidate_python=cand['python_source'],source_parts=r['source_parts'],simplifications=SIMPLIFICATIONS.get(n,'No parts removed.'),repair=cand['parts'],construction_reference=cand['lucide_reference'],candidate_status=q['status'],candidate_findings=q.get('errors',[])+q.get('warnings',[]))
  if q['status']!='pass' and n not in HOLD:HOLD[n]=(cand['parts'],'Candidate retained for another repair: '+'; '.join(e['candidate_findings']))
 if n in HOLD:
  parts,reason=HOLD[n];e.update(outcome='unresolved',primitive_status='skip',previous_variant_needs_review=True,reason=reason,source_coverage_pass=False)
 else:
  assert m.validate_icon().status=='valid'
  cq=compose('container-circle',cand['icon']).validate_icon()
  if getattr(m,'text_canvas_width',32)>32:
   assert m.text_canvas_width>32
   compositions[str(n)]={'icon':cand['icon'],'status':'not_applicable_wide_text','container_circle_status':cq.status,'findings':cq.describe(),'reason':'User explicitly requested natural-width shared-glyph text with 32px ink height. Container-circle placement is not compatible with this width; no scaling or glyph distortion applied. Validate its eventual side placement separately.'}
  else:
   assert cq.status=='valid',cq.describe()
   compositions[str(n)]={'icon':cand['icon'],'status':cq.status,'findings':cq.describe()}
  e.update(outcome='repaired',reason=cand['parts']+' '+SIMPLIFICATIONS.get(n,'No parts removed.')+(' Natural-width text: square container placement is not applicable; side placement must accommodate its full width.' if getattr(m,'text_canvas_width',32)>32 else ''),source_coverage_pass=True,visual_review='Complete original compared with native light/dark renders and enlarged centerlines. User-authorized simplifications recorded separately; remaining identifying features checked at native size. No human approval implied.')
  accepted.append(e)
 if e['outcome']=='unresolved':
  reason=e['reason'].lower()
  e['blocker_group']='Missing shared glyph' if any(t in reason for t in ('no matching','no pound glyph','does not contain','lacks a','lacks the','has no pound','no preferred bitcoin','no dedicated prescription','no shared bitcoin','absent from','matching shared-glyph')) else 'Spacing / visual repair'
 audit.append(e)
for name,data in [('audit',audit),('accepted',accepted),('composition-checks',compositions)]: (W/(name+'.json')).write_text(json.dumps(data,indent=2))
(W/'primitive-status.sqlite3').unlink(missing_ok=True)
con=sqlite3.connect(W/'primitive-status.sqlite3');init_primitive_status(con)
for e in audit:
 if e['outcome']=='unresolved':set_status(con,[e['source_uuid']],'skip','other',e['reason'],user='gpt-6',record=lambda *a,**k:None)
con.commit();con.close()
(W/'primitive-status.json').write_text(json.dumps({e['source_uuid']:{'status':'skip','icon':e['icon'],'note':e['reason']} for e in audit if e['outcome']=='unresolved'},indent=2))
print(len(accepted),'repaired;',len(rows)-len(accepted),'unresolved; all original models preserved.')
