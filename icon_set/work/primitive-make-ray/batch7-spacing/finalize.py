from pathlib import Path
import json, re, html
SOURCE_ICON_ID=None
SOURCE_PATH=None
AUTHOR='gpt-6'
base=Path(__file__).parent
items=json.loads((base/'items.json').read_text())
notes={
1:('Agreement bubble with paired people; compact asymmetric check is legible. Tiny busts use the shared human vocabulary.','VRECT_L leaves vertical room for the bubble above paired busts.','Twin tails reduced to a tapered lower bubble; minimal head and shoulders.'),
2:('Circular Z and upper-left broadcast arc remain legible; diagonal composition follows source.','SQUARE accommodates diagonal broadcast arc and circular badge.','Three waves reduced to one.'),
3:('Symmetric globe hemisphere over short capsule microphone and wide U support. Capsule widened after native-size review.','VRECT_L supports the vertical globe/microphone arrangement.','Globe reduced to hemisphere, equator and one meridian; microphone shortened; horizontal base removed.'),
4:('Symmetric globe hemisphere over short capsule microphone and wide U support. Latitude difference collapses in this reduction.','VRECT_L supports the vertical globe/microphone arrangement.','Globe reduced to hemisphere, baseline latitude and one meridian; microphone shortened; horizontal base removed.'),
5:('Symmetric control handles and central node above an open, recognizable pen nib.','SQUARE balances horizontal handles over the nib.','Broad guide curve, tiny nib hole and separate base band omitted.'),
6:('Complementary crop corners and two rotation arrows read clearly; paired geometry follows 180-degree rotation.','SQUARE provides equal room for crop and rotation directions.','Rotation arrows shortened and inner crop opening rebalanced.'),
7:('Currency coin over a stem and symmetric open leaf sprigs; enlarged coin protects currency shape.','VRECT_L suits the coin above a growing stem.','Leaf outlines reduced to open sprigs; short currency ticks retain the dollar form.'),
8:('Circular coin and angular Algorand mark retain the apex and second sloping stroke.','CIRCLE retains the coin envelope.','Inner diagonal moved to a true shared junction on the right leg.'),
9:('Lower coin, raised medical plus and rising beam preserve cheap-insurance comparison.','SQUARE gives the triangle sufficient height below the two symbols.','Dollar inscription omitted; outlined cross reduced to open plus.'),
10:('Raised coin, lower medical plus and descending beam preserve expensive-insurance comparison.','SQUARE gives the triangle sufficient height below the two symbols.','Dollar inscription omitted; outlined cross reduced to open plus.'),
11:('Two sperm silhouettes inside the specimen field; compact heads and curved tails remain recognizable.','CIRCLE retains the laboratory observation field.','Detached third cell omitted; heads reduced to small circles.'),
12:('Outer ear and single inner fold remain recognizable; short sound chevron preserves incoming signal direction.','SQUARE balances the ear and left signal.','Inner fold reduced to a quarter arc; waveform reduced to one trough.'),
13:('Two concentric hoop outlines with a top clamp and horizontal screw; balanced clear space.','VRECT_L leaves room above the hoop for its clamp.','Two narrow clamp ears merged into one; hoop made slightly oval.'),
14:('Broad clamp flows into hoop; concentric inner ring and attached right screw remain clear.','VRECT_L preserves upright clamp and hoop arrangement.','Inner ring reduced; screw-head oval simplified to bar.'),
15:('Three heart-like lobes form one central knot within the medallion; lower lobes mirror.','CIRCLE enlarges the central crest to preserve its three-lobed identity.','Heart tips merged into one coherent knot; radial stems and exterior tassels omitted.')}
rows=[];results=[]
for n,it in enumerate(items,1):
 run=Path(it['run']);mod=next(run.glob('*.py'));s=mod.read_text();ident=re.search(r"icon_id=['\"]([^'\"]+)",s)[1]
 gate=(run/'build-gate.txt').read_text();validation=(run/'validation.txt').read_text()
 assert 'BUILD GATE PASS (pass, 0 errors, 0 warnings)' in gate
 assert validation.strip()=='status: valid'
 review,why,omissions=notes[n]
 design=json.loads((run/'design.json').read_text());design.update(omissions=omissions,keyshape_reason=why);(run/'design.json').write_text(json.dumps(design,indent=2)+'\n')
 meta={k:it[k] for k in ['concept','source_uuid','reference_path']};(run/f'{ident}.metadata.json').write_text(json.dumps(meta,indent=2)+'\n')
 refs=[it['reference_path']]
 if n==1:refs+=['icon_set/references/human_ref/user.svg']
 if n in (3,4,12):
  name='ear' if n==12 else 'mic';refs += [f'icon_set/references/lucide/{kind}/{name}.svg' for kind in ['original','atomic-debug']]
 result={**meta,'source_path':it['reference_path'],'icon_id':ident,'author':'gpt-6','result_dir':str(run),'module':mod.name,'svg':ident+'.svg','keyshape':design['keyshape'],'keyshape_reason':why,'validation_status':'valid','validation_errors':0,'validation_warnings':0,'build_gate':'pass','build_gate_errors':0,'build_gate_warnings':0,'status':'pass','visual_review':review+' Reviewed at 48px and 240px in light and dark themes.','omissions':omissions,'references':refs,'lucide_construction':('Continuous outer helix and curved inner fold.' if n==12 else 'Rounded capsule, wide U support, true central stand junction.' if n in (3,4) else 'No useful local Lucide match inspected for this design.'),'attempt_count':len(list((run/'attempts').glob('*.py'))),'blockers':[],'artifacts':sorted(p.name for p in run.iterdir() if p.name!='result.json')}
 if n==1:result['human_reference_verification']='user.svg: head center y32 radius2, head bottom34; shoulder arc center y44 radius_y2, crest42. Centerline gap8, visible ink gap4 for both people.'
 (run/'result.json').write_text(json.dumps(result,indent=2)+'\n');results.append(result)
 root=run.resolve();rows.append(f'| {n} | `{it["reference_path"]}` | PASS | [run]({root}) · [SVG]({root}/{ident}.svg) | {omissions} |')
report='# Batch 7 — spacing repairs\n\n15 passed; 0 blocked. Each final model has valid validation and BUILD GATE PASS with zero errors and zero warnings. All outputs are standalone; no registered originals or published files were modified. Author: `gpt-6`.\n\n[Light/dark review sheet](review-final.png)\n\n| # | Reference | Result | Artifacts | Reductions |\n|---|---|---|---|---|\n'+'\n'.join(rows)+'\n'
(base/'REPORT.md').write_text(report);(base/'results.json').write_text(json.dumps(results,indent=2)+'\n')
print('Saved 15 results: pass, no blockers. Attempts:',[r['attempt_count'] for r in results])
