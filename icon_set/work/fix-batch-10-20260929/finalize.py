from pathlib import Path
import json,shutil,cairosvg
ROOT=Path(__file__).resolve().parent;REPO=ROOT.parents[2]
rows=json.loads((ROOT/'batch.json').read_text())
omissions=[
'No essential features omitted; waistband and leg openings use mirrored curves.',
'Three paving tracks reduced to two dashed tracks; solid walking anatomy reduced to round-ended strokes.',
'No separate facial details were present in the reference; continuous neck retained.',
'Distant legs, eye and mane detail omitted; one upright horn, muzzle, stepped hooves and tail retained.',
'Case handle and seam reduced to the carrying-arm attachment; head, walking pose and wide case retained.',
'Clasp fastener dot omitted; wallet fold and clasp preserved.',
'Body thickness reduced to round-ended strokes; extended arms and bent front knee retained.',
'Fine surface detail omitted; oval tracking window and lower button retained.',
'Fine surface detail omitted; oval tracking window and distinct lower cross pad retained.',
'No essential structural features omitted; visor, upper strap and lower head outline retained.',
'Finger outlines reduced to four separate strokes in two splayed pairs; thumb and rounded palm retained.',
'Fine surface detail omitted; oval tracking window and lower trigger retained.',
'Overhead control and beep rays omitted so a complete standing person fits inside the detector.',
'Original diagonal pose made upright; pin head reduced to a shaft. Sewn head, cross eyes and four small limbs retained.',
'Coin rim, slanted open D and two paired currency ticks retained.',
'No features omitted; radial keyshape preserves the horizontal infinity proportions.',
'Secondary button and doubled vibration arcs reduced to a central cross pad and one vertical vibration mark on each side.',
'Seeds omitted to preserve the diagonal cut, flesh opening and separate rind.',
'Four rotational sweeps retained; ends shortened to maintain clearance.',
'Cursor tail simplified; circular profile, swept hair division and arrowhead retained.'
]
reviews=[
'Curved waist and round leg openings remain distinct in both themes; paired sides balanced.',
'Dashes read separately from the walking figure; the actual torso junction is exactly4 ink units below the outlined head.',
'Circular head, curved neck and wide shoulders read as a continuous bust; bilateral curves balance.',
'Upright horn is distinct from the muzzle; curved back and rounded rear hoof soften the silhouette. Left-facing direction retained.',
'Wide carried case and lowered forward arm read clearly; exact4 ink head-to-torso gap retained.',
'Landscape wallet proportions, folded edge and right clasp read clearly.',
'Bent forward knee and diagonal rear leg communicate warrior pose; exact4 ink head gap retained.',
'Oval window stays open at48px; lower button clearly separated from it and the grip.',
'Upper oval window and lower cross control remain distinct at48px.',
'Broad visor and rounded nose arch are symmetric; top and bottom strap spaces remain open.',
'Four raised fingers form two visibly splayed pairs over the palm, with a separate projecting thumb.',
'Oval window is open; slanted lower trigger remains distinct from the grip.',
'Complete outlined-head stick figure reads inside the detector; head-to-shoulder gap is exactly4 ink units.',
'Two stitched cross eyes and the entering pin read at native size; upright reduction and short limbs documented.',
'Slanted D stem and paired ticks remain legible inside the circular coin.',
'Wide mirrored loops and central crossover now match the horizontal reference proportions.',
'Paired grips, cross control and side vibration marks read in both themes.',
'Diagonal slice and continuous curved rind preserve melon identity; flesh opening is clear.',
'Four equally constructed sweeping curves are separated and rotationally balanced.',
'Hair division makes the head a profile; the lower-right cursor remains open and distinct.'
]
for i,r in enumerate(rows,1):
 m=json.loads((ROOT/f'latest-{i}.json').read_text());out=REPO/m['result_dir']
 assert m['validation_status']=='valid' and not m['errors'] and not m['warnings']
 assert m['build_gate']['status']=='pass' and not m['build_gate']['errors'] and not m['build_gate']['warnings']
 h=json.loads((ROOT/(r['key'].replace('/','__')+'.history.json')).read_text())
 from icon_set.scripts.work_queue import disapproval_count
 assert disapproval_count(h)==1
 for label,src in [('reference',REPO/r['reference']),('before',REPO/r['claim_dir']/'before'/(r['icon_id']+'.svg'))]:
  shutil.copyfile(src,out/(label+'.svg'))
  for size in (48,384):
   cairosvg.svg2png(url=str(src),write_to=str(out/f'{label}-{size}.png'),output_width=size,output_height=size,background_color='white')
 m.update(omissions=omissions[i-1],visual_review={'native_light':True,'native_dark':True,'enlarged_light':True,'enlarged_dark':True,'findings':reviews[i-1]},disapprovals_at_claim=1)
 m['keyshape_reason']={'SQUARE':'Square envelope balances the complete subject and its surrounding whitespace.','VRECT_L':'Tall envelope preserves the upright subject with room for internal detail.','HRECT_L':'Wide envelope preserves the landscape silhouette.','HRECT_M':'Compact horizontal envelope keeps the control and side marks together.','CIRCLE':'Radial envelope preserves a round coin or a naturally wide symmetric mark.'}[m['keyshape']]
 m['artifacts']=[p.name for p in out.iterdir() if p.is_file() and p.name not in ('result.json','candidate.json')]
 (out/f"{r['icon_id']}.metadata.json").write_text(json.dumps(m,indent=2)+'\n')
 (ROOT/f'latest-{i}.json').write_text(json.dumps(m,indent=2)+'\n')
 (out/'result.json').write_text(json.dumps(m,indent=2)+'\n')
print('20/20 final runs: valid, full gate pass, zero errors/warnings, visual review complete, histories exactly one disapproval.')
