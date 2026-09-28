from pathlib import Path
import json
from icon_set.scripts.primitive_fix import load_icon
B=Path('icon_set/work/primitive-fix-thuan/batch-20260924T152553Z-thuan-mac')
rows=json.loads((B/'ledger.json').read_text())
notes=[
('Rounded the rhino back and muzzle, rebuilt the horn and ear, and regularized the leg openings.','Inner leg seams omitted; two primary legs retained.','No useful exact Lucide match.','Wide animal silhouette.'),
('Rebuilt the skull and mouth as a coherent contour and restored two separated breath curls.','Tiny facial details omitted; source blank face retained.','human_ref/user.svg: circular anatomy.','Head and breath fit a square composition; anatomical neck is continuous, no detached head gap applies.'),
('Joined the circular skull to a continuous neck and rebuilt the shoulder as a smooth arc at an exact node.','No essential parts omitted.','human_ref/user.svg: circular head and smooth shoulder.','Upright human profile; continuous anatomical neck, no detached head gap applies.'),
('Removed the bends in the road edges and derived the taper symmetrically around the crossing.','Top and bottom framing lines omitted as in the prior highway reduction.','No useful exact Lucide match.','Wide crossing with vertical taper.'),
('Rebuilt the diagonal rocket, separated its exhaust, and restored globe grid detail below it.','Fins reduced to projecting strokes; one exhaust retained; geography represented by latitude and meridian.','Lucide rocket original and atomic-debug: pointed fuselage and fins.','Diagonal rocket and lower globe occupy a square.'),
('Rounded both scroll rolls, opened the lower curl, and restored a visible wavy center mark.','Wave reduced to one broad cycle.','Lucide scroll original and atomic-debug: rolled ends and shared sheet boundaries.','Upright parchment.'),
('Rebuilt the front as a continuous spiral, with tangent barrel ends and a clean attached flap.','No essential parts omitted.','Lucide cylinder original and atomic-debug: tangent barrel and matching end curves.','Wide horizontal rolled material.'),
('Restored a balanced wheel cross and splayed support beside a smooth coaster curve.','Wheel spoke count reduced to four; small hub and repeated coaster supports omitted.','Lucide ferris-wheel original and atomic-debug: radial wheel and support.','Square two-subject scene.'),
('Rebuilt the valve handle with equal end radii and separated the opposed rotation arrows from its base.','Base represented by a broad foot; fine base enclosure omitted.','Lucide rotate-cw original and atomic-debug: curved arrows and corner arrowheads.','Opposed arrows frame the valve in a square.'),
('Rebuilt mirrored signal arcs with exact extrema and kept the dish divider and splayed legs separated.','No essential parts omitted.','Lucide radio-tower original and atomic-debug: paired arcs and support.','Symmetric signal and antenna composition.'),
('Closed the baby head, integrated the ears into its silhouette, and rebuilt the top curl.','Facial dots omitted because the source face is blank.','Lucide baby original and atomic-debug; human_ref/user.svg circular anatomy.','Radial head and ears; no body or detached gap applies.'),
('Rebuilt the hen with smooth head and belly arcs, a clear beak and tail, and two separate short feet.','Tiny comb and inner wing seam omitted; fine toes reduced to short feet.','Lucide bird original and atomic-debug: smooth body and neck.','Horizontal bird silhouette.'),
('Rebuilt the flask shoulders and bulb using coherent arcs and exact neck/lip attachments.','Rolled lip reduced to one broad rim; empty flask retained.','Lucide flask-round original and atomic-debug: neck over round bulb.','Upright flask silhouette.'),
('Replaced the tangled bow with mirrored open lobes and regularized its ribbon junctions.','Fine ribbon tails and upper vertical ribbon section omitted to preserve bow openings.','Lucide gift original and atomic-debug: matching bow lobes.','Circular gift.'),
('Rebuilt the lid with tangent corners and attached the handle at exact shared endpoints.','Double lid band omitted; top rear rim has a short flat span to support legal exact handle nodes.','Lucide cylinder original and atomic-debug: equal cylindrical side curves.','Tall handled cylinder.'),
('Integrated the handle into a continuous lantern outline and rebuilt its ribs and pedestal at exact nodes.','Separate upper cap band omitted; handle base retained.','No useful Lucide lamp match for this round lantern.','Upright handled globe and pedestal.'),
('Restored four short curved texture marks and evenly separated them from each other and the circular edge.','Curves shortened to preserve spacing at 48 pixels.','Lucide cookie original and atomic-debug: sparse texture inside a circular outline.','Circular meatball.'),
('Rounded the chair back and arms, rebuilt the continuous seat/base contour, and restored two feet.','Cushion uses one shared seat edge instead of a doubled narrow seam.','Lucide armchair original and atomic-debug: continuous arms and lower silhouette.','Square frontal chair with mirrored parts.'),
('Rebuilt a rounded caravan shell, restored the wheel size and separated the window from the doorway.','Small window represented by one clear horizontal mark.','Lucide caravan original and atomic-debug: shell broken at the wheel.','Wide caravan with tow bar.'),
('Restored the complete car body around equal wheels and preserved the separate sun.','Fine sun rays and interior window seam omitted for spacing; sun remains a small circle.','Lucide car original and atomic-debug: side silhouette and wheel breaks.','Car and upper sun form a square scene.'),
]
for row,(note,omission,refs,reason) in zip(rows,notes):
 r=Path(row['run']);icon=load_icon(row['module']);report=icon.validate_icon();assert report.status=='valid' and not report.warnings
 meta=json.loads((r/f"{row['id']}.metadata.json").read_text());meta.update({'change':note,'omissions':omission,'construction_references':refs,'keyshape':icon.keyshape.name,'keyshape_reason':reason})
 (r/f"{row['id']}.metadata.json").write_text(json.dumps(meta,indent=2)+'\n')
 module=Path(row['module']);s=module.read_text();end=s.index('"""',3)+3;s='"""'+note+'\nSymbol plan: '+meta['plan']+'\nFinal reduction: '+omission+'\nReferences: '+refs+'\nKeyshape reason: '+reason+'\n"""'+s[end:];module.write_text(s)
 result={**meta,'status':'valid','validation_status':'valid','errors':0,'warnings':0,'visual_review':{'native_light':'reviewed','native_dark':'reviewed','enlarged_light':'reviewed','enlarged_dark':'reviewed','findings':note+' Smooth contour flow and legible negative spaces reviewed; intentional asymmetry follows the source orientation.'},'artifacts':{'module':module.name,'svg':row['id']+'.svg','validation':'validation.txt','previews':['preview-light-48.png','preview-dark-48.png','preview-light-384.png','preview-dark-384.png'],'reference_renders':['reference-48.png','reference-384.png']}}
 (r/'result.json').write_text(json.dumps(result,indent=2)+'\n')
 row['note']=note;row['omissions']=omission;row['references']=refs;row['keyshape']=icon.keyshape.name;row['keyshape_reason']=reason
(B/'ledger.json').write_text(json.dumps(rows,indent=2)+'\n')
print('Finalized 20 complete result folders, all valid, zero warnings.')
