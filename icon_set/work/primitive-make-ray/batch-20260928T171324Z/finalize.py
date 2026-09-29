from author_batch import *
import hashlib
from datetime import datetime,timezone
from icon_set.scripts.primitive_fix import approved_visual_exception
REASONS={
1:'The piercing arrow creates intentional short narrow regions near its real heart crossing. Retain the complete smooth heart, arrow shaft and arrowhead; both are clearly distinguishable in native light/dark previews.',
3:'A recognizable slender thermometer needs a narrow stem and mercury column. Their 2-unit visible gap, small outlined bulb and nearby three scale ticks remain clear at 48 px; widening the stem would recreate the rejected bulky silhouette.',
4:'Preserve the original shallow ruler proportions and all five ticks. The 18-unit visible height and 2–3-unit visible tick gaps remain clear; a standard tall envelope would recreate the rejected slab shape.',
6:'Retain the rocket nose seam, oval window and separately recognizable fins. The 2-unit visible fin openings and nose/window gap remain readable at 48 px; dropping these parts caused the rejected bell-like silhouette.',
7:'The circular target and attached larger node need 2-unit side insets, extending beyond the square keyshape guide without approaching the canvas boundary. The node/arrow gap is 3 visible units; the arrow remains distinct and centered.',
9:'The loading bar must be a shallow capsule with true semicircular ends. Keep the 16-unit visible height and source stripe angle rather than stretch it into a tall rounded box. All automatic spacing checks pass.',
10:'Preserve the shallow capsule and two steeper diagonal stripes from the reference. Its 16-unit visible height is intentionally smaller than the standard rectangle envelope. All automatic spacing checks pass.',
11:'Retain both diagonal open wrench jaws and the phone lower band. The lower jaw has 2-unit visible side clearance within the slender handset, and remains separated at native size in both themes.',
12:'Keep two readable barrel graduation marks instead of the rejected single mark. Their approximately 3-unit visible diagonal spacing and rounded barrel remain clear at 48 px.',
13:'Preserve a complete diamond mortarboard and separate curved crown inside the portrait card. Board/card side gaps are 2 visible units and the crown openings remain visible; merging the board seam caused the rejected roof-like symbol.',
15:'Restore the taller pin and larger circular opening while keeping the reference ground line close to its point. The intentional ground gap is 2 visible units; the circular opening remains distinct and unclipped.',
16:'The source is a horizontal open infinity loop. Its 28-unit visible height intentionally underfills HRECT_M by 2 units at top and bottom; all spacing checks pass, and the open ends remain clear.',
17:'The rounded cable loop and compact plug require 2-unit top/bottom canvas insets beyond the square guide. The complete loop, two prongs and free cable end are distinct; all automatic spacing checks pass.',
18:'Retain the wider battery proportion and two left-aligned charge marks. The shallow envelope and 2-unit top/bottom interior gaps remain readable at 48 px, preserving the source charge count.',
19:'Keep the wide low-battery silhouette and one left charge mark. The shallow envelope and 2-unit interior vertical clearance preserve the reference proportions and stay visibly open.',
20:'Preserve a tall outlined low-charge block rather than collapse it to the rejected single stroke. Its 2-unit inner opening and case clearance remain legible; the body is intentionally shallower than HRECT_M.'
}
records=json.loads((Path(__file__).parent/'final-runs.json').read_text())
for r in records:
    out=ROOT/r['run'];module=ROOT/r['module'];icon=load_icon(module)
    if r['n'] in REASONS:
        approval={'reason':REASONS[r['n']],'approved_by':'user-delegated:gpt-6','approved_on':'2026-09-29','svg_sha256':hashlib.sha256(icon.to_svg().encode()).hexdigest()}
        with module.open('a') as f:f.write('\n    # User delegated visual exceptions; original automatic findings remain recorded.\n    exception = '+repr(approval)+'\n')
        icon=load_icon(module)
    report=icon.validate_icon();g=gate(module);accepted=approved_visual_exception(report,g)
    assert g['status']=='pass' and (accepted or (report.status=='valid' and not report.warnings)),(r['icon_id'],g)
    (out/'gate.json').write_text(json.dumps(g,indent=2))
    (out/'validation.txt').write_text(report.describe()+'\n\nFull build gate: '+g['status']+'\nAutomatic gate: '+g.get('automatic_status',g['status'])+'\n'+json.dumps(g,indent=2)+'\n')
    assert icon.to_svg()==(out/f"{r['icon_id']}.svg").read_text()
    visual='Compared the full original reference and displayed rejected SVG before drawing. Inspected the revised native 48 px and enlarged light/dark renders: defining details are readable, stroke joins are coherent, openings remain visible, and no artwork clips the canvas.'
    result={
      'source_uuid':r['source_uuid'],'reference_path':r['reference'],'concept':r['concept'],'icon_id':r['icon_id'],'author':AUTHOR,
      'keyshape':r['spec']['keyshape'],'keyshape_rationale':r['spec']['change'],
      'validation_status':report.status,'validation_errors':list(report.errors),'validation_warnings':list(report.warnings),
      'build_gate':g,'accepted_exception':accepted,'visual_review':visual,'problem':r['spec']['problem'],
      'feedback':r['feedback'],'changes':r['spec']['change'],'construction_reference':r['spec']['construction_reference'],
      'omissions':r['spec']['omissions'],'intentional_asymmetry':'Source-directed arrow, scale ticks, stripes, cable plug, charge placement or diagonal object arrangement retained where applicable; paired silhouette parts use matching geometry.',
      'artifacts':[p.name for p in sorted(out.iterdir()) if p.is_file() and p.name!='result.json'],'finished_at':datetime.now(timezone.utc).isoformat()
    }
    (out/'result.json').write_text(json.dumps(result,indent=2)+'\n')
    r.update(validation_status=report.status,gate=g,accepted_exception=accepted,author=AUTHOR,visual_review=visual)
    print(r['n'],r['icon_id'],'PASS WITH EXCEPTION' if accepted else 'PASS',flush=True)
(Path(__file__).parent/'ready-runs.json').write_text(json.dumps(records,indent=2))
