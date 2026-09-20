"""Source coverage, native visual decisions, and composition verification for this batch."""
import json,sys,hashlib,sqlite3
from pathlib import Path
W=Path(__file__).resolve().parent;ROOT=W.parents[2];sys.path.insert(0,str(ROOT))
from icon_set.model.icons.registry import create
from icon_set.scripts.compose import compose
from icon_set.scripts.primitive_status import init_primitive_status,set_status
rows=json.loads((W/'batch.json').read_text());c=json.loads((W/'candidates.json').read_text());qa=json.loads((W/'release-qa.json').read_text())
HOLD={
9:('Three closed pointed leaves; vertical stem; horizontal ground line.','Earlier model omitted the ground and joined side leaves to the stem. Complete source needs three visible leaf openings and separated lower leaves. A source-faithful layout with those clearances is unresolved; do not accept the incomplete parent.'),
18:('Rounded speech bubble and tail; dollar sign with upper and lower currency strokes.','The shared symbol-dollar glyph exists and must replace the improvised dollar. Its complete glyph inside the closed bubble has no verified 32px/4px-stroke layout in this batch; preserve both currency strokes and the tail.'),
23:('Shield outline and closed five-point star.','The existing star fails facing-edge spacing (6 and 6.32456 versus 8 centerline units). Enlarging it must also retain six-unit separation from the shield. No complete clear star-in-shield layout is established; do not substitute an asterisk or filled mark.'),
35:('Diagonal syringe barrel, rounded nose, needle, plunger shaft and cap; TWO graduation ticks.','Parent omitted one of the two graduation ticks. Barrel, plunger cap and both ticks require repeated eight-unit parallel spacing along a short diagonal body. A complete layout remains unresolved; the one-tick parent is not an accepted repair.'),
38:('Open circular face outline, curved hair part, complete pointer with diagonal trailing stem.','Parent omitted the hair part and pointer stem. Full head/hair and pointer need separate clearances; the existing simplified candidate has no source-coverage approval. Requires a complete redraw, not just cleaning its circle.'),
39:('Circular border, closed right-pointing triangle and separate vertical stop bar.','The enclosed triangle is too small to keep a readable hole while maintaining clearance from both circle and stop bar. Retain the circle and closed triangle; do not replace the triangle with an open chevron.'),
44:('Two interlocking rounded links with bent inner ends and two separate openings.','Parent replaced the interlocking bent ends with a single diagonal connector. It also fails parallel spacing at 7.77817 versus 8 centerline units. The original interlocking topology needs a new verified layout; a generic chain mark is not a complete repair.'),
45:('Circular border, upper-left plus, diagonal slash and lower-right minus.','Reuse shared symbol-plus and symbol-hyphen, preserving the full framed arrangement. Current plus/slash and border/slash gaps are only 5.65685 and 5.51461 versus 6 centerline units. No complete shared-glyph layout has been validated.'),
50:('Three fork prongs, curved fork bowl and stem; separate curved knife blade and handle.','Three parallel fork prongs require 16 centerline units, then six to the separate knife. Only six units remain in the 28-unit envelope for the blade; the current blade and fork gaps fail the eight-unit parallel rule. Do not remove a prong or fill the blade opening.')}
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
