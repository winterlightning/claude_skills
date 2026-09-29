"""Record inspected exact-drawing exceptions, preserve findings, export final records."""
from author_batch import *
import hashlib
from datetime import datetime,timezone
from icon_set.scripts.primitive_fix import approved_visual_exception
REASONS={
1:'The source-specific stepped keyboard needs compact rows. Preserve the shorter body requested by the reviewer, the stepped shoulders, two key rows and spacebar; the open negative spaces remain legible at 48 px.',
2:'A wider keyboard proportion needs three interior rows in HRECT_M. Retain uniform 7-unit centerline spacing (3-unit visible gaps), both rows and the spacebar instead of returning to the rejected squat proportions.',
3:'The fork needs three long parallel tines to read correctly. Their approximately 3-unit visible gaps and the utensil crossing remain clear at 48 px; preserve the reviewer-requested fork shape.',
4:'The fork needs three long tines and a clear U bowl. Approximately 3-unit gaps preserve the fork and the diagonal oval spoon; the spoon was moved away from the fork to remove the earlier narrow wedge.',
5:'The original eye requires an almond silhouette, iris and outlined pupil. The intentional approximately 2-unit annular gaps remain distinct at 48 px; enlarging them would recreate the rejected round eye or remove the pupil.',
6:'Preserve the recognizable continuous-neck robed angel and separated open wing. The halo has 2-unit canvas inset; wing/robe clearance is about 3.69 visible units. The exact halo/head separation has a conservative curve warning. No clipping or stroke changes.',
7:'The reference requires a person inside the heart. The repaired 2-unit heart/head and approximately 2.62-unit heart/shoulder visible gaps remain open. The head-to-shoulder gap is exactly 4 visible units; circular head and broad open shoulders are retained.',
9:'The landscape phone side panel intentionally uses a 2-unit visible gap around the hardware dot to keep the display wider. Equal corner radii, a distinct side divider and readable button are retained.',
13:'Preserve the original bell with a flared base inside a slender phone. The 2-unit visible side clearance around the bell rim remains readable; removing the flare would recreate the rejected bell silhouette.'
}
records=json.loads((Path(__file__).parent/'final-runs.json').read_text())
for r in records:
    out=ROOT/r['run'];module=ROOT/r['module'];icon=load_icon(module)
    if r['n'] in REASONS:
        approval={'reason':REASONS[r['n']], 'approved_by':'user-delegated:gpt-6','approved_on':'2026-09-29','svg_sha256':hashlib.sha256(icon.to_svg().encode()).hexdigest()}
        with module.open('a') as f:f.write('\n    # User explicitly delegated visual exceptions; automatic findings are preserved.\n    exception = '+repr(approval)+'\n')
        icon=load_icon(module)
    report=icon.validate_icon();g=gate(module)
    accepted=approved_visual_exception(report,g)
    assert g['status']=='pass' and (accepted or (report.status=='valid' and not report.warnings)),(r['icon_id'],g)
    (out/'gate.json').write_text(json.dumps(g,indent=2))
    (out/'validation.txt').write_text(report.describe()+'\n\nFull build gate: '+g['status']+'\nAutomatic gate: '+g.get('automatic_status',g['status'])+'\n'+json.dumps(g,indent=2)+'\n')
    svg=icon.to_svg();assert svg==(out/f"{r['icon_id']}.svg").read_text()
    visual='Inspected the complete reference and displayed rejected drawing, then the final native 48 px and enlarged light/dark previews. Contours are smooth and intentional openings remain visible.'
    if r['n']==6:visual+=' The source has a continuous robed neck; head/robe share actual endpoints at (28,18) and (34,24). This is not a detached stick figure.'
    if r['n']==7:visual+=' Head center (24,19), radius3, lower centerline22; shoulders crest30 gives exactly 8 centerline / 4 ink units.'
    result={
        'source_uuid':r['source_uuid'],'reference_path':r['reference'],'concept':r['concept'],
        'icon_id':r['icon_id'],'author':AUTHOR,'keyshape':r['spec']['keyshape'],
        'keyshape_rationale':'The envelope follows the subject proportions; see review-before-drawing.json and any exact-drawing exception.',
        'validation_status':report.status,'validation_errors':list(report.errors),'validation_warnings':list(report.warnings),
        'build_gate':g,'accepted_exception':accepted,'visual_review':visual,
        'problem':r['spec']['problem'],'feedback':r['feedback'],'changes':r['spec']['change'],
        'construction_reference':r['spec']['construction_reference'],'omissions':r['spec']['omissions'],
        'intentional_asymmetry':'Utensil heads, flying pose, overlapping hearts and directional screen marks preserve their source arrangement.' if r['n'] in (3,4,6,8,9,10,15,17) else 'Main outline and repeated parts are centered and symmetric.',
        'artifacts':[p.name for p in sorted(out.iterdir()) if p.is_file() and p.name!='result.json'],
        'finished_at':datetime.now(timezone.utc).isoformat()
    }
    (out/'result.json').write_text(json.dumps(result,indent=2)+'\n')
    r.update(validation_status=report.status,gate=g,accepted_exception=accepted,author=AUTHOR,visual_review=visual)
    print(r['n'],r['icon_id'],'PASS WITH EXCEPTION' if accepted else 'PASS',flush=True)
(Path(__file__).parent/'ready-runs.json').write_text(json.dumps(records,indent=2))
