"""Finalize visually inspected batch 34; completion receipts are written last."""
from pathlib import Path
import json,shutil,importlib.util,html,os,cairosvg
from PIL import Image,ImageDraw
SOURCE_ICON_ID='7b4f6d04-e199-443e-be81-3c0acef5ca62'
SOURCE_PATH='icon_set/work/todo-references/picture polaroid landscape_7b4f6d04-e199-443e-be81-3c0acef5ca62.svg'
AUTHOR='gpt-6'
ROOT=Path(__file__).parent
rows=json.loads((ROOT/'batch-inputs.json').read_text())
findings=[
'Two peaks, sun and broad bottom margin remain legible in both themes. Smaller mountain opening is compact; sun reads as a filled disc at native size.',
'Front portrait and exposed rear panel are distinct. Circular head is centered over smooth shoulders. Head bottom y23 and shoulder apex y31 give exactly 8 centerline / 4 visible ink units of separation.',
'All three picture layers and foreground landscape are retained. Closely spaced back edges and mountain/sun details remain too dense; manual repair required.',
'Five ray directions, circular sun and two rounded hills remain visible. Several rays merge optically at native size, and the hill junction is crowded. Manual repair required.',
'Two unequal angular mountain ridges and upper-right sun remain legible; foreground ridge was lowered to open the sun gap. Directional asymmetry is intentional.',
'Capsule, oblique division, check and X remain recognizable. Both glyphs crowd the divider; manual repair required.',
'Rounded medicine box, shallow lid and centered medical plus remain clear. Outlined cross was reduced to two coherent strokes.',
'Pin and add badge are recognizable, but overlapping outlines and tiny plus create a dense joint. Manual repair required; no false connection declaration was used to excuse the overlap.',
'Symmetric rounded head narrows through inward-curving shoulders into a distinct slender point. Curve flow is smooth at native size.',
'Symmetric broad lower sweep distinguishes this from pin one. Top semicircle and lower side curves meet with vertical tangents.',
'Centered X, round head and narrow tail remain readable. X arms and marker silhouette are balanced in both themes.',
'Pin, central aperture and narrow ground X remain separate. Pin is stouter and its aperture smaller than the reference to fit the complete composition.',
'Rounded lower point and wider ground X distinguish the variant. Aperture was reduced to preserve spacing; both themes remain legible.',
'Round pin head, straight shaft and wide ground X meet coherently. Head and shaft connect at the circle’s exact lower extreme.',
'Hollow pin is centered above the broad shallow X. The point and crossing maintain a visible gap; inner aperture is smaller than the reference.',
'Plane, divider, cocktail bowl, foot and citrus are all retained. Aircraft interior and garnish area are heavily compressed; manual redesign required.',
'Plane, divider, fork and knife are retained. Aircraft and fork tine openings are too dense at native size; manual redesign required.',
'Walking figure and side luggage read clearly after rebalancing. Head center (22,9), radius 5, and torso start (22,22) give exactly 4 visible ink units of head separation. Bag-to-torso gap remains only 2 ink units; small aircraft is compressed.',
'Antenna pair, screen, feet and play glyph remain clear. Play triangle is vertically compressed relative to the source to keep legal screen clearance.',
'Circular border and right-pointing triangle are clear in both themes, with even visual weight and open negative space.'
]
reasons={
'SQUARE':'The whole composition is approximately square; the centerline extremes are (6,6)–(42,42).',
'CIRCLE':'The circular outer border owns radius 20 on the centerline about (24,24).',
'HRECT_M':'The capsule uses a wide 40×28 centerline envelope, (4,10)–(44,38).',
'VRECT_L':'The upright complete composition uses centerline extremes (8,4)–(40,44).',
'VRECT_M':'The narrow marker-and-ground composition uses centerline extremes (10,4)–(38,44).'}
records=[]
for i,row in enumerate(rows):
 d=Path(row['result_dir']);rec=json.loads((d/'review-draft.json').read_text());p=d/rec['module'];source=p.read_text()
 # Delete an unused helper only; emitted geometry is checked byte-for-byte below.
 start=source.find('    def aircraft(self):');end=source.find('    def build(self):')
 if start>=0:source=source[:start]+source[end:]
 source+='\nKEYSHAPE_REASON='+repr(reasons[rec['keyshape']])+'\n'
 if i in (11,12,14):
  rec['omissions']='No components omitted. Pin aperture and vertical pin proportions reduced to make room for the ground X.'
  source+='FINAL_REDUCTIONS='+repr(rec['omissions'])+'\n'
 p.write_text(source)
 spec=importlib.util.spec_from_file_location('verify34_'+str(i),p);m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m);icon=m.Drawing();report=icon.validate_icon()
 assert icon.to_svg()==(d/(row['icon_id']+'.svg')).read_text()
 assert report.status==rec['validation_status']
 (d/'validation.txt').write_text(report.describe());shutil.copy2(row['reference_path'],d/'reference.svg')
 cairosvg.svg2png(url=row['reference_path'],write_to=str(d/'reference-48.png'),output_width=48,output_height=48,background_color='white')
 human=None
 if i==1:human={'reference':'icon_set/references/human_ref/user.svg','guide':'icon_set/skills/icon-design/human-reference.md','head_center':[20,19],'head_radius':4,'head_bottom':23,'shoulder_apex':[20,31],'centerline_gap':8,'ink_gap':4,'construction':'Detached head in a framed portrait; shoulders attach to the panel bottom.'}
 if i==17:human={'reference':'icon_set/references/human_ref/full_body_ref.png','guide':'icon_set/skills/icon-design/human-reference.md','head_center':[22,9],'head_radius':5,'head_bottom':14,'torso_start':[22,22],'centerline_gap':8,'ink_gap':4,'construction':'Vertical head/upper-torso axis; mark_human_figure traveler emitted. Arms extend down from the neck, so the torso junction remains the nearest body point.'}
 rec.update(keyshape_reason=reasons[rec['keyshape']],svg=row['icon_id']+'.svg',
  validation_findings=report.describe(),validation_errors=len(report.errors),validation_warnings=len(report.warnings),
  visual_review={'inspected_native_light_and_dark':True,'inspected_enlarged_light_and_dark':True,'findings':findings[i],'manual_review_recommended':report.status!='valid'},
  human_construction=human,registered_context='No matching registered Python filename found.',
  artifacts=sorted(f.name for f in d.iterdir() if f.is_file())+['result.json'],
  scope='Standalone folder only. No published, gallery, registry, metadata catalog, queue or runtime-state updates.')
 records.append(rec)

valid=sum(r['validation_status']=='valid' for r in records);blocked=len(records)-valid
report=['# TODO batch 34 of 55','',f'All 20 supplied files processed in order. **{valid} valid without warnings; {blocked} blocked.** All have authored Python, input metadata, SVG, reference renders, light/dark previews and validation evidence. Author: `gpt-6`.','',
'All output stays in standalone result folders. Numeric validation and visual findings are reported separately. Source geometry from earlier revisions remains in the initial-attempt subfolders.','',
'| # | Input concept | Validation | Artifacts |','|---|---|---|---|']
page=['<!doctype html><meta charset="utf-8"><title>TODO batch 34</title><style>body{font:16px system-ui;margin:30px;background:#eee}article{background:white;padding:20px;margin:20px 0}img{width:192px;height:192px;object-fit:contain}pre{white-space:pre-wrap}a{color:#075ab0}.native{width:48px;height:48px}</style>',f'<h1>TODO batch 34 — 20 attempts</h1><p>{valid} valid without warnings; {blocked} blocked.</p>']
for i,rec in enumerate(records):
 d=Path(rec['result_dir']).resolve();svg=d/rec['svg'];report.append(f"| {i+1} | {rec['concept']} | {rec['validation_status']} | [Folder]({d}) · [SVG]({svg}) |")
report.append('')
for i,rec in enumerate(records):
 d=Path(rec['result_dir']).resolve();svg=d/rec['svg'];rel=os.path.relpath(d,ROOT.resolve())
 report.extend([f"## {i+1}. {rec['concept']}",'',f"[Folder]({d}) · [SVG]({svg}) · [Result]({d/'result.json'}) · [Validation]({d/'validation.txt'})",'',
 rec['subject_and_plan'],f"Keyshape: **{rec['keyshape']}**. {rec['keyshape_reason']}",'',
 f"Input: `{rec['reference_path']}`. Construction reference: {rec['construction_references']}",f"Omissions/reductions: {rec['omissions']}",'',
 f"Visual review: {rec['visual_review']['findings']}",'',
 '```text',rec['validation_findings'].strip(),'```',''])
 if rec['human_construction']:report.extend(['Human construction: '+json.dumps(rec['human_construction']), ''])
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
# result.json is deliberately written last for each completed attempt.
for rec in records:(Path(rec['result_dir'])/'result.json').write_text(json.dumps(rec,indent=2))
print(f'{len(records)} receipts saved; {valid} valid; {blocked} blocked.')
