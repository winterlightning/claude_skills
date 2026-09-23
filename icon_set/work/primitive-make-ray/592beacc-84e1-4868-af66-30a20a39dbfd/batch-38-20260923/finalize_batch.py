"""Record batch 38 findings and write result.json receipts last."""
from pathlib import Path
import json,shutil,importlib.util,html,os,cairosvg
from PIL import Image,ImageDraw
SOURCE_ICON_ID='592beacc-84e1-4868-af66-30a20a39dbfd'
SOURCE_PATH='icon_set/work/todo-references/rectangle list_592beacc-84e1-4868-af66-30a20a39dbfd.svg'
AUTHOR='gpt-6'
ROOT=Path(__file__).parent
rows=json.loads((ROOT/'batch-inputs.json').read_text())
findings=[
'Three equal rows remain centered with uniform spacing and clear gaps to the rounded panel in both themes.',
'Two left-aligned lines retain their unequal lengths and the wide panel proportions. Frame corners use a common radius.',
'Right-hand check retains the intentionally empty left side. Check and panel remain separate at native size.',
'Circular head and symmetric shoulder arch remain readable. The square frame is taller than the reference. Head bottom y21 and shoulder apex y29 give exactly 4 visible ink units of separation.',
'All four focus brackets, portrait and outer panel remain present. Lower brackets merge optically into the shoulders and frame gaps are too small. Manual repair required. Detached head gap itself is exactly 4 ink units.',
'All three letters read as SUB in both themes. U interior, letter spacing and B-to-panel clearance are undersized. Full text retained for manual repair.',
'Two equal busts remain identifiable, but shoulder-to-shoulder and shoulder-to-frame gaps are too tight. Each head still has exactly 4 ink units to its own shoulders. Manual repair required.',
'Long stem and lower bulb are centered and clear. This shares bulb radius and frame with UV medium; only stem length differs.',
'Short stem distinguishes medium from high. The bulb, frame, baseline and radii match the high variant.',
'History arc, arrowhead and clock hands remain recognizable but crowd the portrait frame and one another. Manual repair required.',
'Four equal vertical rules maintain uniform eight-unit centerline spacing and exact straight-edge frame clearance. Round joins replace corner arcs.',
'Centered X and rounded frame remain balanced. Equal arms and matching corner radii read cleanly in both themes.',
'Diagonal tag, eyelet and leaf are recognizable. Leaf and stem now share a real endpoint. Eyelet-to-tag and tag-to-leaf gaps still fail; manual repair required.',
'Both outlined bars stay equal in width and height. The diagonal remains attached to the lower bar and clears the upper bar.',
'Mirrored triangles, central axis and left arrow remain distinct. Only the overhead arrow introduces directional asymmetry.',
'Matches reflect left in frame, triangles and axis; the arrowhead is mirrored to point right. All negative spaces remain open.',
'Explosion, diagonal capsule, small house and doorway are retained. Explosion/roof join and small doorway are congested at native size; manual repair required.',
'Triangle, eye lens and circular iris retain the Cao Dai composition. The three nested boundaries crowd heavily at native size; manual repair required.',
'Bone and leaf are now separated. Equal-radius bone lobes improve the smoothness of the initial draft. Bone is steeper and leaf narrower than the source to maintain clearance; organic asymmetry is deliberate.',
'Both hexagons and central circle remain clear as nested shapes, but the center-to-inner-hexagon gap is only one ink unit. Manual repair required; existing registered draft remains unchanged.'
]
reasons={
'SQUARE':'The full composition uses centerline extremes (6,6)–(42,42).',
'HRECT_L':'The wide composition uses centerline extremes (4,8)–(44,40).',
'HRECT_M':'The shallow wide composition uses centerline extremes (4,10)–(44,38).',
'VRECT_L':'The upright panel uses centerline extremes (8,4)–(40,44).',
'VRECT_M':'The narrow upright indicator uses centerline extremes (10,4)–(38,44).'}
records=[]
for i,row in enumerate(rows):
 d=Path(row['result_dir']);rec=json.loads((d/'review-draft.json').read_text());p=d/rec['module'];source=p.read_text()
 source+='\nKEYSHAPE_REASON='+repr(reasons[rec['keyshape']])+'\n'
 if i==18:
  rec['omissions']='No objects omitted. Bone angle made steeper and leaf narrowed to separate both subjects.'
  source+='FINAL_REDUCTIONS='+repr(rec['omissions'])+'\n'
 p.write_text(source)
 spec=importlib.util.spec_from_file_location('verify38_'+str(i),p);m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m);icon=m.Drawing();report=icon.validate_icon()
 assert icon.to_svg()==(d/(row['icon_id']+'.svg')).read_text()
 assert report.status==rec['validation_status']
 (d/'validation.txt').write_text(report.describe());shutil.copy2(row['reference_path'],d/'reference.svg')
 cairosvg.svg2png(url=row['reference_path'],write_to=str(d/'reference-48.png'),output_width=48,output_height=48,background_color='white')
 humans=[]
 for name,cx,cy,radius,apex in ({3:[('person',24,18,3,29)],4:[('person',24,20,3,31)],6:[('left',15,18,3,29),('right',33,18,3,29)]}.get(i,[])):
  humans.append({'figure':name,'guide':'icon_set/skills/icon-design/human-reference.md','reference':'icon_set/references/human_ref/user.svg','head_center':[cx,cy],'head_radius':radius,'head_bottom':cy+radius,'shoulder_apex':[cx,apex],'centerline_gap':apex-cy-radius,'ink_gap':apex-cy-radius-4,'construction':'Detached framed bust, no stick-figure torso. Cardinal ellipse upper bound and circle lower bound establish exact vertical head-to-shoulder clearance.'})
 rec.update(keyshape_reason=reasons[rec['keyshape']],svg=row['icon_id']+'.svg',
  validation_findings=report.describe(),validation_errors=len(report.errors),validation_warnings=len(report.warnings),
  visual_review={'inspected_native_light_and_dark':True,'inspected_enlarged_light_and_dark':True,'findings':findings[i],'manual_review_recommended':report.status!='valid'},
  human_construction=humans,registered_context='Hidden double-hexagon draft inspected and validated as invalid (inner-to-center MIC); left unchanged.' if i==19 else 'No matching registered Python filename found.',
  artifacts=sorted(f.name for f in d.iterdir() if f.is_file())+['result.json'],
  scope='Standalone result folder only. No published, gallery, registry, metadata catalog, queue or runtime-state updates.')
 records.append(rec)
valid=sum(r['validation_status']=='valid' for r in records);blocked=len(records)-valid
report=['# TODO batch 38 of 55','',f'20 supplied files processed in order. **{valid} valid without warnings; {blocked} blocked.** All have authored Python modules, exact input metadata, SVGs, reference renders, native/enlarged light and dark previews, and validation findings. Author: `gpt-6`.','',
'All output stays in standalone result folders. Initial attempts and intermediate revisions remain available where a repair was made. Numeric validation and visual findings are recorded separately.','',
'| # | Input concept | Validation | Artifacts |','|---|---|---|---|']
page=['<!doctype html><meta charset="utf-8"><title>TODO batch 38</title><style>body{font:16px system-ui;margin:30px;background:#eee}article{background:white;padding:20px;margin:20px 0}img{width:192px;height:192px;object-fit:contain}pre{white-space:pre-wrap}a{color:#075ab0}.native{width:48px;height:48px}</style>',f'<h1>TODO batch 38 — 20 attempts</h1><p>{valid} valid without warnings; {blocked} blocked.</p>']
for i,rec in enumerate(records):
 d=Path(rec['result_dir']).resolve();report.append(f"| {i+1} | {rec['concept']} | {rec['validation_status']} | [Folder]({d}) · [SVG]({d/rec['svg']}) |")
report.append('')
for i,rec in enumerate(records):
 d=Path(rec['result_dir']).resolve();rel=os.path.relpath(d,ROOT.resolve())
 report.extend([f"## {i+1}. {rec['concept']}",'',f"[Folder]({d}) · [SVG]({d/rec['svg']}) · [Result]({d/'result.json'}) · [Validation]({d/'validation.txt'})",'',rec['subject_and_plan'],f"Keyshape: **{rec['keyshape']}**. {rec['keyshape_reason']}",'',f"Input reference: `{rec['reference_path']}`. Construction reference: {rec['construction_references']}",f"Omissions/reductions: {rec['omissions']}",'',f"Visual review: {rec['visual_review']['findings']}",'','```text',rec['validation_findings'].strip(),'```',''])
 if rec['human_construction']:report.extend(['Human construction: '+json.dumps(rec['human_construction']),''])
 page.append(f'<article><h2>{i+1}. {html.escape(rec["concept"])} — {rec["validation_status"]}</h2>')
 for name in ('reference.png','light-240.png','dark-240.png','reference-48.png','light-48.png','dark-48.png'):
  page.append(f'<img class="{"native" if "48" in name else ""}" src="{rel}/{name}" alt="{name}">')
 page.append(f'<p>{html.escape(rec["visual_review"]["findings"])}</p><p><a href="{rel}/{rec["svg"]}">SVG</a> · <a href="{rel}/">Folder</a> · <a href="{rel}/validation.txt">Validation</a></p><pre>{html.escape(rec["validation_findings"])}</pre></article>')
(ROOT/'batch-report.md').write_text('\n'.join(report));(ROOT/'index.html').write_text('\n'.join(page))
sheet=Image.new('RGB',(800,480),'#ddd');dr=ImageDraw.Draw(sheet)
for i,rec in enumerate(records):
 d=Path(rec['result_dir']);x=i%4*200;y=i//4*96;dr.text((x+2,y+2),str(i+1)+' '+rec['concept'][:22],fill='black')
 for j,name in enumerate(('reference-48.png','light-48.png','dark-48.png')):sheet.paste(Image.open(d/name).convert('RGB'),(x+5+j*60,y+24))
sheet.save(ROOT/'native-comparison.png')
# Completion receipts are the final writes to each result bundle.
for rec in records:(Path(rec['result_dir'])/'result.json').write_text(json.dumps(rec,indent=2))
print(f'{len(records)} receipts saved; {valid} valid; {blocked} blocked.')
