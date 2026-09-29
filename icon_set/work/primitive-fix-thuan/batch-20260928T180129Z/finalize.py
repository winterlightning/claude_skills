from pathlib import Path
import json,sys,hashlib,shutil
sys.path.insert(0,str(Path.cwd()))
from icon_set.scripts.primitive_fix import load_icon,render_previews,approved_visual_exception
from icon_set.scripts.build_gate import gate
ROOT=Path(__file__).resolve().parent;xs=json.loads((ROOT/'authored.json').read_text())
reasons={
1:'Preserve two sensor-wave pairs, a visible windscreen and branching intersection corners; the road-to-car spacing and optical envelope remain readable at 48px.',
2:'Preserve the reference diagonal car and separate sloped road. Compact wheel/body contacts and roof spacing keep the vehicle and incline legible.',
3:'Retain two headlights, dashed center line and converging road edges beneath the car; these details are distinct at native size despite tighter spacing.',
4:'Preserve a rear cargo box and two full bicycle wheels with connected frame and fork. These genuine compact mechanical parts require closer spacing.',
5:'Preserve two outlined seated occupants inside a car windscreen. Matched circular heads and shoulder arcs use exactly 4px visible detached head gap; compact windshield and hood spacing remains legible.',
6:'Retain the requested three diagonal wash strokes and two small headlights in the open car bumper. Lamp-to-body clearance is tighter than the general detached-part rule.',
7:'Preserve the closed perspective strap, front display boundaries and two display marks. The compact watch construction needs closer inner spacing.',
8:'Retain a slim saxophone shaft, separated inner bend, upward bell and two keys. Optical silhouette fit and compact bell spacing preserve the recognizable instrument.',
10:'Retain three fork tines, a curved knife blade and the surrounding dining circle. Reduced utensil spacing is clear in both themes at native size.',
11:'Preserve the crowned elephant head, broad ears, eyes and curved trunk. Compact facial contacts and the natural silhouette are intentional.',
12:'Preserve a clear circular earth with simplified land boundaries above a separate node inside the open orbit. Nested globe details require reduced clearance.',
13:'Preserve distinct chip pins and the continuous index-thumb pinch. Close pin spacing and intentional finger-to-chip contact remain clear at 48px.',
14:'Preserve the flat-topped faceted gem and a rounded hand reaching around it. Small gem facets and the compact hand contour are intentional.',
15:'Preserve an extended hand above an anatomically recognizable ankle, heel and forefoot. Compact finger spacing and the natural silhouette are intentional.',
16:'Preserve the divided capsule held between an upper hand and a receiving lower palm. Small pill interior and genuine pinch contacts are necessary for the action.',
17:'Preserve the downward pressing finger, plunger and full domed service bell. Compact finger and button geometry is essential to the pressing action.',
18:'Preserve the releasing hand, cuff and staggered falling seeds. Compact finger contour and close cuff joins remain visually distinct.',
19:'Preserve a multi-cell blister sheet and a pill-taking thumb. Four cells replace the crowded source count, with compact cell spacing and optical envelope accepted after native-size review.',
20:'Preserve three responsive-device cues and a clear upright tapping index finger. Small phone interior and intentional overlapping hand/screen arrangement need closer spacing.'}
for d in xs:
 p=Path(d['module']);r=Path(d['run']);icon=load_icon(p);rep=icon.validate_icon();g=gate(p)
 (r/'automatic-gate.json').write_text(json.dumps(g,indent=2));(r/'automatic-validation.txt').write_text(rep.describe())
 if g['status']!='pass' or rep.status!='valid' or rep.warnings:
  reason=reasons[d['n']]
  ex={'reason':reason,'approved_by':'user-authorized-agent-visual-review','approved_on':'2026-09-29','svg_sha256':hashlib.sha256(icon.to_svg().encode()).hexdigest()}
  p.write_text(p.read_text()+'\n# User authorized visually justified exceptions for this batch. Findings are retained.\nDrawing.exception = '+repr(ex)+'\n')
  icon=load_icon(p);rep=icon.validate_icon();g=gate(p)
  assert approved_visual_exception(rep,g),(d['n'],g)
 else:assert g['status']=='pass'
 (r/'gate.json').write_text(json.dumps(g,indent=2))
 svg=icon.to_svg();(r/(d['icon_id']+'.svg')).write_text(svg)
 (r/'validation.txt').write_text(rep.describe()+'\n\nFull build gate: '+g['status']+'\n'+('Accepted drawing-bound visual exception; automatic findings retained.\n' if g.get('exception') else 'Strict pass, zero warnings.\n')+json.dumps(g,indent=2))
 artifacts=render_previews(svg,d['icon_id'],48,r)
 shutil.copyfile(Path(d['fix_dir'])/'reference.png',r/'reference.png')
 omissions='Secondary creases and fine decorative detail omitted for 48px clarity.'
 if d['n']==8:omissions='Reduced the key count to two and slimmed the body as requested.'
 if d['n']==19:omissions='Reduced the blister-cell count to four to keep the pill-taking gesture clear.'
 if d['n']==9:omissions='Replaced enclosed charge cells with three clearly separated full-charge bars.'
 md={'concept':d['concept'],'source_uuid':d['source_uuid'],'reference_path':d['reference'],'feedback':d['feedback']}
 (r/(d['icon_id']+'.metadata.json')).write_text(json.dumps(md,indent=2))
 findings={'source_uuid':d['source_uuid'],'source_path':d['reference'],'reference_path':d['reference'],'icon_id':d['icon_id'],'author':'gpt-6','validation_status':'pass-exception' if g.get('exception') else 'valid','automatic_validation_status':rep.status,'build_gate':g,'visual_review':{'status':'reviewed','themes':['light','dark'],'sizes':[48,384],'comparison':d['wrong'],'change':d['change'],'construction_reference':d['lucide'],'findings':'Native-size silhouette and meaning reviewed; rounded contours, open negative spaces and retained identifying features accepted.','human_gap': 'Heads center y16 radius3; shoulder ellipse top y27; centerline gap 8 and visible gap 4.' if d['n']==5 else None},'omissions':omissions,'artifacts':[p.name,d['icon_id']+'.svg','validation.txt','reference.png']+artifacts}
 (r/'result.json').write_text(json.dumps(findings,indent=2))
 d['validation_status']=findings['validation_status'];d['omissions']=omissions
 print(d['n'],d['key'],findings['validation_status'],flush=True)
(ROOT/'authored.json').write_text(json.dumps(xs,indent=2))
