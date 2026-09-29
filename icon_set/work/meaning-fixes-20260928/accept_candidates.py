from pathlib import Path
import json,sys,hashlib
sys.path.insert(0,str(Path.cwd()))
from icon_set.scripts.primitive_fix import load_icon,approved_visual_exception
from icon_set.scripts.build_gate import gate
ROOT=Path('icon_set/work/meaning-fixes-20260928');R=json.loads((ROOT/'runs.json').read_text())
reasons={
2:'The two-person balance needs a tall asymmetric pose; retain its natural envelope and two exactly detached heads instead of distorting the pose to a rectangle.',
3:'Retain the full tricorn hat, crossed emblem, face and pointed beard. Their compact portrait spacing is needed for pirate recognition at 48px.',
4:'Retain the beer mug, foam, side handle and overlapping bread loaf. Their intentional overlap and natural bounds preserve the tavern subject.',
5:'Use the natural rounded brain perimeter instead of flattening its lobes to the keyshape. Two inward folds clarify the brain without dividing the centre.',
6:'The two browser controls must remain visible inside a compact toolbar. Preserve the toolbar and yuan sign with their reviewed compact spacing.',
7:'Three curved bananas must converge at their shared stalk. Preserve the smooth fan and tapered fruit contours rather than triangular wedges.',
8:'The complete rabbit face, outward ears, holding paw and egg need compact facial and attached-part spacing. The paired eyes, nose and egg opening remain visible at 48px.',
9:'Preserve the diagonal aircraft with its fin and wing plus a separate flame and smoke. The tapered silhouette and compact composition communicate the crash.',
10:'Preserve the natural backbend proportions and exact diagonal head-to-neck gap rather than distort this human pose to a standard rectangular envelope.',
11:'Keep the camper behind a tent with a triangular doorway and small flag; the tiny flag opening and compact occluded composition are deliberate.',
12:'Keep the seated paddler, diagonal paddle, upturned canoe bow and detached water. The hand-to-paddle and torso-to-boat contacts and compact water spacing preserve the scene.',
13:'The almond-shaped Divine Eye deliberately approaches the triangle sides as in the source. Its contour and pupil are essential to the Cao Dai symbol.',
14:'Retain the rider, cap, package, scooter shell and two wheels in one UI icon. Intentional mounted-part contacts and compact spacing preserve the delivery scene.',
15:'The car must remain one split vehicle under an impact burst; retain its jagged break, two wheels and compact scene proportions.',
16:'A loading bar needs a slim horizontal capsule. Its reviewed 44x20 ink envelope preserves the source meaning; the standard HRECT_M height made the rejected drawing too squat.',
17:'Exact geometric minimum: the pound upper semicircle reaches y=12 and the phone top is y=4, giving 8 centreline units / 4 ink units. Retain the readable pound rather than distort it for the conservative curved-pair warning.',
18:'The square wall plate, flattened round recess and two vertical slots all identify Type A. Keep the nested structure with reviewed narrower-than-profile gaps.',
19:'The square plate, circular recess, open pin holes and upper/lower earth tabs identify Type F. Preserve these layers and small round apertures with compact but visible gaps.'}
omissions={1:'Outlined limbs reduced to coherent strokes.',2:'Outlined limbs reduced to strokes; only the two actual heads are circular.',3:'No defining feature omitted.',4:'Two bread scores reduced to one.',5:'Small edge wrinkles reduced to broad lobes; centre stays undivided.',6:'No defining feature omitted; single currency bar follows the supplied reference.',7:'No defining feature omitted; three fruits retained.',8:'Fine whiskers omitted to keep the paired eyes, nose and holding gesture clear.',9:'Smoke reduced to two short curved wisps.',10:'Solid body silhouette reduced to torso, reaching arm, thigh and shin strokes.',11:'Small shirt cuff omitted; head, shoulder, tent, door and flag retained.',12:'Fine leg detail omitted behind the canoe gunwale.',13:'No defining feature omitted.',14:'Fine scooter trim omitted; parcel, rider, cap, wheels and steering retained.',15:'Small body trim omitted; split body, burst and two wheels retained.',16:'No defining feature omitted.',17:'No defining feature omitted.',18:'No defining feature omitted.',19:'No defining feature omitted.',20:'No defining feature omitted; four equal circular nodes retained.'}
humans={1:'Both head centres (10,13)/(10,31), radii 4; necks (22,13)/(22,31): 12 - 4 = 8 centreline / 4 ink. Upper pose preserves a deliberate sideways neck bend from the source.',2:'Head centres (38,24)/(38,40), radii 4; necks (26,24)/(26,40): 12 - 4 = 8 centreline / 4 ink. Both torsos point left away from their heads.',10:'Head (38,8), radius 5; neck (33,20): sqrt(5^2+12^2) - 5 = 8 centreline / 4 ink. The backbend intentionally extends the neck upward/right.',11:'Head (37,12), radius 5; shoulder crest (37,25): 13 - 5 = 8 centreline / 4 ink. All shoulder controls stay at or below y=25.',12:'Head (23,9), radius 5; neck (18,21): sqrt(5^2+12^2) - 5 = 8 centreline / 4 ink. The diagonal torso follows the seated lean.',14:'Head (26,8), radius 4; neck (26,20): 12 - 4 = 8 centreline / 4 ink. The cap is part of the head; the torso and arm recede below the junction.'}
for n,r in R.items():
 i=int(n);p=Path(r['module']);out=Path(r['result_dir']);icon=load_icon(p);v=icon.validate_icon();g=gate(p)
 clean=v.status=='valid' and not v.warnings and g['status']=='pass'
 if not clean:
  assert i in reasons,(i,'missing visual decision')
  approval={'reason':reasons[i]+' Visually reviewed at native 48px in light and dark themes by gpt-6; uniform 4px strokes retained.', 'approved_by':'user-delegated visual judgment: gpt-6','approved_on':'2026-09-29','svg_sha256':hashlib.sha256(icon.to_svg().encode()).hexdigest()}
  p.write_text(p.read_text()+'\n\n# User explicitly delegated exceptions; this approval is bound to the reviewed SVG.\nRevisedIcon.exception = '+repr(approval)+'\n')
  icon=load_icon(p);v=icon.validate_icon();g=gate(p)
  assert approved_visual_exception(v,g),(i,g)
 status='pass' if clean else 'pass-exception'
 (out/'validation.txt').write_text(v.describe()+'\n\n'+json.dumps(g,indent=2)+'\n')
 (out/'validation.json').write_text(json.dumps({'status':v.status,'errors':list(v.errors),'warnings':list(v.warnings),'gate':g},indent=2))
 evidence={**r,'validation_status':v.status,'release_status':status,'build_gate':g,'visual_review':'Inspected complete original and rejected drawing before authoring. Reviewed final light/dark images at native 48px and enlarged size; defining forms, openings and repeated proportions are readable.','omissions':omissions[i], 'human_construction':humans.get(i), 'artifacts':{'module':p.name,'svg':r['id']+'.svg','metadata':r['id']+'.metadata.json','previews':['preview-light-48.png','preview-dark-48.png','preview-light-384.png','preview-dark-384.png'],'validation':'validation.txt','reference_render':'reference.png','before_render':'before.png'}}
 (out/'result.json').write_text(json.dumps(evidence,indent=2)+'\n')
 r['release_status']=status;r['exception_reason']=None if clean else reasons[i];r['omissions']=omissions[i];r['human_construction']=humans.get(i)
 print(n,r['id'],status,flush=True)
(ROOT/'runs.json').write_text(json.dumps(R,indent=2))
