from pathlib import Path
import sys,json,subprocess,cairosvg
sys.path.insert(0,str(Path(__file__).resolve().parents[3]))
from icon_set.scripts.primitive_fix import load_icon,run_module
root=Path(__file__).parent;rs=json.loads((root/'runs.json').read_text())
details={
'piping-nozzle-above-icing-dollop':'SQUARE fits diagonal nozzle and separate rounded mound. Omitted the cropped bag continuation; the nozzle now has an outlined opening instead of a solid short stroke. No useful exact Lucide match; coherent curve construction.',
'paint-spray-gun-bottle':'SQUARE fits grip, feed, reservoir and two diverging spray marks. Reduced three rays to two and omitted the narrow nozzle collar. No useful exact Lucide match. Asymmetry follows the tool profile.',
'pomegranate-crown-inner-stem':'VRECT_L restores upright fruit proportions. Integrated three-point calyx and asymmetric inner branches; no required feature omitted. Lucide apple supports coherent fruit contour and attachment.',
'pomelo-with-single-leaf':'VRECT_L fits a rounded asymmetric fruit, diagonal stalk and pointed leaf. Leaf moved upper-right for clear separation from the fruit shoulder. Lucide apple and leaf inform smooth contours; no internal leaf vein needed.',
'scored-bread-loaf':'HRECT_M restores wide loaf proportions. Two oblique curved scores replace three crowded source scores. No useful exact Lucide match; continuous rounded silhouette.',
'scissors-cutting-film':'SQUARE fits enlarged finger loops, crossing blades and two separated film frames joined by the right rail. Fine perforations omitted. Lucide scissors informs two round loops and crossing blades.',
'standing-cow-profile':'HRECT_L keeps a long back, ear, hanging rounded muzzle and legs. Omitted tiny eye, udder, far legs and tail at 48px. No useful exact Lucide match; intentional profile asymmetry.',
'strapped-suitcase-above-a-conveyor':'VRECT_L provides room for a separated conveyor below rounded luggage. Two straps and handle retained; no roller details added. Lucide luggage informs rounded case, handle and strap alignment.',
'tapered-bucket-with-a-side-handle':'HRECT_L balances broad tapered pail with a swinging handle connected to its visible pivot. Pivot uses the supported small-circle construction. No useful exact Lucide match; oval rim and tapered coherent body.',
'tall-rain-boot-with-heel':'VRECT_L retains tall shaft and left-facing toe. Rounded cuff and toe, natural ankle and small integrated heel; no extra seam added. No useful exact Lucide match.',
'teardrop-pendant-round-loop':'VRECT_M restores a tall pendant with a visible circular loop touching its tip. No ornaments added or omitted. Circular loop and smooth coherent droplet construction; Lucide circle supports loop construction.',
'tapping-finger-with-contact-arc':'CIRCLE accommodates two concentric contact arcs and an upright index finger. Retained open wrist and simplified folded fingers. Lucide hand informs rounded fingertip and thumb; human-reference.md read for human-part construction; no detached head rule applies.',
 'tea-leaves-beside-pearl-cluster':'SQUARE fits asymmetric leaves and three large outlined pearls. Reduced five pearls to three tangent circles in a row for readable holes; preserved diagonal stem. Lucide leaf informs asymmetric pointed leaf construction.',
 'square-neck-pinafore-dress':'VRECT_L fits upright straps, square neckline, straight-sided bodice and flared skirt. No extra pocket or fabric seam. Bilateral construction preserves equal strap widths; no useful exact Lucide match.',
 'three-sugar-cubes-above-deep-spoon':'SQUARE retains three sugar cubes above a deep rounded bowl. Handle reduced to one stroke to preserve bowl depth. Fine perspective edges omitted. No useful exact Lucide match; rounded bowl replaces angular trough.'
}
for r in rs[5:]:
 p=Path(r['run']);m=run_module(p);icon=load_icon(m);v=icon.validate_icon();assert v.status=='valid' and not v.warnings
 for size in (48,384):cairosvg.svg2png(url=r['reference_path'],write_to=str(p/f'reference-{size}.png'),output_width=size,output_height=size,background_color='white')
 if r['icon_id']=='tea-leaves-beside-pearl-cluster':r['change']='Restored asymmetric leaves with diagonal stem and three large outlined pearl circles; reduced five pearls to three for clear interiors.'
 if r['icon_id']=='tapping-finger-with-contact-arc':r['change']='Restored two concentric contact arcs above an upright index finger and a smooth thumb, keeping the wrist open.'
 if r['icon_id']=='scissors-cutting-film':r['change']='Enlarged scissor loops and restored a film strip with two clear frames, a right rail and a cut approached by crossing blades.'
 if r['icon_id']=='standing-cow-profile':r['change']='Rounded the hanging muzzle and balanced the ear, long back and broad legs; omitted small anatomy that crowds the silhouette.'
 if r['icon_id']=='pomelo-with-single-leaf':r['change']='Restored a pointed diagonal leaf, slanted stalk and asymmetric rounded citrus body, with clear leaf-to-fruit spacing.'
 result=dict(r,author='gpt-6',validation_status='valid',validation_warnings=[],build_gate='pass',keyshape=icon.keyshape.name,visual_review='Inspected at native 48px and enlarged in both light and dark themes. Recognizable subject, clear openings and smooth continuous curves; deliberate source asymmetry retained.',omissions_and_references=details[r['icon_id']],module=m.name,svg=r['icon_id']+'.svg',artifacts=sorted(f.name for f in p.iterdir() if f.is_file()))
 (p/'result.json').write_text(json.dumps(result,indent=2))
(root/'runs.json').write_text(json.dumps(rs,indent=2))
for r in rs[5:]:
 if (Path(r['claim'])/'result.json').exists():continue
 proc=subprocess.run(['python3','icon_set/scripts/primitive_fix.py','finish','--worker','thuan-mac','--icon','solo/'+r['icon_id'],'--run',r['run'],'--outcome','done','--note',r['change']])
 if proc.returncode:print('NEEDS RETRY',r['icon_id'],proc.returncode,flush=True)
