from pathlib import Path
import json,sys,cairosvg
sys.path.insert(0,str(Path.cwd()))
from icon_set.scripts.primitive_fix import run_module,load_icon
SOURCE_ICON_ID=None
SOURCE_PATH='batch.json'
AUTHOR='gpt-6'
root=Path(__file__).parent;rows=json.loads((root/'batch.json').read_text())
changes=[
'Restored three visible berry cells with shared junctions and a pointed attached leaf.',
'Lengthened the cob, lowered the two pointed husks, and rebuilt exact cob-to-husk attachment nodes.',
'Smoothed the rising thumb and rounded the palm while retaining a clear finger crease.',
'Added exposed connector tips and differentiated the two plug lengths around the smooth cable bends.',
'Restored a deep cash-drawer base, spaced keypad marks and a raised rectangular display.',
'Replaced dot vents with longer strokes and balanced the housing around its opposing shafts.',
'Added the full hard-hat brim, separated dome from circular jaw, and closed the broad torso base.',
'Replaced solid heads with outlined circles and separated the curved balloon string from the figures.',
'Sharpened the square head outline and widened the eye and mouth strokes to strengthen the pixel-face pattern.',
'Widened the frown and spread the closed eyes; retained a small tear with a visible pointed tip.',
'Rebuilt mirrored moustache lobes with lower proportions and pointed upturned ends.',
'Rebuilt the circular face inside a separate headset band and clear ear ends above broad shoulders.',
'Separated the ear lobes from the forehead and connected the muzzle to the chin; retained circular eye rings.',
'Raised the bent leg and lifted foot to clarify dancing, retaining the exact head-to-torso gap.',
'Restored two table legs between the chairs and reduced the bowl depth.',
'Attached an outlined terminal to the complete battery and retained the corner-to-corner slash.',
'Rebuilt the arms to hold a larger open steering wheel, removing the no-entry-like crossbar.',
'Curved the rear figure’s arm across to the foreground shoulder to make the embrace visible.',
'Splayed the pinky and rebalanced the folded-finger valley and palm while retaining three extended digits.',
'Restored the eyebrow and descending cheek mark, with a distinct curled lower flourish and shared iris endpoints.'
]
omissions=[
'Seven drupelets reduced to three cells; leaf vein omitted.',
'Kernel lattice reduced to one transverse division.',
'Four finger creases reduced to one.',
'Tiny lightning mark, pin sleeves and paired prongs reduced to simple connector tips.',
'Keypad reduced to two marks; small printer slot omitted.',
'Outlined shafts reduced to strokes; vents simplified.',
'Crown ridge and separate desk trim omitted; lower base integrated with torso.',
'Shirt and dress silhouettes reduced to shared stick-figure limbs.',
'Square eye interiors reduced to broad strokes; small lower-mouth notch omitted to preserve spacing.',
'Tear kept compact using the permitted small-circle construction; eye arcs remain minimal.',
'Fine hair detail omitted; proportions fit the widest available SOLO48 keyshape.',
'Hair fringe omitted; earcups reduced to round-ended headset terminals.',
'Eye rings use radius 3 for clearance; triangular nose reduced to connected muzzle stroke.',
'Clothing contour reduced to stick limbs.',
'Tabletop thickness and bowl rim ellipse simplified.',
'Rounded casing corners simplified to crisp corners.',
'Wheel spokes omitted; hands meeting the wheel carry the driving concept.',
'Clothing and hand outline reduced to a single embracing arm stroke.',
'Two folded finger contours reduced to one valley.',
'Small inner curl loop simplified to one smooth flourish.'
]
for i,r in enumerate(rows):
 run=Path(r['run']);module=run_module(run);icon=load_icon(module);r['change']=changes[i];r['omissions']=omissions[i]
 for name,path in [('reference',Path(r['reference'])),('rejected',Path(r['fix_dir'])/'before'/f"{r['id']}.svg")]:
  for size in (48,384):cairosvg.svg2png(url=str(path),write_to=str(run/f'{name}-{size}.png'),output_width=size,output_height=size,background_color='white')
 report=icon.validate_icon();assert report.status=='valid' and not report.warnings
 validation_text=(run/'validation.txt').read_text()
 validation=json.loads(validation_text[validation_text.index('{'):])
 assert validation['status']=='pass' and not validation['errors'] and not validation['warnings']
 details={'source_uuid':r['source_uuid'],'reference_path':r['reference'],'concept':r['concept'],'icon_id':r['id'],'author':'gpt-6','keyshape':icon.keyshape.name,'validation_status':'valid','validation_errors':[],'validation_warnings':[],'build_gate':validation,'visual_review':{'status':'reviewed','native_light_dark':True,'findings':changes[i],'before_problem':r['wrong'],'feedback':'No written feedback or disapproval reason recorded.','omissions':omissions[i],'reference_comparison':True},'artifacts':sorted(p.name for p in run.iterdir() if p.is_file())}
 if i in (7,13):details['human_construction']='Shared full_body_ref.png. Head outline to actual torso junction is exactly 8 centerline units / 4 visible units; head aligned above vertical torso.'
 if i in (6,11,16,17):details['human_construction']='Shared user.svg. Circular jaw and shoulder tangent contact is 4 centerline units / zero visible gap, using scoped contact and the full bust validator.'
 (run/'result.json').write_text(json.dumps(details,indent=2)+'\n')
(root/'batch.json').write_text(json.dumps(rows,indent=2))
print('Recorded 20 valid runs with previews, reference comparisons and result.json.')
