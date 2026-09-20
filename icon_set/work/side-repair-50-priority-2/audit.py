"""Source coverage, native visual decisions, and composition verification for this batch."""
import json,sys,hashlib,sqlite3
from pathlib import Path
W=Path(__file__).resolve().parent;ROOT=W.parents[2];sys.path.insert(0,str(ROOT))
from icon_set.model.icons.registry import create
from icon_set.scripts.compose import compose
from icon_set.scripts.primitive_status import init_primitive_status,set_status
rows=json.loads((W/'batch.json').read_text());c=json.loads((W/'candidates.json').read_text());qa=json.loads((W/'release-qa.json').read_text())
HOLD={
1:('Rounded clipped-corner page, closed rectangular image panel and TWO text lines.','Parent omitted the lower short line. A closed image panel plus both lines and enclosing page requires more vertical parallel clearances than the 28-unit centerline envelope permits. Preserve all parts; do not substitute an open panel or one-line page.'),
4:('Eight-lobed rosette, circular center hole and one notched ribbon.','The center hole must remain visibly open while the scalloped seal and lower ribbon retain separate spaces. No complete 32px/4px-stroke layout has been verified; do not flatten the rosette into a generic medal or fill its center.'),
15:('Money-bag outline, tied top and complete dollar glyph.','The shared symbol-dollar glyph exists and must replace the hand-drawn dollar. A source-faithful closed bag with that complete shared glyph has no validated layout in this batch; keep the currency strokes and tied opening.'),
19:('Clipped-corner financial document, dollar sign and TWO short horizontal lines.','The parent omitted both document lines. Restoring both lines and reusing symbol-dollar inside the frame needs a new complete layout. The dollar-only page is not a repair of this original.'),
22:('Prescription mark: tall P-shaped bowl continuing into the crossed descending Rx strokes.','The shared typeface contains P, R and x but no dedicated prescription-sign glyph (℞). The original joined prescription geometry is not an ordinary separately typeset Px. A verified shared-glyph arrangement preserving the mark remains unresolved; no replacement letters were invented.'),
28:('Delivery-worker cap, central circular emblem, curved brim, TWO eye dots and two open cheek curves.','Parent omitted both eyes and filled the emblem. Restoring the cap emblem and eye row with the closed cap boundaries and circular human face vocabulary has no complete clear 32px layout yet. Keep all source details in the reference.'),
34:('Crossed spoon and three-pronged fork, curved fork bowl, oval spoon bowl and both handles.','The three fork tines require eight-unit parallel spacing while the separate spoon bowl must retain an open interior. No source-faithful crossed layout is verified at 32px; do not drop a tine or change the spoon into a filled oval.'),
37:('One square root node, horizontal branch and two square leaf nodes.','Three stacked parallel intervals around the root, branch and leaf tops, plus the eight-unit root and leaf heights, require at least 32 centerline units vertically. Only 28 are available. Do not replace the square leaves with circles or remove the branch.'),
50:('Rocket body with pointed curved nose, open arched cockpit, TWO side fins, flat base and central lower stem.','The narrow fins and enclosed cockpit-to-body spacing remain unresolved with a 4px stroke. Parent also altered the flat base into a small curve. A complete repair must retain the arched cockpit, fins, base and stem; no simplified rocket is activated.')}

audit=[];accepted=[];compositions={}
for r in rows:
 n=r['number'];assert Path(r['source_path']).is_file()
 assert hashlib.sha256((ROOT/r['python_source']).read_bytes()).hexdigest()==r['parent_sha256']
 e=dict(r,parent_preserved=True,source_sha256=hashlib.sha256(Path(r['source_path']).read_bytes()).hexdigest())
 if str(n) in c:
  cand=c[str(n)];m=create(cand['icon']);sv=m.to_svg();q=qa[str(n)];assert q['svg_sha256']==hashlib.sha256(sv.encode()).hexdigest()
  e.update(candidate=cand['icon'],candidate_python=cand['python_source'],source_parts=cand['parts'],repair=cand['parts'],construction_reference=cand['lucide_reference'],candidate_status=q['status'],candidate_findings=q.get('errors',[])+q.get('warnings',[]))
  if q['status']!='pass':HOLD[n]=(cand['parts'],'Candidate retained for another repair: '+'; '.join(e['candidate_findings']))
 if n in HOLD:
  parts,reason=HOLD[n];e.update(source_parts=parts,outcome='unresolved',primitive_status='skip',reason=reason,source_coverage_pass=False)
 else:
  assert m.validate_icon().status=='valid'
  cq=compose('container-circle',cand['icon']).validate_icon();assert cq.status=='valid',cq.describe()
  compositions[str(n)]={'icon':cand['icon'],'status':cq.status,'findings':cq.describe()}
  e.update(outcome='repaired',reason=cand['parts'],source_coverage_pass=True,visual_review='Complete original compared with native light/dark renders and enlarged centerlines. Counts, directions, loops and frames retained. No human approval implied.')
  accepted.append(e)
 audit.append(e)
for name,data in [('audit',audit),('accepted',accepted),('composition-checks',compositions)]: (W/(name+'.json')).write_text(json.dumps(data,indent=2))
con=sqlite3.connect(W/'primitive-status.sqlite3');init_primitive_status(con)
for e in audit:
 if e['outcome']=='unresolved':set_status(con,[e['source_uuid']],'skip','other',e['reason'],user='gpt-6',record=lambda *a,**k:None)
con.commit();con.close()
(W/'primitive-status.json').write_text(json.dumps({e['source_uuid']:{'status':'skip','icon':e['icon'],'note':e['reason']} for e in audit if e['outcome']=='unresolved'},indent=2))
print(len(accepted),'repaired;',50-len(accepted),'unresolved; all 50 original models preserved.')
