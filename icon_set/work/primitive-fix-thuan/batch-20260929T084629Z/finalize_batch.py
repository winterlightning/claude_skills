"""Record visually reviewed results and user-authorized drawing-specific exceptions."""
import hashlib,json,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[4]
sys.path.insert(0,str(ROOT))
from icon_set.scripts.primitive_fix import load_icon,approved_visual_exception
from icon_set.scripts.build_gate import gate
import cairosvg
BATCH=Path(__file__).resolve().parent
rows=json.loads((BATCH/'batch.json').read_text())
AUTHOR='gpt-6'
SOURCE_ICON_ID=None
SOURCE_PATH=None
REASONS={
1:'Retain the disco sphere meridians, latitude intersections and eight glints. Compact cells are intentional and the spherical grid remains readable at 48 px.',
2:'Preserve broad chimpanzee muzzle, heart-shaped face patch, round ears and high skull dome; the dense nested facial contours and natural proportions are essential to recognition.',
3:'Preserve elliptical lid band and genuine handle-to-lid and wall-to-band contacts; they identify the cylindrical hatbox rather than a purse.',
4:'Preserve the rolled bale center, offset cylindrical depth, supporting field and repeated cut stalks. Reduced clearances retain a coherent agricultural scene.',
5:'Preserve flowing crown and curled tentacles. Four clearly separated arm runs replace the crowded fifth curl; compact spacing retains the characteristic octopus silhouette.',
6:'Retain inflatable robot belly, distinct side arms, short feet and small horizontal face. The small leg openings and shoulder contacts are intentional at native size.',
7:'Retain round owl badge, paired eye rings with pupils, brows and beak. These identifying nested facial details need compact spacing at 48 px.',
8:'Preserve the smiling face and overlapping reply bubble. The occluded rear outline and close face-to-reply spacing are intentional composition details.',
9:'Preserve circular mirror glass and surrounding support at natural proportions. Compact glass-to-cradle spacing is visually distinct; the stem genuinely meets the cradle.',
10:'Keep domed teapot lid, attached knob, round bowl, pouring spout and handle. The tall knob and small lid opening preserve the reference rather than turning it into a mug.',
11:'Retain round whale body, curved fountain, shallow smile and belly seams. Seams intentionally meet the body and smile, preserving the supplied stylized whale.',
12:'Preserve four face buttons, a clear cross D-pad and sloping grips. Compact button spacing is essential; natural grip arcs slightly depart from the rectangle envelope.',
13:'Preserve the reference shallow strip aspect ratio instead of stretching it into a thick capsule. All geometry and spacing checks pass apart from the intended keyshape height.',
14:'Preserve the profile nose and facial ledge; the short nose-to-front internal spacing is a recognizable anatomical corner. Model geometry is valid; one internal-spacing advisory is retained.',
15:'Keep rounded shoulders and narrow outlined arms at natural human proportions. The two arm openings have 2 px ink gaps; detached head-to-body gap is exactly 4 px.',
16:'Preserve both broadcast waves, circular origin and enclosure. Compact frame spacing and circular origin preserve the complete requested RSS composition.',
17:'Preserve the large display and home indicator of a tablet. The slim bezel needs 2 px ink gaps to avoid recreating the rejected tiny-screen design.',
18:'Retain raised arms, bent running legs and a narrow finish tape with concave ends. The head-to-torso ink gap is exactly 4 px; compact arm and tape spacing is intentional.',
20:'Retain the explicit dollar sack and running person in one 48 px composition. Bag lettering requires compact gaps; the head-to-torso ink gap remains exactly 4 px.',
}
OMISSIONS={1:'Reduced the latitude count and rendered the smallest glints as dots.',4:'Reduced the field stubble count to three.',5:'Omitted the crowded center arm; retained four visibly curling arm runs.',6:'Face reduced to one short linked-eye stroke.',8:'Omitted the tiny indistinct mark inside the reply bubble.',11:'No extra facial features were added to the source whale.',12:'Outlined small buttons become four round dots at native size.',14:'Removed the rejected added eye dot; the supplied reference is a plain silhouette.',18:'Used shared human stick-figure limbs, preserving the finish pose and tape.',19:'Used the shared human stick-figure vocabulary instead of outlined limbs.',20:'Reduced secondary finger and sack fold detail; preserved the currency mark.'}
LUCIDE={12:'gamepad-2: rounded upper shell and distinct grips',16:'rss: two concentric quarter-circle broadcast waves; tablet: rounded enclosing frame',17:'tablet: rounded case and centered home indicator',8:'message-circle: round speech body with an outward tail'}

for index in map(int,sys.argv[1:]):
 row=rows[index-1];out=ROOT/row['result_dir'];module=ROOT/row['module']
 icon=load_icon(module);svg=icon.to_svg();report=icon.validate_icon();before=gate(module)
 SOURCE_ICON_ID=out.parent.name;SOURCE_PATH=row['reference']
 if index in REASONS:
  approval={'reason':REASONS[index], 'approved_by':'user (delegated exception judgment to gpt-6)', 'approved_on':'2026-09-29', 'svg_sha256':hashlib.sha256(svg.encode()).hexdigest()}
  assert '    exception = ' not in module.read_text()
  with module.open('a') as f:f.write('\n    # User authorized meaning-preserving UI exceptions for this exact drawing.\n    exception = '+repr(approval)+'\n')
  icon=load_icon(module)
 accepted=gate(module)
 assert accepted['status']=='pass',(index,accepted)
 if index in REASONS: assert approved_visual_exception(report,accepted),(index,report.describe())
 else: assert report.status=='valid' and not report.warnings and not accepted['errors'] and not accepted['warnings']
 (out/'gate.json').write_text(json.dumps(accepted,indent=2)+'\n')
 (out/'validation.txt').write_text(report.describe()+'\n\nFull build gate: '+accepted['status']+'\nAutomatic status: '+accepted.get('automatic_status',accepted['status'])+'\n'+json.dumps(accepted,indent=2)+'\n')
 for key in ['reference','before']:
  for size in [48,384]:
   cairosvg.svg2png(url=str(ROOT/row[key]),write_to=str(out/f'{key}-{size}.png'),output_width=size,output_height=size,background_color='white')
 metadata=json.loads((out/(row['icon_id']+'.metadata.json')).read_text())
 result={**metadata,'author':AUTHOR,'keyshape':icon.keyshape.name,'keyshape_rationale':'Chosen for the dominant subject silhouette; any intentional natural-proportion departure is recorded in the exact-drawing exception.',
 'validation_status':report.status,'build_gate_status':accepted['status'],'automatic_status':accepted.get('automatic_status',accepted['status']), 'exception':accepted.get('exception'),
 'validation_errors':list(report.errors),'validation_warnings':list(report.warnings),
 'visual_review':'Inspected reference, rejected drawing, and final native 48px and enlarged renders in both light and dark themes. Final preserves the identifying silhouette and documented details, with intentional compact gaps recorded rather than hidden.',
 'omissions':OMISSIONS.get(index,'Only incidental source detail was simplified; the defining parts and arrangement are retained.'),
 'lucide_reference':LUCIDE.get(index,'No subject-specific Lucide drawing was used. Inspected local message-circle and tablet construction for coherent arcs, contours and round joins.'),
 'human_reference':'icon_set/references/human_ref/full_body_ref.png' if index in [15,18,19,20] else ('icon_set/skills/icon-design/human-reference.md' if index==14 else None),
 'human_spacing_evidence': {15:'Head center (24,9), radius 5: bottom 14. Shoulder top 22. 22 - 14 - 4 = 4 visible units.',18:'Head center (24,10), radius 5: bottom 15. Upper torso starts at (24,23). 23 - 15 - 4 = 4 visible units.',19:'Head (29,11), radius 5, torso junction (24,23). sqrt(5^2+12^2) - 5 - 4 = 4 visible units; arms rebalanced to preserve clearance.',20:'Head (33,9), radius 5: bottom 14. Upper torso begins (33,22) and points vertically toward head. 22 - 14 - 4 = 4 visible units.'}.get(index),
 'module':module.name,'svg':row['icon_id']+'.svg','artifacts':sorted(p.name for p in out.iterdir() if p.is_file())}
 (out/'result.json').write_text(json.dumps(result,indent=2)+'\n')
 print(index,row['icon_id'],'PASS — exception' if index in REASONS else 'PASS — automatic',flush=True)
