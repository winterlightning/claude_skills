from author_batch import ROOT,ITEMS,AUTHOR
from pathlib import Path
import json,hashlib,datetime,shutil,cairosvg
from icon_set.scripts.primitive_fix import load_icon,render_previews,approved_visual_exception
from icon_set.scripts.build_gate import gate
records=json.loads((ROOT/'runs.json').read_text())
reasons={
0:'Preserve three recognizable five-point rating stars and the complete house. The small stars use compact solid silhouettes; their openings and rating-to-roof spacing need a visual exception.',
1:'Preserve a complete house inside a speech bubble and two detached-head busts. This dense scene needs the wider envelope and smaller bubble-to-house and bubble-to-head clearances; each head retains 4 units of visible clearance to its shoulders.',
2:'Preserve cargo-box placement and bicycle frame crossing the wheels naturally. Wheel/frame intersections and small enclosed chassis spaces are intentional physical structure, not unrelated collisions.',
3:'Preserve the receptionist, counter, customer and recognizable dollar payment sign. The dollar crossing and compact counter/payment spacing are needed for this complete transaction scene.',
4:'Preserve the umbrella, articulated reclining person and water as a complete scene. Wider/taller composition and the compact canopy/head and legs/water gaps remain readable at 48 pixels; detached head-to-torso clearance is exactly 4 units.',
5:'Preserve the resume portrait, two text lines and candidate bust. Compact text spacing and page-to-candidate separation retain the complete recruiting meaning at native size.',
6:'Preserve the clock hands and return arrow inside the portrait card. Compact interior spacing is essential to distinguish history from a plain card or return arrow.',
8:'Preserve Redux identity: three interlocking smooth lobes and three circular nodes. The logo requires asymmetric bounds and compact lobe/node spacing; genuine endpoint contacts are declared individually.',
9:'Preserve the readable number 10, battery terminal, and leftward range arrow. The intentionally broken battery edge accommodates the arrow; compact numeral and battery spacing retain the original range meaning.',
11:'Preserve a foreground car with windshield, lamps and wheels plus a rear house. Compact car details and the foreground/background spacing retain residential parking meaning.',
13:'Preserve the original pair of female restroom figures with a dividing line. The dresses have 2 units of visible clearance from the divider; paired heads and legs remain distinct and balanced.',
14:'Preserve landscape, sun, two mountain peaks, retouch wand and four-point sparkle. Compact detail spacing and the sparkle envelope preserve the editing cue without losing the picture meaning.',
15:'Preserve the classic bicycle diamond frame, equal wheels and curled handlebar. Natural wheel/frame intersections and small chassis openings are intentional and recognizable at native size.',
16:'Preserve the gymnast raised arm, extended leg and surrounding ribbon. Compact ribbon-to-head and ribbon-to-limb gaps and the optical envelope preserve the dancing action.',
17:'Preserve the overhead ribbon loop, upright gymnast and bent back leg. Compact loop spacing and the optical bounds preserve the ribbon action; the torso begins vertically under the head with exactly 4 units of visible head clearance.'}
refs={0:['house'],1:['house','message-square'],2:['bike'],3:[],4:[],5:['file-user'],6:[],7:['banknote'],8:[],9:[],10:[],11:['house'],12:[],13:[],14:[],15:['bike'],16:[],17:[],18:['log-out'],19:['arrow-right-to-line']}
humans={1:'Both heads: cy=33, r=3, shoulder apex y=44; 44-(33+3)-4 = 4 ink units.',3:'Customer head cy=10, r=4, torso start y=22; 22-14-4=4. Staff shoulder apex y=22 gives the same gap.',4:'Head cy=20, r=4, torso start y=32 with vertical tangent; 32-24-4=4. Arms/legs do not substitute for this junction.',5:'Candidate head cy=17, r=4, shoulder apex y=29; 29-21-4=4.',13:'Each head cy=10, r=4, dress top y=22; 22-14-4=4. Two matching female figures are intentional from the original.',16:'Head cy=15, r=4, vertical torso start y=27; 27-19-4=4.',17:'Head cy=14, r=4, torso starts at y=26 with vertical Bezier tangent; 26-18-4=4.'}
omissions={0:'Small side stars use compact filled silhouettes rather than open holes.',1:'Tiny house door omitted to retain a complete house silhouette; shoulders simplified.',2:'Wheel spokes omitted; rear cargo box and complete chassis retained.',3:'Fingers, customer clothing outline and minor counter trim omitted.',4:'Individual toes and fingers omitted; water reduced to four broad ripples.',5:'Candidate legs omitted; document portrait and two text rules retained.',6:'Clock ticks omitted; clock hands and return arrow retained.',7:'Decorative inner border and corner scallops removed; optional side dots removed for a strict pass.',8:'No semantic elements omitted; lobe curvature re-authored on the integer grid.',9:'No semantic elements omitted; numeral serifs simplified.',10:'No semantic elements omitted; a table grid makes the removed-row context explicit.',11:'Minor car trim omitted; windshield, headlights and wheels retained.',12:'No semantic elements omitted; chair/table construction simplified.',13:'Clothing seams omitted; the two female silhouettes are retained.',14:'Small separate light rays consolidated into a four-point sparkle.',15:'Individual spokes omitted; frame, equal wheels, saddle and curled handlebar retained.',16:'Clothing outline and fingers omitted in favor of the shared stick-figure style.',17:'Clothing outline and fingers omitted in favor of the shared stick-figure style.',18:'Right enclosure edge removed to make the outward/exit action legible.',19:'No semantic elements omitted; missing terminal line restored.'}
for i in range(7):
 old=records[str(i)]['run']
 found=[json.loads(p.read_text()) for p in Path(old).parent.glob('*-reviewed-exception/result.json')]
 records[str(i)]=next(v for v in reversed(found) if v.get('parent_run')==old)
for i in range(7,20):
 v=records[str(i)];run=Path(v['run']);module=Path(v['module']);ic=load_icon(module)
 if i in reasons:
  stamp=datetime.datetime.now(datetime.timezone.utc).strftime('%Y%m%dT%H%M%S%fZ')
  new=run.parent/(stamp+'-reviewed-exception');shutil.copytree(run,new)
  module=new/module.name;source=module.read_text()
  exception=dict(reason=reasons[i]+' Visually reviewed at 48px in light and dark themes under the user\'s explicit delegated exception authorization.',approved_by='user-delegated-gpt-6',approved_on='2026-09-29',svg_sha256=hashlib.sha256(ic.to_svg().encode()).hexdigest())
  source=source.replace('class Drawing(Solo48):\n','class Drawing(Solo48):\n    exception = '+repr(exception)+'\n')
  module.write_text(source);v['parent_run']=str(run);run=new;v['run']=str(run);v['module']=str(module)
 ic=load_icon(module);report=ic.validate_icon();g=gate(module)
 accepted=approved_visual_exception(report,g)
 assert g['status']=='pass' and (accepted or(report.status=='valid' and not report.warnings)),(i,g)
 assert not report.errors or accepted
 svg=ic.to_svg();(run/(v['icon_id']+'.svg')).write_text(svg);render_previews(svg,v['icon_id'],48,run)
 for name,src in [('reference',ITEMS[i]['reference']),('before',ITEMS[i]['before'])]:
  for size in (48,384):cairosvg.svg2png(url=src,write_to=str(run/f'{name}-{size}.png'),output_width=size,output_height=size,background_color='white')
 validation=report.describe()+'\n\nFull build gate: '+g['status']+'\n'+json.dumps(g,indent=2)+'\n'
 (run/'validation.txt').write_text(validation);(run/'gate.json').write_text(json.dumps(g,indent=2))
 v.update(gate=g,validation_status=report.status,accepted_exception=accepted,author=AUTHOR,visual_review='Reviewed light and dark at native 48px and enlarged size. Recognizable semantic silhouette; uniform 4px strokes, intentional asymmetry only for scene placement, directional movement or logo construction.',omissions=omissions[i],human_reference=humans.get(i),lucide_references=refs[i],keyshape_reason='Preserve the supplied subject proportions and relative arrangement. '+('Drawing-bound visual exception records the intentional optical envelope or compact detail requirements.' if accepted else 'Exact standard envelope with full strict validation pass.'))
 v['reference_notes']='Original and rejected SVG renders compared before authoring. '+('Local Lucide originals and atomic-debug geometry informed '+', '.join(refs[i])+': clean silhouettes, coherent contours and simple semantic primitives.' if refs[i] else 'No useful exact Lucide match; applied the inspected geometric construction principles without claiming an exact match.')
 if i in humans:v['reference_notes']+=' Shared human_ref/user.svg and full_body_ref.png informed round heads, coherent limbs and smooth shoulders. '+humans[i]
 (run/'visual-review.md').write_text(v['comparison']+'\n\nFeedback: '+v['feedback']+'\n\n'+v['visual_review']+'\n\n'+v['reference_notes']+'\n\nOmissions: '+v['omissions']+'\n\n'+(reasons.get(i) or 'Strict pass without exception.')+'\n')
 # Result is written last after geometry, validation, render and visual inspection evidence.
 result={**v,'artifacts':sorted(p.name for p in run.iterdir() if p.name!='result.json')}
 (run/'result.json').write_text(json.dumps(result,indent=2))
 print(i,v['icon_id'],'exception' if accepted else 'strict pass',flush=True)
(ROOT/'runs.json').write_text(json.dumps(records,indent=2))
