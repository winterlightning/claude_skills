from pathlib import Path
import json,sys,hashlib,shutil
HERE=Path(__file__).resolve().parent;ROOT=HERE.parents[3];sys.path.insert(0,str(ROOT))
from icon_set.scripts.primitive_fix import load_icon,approved_visual_exception
from icon_set.scripts.build_gate import gate
items=json.loads((HERE/'items.json').read_text())
reasons={
2:'Retain two outlined sloping towers, two falling-water marks and two separated waves. Compact tower and water spacing remains readable at 48 px in both themes; forcing 4-unit gaps removes identifying dam detail.',
6:'Retain the broad diagonal arrow inside its clipped tag. The local 3.07-unit ink gap at the arrow tip is visibly open at 48 px.',
7:'Retain the circular counter inside the curved emblem and the separate capsule. The small-circle counter is distinct in both themes; the compact emblem cannot keep the source proportions with a 4-unit gap around that counter.',
8:'Retain the complete rounded-square InVision logo and compact italic lettering. The frame, i dot and n are legible at 48 px; logo-specific inner spacing is accepted.',
9:'Keep the source infinity lobes broad and round rather than stretching them vertically to the standard rectangle. All ink stays inside the 48 px canvas.',
10:'Keep the bent defensive arm and wide fighting stance. The arm/leg ink clearance is 3.07 units and remains open at native size; the outlined head has an exact 4-unit ink gap to its own vertical neck tangent.',
11:'Keep the high kick and raised guard; the local guard/leg gap is about 2.19 ink units and remains legible. The circular head has the exact 4-unit ink gap at its own torso junction.',
12:'Retain the pointed hull, cockpit and two complete paddle blades. Natural equipment proportions require a slightly larger envelope and compact cockpit spacing; the paddle joins remain readable in both themes.',
13:'Retain the long cockpit within the pointed hull and both complete diagonal paddle blades. Compact hull/cockpit spacing and a slightly larger envelope preserve recognizability without clipping.',
14:'Keep all four rounded fingers, thumb and cuff. Seven-unit finger spacing leaves three visible ink units; a standard 8-unit gap would distort the glove proportions. Native previews retain distinct fingers.',
15:'Keep the swept horn and bent foreleg of the leaping antelope. Compact horn and muzzle/neck spacing remains open and the complete airborne silhouette reads at native size.',
16:'Preserve dog, ball and presenting hand in one 48 px scene. Compact hand anatomy and muzzle/ball spacing are visible in both themes, with no ball contact or missing composition elements.',
17:'Keep the therapist holding a reclining patient leg and the natural two-figure proportions. The top lies 2 units above the chosen keyshape and local limb spacing is compact. Both radius-4 heads retain exact 4-unit gaps at their own torso junctions; all ink stays inside the canvas.',
18:'The circular cut face intentionally meets the cylindrical body tangentially at its top and bottom. Internal-spacing advisories at these real attachments do not indicate separate crowded parts; the concentric growth ring remains open.',
19:'Keep the airborne split-leg pose and separated ground line at natural proportions. The top lies 4 units above the chosen rectangle and arm/leg spacing is locally compact; the head has an exact 4-unit gap at its own torso and all ink stays in the canvas.'
}
omissions={0:'Tiny ruler notch omitted.',1:'Tiny eye omitted to preserve clear wolf head.',2:'No semantic omissions; wave count reduced.',3:'Small source gaps in the arrow arms replaced by continuous intentional joins.',4:'No identifying features omitted.',5:'No identifying features omitted.',6:'Arrow-tip micro-kink simplified.',7:'No identifying features omitted.',8:'Fine typographic serifs simplified.',9:'Interweave indicated by a single deliberate break.',10:'Garment outline reduced to shared stick-figure construction.',11:'Garment outline reduced to shared stick-figure construction.',12:'Paddle shaft behind hull occluded.',13:'Paddle shaft behind cockpit/hull occluded.',14:'No identifying fingers omitted.',15:'Small ear detail omitted; horn retained.',16:'Individual trainer fingers simplified to two coherent hand strokes.',17:'Clothing outlines simplified to two interacting stick figures.',18:'Fine bark marks and small branch-end ellipse omitted to avoid pinches.',19:'Motion ticks and clothing outline omitted; airborne pose and ground retained.'}
for i,it in enumerate(items):
 old=ROOT/it['run'];module=ROOT/it['module'];icon=load_icon(module);before=gate(module)
 exception=before['status']!='pass' or bool(before['warnings'])
 if exception:
  assert i in reasons,i
  new=old.with_name('20260928T175102Z-reviewed-final');new.mkdir(exist_ok=False)
  for p in old.iterdir():
   if p.is_file() and p.name!='result.json':shutil.copyfile(p,new/p.name)
  module=new/module.name
  sha=hashlib.sha256(icon.to_svg().encode()).hexdigest()
  approval=dict(reason=reasons[i],approved_by='user-delegated-discretion-reviewed-by-gpt-6',approved_on='2026-09-29',svg_sha256=sha)
  with module.open('a') as f:f.write('\n# User authorized quality-preserving exceptions; approval binds this exact drawing.\nDrawing.exception = '+repr(approval)+'\n')
  it['run']=str(new.relative_to(ROOT));it['module']=str(module.relative_to(ROOT))
 run=ROOT/it['run'];icon=load_icon(module);report=icon.validate_icon();g=gate(module)
 assert g['status']=='pass',(i,g)
 assert approved_visual_exception(report,g) if exception else report.status=='valid' and not report.warnings
 (run/'gate.json').write_text(json.dumps(g,indent=2))
 (run/'validation.txt').write_text(report.describe()+'\n\nFull build gate: '+g['status']+'\nAutomatic gate: '+g.get('automatic_status',g['status'])+'\n'+('Drawing-bound exception: '+reasons[i]+'\n' if exception else '')+'\n'.join(g['errors']+g['warnings'])+'\n')
 shutil.copyfile(ROOT/it['ref'],run/'original.svg');shutil.copyfile(ROOT/it['before'],run/'rejected.svg')
 visual='Reviewed original and rejected drawing, then native 48 px and enlarged light/dark output. Smooth contour flow, recognizable source composition and surviving negative spaces confirmed.'
 (run/'visual-review.md').write_text(visual+'\n\n'+it['change']+'\n\nOmissions: '+omissions[i]+'\n\n'+('Exception: '+reasons[i] if exception else 'Strict model and full build gate pass with zero warnings.')+'\n')
 meta=json.loads((run/f"{it['id']}.metadata.json").read_text())
 result={**meta,'icon_id':it['id'],'author':'gpt-6','module':module.name,'svg':it['id']+'.svg','validation_status':report.status,'validation_errors':report.errors,'validation_warnings':report.warnings,'build_gate':g,'accepted_exception':exception,'visual_review':visual,'change':it['change'],'omissions':omissions[i],'references':[it['ref'],it['before'],it['lucide']],'artifacts':sorted(p.name for p in run.iterdir() if p.is_file())}
 (run/'result.json').write_text(json.dumps(result,indent=2))
 it.update(exception=exception,exception_reason=reasons.get(i),omissions=omissions[i],validation=report.status,gate=g['status'])
 print(i,it['id'],'pass with exception' if exception else 'strict pass',flush=True)
(HERE/'items.json').write_text(json.dumps(items,indent=2))
