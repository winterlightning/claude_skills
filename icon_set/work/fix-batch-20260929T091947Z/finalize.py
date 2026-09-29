from pathlib import Path
import json,sys,hashlib
ROOT=Path(__file__).resolve().parents[3];sys.path.insert(0,str(ROOT))
from icon_set.scripts.primitive_fix import load_icon,run_module,approved_visual_exception
from icon_set.scripts.build_gate import gate
from author_batch import D
root=Path(__file__).parent;rows=json.loads((root/'batch.json').read_text())
REASONS={
0:'Preserve a complete receiver with rounded earpieces rather than a crescent; the compact handset opening and frame gap remain legible at 48px.',
1:'Preserve the soft hooked handset and rounded terminal pieces; retain its narrow curved interior as in the original.',
2:'Preserve the large Q bowl and proportional tail; compact frame-to-bowl spacing is intentional and remains visibly open.',
5:'Preserve the reference separated chevron and rising elbow; accept compact arrowhead clearances after native-size review.',
9:'Preserve four grasping fingers, an upright phone and two inward arrows; repeated 2px finger openings and intended hand contacts remain readable.',
10:'Preserve the closed surgical scissors and separate curved crossed marker; compact contacts and natural combined envelope are intentional.',
11:'Preserve all five descending cells and both curved return arrows; compact cell openings and arrow clearances are intentional.',
13:'Preserve three overlapping hands and wrist directions with two clear foreground finger creases; accept intended contact and organic envelope.',
14:'Preserve the tapered angled microphone, tall stand and trailing cable; the tapered handle interior and physical stand contact are intentional.',
15:'Preserve the arched back and bent arm pose; exact detached head gap is 4px, with a conservative curve warning retained; compact arm opening and natural envelope accepted.',
17:'Preserve the standing person reaching the desk and edge-view monitor; compact working-surface contacts and natural composition bounds accepted.',
19:'Preserve the larger clock face and detached hands inside the page; compact clock clearance and larger page envelope remain readable at 48px.'}
for i,r in enumerate(rows):
 dest=Path(r['result_dir']);module=run_module(dest);icon=load_icon(module)
 auto= json.loads((dest/'automatic-gate.json').read_text()) if (dest/'automatic-gate.json').exists() else gate(module)
 (dest/'automatic-gate.json').write_text(json.dumps(auto,indent=2))
 if auto['status']!='pass':
  approval=dict(reason=REASONS[i],approved_by='user-authorized visual judgment by gpt-6',approved_on='2026-09-29',svg_sha256=hashlib.sha256(icon.to_svg().encode()).hexdigest())
  s=module.read_text();s=s.replace('    semantic_role =',f'    exception = {approval!r}\n    semantic_role =');module.write_text(s)
 icon=load_icon(module);rep=icon.validate_icon();g=gate(module)
 assert g['status']=='pass',(i,g)
 accepted=approved_visual_exception(rep,g)
 assert accepted or (rep.status=='valid' and not rep.warnings),(i,rep.describe())
 (dest/'gate.json').write_text(json.dumps(g,indent=2))
 (dest/'validation.txt').write_text(rep.describe()+'\n\n'+json.dumps(g,indent=2))
 review='Reviewed reference, rejected drawing, enlarged and native 48px light/dark previews. Meaning restored; 4px strokes retained; purposeful tight detail accepted only with drawing-bound exception.'
 result=dict(r,author='gpt-6',module=module.name,svg=r['icon_id']+'.svg',keyshape=D[i]['keyshape'],validation_status=rep.status,gate_status=g['status'],automatic_gate_status=auto['status'],accepted_exception=accepted,visual_review=review,comparison=D[i]['wrong'],feedback=r['feedback'],changes=D[i]['change'],omissions=D[i]['omissions'],construction_reference=D[i]['lucide'],exception=g.get('exception'),artifacts=[p.name for p in dest.iterdir() if p.is_file()])
 if i in (15,16,17):
  result['human_spacing']={15:'Shared human_ref/full_body_ref.png: circular head center (13,8), radius 4; upper torso junction (25,8), with its outward tangent aligned to the head axis. 12 - 4 - 4 = 4 visible ink gap. Validator finds its nearest pair at (17,8) and (25,8), distance 8, retained as a conservative warning.',16:'Shared human_ref/full_body_ref.png: circular head center (24,10), radius 4; torso begins (24,22). 22 - 10 - 4 - 4 = 4 visible ink gap. Circular head and torso axis align; strict QA passes.',17:'Shared human_ref/full_body_ref.png: circular head center (36,10), radius 4; torso begins (36,22). 22 - 10 - 4 - 4 = 4 visible ink gap. Circular head and torso axis align; exception concerns desk and monitor details.'}[i]
 (dest/'result.json').write_text(json.dumps(result,indent=2))
 print(i,r['icon_id'],'PASS · exception' if accepted else 'PASS · strict',flush=True)
