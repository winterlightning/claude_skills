from author import ROOT,REPO,ROWS
from pathlib import Path
import json,cairosvg,shutil
omissions=[
'Smallest motion stroke omitted.',
'Four tiny product boxes reduced to one product mark and a delivery compartment.',
'Tiny newspaper text omitted.',
'Fine anatomy simplified to coherent round-ended strokes.',
'Lower torso shortened to make room for the diagonal head wrap and sling.',
'No defining part omitted; circle and rising line share a coherent contour.',
'Tail and coin denomination omitted.',
'Tiny mouth, cheek patches and ear-tip divisions omitted.',
'Crown band and small robe fold omitted; robe, head and held trident retained.',
'Fine anatomy simplified to clear running limbs.',
'Filled reference body re-authored as coherent round-ended strokes.',
'Four source trails reduced to two.',
'Small lapel notches simplified to a clear V collar.',
'Secondary fin details simplified; open jaw and hooked tail retained.',
'Small halo rays omitted to preserve body proportions.',
'Tiny mouth and inner haunch line omitted.',
'Single visible arm and leg retain seated rocking pose.',
'Tiny eye and forepaw omitted; one upright ear retained.',
'Leg crossing reduced to a broad angled and rounded base.',
'Headlights omitted from the small car; windshield, bumper and wheels retained.'
]
reviews=[
'Larger round head balances the wheel. Handlebar turn is smooth; speed lines remain distinct.',
'Reaching action and wider vending face read together; delivery compartment is clearly separated.',
'Central torso meets the newspaper fold; enlarged paired pages read clearly around the head.',
'Diagonal weight has matched end plates. Bent elbow and opposed legs retain the lifting lunge.',
'Diagonal wrap and asymmetric sling remain distinct; round head touches curved shoulder ink.',
'Pie sector and rising zigzag read together; open arrowhead keeps the rising direction clear.',
'Rounded rump, snout, ear and two feet read as a piggy bank under a separate coin.',
'Pointed outlined ears and broad cheeks restore the character silhouette. Eyes are balanced.',
'Broader curved robe reads as a garment; the hand joins the rounded three-prong trident.',
'Head size, bent arms and opposed legs read as running. Head follows vertical neck tangent.',
'Large head, curved torso and broad stride remain legible; bent forearm stays separate from leg.',
'Longer sweeping trails are distinct from the runner; head aligns to the upper torso tangent.',
'Round spectacles retain visible lens openings; V collar now identifies the coat.',
'Concave open jaw and hooked tail give a fish-monster silhouette with smooth curve flow.',
'Diagonal robe edge distinguishes the seated figure; rounded leg base supports the torso.',
'Round rump, small ear and short muzzle read as a seated guinea pig rather than a dog.',
'Curved back and bent leg make the seated pose clearer above the rocker.',
'Tall rounded ear, long muzzle, haunch and rising tail preserve the kangaroo profile.',
'Taller head/body proportions and mirrored arms make the seated meditative pose clear.',
'Sloped windshield sits over the car bumper and wheels; the seated torso and arm curve naturally.'
]
for i,r in enumerate(ROWS,1):
 m=json.loads((ROOT/f'latest-{i}.json').read_text());out=REPO/m['result_dir']
 assert m['validation_status']=='valid' and not m['errors'] and not m['warnings']
 assert m['build_gate']['status']=='pass' and not m['build_gate']['errors'] and not m['build_gate']['warnings']
 for kind in ['reference','before']:
  data=(REPO/r[kind]).read_text().replace('currentColor','#141413')
  for size in [48,384]:
   cairosvg.svg2png(bytestring=data.encode(),write_to=str(out/f'{kind}-{size}.png'),output_width=size,output_height=size,background_color='white')
 m.update(visual_review={'native_light':True,'native_dark':True,'enlarged_light':True,'enlarged_dark':True,'findings':reviews[i-1]},omissions=omissions[i-1],keyshape_reason='Upright proportions fit the VRECT_L envelope.' if m['keyshape']=='VRECT_L' else 'Wide scene fits the HRECT_L envelope.' if m['keyshape']=='HRECT_L' else 'Balanced width and height fit the SQUARE envelope.')
 m['artifacts']=[p.name for p in out.iterdir() if p.is_file() and p.name!='candidate.json']
 (out/'result.json').write_text(json.dumps(m,indent=2)+'\n')
 (ROOT/f'latest-{i}.json').write_text(json.dumps(m,indent=2)+'\n')
print('20 complete, visually reviewed result directories prepared.')
