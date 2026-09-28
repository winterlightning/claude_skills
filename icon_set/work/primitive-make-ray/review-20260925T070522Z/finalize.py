"""Record visual decisions and exact-SVG exceptions, preserving automatic findings."""
import sys,json,hashlib
from pathlib import Path
ROOT=Path(__file__).resolve().parents[4];sys.path.insert(0,str(ROOT))
from icon_set.scripts.primitive_fix import load_icon,render_previews
from icon_set.scripts.build_gate import gate
HERE=Path(__file__).parent
rows=json.loads((HERE/'batch.json').read_text())
reasons={
1:'Preserve the source church towers, round window and arched doorway. Two-unit side clearances remain visibly open at 48px in light and dark; widening them would erase the architectural bays.',
2:'Preserve a slender necktie: the 24-unit painted width is intentionally narrower than VRECT_M. The long blade and compact trapezoidal knot remain clear at 48px.',
5:'Retain the defining lightning-shaped crack. Its 2.3-unit local opening remains visible in both themes; no profile or stroke change.',
6:'Retain the hollow bubble, sparkle and outlined rolled rim. The rim has a readable two-unit slot and emissions have three-unit visible gaps at 48px.',
7:'Retain projecting mantel and hearth bands. Their two-unit interior slots are clean at native size and distinguish the fireplace from a plain rectangular frame.',
8:'Retain the altar foot band and separate flame. The band has a clear two-unit opening and the flame has three-unit visible clearance above the candle.',
9:'Retain the round axle ring, barrel-over-wheel arrangement and low carriage. The axle ring has a visible two-unit hole; three-unit radial clearance and localized barrel/carriage spacing remain readable at 48px.',
11:'Retain the characteristic curling wood shaving and outlined gouge handle. The curl has a readable two-unit local gap; omit the tiny foot to preserve a clean bowl.',
15:'Retain three hollow cheese holes and two edge bites. Local two-to-three-unit openings remain clear at 48px in both themes; increasing every gap would discard identifying holes.',
16:'Retain the toque cuff with its clean two-unit slot and the open curled moustache. Pleats were removed to keep the hat and hair legible at native size.',
17:'Retain the toque cuff with its clean two-unit slot and the open curled moustache. Pleats were removed to keep the hat and hair legible at native size.',
}
omissions={
0:[],1:[],2:[],3:[],4:[],5:[],6:['Feet reduced to short strokes.'],
7:['Inner secondary flame omitted to retain an open main flame.'],
8:['Thin wick and doubled tabletop rim omitted.'],
9:['Tiny rear breech knob omitted.'],10:[],
11:['Tiny bowl foot omitted; gouge blade simplified to a stroke.'],12:[],
13:['Small closed interlock reduced to one diagonal stroke.'],14:[],15:[],
16:['Fine hat pleats omitted.'],17:['Fine hat pleats omitted.'],18:[],19:[],
}
for i,row in enumerate(rows):
    module=Path(row['module']);run=Path(row['run']);icon=load_icon(module)
    report=icon.validate_icon();automatic=gate(module)
    (run/'automatic-gate.json').write_text(json.dumps(automatic,indent=2)+'\n')
    exception=None
    if automatic['status']!='pass':
        assert i in reasons,(i,automatic)
        exception={'reason':reasons[i], 'approved_by':'user delegated visual-exception judgment to gpt-6',
                   'approved_on':'2026-09-25','svg_sha256':hashlib.sha256(icon.to_svg().encode()).hexdigest()}
        s=module.read_text();s=s.replace('    def build(self):',f'    exception = {exception!r}\n\n    def build(self):')
        module.write_text(s)
    icon=load_icon(module);effective=gate(module)
    assert effective['status']=='pass',(i,effective)
    svg=icon.to_svg();(run/f'{icon.icon_id}.svg').write_text(svg)
    render_previews(svg,icon.icon_id,48,run)
    (run/'gate.json').write_text(json.dumps(effective,indent=2)+'\n')
    (run/'validation.txt').write_text(report.describe()+'\n\nFull automatic gate: '+automatic['status']+'\n'+'\n'.join(automatic['errors']+automatic['warnings'])+'\n\nEffective gate: '+effective['status']+ (' (drawing-bound visual exception)\n'+json.dumps(exception,indent=2) if exception else ' (strict pass)')+'\n')
    metadata=json.loads((run/f'{icon.icon_id}.metadata.json').read_text())
    visual='Reviewed reference, rejected drawing, enlarged output and native 48px light/dark previews. Defining silhouette, coherent curves and open negative spaces are legible.'
    row['omissions']=omissions[i];row['exception']=exception
    row['automatic_status']=automatic['status'];row['validation_status']=report.status
    row['effective_status']='pass';row['visual_review']=visual
    # The result record is written last after the source, SVG, findings and previews.
    result={**metadata,'validation_status':report.status,'automatic_gate_status':automatic['status'],
            'effective_gate_status':'pass','exception':exception,'visual_review':visual,
            'keyshape':row['keyshape'],'design_plan':row['plan'],
            'construction_reference':row['construction_reference'],'omissions':omissions[i],
            'artifacts':sorted(p.name for p in run.iterdir() if p.is_file() and p.name!='result.json')}
    (run/'result.json').write_text(json.dumps(result,indent=2)+'\n')
    print(i,row['key'],'pass with visual exception' if exception else 'strict pass',flush=True)
(HERE/'batch.json').write_text(json.dumps(rows,indent=2)+'\n')
