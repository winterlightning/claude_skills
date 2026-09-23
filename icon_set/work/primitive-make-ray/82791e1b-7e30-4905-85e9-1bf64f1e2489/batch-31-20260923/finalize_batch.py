"""Save the reviewed batch findings and completion receipts last."""
from pathlib import Path
import json, shutil, importlib.util, html
from icon_set.model.keyshapes import Keyshape
from icon_set.model.profiles import Profile
SOURCE_ICON_ID='82791e1b-7e30-4905-85e9-1bf64f1e2489'
SOURCE_PATH='icon_set/work/todo-references/online learning online course 2_82791e1b-7e30-4905-85e9-1bf64f1e2489.svg'
AUTHOR='gpt-6'
ROOT=Path(__file__).parent
rows=json.loads((ROOT/'batch-inputs.json').read_text())
findings=[
'Book halves mirror correctly and the binding remains clear. Field is taller than the reference to accommodate its rule with legal spacing.',
'Circular arch and centered keyhole read clearly in both themes. Keyhole is narrower than the source to clear the open arch ends.',
'Right-facing dog and sloping shelter remain recognizable, but the ear crowds the roof and the legs have cramped internal gaps. Manual repair required.',
'Six fuel cells remain open in both themes. Compact symmetric flame loses the reference’s asymmetric flicker; visual refinement recommended despite numeric validity.',
'Curved ear, projecting snout, panel and apple are retained. Apple crowds the panel and the snout. Dense composition requires manual repair.',
'Mirrored gable, side walls and foreground device remain distinct. The device crosses the building baseline intentionally.',
'Tank, valve and timer read clearly, but the valve band, hose contact, clock hands and adjacent round outlines do not meet clearance. Manual repair required.',
'Three equal circular wells retain the triangular arrangement and consistent gaps. Circular outer palette is balanced.',
'Framed sun and layered mountains remain recognizable. Tiny sun hole closes at native size; the filled-disc appearance is a visible reduction.',
'Bent front leg and rear leg preserve the crossing pose. Smooth hip and thigh curves improve the initial angular draft. Toe remains heavier than the reference; review recommended.',
'Image stays upper right with two short rules at left and a long rule below. One source text row is omitted to preserve whitespace.',
'T and left arrow remain clear, with shared top midpoint and an open arrow-to-stem gap. Directional asymmetry is intentional.',
'P+B reads clearly at native size. Narrow bowls and centered plus preserve complete lettering with legal gaps.',
'P+R reads clearly at native size. Narrow bowls match P+B construction; R diagonal deliberately breaks symmetry.',
'P, two wave arcs and triangular obstacle are separated visually, but the inner wave still crowds the P bowl by the numeric rule. Manual repair required.',
'Car and circular parking P remain identifiable, but badge letter, headlights and car outlines are crowded. Manual repair required.',
'Tall sign post, short right edge and P remain clear. Open right/bottom frame matches the supplied reference’s intentional asymmetry.',
'Centered rounded panel and rising check retain generous whitespace and smooth corners in both themes.',
'Background world disc and foreground passport retain their overlap. Small globe is too dense and reads like a target; the world also misses exact keyshape bounds. Manual repair required.',
'Binding and passport cover are clear, but the reduced globe reads more like a cross in a circle than curved globe meridians. Visual refinement recommended despite numeric validity; the source contains no visible hand.'
]
reasons={'SQUARE':'The full composition is approximately square and uses the 36×36 centerline envelope.',
'CIRCLE':'A dominant round outline owns the radial envelope centered at (24,24).',
'VRECT_M':'The tall, narrow subject uses the 28×40 centerline envelope.',
'VRECT_L':'The upright passport uses the 32×40 centerline envelope.',
'HRECT_L':'The side-by-side lettering uses the wide 40×32 centerline envelope.',
'HRECT_M':'The wide composition uses the 40×28 centerline envelope.'}
records=[]
for i,row in enumerate(rows):
 d=Path(row['result_dir']);rec=json.loads((d/'review-draft.json').read_text());p=d/rec['module']
 bounds=Keyshape[rec['keyshape']].bounds_for(Profile.SOLO48)
 source=p.read_text();source+='\nKEYSHAPE_INK_BOUNDS = '+repr(bounds)+'\nKEYSHAPE_REASON = '+repr(reasons[rec['keyshape']])+'\n'
 p.write_text(source)
 spec=importlib.util.spec_from_file_location('verify_final_'+str(i),p);m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m);icon=m.Drawing();report=icon.validate_icon()
 assert icon.to_svg()==(d/(row['icon_id']+'.svg')).read_text()
 assert report.status==rec['validation_status']
 (d/'validation.txt').write_text(report.describe())
 shutil.copy2(row['reference_path'],d/'reference.svg')
 rec.update(keyshape_ink_bounds=bounds,keyshape_reason=reasons[rec['keyshape']],
  visual_review={'inspected_native_light_and_dark':True,'inspected_enlarged_light_and_dark':True,'findings':findings[i],
                 'manual_review_recommended':report.status!='valid' or i in (3,9,19)},
  validation_findings=report.describe(),
  validation_errors=len(report.errors),validation_warnings=len(report.warnings),
  human_reference='icon_set/skills/icon-design/human-reference.md; icon_set/references/human_ref/full_body_ref.png' if i==9 else None,
  human_gap='Not applicable: only legs, no head.' if i==9 else 'No detached human head.',
  svg=row['icon_id']+'.svg',artifacts=sorted(f.name for f in d.iterdir() if f.is_file())+['result.json'],
  registered_context='Existing hidden crossed-stockinged-legs draft inspected for context; unchanged.' if i==9 else 'No matching registered filename found.',
  scope='Standalone folder only; no gallery, registry, metadata catalog, queue, runtime state or published writes.')
 records.append(rec)

report=['# TODO batch 31 of 55','',
        '20 supplied references processed in order. 14 candidates validate without warnings; 6 retain blocking findings. Native and enlarged light/dark previews were inspected. Numeric validity is distinct from the visual caveats below. Author: `gpt-6`.','',
        'All artifacts are standalone. Earlier draft evidence is retained inside each revised attempt. No published/gallery/registry/queue/runtime-state changes were made.','']
page=['<!doctype html><meta charset="utf-8"><title>TODO batch 31</title><style>body{font:16px system-ui;margin:30px;background:#eee}article{background:white;padding:20px;margin:20px 0}img{width:192px;height:192px;object-fit:contain}pre{white-space:pre-wrap}a{color:#075ab0}.native{width:48px;height:48px}</style><h1>TODO batch 31 — 20 attempts</h1><p>14 numerically valid; 6 blocked. Visual caveats are recorded individually.</p>']
for i,rec in enumerate(records):
 d=Path(rec['result_dir']).resolve();svg=d/rec['svg']; result=d/'result.json';validation=d/'validation.txt'
 report.extend([f"## {i+1}. {rec['concept']} — {rec['validation_status']}",'',
  f"[Folder]({d}) · [SVG]({svg}) · [Result]({result}) · [Validation]({validation})",'',
  f"{rec['subject_and_plan']}",f"Keyshape: **{rec['keyshape']}**, visible ink bounds `{rec['keyshape_ink_bounds']}`. {rec['keyshape_reason']}",'',
  f"Reference: `{rec['reference_path']}`. Construction: {rec['construction_references']}",f"Omissions/reductions: {rec['omissions']}",'',
  f"Visual review: {rec['visual_review']['findings']}",''])
 if rec['validation_status']!='valid':report.extend(['```text',rec['validation_findings'].strip(),'```',''])
 else:report.extend(['Validation: valid, zero warnings.',''])
 import os
 rel=os.path.relpath(d,ROOT.resolve())
 page.append(f'<article><h2>{i+1}. {html.escape(rec["concept"])} — {rec["validation_status"]}</h2>')
 for name in ('reference.png','light-240.png','dark-240.png','light-48.png','dark-48.png'):
  page.append(f'<img class="{"native" if "48" in name else ""}" src="{rel}/{name}" alt="{name}">')
 page.append(f'<p>{html.escape(rec["visual_review"]["findings"])}</p><p><a href="{rel}/{rec["svg"]}">SVG</a> · <a href="{rel}/">Folder</a> · <a href="{rel}/validation.txt">Validation</a></p><pre>{html.escape(rec["validation_findings"])}</pre></article>')
(ROOT/'batch-report.md').write_text('\n'.join(report))
(ROOT/'index.html').write_text('\n'.join(page))
# Completion receipts are the last artifacts written for each attempt.
for rec in records:
 (Path(rec['result_dir'])/'result.json').write_text(json.dumps(rec,indent=2))
print('Final receipts:',len(records),'valid:',sum(r['validation_status']=='valid' for r in records),'invalid:',sum(r['validation_status']=='invalid' for r in records))
