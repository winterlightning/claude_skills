"""Save batch 41 review evidence; completion receipts are written last."""
from pathlib import Path
import json,shutil,importlib.util,html,os,cairosvg
from PIL import Image,ImageDraw
SOURCE_ICON_ID='0918c48a-7ee6-4895-9035-4645fdc17ae1'
SOURCE_PATH='icon_set/work/todo-references/scoreboard_0918c48a-7ee6-4895-9035-4645fdc17ae1.svg'
AUTHOR='gpt-6'
ROOT=Path(__file__).parent
rows=json.loads((ROOT/'batch-inputs.json').read_text())
findings=[
'Both hanging tabs and the complete 2:0 score remain recognizable. Hangers, score glyphs, colon and panel are too close; manual repair required.',
'Both ground posts and the complete 2:0 score are retained. The zero crowds the right wall and glyph/colon clearances fail; manual repair required.',
'Concave action bubble and all six surrounding marks remain clear. The rays are short dash/dot-like marks at native size; symmetry and empty center are preserved.',
'Eight cardinal/corner points remain balanced with consistent stepped shoulders. Deliberate sharp corners preserve the angular source seal.',
'Rounded search field and right-hand magnifier remain clear. The handle is short and the field taller than the reference to preserve interior space.',
'Round lens and lower-right handle remain clear at native size. The handle attaches to an exact point on the circular contour.',
'Walking person, direction arrow and chair remain separate. Outline thickness of the source chair and figure is reduced to strokes. Head-to-upper-torso gap is exactly 4 ink units.',
'Head, shoulders, arm edge and foreground magnifier remain recognizable, but the lens intersects the shoulder and crowds head/torso details. Manual repair required. Human head-to-shoulder gap is exactly 4 ink units.',
'Car, two radio arcs, roof and paired lamps/wheels remain identifiable. Radio arcs and headlamps have insufficient clearance; manual repair required.',
'Dollar remains legible in the larger retained form. Compact glyph trial was rejected visually; vertical stem now still crowds the screen. Manual repair required.',
'Euro and two right-hand rules remain legible in the common terminal. Currency height is reduced and screen corners use round joins; numeric clearance passes.',
'Pound remains legible in the larger retained form. Compact trial was rejected visually; foot and turning stroke crowd the lower screen edge. Manual repair required.',
'Yuan branching stroke, single currency bar, two rules and terminal remain recognizable. Glyph height and menu rules are reduced to open screen clearance.',
'Circular dot and open comma preserve the semicolon. Comma quarters join continuously into a smooth descending tail; the narrow glyph fits the radial keyshape.',
'Left arrow remains centered within the rounded square, with clear interior space and equal chevron arms.',
'Right arrow mirrors the left version and preserves the actual supplied picture despite the backward filename.',
'Open-front cylinder, side bands and outstretched figure remain present. Cylinder wall/window gaps and legs near the lower rim are crowded; manual repair required. Human head/torso gap itself is exactly 4 ink units.',
'Eye lens, iris, magnifying ring and handle remain identifiable, but the nested eye boundaries are heavily crowded. Manual repair required.',
'Serif M retains both upright stems, deep central point and four terminal serifs. Source double outlines are reduced to a single-stroke letter; the character remains clear.',
'Two offset crosses remain visible inside the rounded panel. The right cross has a taller lower stem, while its upper arm is deliberately short at native size.'
]
reasons={
'SQUARE':'The complete composition uses centerline extremes (6,6)–(42,42).',
'HRECT_L':'The wide composition uses centerline extremes (4,8)–(44,40).',
'HRECT_M':'The shallow wide composition uses centerline extremes (4,10)–(44,38).',
'CIRCLE':'The narrow punctuation fits radius 20 on the centerline about (24,24); top dot and tail reach the radial extremes without widening the glyph.'}
records=[]
for i,row in enumerate(rows):
 d=Path(row['result_dir']);rec=json.loads((d/'review-draft.json').read_text());p=d/rec['module'];source=p.read_text()
 source+='\nKEYSHAPE_REASON='+repr(reasons[rec['keyshape']])+'\nFINAL_REDUCTIONS='+repr(rec['omissions'])+'\n';p.write_text(source)
 spec=importlib.util.spec_from_file_location('verify41_'+str(i),p);m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m);icon=m.Drawing();report=icon.validate_icon()
 assert icon.to_svg()==(d/(row['icon_id']+'.svg')).read_text()
 assert report.status==rec['validation_status']
 (d/'validation.txt').write_text(report.describe());shutil.copy2(row['reference_path'],d/'reference.svg')
 cairosvg.svg2png(url=row['reference_path'],write_to=str(d/'reference-48.png'),output_width=48,output_height=48,background_color='white')
 human=None
 if i==6:human={'guide':'icon_set/skills/icon-design/human-reference.md','reference':'icon_set/references/human_ref/full_body_ref.png','figure':'walker','head_center':[14,10],'head_radius':4,'head_bottom':14,'torso_junction':[14,22],'centerline_gap':8,'ink_gap':4,'evidence':'Head and vertical torso share x=14. Arms extend down from the torso start; mark_human_figure walker emitted.'}
 if i==7:human={'guide':'icon_set/skills/icon-design/human-reference.md','reference':'icon_set/references/human_ref/user.svg','head_center':[16,12],'head_radius':6,'head_bottom':18,'shoulder_y':26,'centerline_gap':8,'ink_gap':4,'evidence':'Horizontal shoulder from (14,26) to (22,26) lies below the head axis; nearest head/body pair is (16,18) to (16,26). No stick torso in this partial portrait.'}
 if i==16:human={'guide':'icon_set/skills/icon-design/human-reference.md','reference':'icon_set/references/human_ref/full_body_ref.png','figure':'person','head_center':[24,18],'head_radius':4,'head_bottom':22,'torso_junction':[24,30],'centerline_gap':8,'ink_gap':4,'evidence':'Head, torso and arm junction share x=24. Arms lie on y=30; mark_human_figure person emitted.'}
 rec.update(keyshape_reason=reasons[rec['keyshape']],svg=row['icon_id']+'.svg',
  validation_findings=report.describe(),validation_errors=len(report.errors),validation_warnings=len(report.warnings),
  visual_review={'inspected_native_light_and_dark':True,'inspected_enlarged_light_and_dark':True,'findings':findings[i],'manual_review_recommended':report.status!='valid'},
  human_construction=human,registered_context='No matching registered Python filename found.',
  artifacts=sorted(f.name for f in d.iterdir() if f.is_file())+['result.json'],
  scope='Standalone result folder only. No published, gallery, registry, metadata catalog, queue or runtime-state updates.')
 records.append(rec)
valid=sum(r['validation_status']=='valid' for r in records);blocked=len(records)-valid
report=['# TODO batch 41 of 55','',f'20 supplied references processed in order. **{valid} valid without warnings; {blocked} blocked.** Every attempt includes Python, exact source metadata, SVG, reference renders, native/enlarged light and dark previews, and validation evidence. Author: `gpt-6`.','',
'All output stays in standalone folders. Earlier candidates are preserved where repairs were made. Numeric results and visual findings are distinguished below. Scoreboard rows 1 and 2 have distinct source UUIDs and remain separate drawings.','',
'| # | Input concept | Validation | Artifacts |','|---|---|---|---|']
page=['<!doctype html><meta charset="utf-8"><title>TODO batch 41</title><style>body{font:16px system-ui;margin:30px;background:#eee}article{background:white;padding:20px;margin:20px 0}img{width:192px;height:192px;object-fit:contain}pre{white-space:pre-wrap}a{color:#075ab0}.native{width:48px;height:48px}</style>',f'<h1>TODO batch 41 — 20 attempts</h1><p>{valid} valid without warnings; {blocked} blocked.</p>']
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
# These receipts are deliberately the last writes in each completed result bundle.
for rec in records:(Path(rec['result_dir'])/'result.json').write_text(json.dumps(rec,indent=2))
print(f'{len(records)} receipts saved; {valid} valid; {blocked} blocked.')
