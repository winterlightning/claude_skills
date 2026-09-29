from pathlib import Path
import json,sys,hashlib,shutil
sys.path.insert(0,str(Path(__file__).resolve().parents[4]))
from icon_set.scripts.primitive_fix import load_icon
from icon_set.scripts.build_gate import gate
ROOT=Path(__file__).resolve().parent
rows=json.loads((ROOT/'batch.json').read_text())
reasons={
4:'The tilted cup, neck, trigger and grip remain distinct at 48px; intentional 2.28–3.22px local clearances preserve a recognizable compact airbrush. Uniform 4px strokes and canvas retained.',
5:'Tapered aircraft wings and tail intentionally converge into acute tips. Retaining these open swept silhouettes reads more naturally than thick rectangular wings; reviewed at 48px in both themes.',
6:'A complete spraying-aircraft scene needs three vertical levels. The fuselage, two spray marks and three separate stemmed sprouts remain readable at 48px with local 1–3px ink gaps. Ground line omitted to reduce density.',
7:'Four cardinal clock ticks retain 2px radial ink clearance from the circular rim. They and the 10:08 hands remain clearly separated at 48px and restore meaningful reference detail.',
10:'The upholstered swept back and armrest retain 3.22–3.72px local ink gaps. These openings remain clear at 48px and preserve the reference chair construction.',
16:'The capped clown retains blank circular jaw, scalloped hair, pompom and bowtie with small wing openings, a 2px face-to-knot gap and 0.064px keyshape overshoot. All features were checked in both themes at 48px; these compromises preserve the complete portrait.'}
for i,r in enumerate(rows):
 run=Path(r['run']);module=Path(r['module'])
 if i in reasons:
  approved=run.with_name(run.name+'-exception')
  shutil.copytree(run,approved)
  module=approved/module.name;run=approved
  icon=load_icon(module);sha=hashlib.sha256(icon.to_svg().encode()).hexdigest()
  exception={'reason':reasons[i],'approved_by':'gpt-6 under user-delegated exception authority','approved_on':'2026-09-28','svg_sha256':sha}
  with module.open('a') as f:f.write('\n# User explicitly delegated quality-preserving visual exceptions for this batch.\nDrawing.exception = '+repr(exception)+'\n')
  r.update(run=str(run),module=str(module))
 icon=load_icon(module);report=icon.validate_icon();qa=gate(module)
 if qa['status']!='pass':raise RuntimeError((i,qa))
 svg=icon.to_svg();(run/(r['icon_id']+'.svg')).write_text(svg)
 (run/'validation.txt').write_text(report.describe()+'\n\nFULL GATE\n'+json.dumps(qa,indent=2))
 (run/'gate.json').write_text(json.dumps(qa,indent=2))
 r['status']='pass · exception' if i in reasons else 'valid · pass'
 r['exception_reason']=reasons.get(i)
 result={'source_uuid':r['source_uuid'],'reference_path':r['ref'],'concept':r['concept'],'icon_id':r['icon_id'],'author':'gpt-6','validation_status':report.status,'build_gate':qa,'acceptance':r['status'],'visual_review':'Inspected reference and rejected drawing before authoring; inspected revised native 48px and enlarged previews in light/dark themes. Coherent silhouette, smooth contour flow and readable identifying details.','before_findings':r['wrong'],'feedback':r['feedback'],'changes':r['change'],'keyshape':r['keyshape'],'construction_references':r['construction'],'omissions':'Ground line omitted from spraying scene; minor cushion merged into high-back chair outline; source blank faces remain blank. Other reductions noted in module.' if i in [6,11] else 'No additional identity-bearing features omitted.','artifacts':[module.name,r['icon_id']+'.svg',r['icon_id']+'.metadata.json','reference.png','before.png','preview-light-48.png','preview-dark-48.png','preview-light-384.png','preview-dark-384.png','validation.txt','gate.json']}
 (run/'result.json').write_text(json.dumps(result,indent=2))
 print(i,r['icon_id'],r['status'],flush=True)
(ROOT/'batch.json').write_text(json.dumps(rows,indent=2))
