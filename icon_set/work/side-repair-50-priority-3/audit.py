"""Source coverage, native visual decisions, and composition verification for this batch."""
import json,sys,hashlib,sqlite3
from pathlib import Path
W=Path(__file__).resolve().parent;ROOT=W.parents[2];sys.path.insert(0,str(ROOT))
from icon_set.model.icons.registry import create
from icon_set.scripts.compose import compose
from icon_set.scripts.primitive_status import init_primitive_status,set_status
rows=json.loads((W/'batch.json').read_text());c=json.loads((W/'candidates.json').read_text());qa=json.loads((W/'release-qa.json').read_text())
HOLD={5: ('Two Wi-Fi arcs, trapezoidal windshield, rounded bumper and TWO wheel stems.', 'The parent omitted both wheel stems. Restoring both wheels, two wireless arcs and the enclosed windshield/bumper requires additional vertical clearances. No complete 32px layout is verified; do not remove a Wi-Fi arc or wheel to force a pass.'), 6: ('Rounded enclosing square with FIVE vertical barcode strokes of alternating lengths.', 'The parent reduced five bars to three. Five parallel bars require four 8-unit intervals before adding clearance to the frame, exceeding the 28-unit centerline envelope. Full source retained for review.'), 33: ('Enclosing circle, three-tine fork with curved bowl and long handle, and a separate closed knife blade with handle.', 'The parent omitted the center fork tine and knife blade. The complete fork, blade and outer circle have no verified SUB32 layout with the required internal spacing. Keep the complete original; do not substitute two plain strokes.'), 36: ('Circular human head, center-parted hairline, two outward hair tips, and closed rounded shoulder silhouette.', 'The hairline and head must leave an open forehead region, and the detached shoulders need exactly four units of visible clearance. No source-complete layout retaining both hair tips and the closed shoulder base is verified at 32px.'), 39: ('Full registered trademark: enclosing circle and capital R.', 'Must reuse shared letter-r-uppercase inside the complete enclosing circle. Its bowl and diagonal leg require a new layout with an open counter and frame clearance; no compliant complete placement is verified. Do not remove the circle.'), 43: ('Enclosing circle and yuan-style Y mark with ONE crossbar.', 'The enclosed currency mark must preserve its one-bar source variant while using the shared typeface system. No verified matching shared-glyph variant and framed SUB32 layout is available in this batch; do not invent a replacement character or omit the circle.'), 44: ('Three equal tangent outline circles: one above two aligned below.', 'The parent turned tangent circles into overlapping loops. Three equal circles in an equilateral tangent arrangement cannot retain integer centers and radii on this grid. No source-faithful arrangement is verified; overlapping circles are not accepted as the repair.'), 46: ('Detached circular head above flared dress, indented lower sides and closed short lower body.', 'The complete dress/lower-body outline must remain open internally while the detached head keeps exactly four units of ink clearance. The short parallel skirt and lower-body edges do not have a verified legal layout at 32px.'), 47: ('Rounded square frame containing a separate small square, circle and upright triangle.', 'The parent attached the square and triangle to the frame and distorted the circle. All three interior shapes must remain separate with open interiors and legal frame clearance. No complete arrangement is verified within the 28-unit centerline span.'), 49: ('Graduate bust with mortarboard diamond, cap band, circular jaw and closed rounded shoulders.', 'The parent collapsed the cap band into the face and opened the shoulder base. Retaining the band, circular jaw, closed shoulders and exact detached head gap has no complete validated SUB32 arrangement yet.')}

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
  parts,reason=HOLD[n];e.update(source_parts=parts,outcome='unresolved',primitive_status='skip',previous_variant_needs_review=True,reason=reason,source_coverage_pass=False)
 else:
  assert m.validate_icon().status=='valid'
  cq=compose('container-circle',cand['icon']).validate_icon()
  if n in (38,40):
   assert m.text_canvas_width>32
   compositions[str(n)]={'icon':cand['icon'],'status':'not_applicable_wide_text','container_circle_status':cq.status,'findings':cq.describe(),'reason':'User explicitly requested natural-width shared-glyph text with 32px ink height. Container-circle placement is not compatible with this width; no scaling or glyph distortion applied. Validate its eventual side placement separately.'}
  else:
   assert cq.status=='valid',cq.describe()
   compositions[str(n)]={'icon':cand['icon'],'status':cq.status,'findings':cq.describe()}
  e.update(outcome='repaired',reason=cand['parts']+(' Natural-width text: square container placement is not applicable; side placement must accommodate its full width.' if n in (38,40) else ''),source_coverage_pass=True,visual_review='Complete original compared with native light/dark renders and enlarged centerlines. Counts, directions, loops and frames retained. No human approval implied.')
  accepted.append(e)
 audit.append(e)
for name,data in [('audit',audit),('accepted',accepted),('composition-checks',compositions)]: (W/(name+'.json')).write_text(json.dumps(data,indent=2))
(W/'primitive-status.sqlite3').unlink(missing_ok=True)
con=sqlite3.connect(W/'primitive-status.sqlite3');init_primitive_status(con)
for e in audit:
 if e['outcome']=='unresolved':set_status(con,[e['source_uuid']],'skip','other',e['reason'],user='gpt-6',record=lambda *a,**k:None)
con.commit();con.close()
(W/'primitive-status.json').write_text(json.dumps({e['source_uuid']:{'status':'skip','icon':e['icon'],'note':e['reason']} for e in audit if e['outcome']=='unresolved'},indent=2))
print(len(accepted),'repaired;',50-len(accepted),'unresolved; all 50 original models preserved.')
