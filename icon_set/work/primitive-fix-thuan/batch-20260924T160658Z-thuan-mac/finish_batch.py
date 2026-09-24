from pathlib import Path
import json,sys,subprocess,re
import cairosvg
ROOT=Path(__file__).resolve().parents[4];sys.path.insert(0,str(ROOT))
from icon_set.scripts.primitive_fix import load_icon
SOURCE_ICON_ID=None;SOURCE_PATH=None;AUTHOR='gpt-6'
BATCH=Path(__file__).parent
notes={
'rounded-cup-brassiere':'Rebuilt mirrored curved cup tops and smooth teardrop bowls; straight straps and shared bridge endpoints.',
'rounded-light-bulb':'Rebuilt a symmetric circular dome with smooth narrowing shoulders and a consistent rounded base.',
'rounded-scoop-ice-cream-cone':'Rebuilt circular scoop and tangent shoulder transitions; straight symmetric cone sides.',
'rounded-teacup':'Rebuilt the bowl with smooth elliptical lower corners and an exactly attached elliptical handle.',
'segmented-hand-grenade-with-ring':'Rebuilt a symmetric oval body and straight segmentation; safety ring and cap now meet at exact nodes.',
'serpentine-sea-dragon':'Rebuilt the neck and coil as one smooth S-shaped stroke with matched tangents, retaining the swept crest and jaw. Double neck outline simplified for readability.',
'shopping-cart-rounded':'Rebuilt straight basket walls with a continuous handle slope and two identical wheel circles.',
'side-view-bumper-car':'Rebuilt a smooth nose and seat recess, round bumper ends and straight power pole; attachments share exact nodes.',
'soap-bar-with-foam':'Rebuilt straight perspective edges and geometric foam lobes with a clean continuous lower outline.',
'sonic-head-three-quarter':'Rebuilt curved swept spines and muzzle, a pointed ear, two short eye strokes and a smooth smile; fine facial partitions omitted at 48px.',
'steaming-car-with-raised-hood':'Restored a connected car silhouette around equal wheels, with a straight raised hood and a smooth steam stroke.',
'storefront':'Rebuilt three identical awning scallops, straight panel seams and a centered doorway; shop walls join the scallop bottoms exactly.',
'sun-setting-behind-waves':'Rebuilt three identical smooth wave patterns at equal spacing, with tangent joins and a symmetric semicircular sun.',
'sydney-opera-house-shells':'Rebuilt coherent curved sail shells above a straight podium, preserving the tall central shell and shared endpoints.',
 'three-round-berries-on-a-leafy-stem':'Rebuilt equal round berries with a smooth curved stem and pointed leaf; retained all three fruit.',
 'tracked-bulldozer-with-front-blade':'Rebuilt the cab and engine with straight edges, a capsule track and a coherent curved blade; joins use shared nodes.',
 'triangular-ozone-molecule':'Rebuilt three identical circular atoms and three truly straight bonds with exact circle attachments.',
 'two-falling-bombs-solo':'Rebuilt two identical elongated capsule bodies and straight tail fins, retaining the diagonal stagger.',
 'upward-growth-trend-arrow':'Rebuilt every zigzag leg at 45 degrees and equal perpendicular arrowhead arms.',
 'utility-bucket-with-handle':'Rebuilt symmetric rim and bail arcs, truly straight tapered sides and tangent base transitions.'}
rows=[]
for claimfile in sorted((ROOT/'icon_set/work/primitive-fix-thuan').glob('*/20260924T160658Z-thuan-mac/claim.json')):
 claim=json.loads(claimfile.read_text());item=claim['item'];iconid=item['icon_id'];ref=next((claimfile.parent/'reference').glob('*.svg'));uuid=re.search(r'[0-9a-f-]{36}$',ref.stem)[0]
 out=ROOT/'icon_set/work/primitive-make-ray'/uuid/'20260924T160658Z-thuan-mac-centerlines'
 meta=json.loads((out/f'{iconid}.metadata.json').read_text());mod=next(out.glob('*.py'));icon=load_icon(mod);validation=icon.validate_icon()
 assert validation.status=='valid' and not validation.errors and not validation.warnings
 if iconid=='rounded-teacup':meta['plan']=meta['plan'].replace('Bowl sides tangent to quarter circles.','Bowl sides tangent to quarter ellipses.')
 if iconid=='sonic-head-three-quarter':
  meta['plan']=meta['plan'].replace('oval eye','two short eye strokes')
  meta['omissions']='Fine eye/muzzle partitions omitted to keep the face open at 48px.'
 (out/f'{iconid}.metadata.json').write_text(json.dumps(meta,indent=2)+'\n')
 cairosvg.svg2png(url=str(ref),write_to=str(out/'reference-48.png'),output_width=48,output_height=48)
 result=dict(meta,validation_status=validation.status,validation_errors=[],validation_warnings=[],visual_review=notes[iconid]+' Inspected at native 48px and enlarged size in light and dark themes.',artifacts=sorted(p.name for p in out.iterdir() if p.name!='result.json'))
 (out/'result.json').write_text(json.dumps(result,indent=2)+'\n')
 existing=claimfile.parent/'result.json'
 if not existing.exists():
  cp=subprocess.run([sys.executable,'icon_set/scripts/primitive_fix.py','--worker','thuan-mac','finish','--icon',item['key'],'--run',str(out.relative_to(ROOT)),'--outcome','done','--note',notes[iconid]],cwd=ROOT,text=True,capture_output=True)
  print(cp.stdout,flush=True)
  if cp.returncode: print(cp.stderr,flush=True);raise SystemExit(cp.returncode)
 finish=json.loads(existing.read_text());assert finish['outcome']=='done'
 rows.append(dict(key=item['key'],feedback=item.get('feedback'),note=notes[iconid],run=str(out),svg=str(out/f'{iconid}.svg'),validation='valid; zero errors and warnings',outcome=finish['outcome'],review_status=finish.get('review_status'),keyshape=meta['keyshape'],omissions=meta['omissions'],references=meta['construction_reference'],plan=meta['plan']))
 (BATCH/'outcomes.json').write_text(json.dumps(rows,indent=2)+'\n')
lines=['# Centerline repair batch — thuan-mac','',f'{len(rows)} icons repaired, validated and reported done through primitive_fix.py. Each production revision returned to Ready.','', 'Reviewer feedback for every icon: “Bad stroke drawn.” User specification: smooth, even centerlines, straight lines, clean joins, consistent stroke and appropriate symmetry; preserve the concept.','', 'All revisions were inspected at native size and enlarged in both themes. AUTHOR: gpt-6.','']
for r in rows:
 lines += ['## '+r['key'],'',r['note'],'',f"- Feedback: {r['feedback']}",f"- RESULT_DIR: [{Path(r['run']).name}]({r['run']})",f"- SVG: [{Path(r['svg']).name}]({r['svg']})",f"- Validation: {r['validation']}",f"- Reported outcome: {r['outcome']}; production review status: {r['review_status']}",f"- Keyshape and construction: {r['keyshape']}. {r['plan']}",f"- Construction reference: {r['references']}",f"- Simplifications: {r['omissions']}",'']
(BATCH/'report.md').write_text('\n'.join(lines))
print(f'COMPLETE: {len(rows)} done',flush=True)
