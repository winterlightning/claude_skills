from author import ROOT,REPO,ROWS
import json,cairosvg
omissions=[
'Racket strings and fine anatomy omitted at48; head, forehand arm and stance retained.',
'Three small bearing holes and central bearing reduced to four dots to fit the three-lobed body.',
'Blade thickness varies slightly on the integer grid; three rounded blades and hub retained.',
'Fine branch steps omitted; three pointed canopies and three centered trunks retained.',
'Third eye and side eyes use dots; horn interiors omitted.',
'Fine jacket taper omitted for clearance; bow, lapels and seam retained.',
'Filled/angular body regions reduced to coherent round-ended limbs.',
'Parted hair reduced to short swept hairlines; circular heads and ponytail retained.',
'Exact circle intersections approximated with smooth integer-grid cubic spans; equal round outer quadrants and central lens retained.',
'Tiny rear lower-corner detail omitted behind the foreground envelope.',
'Text on pages and short neck line omitted; cap, circular jaw, shoulders and open book retained.',
'Tiny collar seam omitted; tent roof/body, crown, face and shoulders retained.',
'Dog eye, tail and fine anatomy omitted; bag, walker, leash and dog stance retained.',
'Inner tail outline omitted; rounded head, two horns and flowing S body retained.',
'Fine tail notches omitted; pointed inner head and round curled wing retained.',
'Secondary flame tips simplified; fox ear/snout and curled flame retained.',
'Small left hillside row fragment omitted; opposing hill and three sweeping crop rows retained.',
'No defining part omitted; paper lip and full-height roll retained.',
'Tuning pegs, strings and bridge omitted to keep soundhole and body clear.',
'No defining part omitted; open jaw, rounded shoulders and upright handle retained.'
]
reviews=[
'Enlarged head follows the upper torso. Oval racket and bent arm read as a forehand stance in both themes.',
'Curved three-lobed body now reads as a spinner; four bearing marks are clear at native size.',
'Round hub and three rounded blade tips retain a balanced propeller silhouette.',
'Three centered trunks distinguish the scene from mountain peaks; narrower foreground tree leaves clean gaps.',
'Longer horns and tapered brow/muzzle retain three clearly separated eyes.',
'Shallower bow, long V lapels and center seam make the formal jacket readable.',
'Equal larger heads, sloping arms and joined central hand make the pair clearer.',
'Short hair strokes and curved ponytail distinguish the two circular child heads.',
'Equal rounder lobes and clean central lens preserve the horizontal Venn arrangement.',
'Rear flap and rounded foreground envelope distinguish the two overlapping letters.',
'Domed cap over a longer circular jaw and deeper open pages distinguish reader from a barred circle.',
'Broad roof and long tent body read beside the symmetric crowned bust; jaw touches shoulder ink.',
'Teardrop bag, separated legs and dog back/head remain distinct in both themes.',
'Rounded snout and coherent S curve improve the dragon silhouette while retaining both horns.',
'Curved inner neck and beak are separated from the surrounding circular wing.',
'Pointed fox ear and snout restore the animal cue within the curled flame.',
'Opposing hillside meets the sweeping crop rows at a clean junction; spacing is even and open.',
'Top paper lip and deep rolled edge clarify the unrolled sheet.',
'Rounded headstock and smoother waist leave a visible round soundhole; natural upright guitar proportions.',
'Rounded head-to-handle transitions soften the wrench and preserve the open U jaw.'
]
why={
'SQUARE':'Balanced width and height fit the square envelope.',
'HRECT_L':'The wide subject or scene fits the 44 by 36 visible envelope.',
'HRECT_M':'A 44 by 32 envelope keeps the overlapping lobes rounder than the rejected tall ovals.',
'VRECT_L':'Upright proportions fit the 36 by 44 visible envelope.',
'VRECT_M':'The guitar uses a slimmer 32 by 44 visible envelope.',
'CIRCLE':'The curled dragon surrounds a radial circular envelope.'}
for i,r in enumerate(ROWS,1):
 m=json.loads((ROOT/f'latest-{i}.json').read_text());out=REPO/m['result_dir']
 assert m['validation_status']=='valid' and not m['errors'] and not m['warnings']
 assert m['build_gate']['status']=='pass' and not m['build_gate']['errors'] and not m['build_gate']['warnings']
 for kind in ['reference','before']:
  data=(REPO/r[kind]).read_text().replace('currentColor','#141413')
  for size in [48,384]:cairosvg.svg2png(bytestring=data.encode(),write_to=str(out/f'{kind}-{size}.png'),output_width=size,output_height=size,background_color='white')
 m.update(visual_review={'native_light':True,'native_dark':True,'enlarged_light':True,'enlarged_dark':True,'findings':reviews[i-1]},omissions=omissions[i-1],keyshape_reason=why[m['keyshape']])
 m['artifacts']=[p.name for p in out.iterdir() if p.is_file() and p.name!='candidate.json']
 (out/'result.json').write_text(json.dumps(m,indent=2)+'\n');(ROOT/f'latest-{i}.json').write_text(json.dumps(m,indent=2)+'\n')
print('20 visually reviewed result folders complete; all valid/full gate pass, zero warnings.')
