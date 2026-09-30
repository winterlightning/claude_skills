from pathlib import Path
import json, sys
ROOT=Path(__file__).resolve().parents[4];sys.path.insert(0,str(ROOT))
from icon_set.scripts.primitive_fix import load_icon,run_module
BASE=Path(__file__).parent;rows=json.loads((BASE/'claims.json').read_text());runs=json.loads((BASE/'runs.json').read_text())
changes=[
'Restored the diagonal capsule and four radial projections, preserving both inclusions.',
'Lengthened the upright palm and fingers, widened the thumb, and retained rounded fingertips.',
'Extended the raised hands, clarified the thumbs and brought the upper binding across the wrists.',
'Reoriented the palm horizontally and opened the space between the thumb and outer fingers.',
'Restored a speech tail, rounded the enclosure, and rebuilt the bag handle and side profile.',
'Restored an outlined bow tie below the circular fanged face and pointed ears.',
'Enlarged the domed cap and rebalanced its spacing above the circular face and veil.',
'Restored a round bulb and a slimmer stem, with a shorter temperature column.',
'Restored a slender ruler body with short alternating tick lengths and rounded ends.',
'Enlarged the medical cross and central toe opening, with a taller paw pad.',
'Restored a folded-finger crease beneath the two raised fingers.',
'Replaced the pointed pentagonal cap with a flatter rounded crown; retained a circular jaw and uniform seam.',
'Restored the visitor torso and separated legs beside the circular wheel and support.',
'Restored a fourth flowing panel seam and complete shared seam junctions.',
'Replaced elongated oval reels with matching circular loops joined at their bottom tangents.',
'Replaced elongated oval reels with matching circular loops joined at their bottom tangents.',
'Restored a broad stuffed torso and rounded legs; the pin now enters the shoulder.',
'Added a curved panel seam and rebuilt the circular rim with exact shared attachment points.',
'Restored a sloping nose and rounded chin below the visor, preserving the continuous neck profile.',
'Replaced pocket chevrons with two closed pocket outlines and rebalanced their spacing below the collar.'
]
omissions=[
'Inclusion rings reduced to two dots; four clear projections replace the fine perimeter series.',
'Three long fingertips replace four crowded fingers; thumb retained.',
'Two binding strokes replace three; fine finger bends reduced.',
'Fine skin creases omitted.',
'Tiny facial details and the far speech wall omitted to retain a clear profile and bag.',
'Shoulder outline, fine eyes and hairline omitted so the bow tie and fangs survive at 48 px.',
'No facial microdetails added; source cap, face and veil retained.',
'Tiny bulb-center point omitted.',
'Three ticks replace six; rounded ends permit a slender profile within the radial envelope.',
'Side toe rings use the existing small-circle exception and read as round marks at native size.',
'Multiple folded-finger details reduced to one crease.',
'Collar lapels, cap emblem and sleeve divisions omitted; uniform seam retained.',
'Tiny cabin rings omitted; wheel, spokes, support and standing visitor retained.',
'Four broad seams replace six finer source seams.',
'None.',
'None.',
'Left arm reduced to one stroke; right arm merges into the stuffed shoulder silhouette. Toy anatomy retains a continuous head/body connection.',
'Four broad seams replace finer repeated source seams.',
'Fine facial marks omitted.',
'Pocket flap seams and central button placket omitted.'
]
refs=[
'No useful exact local Lucide match; source diagonal capsule construction.',
'Lucide hand original and atomic-debug; shared human reference for rounded human parts.',
'Lucide hand original and atomic-debug; shared human reference. Mirrored hands.',
'Lucide hand-helping original and atomic-debug; source horizontal offering gesture.',
'Lucide message-square original and atomic-debug; supplied bag and left-facing profile.',
'Shared human_ref/user.svg circular head; source pointed ears, fangs and bow tie. Bow tie is an accessory; shoulders are omitted.',
'Shared human reference for circular jaw; supplied domed cap and veil. Mirror axis x=24.',
'Lucide thermometer original and atomic-debug; circular lower bulb and upright stem.',
'Lucide ruler original and atomic-debug; attached alternating ticks.',
'Lucide paw-print original and atomic-debug; source three-toe pad and medical cross.',
'Lucide hand-metal and hand originals and atomic-debug; shared human reference.',
'Shared human_ref/user.svg circular jaw and shoulders. Jaw bottom y=26; shoulder top y=30; 4-unit centerline separation gives zero visible ink gap, declared with an actual contact.',
'Shared human_ref/full_body_ref.png. Head center (10,15), radius4; torso starts (10,27): exactly 8 centerline / 4 ink units of detached head clearance, aligned on x=10.',
'Lucide volleyball original and atomic-debug: curved panel seams and shared junctions.',
'Lucide voicemail original and atomic-debug: two circular loops and tangent bridge.',
'Lucide voicemail original and atomic-debug: two circular loops and tangent bridge.',
'Supplied toy and shared human reference for rounded limb vocabulary. Continuous stuffed toy head and body; pin comes from upper right.',
'Lucide volleyball original and atomic-debug: curved panels and shared junctions.',
'Shared human reference and Lucide headset original and atomic-debug. Continuous left-facing profile with neck; no detached head gap.',
'Lucide shirt original and atomic-debug: mirrored shoulders; supplied collar and paired pockets.'
]
report=['# Once-disapproved solo fix batch 08 — 20 icons','','Claim: --limit 20 --offset 0 --max-disapprovals 1; worker thuan-mac. Production returned all 20 claims. No written reviewer feedback or reason was recorded for these icons.','','All modules use AUTHOR = "gpt-6". Each was compared with its original and rejected drawing, then reviewed at 48 px in light and dark themes. Each passes model validation and the full QA gate with zero warnings. Production completion is appended after finish succeeds.','']
for i,r in enumerate(rows):
 out=ROOT/runs[str(i)];module=run_module(out);icon=load_icon(module);v=icon.validate_icon();g=json.loads((out/'gate.json').read_text());assert v.status=='valid' and not v.warnings and g['status']=='pass' and not g['warnings'],r['key']
 meta=json.loads(next(out.glob('*.metadata.json')).read_text());key=r['key'].split('/')[1];comparison=(out/'review-before.txt').read_text().splitlines()[0]
 if i==6:comparison='The rejected drawing has an undersized cap and an unbalanced face/veil relationship. No written reviewer feedback.'
 if i==11:comparison='The rejected pilot cap is a sharp pentagon, unlike the flatter rounded crown in the reference. No written reviewer feedback.'
 rationale={'SQUARE':'Balanced overall composition; centerline extremes (6,6)-(42,42).','VRECT_L':'Vertical composition; centerline extremes (8,4)-(40,44).','VRECT_M':'Narrow upright gesture; centerline extremes (10,4)-(38,44).','HRECT_L':'Horizontal composition; centerline extremes (4,8)-(44,40).','HRECT_M':'Horizontal offering hand; centerline extremes (4,10)-(44,38).','CIRCLE':'Radial centerline limit 20 around (24,24), preserving the natural circular or slender subject proportions.'}[icon.keyshape.name]
 visual='Reviewed enlarged and native 48 px light/dark previews: identifying parts remain legible, clear openings, coherent curves and balanced negative space. '+changes[i]
 source=module.read_text();start=source.index('"""');end=source.index('"""',start+3)+3
 source='"""'+comparison+'\n'+changes[i]+'\nConstruction: '+refs[i]+'\nOmissions: '+omissions[i]+'\nKeyshape: '+icon.keyshape.name+'. '+rationale+'\n"""'+source[end:];module.write_text(source)
 (out/'visual-review.txt').write_text(visual+'\n'+refs[i]+'\nOmissions: '+omissions[i]+'\n')
 result={**meta,'source_path':r['ref'],'source_key':r['key'],'icon_id':key,'author':'gpt-6','validation_status':'valid','validation_errors':[],'validation_warnings':[],'build_gate':g,'comparison':comparison,'reviewer_feedback':r['feedback'],'changes':changes[i],'visual_review':visual,'construction_references':refs[i],'omissions':omissions[i],'keyshape':icon.keyshape.name,'keyshape_reason':rationale,'artifacts':{'module':module.name,'svg':key+'.svg','metadata':key+'.metadata.json','previews':[f'preview-{t}-{s}.png' for t in ('light','dark') for s in (48,384)],'validation':'validation.txt','gate':'gate.json'}}
 (out/'result.json').write_text(json.dumps(result,indent=2)+'\n')
 report += ['## '+r['key'],'',comparison,'',changes[i],'',refs[i],'','Omissions: '+omissions[i],'',f'Keyshape: {icon.keyshape.name}. {rationale} AUTHOR: gpt-6. Model valid; full QA pass; zero warnings.','',f'[RESULT_DIR]({out}) · [SVG]({out/(key+".svg")}) · [Validation]({out/"validation.txt"})','']
report+=['## Visual evidence','']
for i in range(1,5):report.append(f'[Original/rejected comparison {i}]({BASE.resolve()/f"compare-{i}.png"}) · [Native light/dark final review {i}]({BASE.resolve()/f"drafts-{i}.png"})\n')
(BASE/'REPORT.md').write_text('\n'.join(report));(BASE/'finish-notes.json').write_text(json.dumps(changes,indent=2))
print('Finalized 20 clean standalone runs and the batch report.')
