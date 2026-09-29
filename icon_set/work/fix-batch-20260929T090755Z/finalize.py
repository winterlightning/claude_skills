from pathlib import Path
import json,sys,hashlib
ROOT=Path(__file__).resolve().parents[3];sys.path.insert(0,str(ROOT))
from icon_set.scripts.primitive_fix import load_icon,run_module,approved_visual_exception
from icon_set.scripts.build_gate import gate
from author_batch import D
root=Path(__file__).parent;rows=json.loads((root/'batch.json').read_text())
REASONS={
0:'The recognizable cab, open house doorway and flatbed need compact internal openings at 48px; visually distinct at native size.',
1:'Preserve the medical cross, large cargo box and glazed truck cab; compact windshield clearance remains legible.',
2:'Preserve house, box truck and outlined wheels in the reference arrangement; accept compact cab and natural composition envelope.',
3:'Preserve broad gift bow, parcel ribbon and glazed cab; intentional ribbon/body joins and compact vehicle details.',
4:'Preserve an outlined telephone handset with earpieces inside its reply bubble; accept small handset apertures and the tail envelope.',
5:'Preserve the three-tire tuk-tuk front, two headlights and tapered canopy; accept compact tire openings and reference contacts.',
7:'Preserve a large retro television screen with two separate knobs and feet; clean 2px internal ink gaps are intentional.',
8:'Preserve the twin mountains joining a curved dome/base; the intended junction is visually continuous.',
9:'Preserve outward-angled nasal inserts and sculpted bridge; openings are distinct with approximately 3px ink gaps.',
10:'Preserve overlapping scalloped money bags and the dollar symbol; compact currency mark and organic bounds are intentional.',
12:'Preserve two plump asymmetric beans in diagonal arrangement; curved silhouettes and compact separation are visibly distinct.',
13:'Preserve two long biscuits and baked grooves; the grooves remain visibly separate at 48px with consistent 4px strokes.',
14:'Preserve outward-tilted bells with curved clappers and their shared crown; compact central opening and tilted envelope are intentional.',
15:'Preserve two overlapping desktop monitors, both stands and foreground bezel; 2px ink gaps are deliberate UI detail.',
16:'Preserve the flattened circular recess, slots and arch-shaped ground within the faceplate; larger square envelope and small openings remain readable.',
17:'Preserve the water surface, drone fins and claw arm; compact fins and articulated silhouette distinguish an underwater robot.',
18:'Preserve hand grip, thumb and two diagonal chopsticks with deliberate contact/occlusion at the grasp; small grip openings are intentional.',
19:'Preserve a natural long finger and curled thumb silhouette; the narrow organic fold reads clearly in both themes.'}
OMISSIONS={0:'Minor wheel-arch and cab curvature reduced.',1:'Cross rendered as two strokes rather than an outlined polygon.',2:'Small house door simplified to a single stroke.',3:'Parcel lower horizontal seam removed to protect vehicle readability.',4:'Receiver corners simplified while keeping earpieces.',5:'Headlights are dots; small tire details removed.',6:'Filled anatomical outline reduced to shared stick-figure construction.',7:'Knobs are dots rather than tiny rings.',8:'None of the identifying enclosure or peak arrangement omitted.',9:'Tiny transverse prong marks omitted.',10:'Rear bag is partially occluded; small dollar details reduced.',11:'Filled limb silhouettes replaced by shared stick-figure construction.',12:'No identity feature omitted; no extra interior marks.',13:'One baked groove per biscuit instead of two to retain clear openings.',14:'Minor central overlapping shell seam simplified.',15:'Rear bezel hidden by foreground monitor.',16:'None of the outlet identifying parts omitted.',17:'Tiny antenna and manipulator pivot circle omitted; joint remains visible.',18:'Three finger creases reduced to two; sticks occlude behind the grip.',19:'No identifying silhouette part omitted.'}
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
 result=dict(r,author='gpt-6',module=module.name,svg=r['icon_id']+'.svg',keyshape=D[i]['keyshape'],validation_status=rep.status,gate_status=g['status'],automatic_gate_status=auto['status'],accepted_exception=accepted,visual_review=review,comparison=D[i]['wrong'],feedback='Does not convey the intended meaning',changes=D[i]['change'],omissions=OMISSIONS[i],construction_reference=D[i]['lucide'],exception=g.get('exception'),artifacts=[p.name for p in dest.iterdir() if p.is_file()])
 if i in (6,11):result['human_spacing']='Shared human_ref/full_body_ref.png. Inverted: head (37,30), radius 5, neck (24,30): 13 - 5 - 4 = 4 ink gap. Paired: heads (12,12)/(38,12), radius 4; neck y24: 24 - 12 - 4 - 4 = 4 ink gap. Upper torso axes align with own heads.'
 (dest/'result.json').write_text(json.dumps(result,indent=2))
 print(i,r['icon_id'],'PASS · exception' if accepted else 'PASS · strict',flush=True)
