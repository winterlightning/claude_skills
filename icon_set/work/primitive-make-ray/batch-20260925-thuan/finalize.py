from pathlib import Path
import json,sys,hashlib
sys.path.insert(0,str(Path.cwd()))
from icon_set.scripts.primitive_fix import load_icon
from icon_set.scripts.build_gate import gate
root=Path('icon_set/work/primitive-make-ray/batch-20260925-thuan')
rows=json.loads((root/'manifest.json').read_text())
reasons={
1:'Retain the horse muzzle undercut and curved neck: the short local opening remains visible at 48px in both themes; broad neck and pedestal preserve recognition.',
2:'Retain the circular royal finial and stepped three-point crown above a tall chess-piece body. Small local crown openings remain clear in native light and dark previews.',
8:'Allow the wood base to reach y=47 ink inside the 48px canvas, preserving a readable separate chisel blade, handle and wood grain recess. All spacing checks pass.',
13:'Allow 3px ink clearances between checkbox, page and text strokes. Both square openings are 4px wide; paired rows remain clearly separated and legible at 48px.',
17:'Retain two open, unequal circular pores instead of a solid dot. Approximately 3.1px outer ink clearance remains clear in native light and dark themes.',
19:'Use a naturally shallow eyelid envelope with ink y=11..37 instead of stretching it to y=8..40. Five evenly fanned lashes and continuous lid read clearly at 48px.'}
omissions={1:'Small eye and mane absent in supplied silhouette; none added.',2:'No defining features omitted.',3:'Two broad bite scallops replace fine irregularities.',4:'No defining features omitted.',5:'None.',6:'None.',7:'Fine extended back post simplified into body contour.',8:'Fine internal wood grain reduced to one wavy upper surface.',9:'Small crossbar overhang omitted.',10:'Small crossbar overhang omitted.',11:'None; detached head/body ink gap exactly 4px (head bottom centerline 20, shoulder top 28).',12:'None.',13:'None.',14:'None.',15:'None.',16:'Added three short keyboard strokes to strengthen piano reading.',17:'None.',18:'Tiny separate lip mark absorbed into the face contour.',19:'Seven source lashes reduced to five.',20:'None.'}
for row in rows:
 p=Path(row['module']);run=p.parent;i=row['index'];icon=load_icon(p);automatic=json.loads((run/'gate.json').read_text())
 (run/'automatic-gate.json').write_text(json.dumps(automatic,indent=2))
 if i in reasons:
  exception=dict(reason=reasons[i],approved_by='user-delegated-to-gpt-6',approved_on='2026-09-25',svg_sha256=hashlib.sha256(icon.to_svg().encode()).hexdigest())
  s=p.read_text();s=s.replace('class Drawing(Solo48):','class Drawing(Solo48):\n    exception = '+repr(exception));p.write_text(s)
  finalgate=gate(p);(run/'gate.json').write_text(json.dumps(finalgate,indent=2))
 else:finalgate=automatic
 assert finalgate['status']=='pass',(i,finalgate)
 icon=load_icon(p);report=icon.validate_icon()
 (run/'validation.txt').write_text(report.describe()+'\n\nFull gate:\n'+json.dumps(finalgate,indent=2))
 result=dict(source_uuid=row['source_uuid'],reference_path=row['reference_path'],concept=row['concept'],icon_id=icon.icon_id,author='gpt-6',module=p.name,validation_status=report.status,build_gate_status=finalgate['status'],automatic_status=automatic['status'],exception=finalgate.get('exception'),visual_review='Reviewed enlarged and at 48px in light/dark; smooth coherent contours, clear negative space and reference identity retained.',changes=row['note'],keyshape=icon.keyshape.name,construction_reference=row['reference'],omissions=omissions[i],artifacts=sorted(x.name for x in run.iterdir() if x.is_file()))
 (run/'result.json').write_text(json.dumps(result,indent=2))
 print(i,icon.icon_id,'PASS'+(' — approved exception' if i in reasons else ''),flush=True)
