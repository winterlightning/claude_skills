"""Record reviewed outcomes without changing authored geometry."""
from pathlib import Path
import importlib.util
import json
import shutil
import html
from PIL import Image, ImageDraw

SOURCE_ICON_ID = '0c038416-c2a9-4ae0-ab80-a793e4a0b0c7'
SOURCE_PATH = 'icon_set/work/todo-references/playlist album_0c038416-c2a9-4ae0-ab80-a793e4a0b0c7.svg'
AUTHOR = 'gpt-6'
ROOT=Path(__file__).parent
ENTRIES=json.loads((ROOT/'batch-inputs.json').read_text())
FINDINGS=[
    'The album frame, rising beam and two noteheads read clearly in light and dark at 48px. Rounded frame is balanced; the tilted beam preserves the reference asymmetry. Noteheads use the permitted small-circle construction.',
    'Roof, door and stacked toy remain identifiable. Toy occupies the right bay intentionally; it is a pawn-like play object, not a detached human figure. The tiny toy base is dense at 48px but remains distinguishable.',
    'Circular enclosure, equal prongs, bowl and descending cable read cleanly in both themes. Bilateral structure is preserved. The supplied drawing contains no visible bolt.',
    'Circle and plug are balanced; the cable deliberately curves right to match the input. The supplied drawing contains no visible minus sign.',
    'Open circular enclosure, plug and lower-right cross remain distinct. The plug is smaller and offset left to give the cross legal clearance. Mirrored pins and matched cross strokes remain coherent.',
    'Rounded enclosure widened to VRECT_L; pins, bowl and exiting cable retain their arrangement. Shared corner radii and smooth bowl tangents read clearly at native size.',
    'Five-point star is centered over equal supports. Single platform rail replaces the thin double rim; open star and podium remain recognizable in both themes.',
    'Upright monitor preserves the waveform, divider and paired controls. The reduced waveform amplitude makes room for a clear control band. Equal button spacing and rounded corners remain consistent.',
    'Retained full weave and folded corner are faithful but crowded. Rejected the numerically valid two-cell reduction because it resembled a window. Final is invalid: sheet/fold diagonal gap and fold/rightmost-strand crowding remain.',
    'Outlined sterling sign retains the hook, crossbar and foot. Final is invalid: the lower crossbar and upper foot are only 6 units apart on centerlines. Retained the coherent outlined glyph rather than distort its bar alignment.',
    'Outer circular rim and smaller diagonally divided inner disk remain recognizable. Seam endpoints meet the disk exactly; deliberate diagonal asymmetry matches the source.',
    'Panel and half gear retain their arrangement and two equal panel marks. Panel widened by one unit to remove uncertified curve clearance. Gear teeth are intentionally angular; hub remains on the panel boundary.',
    'Retained the larger curled fetal outline within the fan. Rejected the smaller numerically valid version because its interior filled in. Final is invalid: head side of baby is too close to the right fan edge. This is a connected anatomical silhouette, with no detached head gap.',
    'Mirrored torso sides and central heart-shaped pelvic mark remain recognizable in both themes. Smooth sides preserve natural waist/hip changes. A torso fragment has no head-to-body gap to measure.',
    'Curled page, Rx and writing lines are present, but the full composition is too dense at 48px. Final is invalid: writing-line spacing, lower page clearance and Rx-to-page clearance fail. The lines and letter are preserved for review rather than silently removed.',
    'Large Rx remains legible inside the rounded frame. Letter bowl and stems are coherent; crossing is intentional. The content is deliberately asymmetric because it is lettering.',
    'Printer input, housing, output and diagonal disabling slash all remain readable. The slash intentionally crosses the printer composition; its direction matches the reference.',
    'Both cupped hands and all three code marks remain recognizable. Hands are short and their thumb turns are dense at native size, but mirrored palms and the code-to-hand gap remain clear. These are hand fragments, with no detached head gap.',
    'Tapered shield and angular three preserve the CSS3 identity. Shield is bilateral; the numeral remains intentionally asymmetric. Lower corners and numeral retain purposeful angular turns.',
]
WHY={
    'CIRCLE':'The enclosing circular rim is the dominant silhouette, centered at (24,24) with radius 20 on the centerline.',
    'SQUARE':'The complete composition has a square overall envelope and uses the (6,6)–(42,42) centerline extremes.',
    'VRECT_L':'The upright composition benefits from the 32-by-40 centerline envelope, (8,4)–(40,44).',
    'VRECT_M':'The narrow upright glyph uses the 28-by-40 centerline envelope, (10,4)–(38,44).',
    'HRECT_L':'The broad ultrasound fan uses the 40-by-32 centerline envelope, (4,8)–(44,40).',
}

records=[]
for i,(e,finding) in enumerate(zip(ENTRIES,FINDINGS),1):
    d=Path(e['result_dir']);slug=e['icon_id'];plan=json.loads((d/'plan.json').read_text());p=d/plan['python']
    # The final class owns the envelope; keep the prose aligned with repairs.
    source=p.read_text()
    import re
    source=re.sub(r'Envelope: .*?; derive its bounds from Keyshape.bounds_for\(Profile.SOLO48\)\.',f"Envelope: {plan['keyshape']}. {WHY[plan['keyshape']]}",source)
    p.write_text(source)
    spec=importlib.util.spec_from_file_location('verify_'+e['source_uuid'].replace('-','_'),p)
    module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)
    assert module.SOURCE_ICON_ID==e['source_uuid'] and module.SOURCE_PATH==e['reference_path'] and module.AUTHOR==AUTHOR
    assert module.Drawing().to_svg()==(d/(slug+'.svg')).read_text()
    status=json.loads((d/'export-status.json').read_text())
    assert status['status'] in ('valid','invalid','review')
    if status['status']=='valid': assert status['errors']==0 and status['warnings']==0
    shutil.copy2(e['reference_path'],d/'reference.svg')
    # Historical errors remain explicit evidence, not current export failures.
    if (d/'error.txt').exists(): (d/'error.txt').rename(d/'initial-export-error.txt')
    metadata=dict(e,keyshape=plan['keyshape'],subject=plan['subject'])
    (d/(slug+'.metadata.json')).write_text(json.dumps(metadata,indent=2)+'\n')
    review=dict(native_size=48,enlarged_size=240,themes=['light','dark'],findings=finding,
                visually_accepted=status['status']=='valid',
                human_reference='icon_set/references/human_ref/full_body_ref.png' if i in (2,13,14,18) else None,
                human_gap='Not applicable: no detached human head/body figure.' if i in (2,13,14,18) else None)
    (d/'visual-review.json').write_text(json.dumps(review,indent=2)+'\n')
    required=[plan['python'],slug+'.svg',slug+'.metadata.json','reference.svg','reference.png','light-48.png','dark-48.png','light-240.png','dark-240.png','validation.txt','visual-review.json','plan.json']
    assert all((d/name).is_file() for name in required)
    record=dict(source_uuid=e['source_uuid'],source_path=e['reference_path'],reference_path=e['reference_path'],concept=e['concept'],icon_id=slug,author=AUTHOR,
                batch=35,position=i,keyshape=plan['keyshape'],keyshape_reason=WHY[plan['keyshape']],
                validation_status=status['status'],validation_errors=status['errors'],validation_warnings=status['warnings'],
                validation_findings=(d/'validation.txt').read_text(),visual_review=review,omissions=plan['omissions'],
                construction_references=plan['construction_reference'],artifacts=required,
                result_dir=str(d),attempt_complete=True)
    records.append(record)

# A native/enlarged overview is kept in the first result folder.
for start in (0,10):
    sheet=Image.new('RGB',(1200,600),'#e5e5e5');draw=ImageDraw.Draw(sheet)
    for j,r in enumerate(records[start:start+10]):
        d=Path(r['result_dir']);x=j%5*240;y=j//5*300
        for k,t in enumerate(('light','dark')):
            sheet.paste(Image.open(d/(t+'-240.png')).resize((120,120)),(x+k*120,y+20))
            sheet.paste(Image.open(d/(t+'-48.png')),(x+k*120+36,y+160))
        draw.text((x+5,y+220),f"{r['position']}. {r['concept']}",fill='black')
        draw.text((x+5,y+240),r['validation_status'],fill='black')
    sheet.save(ROOT/f'final-overview-{start}.png')

counts={k:sum(r['validation_status']==k for r in records) for k in ('valid','invalid','review')}
summary=['# Primitive make ray — batch 35 of 55','',f"All 19 inputs authored in requested order. {counts['valid']} valid, {counts['invalid']} invalid, {counts['review']} review. AUTHOR introduced as `gpt-6`.",'',
         'Every run contains the standalone Python original, source metadata, canonical SVG, input render, native and enlarged light/dark previews, validation and visual-review findings. Failed and rejected candidates are retained. No published, registry, gallery, queue or runtime-state writes were made.','',
         '| # | Input | Keyshape | Result | Artifacts |','|---|---|---|---|---|']
for r in records:
    d=Path(r['result_dir']).resolve()
    summary.append(f"| {r['position']} | {r['concept']} | {r['keyshape']} | {r['validation_status']} | [Folder]({d}) · [SVG]({d/(r['icon_id']+'.svg')}) |")
for r in records:
    summary += ['',f"## {r['position']}. {r['concept']}",'',r['visual_review']['findings'],'',
                f"Keyshape: {r['keyshape']}. {r['keyshape_reason']}",'',
                f"Construction: {r['construction_references']}",'',f"Omissions/reductions: {r['omissions']}",'',
                '```text',r['validation_findings'].rstrip(),'```']
(ROOT/'batch-report.md').write_text('\n'.join(summary)+'\n')
(ROOT/'batch-summary.json').write_text(json.dumps(dict(batch=35,count=19,counts=counts,results=records),indent=2)+'\n')

# Completion sentinels are written last, after all source/exports/review checks.
for r in records:
    d=Path(r['result_dir'])
    assert not (d/'result.json').exists()
    (d/'result.json').write_text(json.dumps(r,indent=2)+'\n')
print(json.dumps(dict(count=19,counts=counts,report=str(ROOT/'batch-report.md')),indent=2))
