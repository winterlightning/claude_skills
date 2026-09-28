from pathlib import Path
import json,sys,ast
sys.path.insert(0,str(Path.cwd()))
from icon_set.scripts.primitive_fix import load_icon
root=Path(__file__).parent;rows=json.loads((root/'batch.json').read_text())
omissions={0:'Tiny eye omitted to preserve clearance around the muzzle.',1:'Tiny eye omitted; hoop shown interrupted behind the dog.',2:'Inner haunch stroke and double tail outline omitted to keep the lifted paw legible.',3:'Finger divisions and inner ear detail omitted at 48px.',4:'Short left neck edge reduced into cone corner.',5:'Fine strings, sound holes and endpin omitted to retain a clear rounded instrument silhouette.',6:'No defining feature omitted; mouse buttons and both click waves retained.',7:'Secondary small bottom diamond omitted to give the bead and main diamond usable space.',8:'Pedestal reduced to an open bar and stem.',9:'No leg omitted; head and abdomen simplified to circular outlines.',10:'No feature omitted.',11:'Iris reduced to a small circle; tiny lens reflection omitted.',12:'Double collar reduced to a single nozzle divider.',13:'Fine nozzle transition simplified to an open broad pointed end.',14:'Fine nozzle transition simplified; open pointed contour retained.',15:'Tail strokes shortened to maintain mandated clearance.',16:'Inner beak divider and small foot flourish omitted.',17:'Foam lobes reduced to broad rounded scallops.',18:'Two source extraction specks below the foot omitted.',19:'Individual small toe divisions reduced to broad lobes; map regions retained.'}
for i,r in enumerate(rows):
 run=Path(r['result_dir']);p=next(run.glob('*.py'));s=p.read_text()
 reference='Lucide dog: coherent rounded animal contours.' if i in (0,1,2,3,4) else 'Lucide pipette: smooth diagonal tool silhouette and shared collar attachment.' if i in (12,13,14) else 'No useful exact Lucide match inspected; supplied reference guided the geometric reconstruction.'
 s=s.replace('Lucide: dog (rounded animal contours), pipette (coherent diagonal tool construction).',reference)
 s=s.replace('Human parts: human_ref/full_body_ref.png; no detached human head in these subjects.','Human reference: icon_set/references/human_ref/full_body_ref.png; hand/foot contour only, no detached head.' if i in (3,18,19) else '')
 p.write_text(s)
 icon=load_icon(p);v=icon.validate_icon();assert v.status=='valid' and not v.errors and not v.warnings
 r.update(author='gpt-6',keyshape=icon.keyshape.name,omissions=omissions[i],construction_reference=reference,validation_status=v.status,validation_errors=[],validation_warnings=[],visual_review='Inspected reference, before SVG, and revised SVG in light and dark at 48px and 192px. Rounded contour flow and readable subject accepted; intentional directional asymmetry retained.',artifacts=[q.name for q in sorted(run.iterdir()) if q.is_file()])
 r['note']=r['note']+' '+omissions[i]
 (run/'result.json').write_text(json.dumps(r,indent=2)+'\n')
(root/'batch.json').write_text(json.dumps(rows,indent=2)+'\n')
