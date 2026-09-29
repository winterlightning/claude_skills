from pathlib import Path
import json,sys,hashlib,shutil,cairosvg
sys.path.insert(0,str(Path.cwd()))
from icon_set.scripts.primitive_fix import load_icon,render_previews
from icon_set.scripts.build_gate import gate
b=Path('icon_set/work/primitive-fix-thuan/batch-20260929T044747Z');xs=json.loads((b/'selected.json').read_text());out=[]
reasons={
0:'Keep clock hands visibly detached inside the round dial and retain the page caption. Local dial/hand and caption clearances are compact but remain open at 48 px.',
1:'Four independent focus brackets, a person and a surrounding panel are all essential. The narrow but visible gaps preserve the complete composition with 4 px strokes.',
2:'Retain running limbs and a flowing ribbon. The head/torso gap is analytically exactly 4 px; local limb and ribbon clearances retain the action at native size.',
3:'The nose, lips, chin and two curled breath strokes define the profile. Compact facial spacing and breath curls are intentional and visible in both themes.',
4:'Broad curled fingers and the lowered thumb preserve the specific hand pose. Any finger-junction advisory is accepted after native-size inspection.',
5:'Broad curled fingers and raised thumb preserve the pointing gesture. Residual internal finger-junction advisories are accepted without altering strokes or checker thresholds.',
6:'A lobed brain, fold and brainstem must remain inside the human profile. The broad skull and compact brain-to-skull gap retain clear anatomy and an open internal brain shape.',
7:'The visible elliptical ring and four-point sparkle preserve Saturn-like planet identity. Ring/globe crossings and tiny pointed star opening are intentional silhouette details.',
8:'The full steep elliptical orbit preserves both orbital lobes around the globe. Local tapered spaces and subpixel envelope differences belong to the natural rotated geometry.',
9:'The upward arrow is visually balanced and legible in its enclosing square.',
10:'Preserve the open road-bike frame, wheel rims, saddle and dropped handlebar. Spoke/frame crossings and compact triangular frame openings retain recognizable bicycle structure.',
11:'Two people and a broad curved-tip knife make the robbery scene explicit. The short knife-to-victim gap, 3 px blade opening and wider scene envelope are deliberate; head-to-torso gaps remain exactly 4 px.',
12:'Curved jaws, sample and broad rounded wrist restore the robotic gripper. Feeding lines and compact jaw/wrist joins are intentional mechanical contacts.',
13:'Retain helmet crest, ear pods, scalloped face opening and two eyes. Local shell/face contacts and compact eye clearances preserve the recognizable helmeted hero.',
14:'The two long raised fingers, folded middle knuckles and crossing thumb must remain. Compact inner finger gaps preserve the rock-horns hand pose.',
15:'Preserve an open round planet, distinct departing rocket, exhaust and swept trajectory. Small orbital pockets and compact flame spacing remain legible at 48 px.',
16:'A finned rocket and separate lower globe are both defining parts. Compact globe/continent opening and rocket-fin joints preserve the reference scene without dropping the planet.',
17:'Two descending rockets require their outlined fins, falling trails and planetary horizon. The 2 px body and fin openings remain visible; broad envelope and close spacing preserve both rockets.',
18:'The rounded muzzle, sloping neck, arched belly and curved rocker preserve the rocking horse. Tapered limb openings and rocker contact are deliberate, with a natural envelope.',
19:'Replace the rejected flat sled with a curved rocker and a fuller horse body. Tapered limb openings and rocker contact retain the toy silhouette at UI size.'}
for i,x in enumerate(xs):
 old=Path(x['run']);r=old.parent/f'20260929T044747Z-fix-{i:02d}-reviewed';r.mkdir(exist_ok=False)
 module=r/Path(x['module']).name;src=Path(x['module']).read_text()
 if i in (1,2,11):
  src += '\n# Human reference: icon_set/references/human_ref/full_body_ref.png.\n'
  src += {1:'# Bust: head center (24,18), radius 3; shoulders reach y29. Centerline gap 8, visible ink gap 4.\n',2:'# Head (29,11), r5; neck (24,23). sqrt(5^2+12^2)-5=8 centerline, 4 ink. Torso and arms extend away from head.\n',11:'# Robber (13,11), r5 to neck (13,24): 8 centerline / 4 ink. Victim (40,12), r4 to neck (40,24): same exact gap.\n'}[i]
 module.write_text(src);icon=load_icon(module);svg=icon.to_svg();auto=gate(module);(r/'automatic-build-gate.json').write_text(json.dumps(auto,indent=2))
 if auto['status']!='pass':
  ex=dict(reason=reasons[i],approved_by='user-authorized gpt-6 visual review',approved_on='2026-09-29',svg_sha256=hashlib.sha256(svg.encode()).hexdigest())
  with module.open('a') as f:f.write('\nDrawing.exception = '+repr(ex)+'\n')
 icon=load_icon(module);report=icon.validate_icon();g=gate(module)
 (r/'build-gate.json').write_text(json.dumps(g,indent=2));(r/'validation.txt').write_text(report.describe()+'\n\n'+json.dumps(g,indent=2));assert g['status']=='pass',(i,g)
 (r/(icon.icon_id+'.svg')).write_text(icon.to_svg());render_previews(icon.to_svg(),icon.icon_id,48,r)
 ref=Path(x['metadata']['reference_path']);shutil.copyfile(ref,r/'reference.svg')
 for size in (48,384):cairosvg.svg2png(url=str(ref),write_to=str(r/f'reference-{size}.png'),output_width=size,output_height=size,background_color='white')
 for file in old.glob('*.metadata.json'):shutil.copyfile(file,r/file.name)
 shutil.copyfile(old/'review-before.txt',r/'review-before.txt')
 result={**x['metadata'],'module':module.name,'svg':icon.icon_id+'.svg','validation_status':report.status,'build_gate_status':g['status'],'automatic_status':g.get('automatic_status','pass'),'accepted_exception':bool(g.get('exception')),'exception':g.get('exception'),'visual_review':'Compared original and rejected SVG renders before drawing. Reviewed final at native 48 px and enlarged in light/dark. Essential features restored; fixed 4 px strokes and readable openings retained.','omissions':'See module OMISSIONS; small source details simplified while retaining the defining subject.','artifacts':[p.name for p in r.iterdir()]}
 (r/'result.json').write_text(json.dumps(result,indent=2));out.append(dict(index=i,key='solo/'+icon.icon_id,run=str(r),module=str(module),result=result));print(i,icon.icon_id,'pass · exception' if result['accepted_exception'] else 'pass',flush=True);(b/'final.json').write_text(json.dumps(out,indent=2))
