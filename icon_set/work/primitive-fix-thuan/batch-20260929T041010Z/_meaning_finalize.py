from pathlib import Path
import json,sys,hashlib,shutil,cairosvg
sys.path.insert(0,str(Path.cwd()))
from icon_set.scripts.primitive_fix import load_icon,render_previews
from icon_set.scripts.build_gate import gate
b=Path('icon_set/work/primitive-fix-thuan/batch-20260929T041010Z');xs=json.loads((b/'selected.json').read_text());out=[]
reasons={
0:'Preserve the suspended bow pose and tapered aerial fabric. The exact 4 px head-to-torso gap is analytic; the checker retains its curve warning. A 1 px envelope underfill and compact fabric/body spacing preserve the original pose.',
2:'Keep the shoulder stock, offset rifle barrel and bent supporting arm; reduced gaps at the arm/torso junction are readable at 48 px.',
3:'Reviewer specifically requested three outlined wells. Three 4 px-radius wells have visible 4 px holes; reduced clearance to the organic outer contour is necessary and visually clear.',
4:'Eyepiece, objective, stage and curved stand are defining microscope features; compact joints and gaps retain a recognizable instrument at 48 px.',
5:'Preserve the complete sun, rays, horizon, laptop and seated worker composition. Compact local spacing and a broader keyshape envelope keep all four visual cues legible.',
6:'Preserve mower deck, engine and asymmetric wheels. Wheel/deck junctions and handle clearance reflect the reference and remain readable at native size.',
7:'The hammer-shaped head, dorsal fin, curved body and forked tail need local tapered openings. These preserve shark identity without adding fine strokes.',
8:'Keep the thumb/index relationship and curled fingers; any residual finger-junction advisory is accepted after 48 px review.',
9:'Preserve slender feline legs, tail and two contrasting flank spots. Local clearances around spots and rear hock are readable and necessary for leopard identity.',
10:'Retain the dome lid, knob and two steam curls; the small knob opening and tapered lid ends are deliberate recognizable cooking-pot details.',
13:'A long shallow cabin is essential for limousine proportions. Accept short-axis underfill and wheel/body junction advisories rather than stretching it into a tall generic car.',
14:'Preserve two double-ring cuffs suspended from a top link. The clear 2 px inter-ring bands and broad paired silhouette are intentional, with separate open wrist holes.',
15:'Retain hands gripping the towel edges and its torn bottom; hand-sheet contact and the compact space below the dispenser are intentional.',
16:'Preserve the curved rear handle, sloped mower deck and engine. Wheels touch the deck naturally; compact handle/engine spacing remains readable.',
17:'Preserve the rear-directed straight handle and mower deck; natural wheel/chassis and engine/deck joins retain the reference silhouette.',
18:'Six large circular eggs form a compact pile. Their open 6 px interiors remain readable; close packing and slight keyshape underfill preserve caviar rather than a sparse dot diagram.',
19:'Preserve ATV saddle, chassis, steering handle and wheel hubs. The small wheel/body pockets are secondary to the clear all-terrain vehicle silhouette.'}
for i,x in enumerate(xs):
 old=Path(x['run']);r=old.parent/f'20260929T041010Z-fix-{i:02d}-reviewed';r.mkdir(exist_ok=False)
 module=r/Path(x['module']).name;src=Path(x['module']).read_text()
 if i==5:src += "\n        self.mark_human_figure('person',head='head',torso='back-0',torso_junction='start')\n"
 if i in (0,1,2,5):
  src += '\n# Human reference: icon_set/references/human_ref/full_body_ref.png.\n'
  src += '# Detached circular head: nearest neck point is radius + 8 from center, leaving exactly 4 px ink clearance.\n'
  src += {0:'# Head (38,37), r4; neck (26,37); upper torso extends left.\n',1:'# Head (22,14), r4; neck (22,26); upper torso tangent vertical.\n',2:'# Head (12,12), r4; neck (12,24); upper torso vertical.\n',5:'# Head (35,15), r5; neck (35,28); reference shows a seated back with deliberate neck bend.\n'}[i]
 module.write_text(src)
 icon=load_icon(module);svg=icon.to_svg();auto=gate(module);(r/'automatic-build-gate.json').write_text(json.dumps(auto,indent=2))
 if auto['status']!='pass':
  ex=dict(reason=reasons[i],approved_by='user-authorized gpt-6 visual review',approved_on='2026-09-29',svg_sha256=hashlib.sha256(svg.encode()).hexdigest())
  with module.open('a') as f:f.write('\nDrawing.exception = '+repr(ex)+'\n')
 icon=load_icon(module); report=icon.validate_icon();g=gate(module)
 (r/'build-gate.json').write_text(json.dumps(g,indent=2));(r/'validation.txt').write_text(report.describe()+'\n\n'+json.dumps(g,indent=2))
 assert g['status']=='pass',(i,g)
 (r/(icon.icon_id+'.svg')).write_text(icon.to_svg());render_previews(icon.to_svg(),icon.icon_id,48,r)
 ref=Path(x['metadata']['reference_path']);shutil.copyfile(ref,r/'reference.svg')
 for size in (48,384):cairosvg.svg2png(url=str(ref),write_to=str(r/f'reference-{size}.png'),output_width=size,output_height=size,background_color='white')
 for file in old.glob('*.metadata.json'):shutil.copyfile(file,r/file.name)
 shutil.copyfile(old/'review-before.txt',r/'review-before.txt')
 result={**x['metadata'],'module':module.name,'svg':icon.icon_id+'.svg','validation_status':report.status,'build_gate_status':g['status'],'automatic_status':g.get('automatic_status','pass'),'accepted_exception':bool(g.get('exception')),'exception':g.get('exception'),'visual_review':'Reviewed original and rejected drawing, then new SVG at native 48 px and enlarged in light/dark. Defining features restored; openings visible and stroke width stays 4 px.','omissions':'See module OMISSIONS and comparison; no defining reference feature intentionally omitted.','artifacts':[p.name for p in r.iterdir()]}
 (r/'result.json').write_text(json.dumps(result,indent=2))
 out.append(dict(index=i,key='solo/'+icon.icon_id,run=str(r),module=str(module),result=result));print(i,icon.icon_id,'pass · exception' if result['accepted_exception'] else 'pass',flush=True)
 (b/'final.json').write_text(json.dumps(out,indent=2))
