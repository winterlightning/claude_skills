"""Save batch 46 review evidence; completion receipts are written last."""
from pathlib import Path
import json,shutil,importlib.util,html,os,cairosvg
from PIL import Image,ImageDraw
SOURCE_ICON_ID='eba62204-89c9-492a-958f-b4f34fbc386d'
SOURCE_PATH='icon_set/work/todo-references/square dot top_eba62204-89c9-492a-958f-b4f34fbc386d.svg'
AUTHOR='gpt-6'
ROOT=Path(__file__).parent
rows=json.loads((ROOT/'batch-inputs.json').read_text())
findings=['Circular tab interrupts the frame top at shared circle endpoints. The shortened frame remains balanced.', 'Centered downward arrow has equal chevron arms. Source direction preserved despite filename.', 'Centered downward arrow intentionally matches the separate source UUID; filename direction is not depicted.', 'Envelope outline and downward flap remain legible. Lower fold seams were removed after they collapsed in the initial preview.', 'Speech bubble and lower-left tail remain recognizable. This is the source picture despite the letter filename; inner corners use round joins.', 'Wine glass has a symmetrical open bowl, centered short stem and foot. Clear space remains around the full composition.', 'All eight inward ticks remain equally spaced and connected to the frame. The center remains open.', 'Paired heart lobes meet at a central cleft and flow into the pointed base. Space around the heart is balanced.', 'Centered vertical I retains generous space within the frame.', 'Dot and vertical stem remain separate. Hollow source dot and outlined stem are reduced to solid dot and single stroke.', 'Right arrow remains centered and clear. Actual supplied picture retained despite the square j filename.', 'Broad left arrow retains its concave neck corners and equal upper/lower arms. Round joins replace source curved bends.', 'Three equal rules have uniform nine-unit vertical pitch and equal side margins.', 'Round shackle and small body remain readable as a padlock. Lower body height is reduced to open its clearance to the frame.', 'Circular head and shallow shoulders remain symmetrical. Head center (24,19), radius4 gives bottom23; shoulders apex31 gives exactly 8 centerline / 4 ink gap. Shoulders are flatter than the source.', 'Diagonal megaphone and rounded handle remain identifiable. Handle crowds the lower frame; manual repair required. A numerically valid compact trial resembled a sailboat and was rejected.', 'Centered O has balanced interior and exterior negative space.', 'Single-stroke P retains upright stem and round bowl. Bowl return meets the stem at a shared node.', 'Source R remains recognizable with a diagonal leg attached at the bowl return. Filename parking slash does not match the source picture.', 'Outlined P retains the source solid-letter silhouette and internal counter, but strokes crowd the counter and stem. MIC fails on multiple P edges; manual repair required.']
reasons={
'SQUARE':'The complete composition uses centerline extremes (6,6)–(42,42).',
'HRECT_L':'The wide composition uses centerline extremes (4,8)–(44,40).',
'HRECT_M':'The shallow wide composition uses centerline extremes (4,10)–(44,38).',
'CIRCLE':'The narrow punctuation fits radius 20 on the centerline about (24,24); top dot and tail reach the radial extremes without widening the glyph.'}
records=[]
for i,row in enumerate(rows):
 d=Path(row['result_dir']);rec=json.loads((d/'review-draft.json').read_text());p=d/rec['module'];source=p.read_text()
 source+='\nKEYSHAPE_REASON='+repr(reasons[rec['keyshape']])+'\nFINAL_REDUCTIONS='+repr(rec['omissions'])+'\n';p.write_text(source)
 spec=importlib.util.spec_from_file_location('verify46_'+str(i),p);m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m);icon=m.Drawing();report=icon.validate_icon()
 assert icon.to_svg()==(d/(row['icon_id']+'.svg')).read_text()
 assert report.status==rec['validation_status']
 (d/'validation.txt').write_text(report.describe());shutil.copy2(row['reference_path'],d/'reference.svg')
 cairosvg.svg2png(url=row['reference_path'],write_to=str(d/'reference-48.png'),output_width=48,output_height=48,background_color='white')
 human=None
 if i==14:human={'guide':'icon_set/skills/icon-design/human-reference.md','reference':'icon_set/references/human_ref/user.svg','head_center':[24,19],'head_radius':4,'head_bottom':23,'shoulder_apex':[24,31],'centerline_gap':8,'ink_gap':4,'evidence':'Ellipse shoulder endpoints (15,33) and (33,33), rx9 ry2, give apex (24,31), directly below the circular head. Portrait has no stick torso.'}

 rec.update(keyshape_reason=reasons[rec['keyshape']],svg=row['icon_id']+'.svg',
  validation_findings=report.describe(),validation_errors=len(report.errors),validation_warnings=len(report.warnings),
  visual_review={'inspected_native_light_and_dark':True,'inspected_enlarged_light_and_dark':True,'findings':findings[i],'manual_review_recommended':report.status!='valid'},
  human_construction=human,registered_context='No matching registered Python filename found.',
  artifacts=sorted(f.name for f in d.iterdir() if f.is_file())+['result.json'],
  scope='Standalone result folder only. No published, gallery, registry, metadata catalog, queue or runtime-state updates.')
 records.append(rec)
valid=sum(r['validation_status']=='valid' for r in records);blocked=len(records)-valid
report=['# TODO batch 46 of 55','',f'20 supplied references processed in order. **{valid} valid without warnings; {blocked} blocked.** Every attempt includes Python, exact source metadata, SVG, reference renders, native/enlarged light and dark previews, and validation evidence. Author: `gpt-6`.','',
'All output stays in standalone folders. Earlier candidates are preserved where repairs were made. Numeric results and visual findings are distinguished below. Arrow rows 2 and 3 have distinct source UUIDs and remain separate drawings. Filename/picture mismatches retain the actual supplied picture.','',
'| # | Input concept | Validation | Artifacts |','|---|---|---|---|']
page=['<!doctype html><meta charset="utf-8"><title>TODO batch 46</title><style>body{font:16px system-ui;margin:30px;background:#eee}article{background:white;padding:20px;margin:20px 0}img{width:192px;height:192px;object-fit:contain}pre{white-space:pre-wrap}a{color:#075ab0}.native{width:48px;height:48px}</style>',f'<h1>TODO batch 46 — 20 attempts</h1><p>{valid} valid without warnings; {blocked} blocked.</p>']
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
