from pathlib import Path
import json,re,shutil
from PIL import Image,ImageDraw
SOURCE_ICON_ID=None
SOURCE_PATH=None
AUTHOR='gpt-6'
b=Path(__file__).parent;items=json.loads((b/'items.json').read_text())
notes={
1:('Bluetooth rune remains legible inside a circular border; expanded triangles retain clear openings.','CIRCLE preserves the source badge.','Rune loops widened; no defining part omitted.'),
2:('Slanted sockets read as a skull; mirrored eyes join the cheeks. Ring and central tooth remain separate.','CIRCLE preserves the badge around the skull.','Eye sockets extended to genuine cheek junctions; dome slightly flattened and center tooth shortened.'),
3:('Skull and diagonal crossbones remain recognizable within the ring. Bone runs meet real skull and ring nodes.','CIRCLE preserves the enclosing warning badge.','Eyes merged into cheek sockets; center tooth omitted; bone ends joined to border.'),
4:('Horizontal sockets distinguish this skull from the slanted-eye variant; dome and narrowed jaw remain clear.','CIRCLE preserves the badge around the skull.','Dot eyes extended into open sockets joined to the cheeks; center tooth shortened.'),
5:('Circular head and open shoulders read as a person inside a clipped-corner file.','VRECT_L preserves the portrait page.','Bust narrowed and shifted left to clear the folded corner.'),
6:('Clipped file top, shield rim, rounded shield base and centered medical plus remain visible.','VRECT_L accommodates the upright integrated file and shield.','Lower page and shield walls merged into one real outline.'),
7:('Small head and open shoulders remain identifiable inside the tall heart; lower flanks provide clear space.','VRECT_L adds room below the shallow notch.','Bust reduced; heart notch made shallower and lower flanks widened.'),
8:('Four teeth and a circular core form a compact gear inside the house.','SQUARE balances house and settings symbol.','Six crowded lobes reduced to four cardinal teeth; central dot omitted.'),
9:('Three toe dots and a larger closed central pad read as a paw; the earlier face-like open pad was rejected.','SQUARE preserves the house envelope.','Toe outlines reduced to dots; triangular pad replaced with a larger circular pad.'),
10:('Right-facing play triangle remains clear within the house.','SQUARE preserves the house envelope.','Secondary circular button bezel omitted to leave a readable play opening.'),
11:('Diagonal capsule inside the circular lens retains the reference direction; handle joins an exact lens node.','SQUARE fits the lens and diagonal handle.','Capsule shortened; internal divider omitted after internal-spacing failure.'),
12:('Bug body, two antenna strokes and side legs remain above the envelope fold.','SQUARE gives the card enough width for its bug.','Card/envelope side walls merged; bug divider, lower legs and envelope seam strokes omitted.'),
13:('Upright phone, lower band and full circled plus remain readable. The dot-like compact-plus and square-phone alternatives were rejected.','VRECT_L preserves the phone proportions.','Plus spokes extended to true cardinal circle junctions; all named symbols retained.'),
14:('Wide almond-shaped eye reads clearly inside the phone; native review prompted a flatter eye contour.','VRECT_L preserves the upright phone and lower band.','Tiny pupil omitted; lid curves widened relative to height.'),
15:('Returning ridge reads as a simplified fingerprint in an upright phone; smooth arch and inner stem retain ridge flow.','VRECT_L preserves the phone proportions.','Fingerprint reduced to one continuous returning ridge; lower separator omitted.')}
results=[];rows=[];sheet=Image.new('RGB',(1100,930),'#e4e7eb');draw=ImageDraw.Draw(sheet)
for n,it in enumerate(items,1):
 run=Path(it['run']);mod=next(run.glob('*.py'));s=mod.read_text();ident=re.search(r"icon_id=['\"]([^'\"]+)",s)[1]
 gate=(run/'build-gate.txt').read_text();validation=(run/'validation.txt').read_text()
 assert 'BUILD GATE PASS (pass, 0 errors, 0 warnings)' in gate,(n,gate)
 assert validation.strip()=='status: valid',(n,validation)
 review,why,omissions=notes[n];design=json.loads((run/'design.json').read_text());design.update(omissions=omissions,keyshape_reason=why,visual_review=review)
 (run/'design.json').write_text(json.dumps(design,indent=2)+'\n')
 # Keep the module's prose consistent with its final geometry; no geometry changes.
 header='"""'+it['concept']+': fresh spacing repair.\nPlan: '+review+'\nKeyshape '+design['keyshape']+': '+why+'\nOmissions: '+omissions+'\n"""'
 s=re.sub(r'\A""".*?"""',lambda m:header,s,count=1,flags=re.S);mod.write_text(s)
 meta={k:it[k] for k in ['concept','source_uuid','reference_path']};(run/f'{ident}.metadata.json').write_text(json.dumps(meta,indent=2)+'\n');shutil.copyfile(it['reference_path'],run/'reference.svg')
 refs=[it['reference_path']];lucide=None
 if n==1:lucide='bluetooth'
 elif n in (2,3,4):lucide='skull'
 elif n in (5,6):lucide='file'
 elif n in (13,14,15):lucide='smartphone'
 if lucide:refs += [f'icon_set/references/lucide/{kind}/{lucide}.svg' for kind in ['original','atomic-debug']]
 if n in (5,7):refs += ['icon_set/references/human_ref/user.svg']
 result={**meta,'source_path':it['reference_path'],'icon_id':ident,'author':'gpt-6','result_dir':str(run),'module':mod.name,'svg':ident+'.svg','keyshape':design['keyshape'],'keyshape_reason':why,'validation_status':'valid','validation_errors':0,'validation_warnings':0,'build_gate':'pass','build_gate_errors':0,'build_gate_warnings':0,'status':'pass','visual_review':review+' Reviewed at 48px and enlarged in light and dark themes.','omissions':omissions,'references':refs,'construction_reference':lucide or 'No useful local Lucide match inspected for this composition.','attempt_count':len(list((run/'attempts').glob('*.py'))),'blockers':[],'artifacts':sorted(p.name for p in run.iterdir() if p.name!='result.json')}
 if n==5:result['human_reference_verification']='user.svg: circular head center(22,17), radius4 gives bottom21; shoulders apex(22,29). Exact centerline gap8 and visible ink gap4.'
 if n==7:result['human_reference_verification']='user.svg: circular head center(24,19), radius2 gives bottom21; shoulders apex(24,29). Exact centerline gap8 and visible ink gap4.'
 (run/'result.json').write_text(json.dumps(result,indent=2)+'\n');results.append(result)
 root=run.resolve();rows.append(f'| {n} | `{it["reference_path"]}` | PASS | [run]({root}) · [SVG]({root}/{ident}.svg) | {omissions} |')
 x=(n-1)%5*220;y=(n-1)//5*310
 for j,t in enumerate(['light','dark']):
  sheet.paste(Image.open(run/f'{t}-240.png').resize((130,130)),(x,y+130*j));sheet.paste(Image.open(run/f'{t}-48.png'),(x+145,y+45+130*j))
 draw.text((x+3,y+265),f'{n}. {it["concept"][:27]}',fill='black')
sheet.save(b/'review-final.png')
report='# Batch 9 — spacing repairs\n\n15 passed; 0 blocked. Every final module passes validate_icon() and BUILD GATE with zero errors and zero warnings. Each reference received a fresh standalone run; no published or registered originals were changed. Author: `gpt-6`.\n\n[Light/dark review sheet](review-final.png)\n\nThe circled-plus phone needed seven attempts. Its final design retains the circle, visible plus, upright phone and lower band; each spoke genuinely joins the circle. Earlier numerically passing but visually unsuitable reductions were rejected.\n\n| # | Reference | Result | Artifacts | Reductions |\n|---|---|---|---|---|\n'+'\n'.join(rows)+'\n'
(b/'REPORT.md').write_text(report);(b/'results.json').write_text(json.dumps(results,indent=2)+'\n')
print('15 passes, zero blocked. Attempt counts:',[r['attempt_count'] for r in results])
