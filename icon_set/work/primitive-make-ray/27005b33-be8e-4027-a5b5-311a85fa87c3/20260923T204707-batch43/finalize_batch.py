"""Finalize reviewed batch 43 artifacts and write completion records last."""
from pathlib import Path
import importlib.util, json, re
from PIL import Image, ImageDraw
SOURCE_ICON_ID='27005b33-be8e-4027-a5b5-311a85fa87c3'
SOURCE_PATH='icon_set/work/todo-references/signboard 1_27005b33-be8e-4027-a5b5-311a85fa87c3.svg'
AUTHOR='gpt-6'
ROOT=Path(__file__).parent
ENTRIES=json.loads((ROOT/'batch-inputs.json').read_text())
FINDINGS=[
 'Panel, two hangers and right-side post read cleanly in both themes. Repaired the post corner to a tangent quarter-circle. The offset panel and right support intentionally preserve the input asymmetry.',
 'Blank board, equal corner radii and centered upright retain the complete reference. Native light/dark views have clear negative space and balanced proportions.',
 'Blank board and centered post match this separately supplied reference. Equal radii, centered support and clear panel interior remain consistent in both themes.',
 'Wide short panel and centered stem preserve the reference proportions. The panel has continuous rounded corners and an open, uncluttered interior.',
 'Neutral torso, circular head, two checks and cross are all distinct at 48px. Head radius 6 and shoulder half-width 9 follow the shared human vocabulary. Head bottom y=18 and shoulder apex y=26 prove 8 centerline units, or exactly 4 visible units, on the x=15 axis. These are torso outlines, not stick-figure limbs.',
 'Woman silhouette and all three hierarchy nodes remain identifiable. Head radius 6, shoulder half-width 6 and dress half-width 9 retain human proportions. Head bottom y=18 to shoulder apex y=26 is exactly 8 centerline / 4 visible units on x=15. Node positions share one vertical series with 15-unit spacing. The composition intentionally places the hierarchy to the right.',
 'The device enclosure, plus control, round button, feet and primary Z remain recognizable. Removed only the smaller repeated Z, and enlarged the device interior. Both themes show separated controls; the very short feet are deliberate.',
 'The open circular rim, angled hands and primary Z read clearly. Removed the smaller repeated Z, keeping the sleep-clock identity and the intentionally open upper-right rim.',
 'The complete house, two wireless arcs and opposed chevrons are present, but spacing is unresolved. Wireless-inner/roof, roof/walls and both chevrons/walls fail MIC. Retained the defining two-arc wireless mark and opening arrows rather than remove them for a numeric pass.',
 'The sloped induction surface, two wireless arcs, three front sections and lower base remain present. The lower flange fills in at native size; base/front and signal-to-frame gaps fail MIC. This is a retained failed candidate, not visual approval.',
 'Refrigerator, freezer divider, paired handles, two signal arcs and offset phone remain recognizable, but the signal and phone overlap/crowd the appliance. Handle-to-wall, appliance-to-phone and wireless clearances fail; two curve warnings remain. The source arrangement is retained for review.',
 'Toast silhouette, rounded toaster and arc/point wireless mark remain readable. Removed the inner repeated arc and decorative bottom seam. Paired bread shoulders use smooth curves; signal and point have clear negative space in both themes.',
 'The open TV contour, centered pedestal, separate phone and wireless arc read at 48px. Kept the intentionally interrupted screen border around the phone; reduced the signal to one arc. Small TV-top adjustment removed the exact-clearance warning.',
 'Frame, header/footer, three panels, both navigation chevrons and pedestal are all present. Chevrons merge into the narrow center band at native size, matching the MIC failures against the header. Retained complete contents as an invalid candidate.',
 'Round watch and euro sign are recognizable, but upright strap openings are too thin visually and the euro bar is too close to the case. A diagonal alternate opens the straps but leaves only about 4 centerline units between euro-bar and case. Neither layout is accepted.',
 'Square watch and dollar sign retain their meanings. The upright strap loops close at native size and fail parallel spacing; dollar-stem also crowds the case. A diagonal alternate preserves open straps but the dollar-to-case gap still fails. Upright candidate retained as invalid.',
 'Square watch, pound hook, crossbar and baseline remain identifiable. Upright straps fail parallel spacing and pound-hook crowds the case. A diagonal alternate leaves the pound-stem too near the diamond case. Upright candidate retained as invalid.',
 'Phone, protruding banknote, four corner decorations and dollar mark are retained. The dense note loses interior clarity at native size. Banknote/footer, phone/glyph and paired corner gaps fail MIC. No claim of visual acceptance is made.',
 'The complete blank circular watch is diagonal so its strap openings remain visible. The face is a true radius-13 circle about (24,24), with exact integer 5-12-13 attachment nodes. Opposed straps share mirrored geometry, and both themes show clear openings. Rejected the upright version visually because its strap holes filled in despite numeric validity.',
 'This separately supplied blank circular watch uses the same fresh geometric construction: a radius-13 circular face and mirrored diagonal straps on SQUARE. The intentional rotation preserves the subject while opening strap clearances. The initial upright candidate is retained as rejected visual evidence.',
]
REASONS={
 'SQUARE':'Visible extremes (4,4)–(44,44), centerline extremes (6,6)–(42,42). This balances the complete composition; for blank watches the diagonal strap endpoints own these extremes.',
 'HRECT_L':'Visible extremes (2,6)–(46,42), centerline extremes (4,8)–(44,40). The wide composition benefits from the 40-unit horizontal centerline span.',
 'VRECT_L':'Visible extremes (6,2)–(42,46), centerline extremes (8,4)–(40,44). The tall overall composition uses the full vertical budget.',
}
records=[]
for i,(e,finding) in enumerate(zip(ENTRIES,FINDINGS),1):
    d=Path(e['result_dir']);slug=e['icon_id'];plan=json.loads((d/'plan.json').read_text());p=d/plan['python']
    source=p.read_text()
    source=re.sub(r'Symbol plan: .*?\nKeyshape: .*?\nReduction: .*?\n',f"Symbol plan: {plan['construction_reference']}\nKeyshape: {plan['keyshape']}. {REASONS[plan['keyshape']]}\nReduction: {plan['omissions']}\n",source,count=1)
    p.write_text(source)
    spec=importlib.util.spec_from_file_location('verify_'+e['source_uuid'].replace('-','_'),p)
    module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)
    assert module.SOURCE_ICON_ID==e['source_uuid'] and module.SOURCE_PATH==e['reference_path'] and module.AUTHOR==AUTHOR
    assert module.Drawing().to_svg()==(d/(slug+'.svg')).read_text()
    status=json.loads((d/'export-status.json').read_text());assert status['status'] in ('valid','invalid','review')
    if status['status']=='valid':assert status['errors']==0 and status['warnings']==0
    meta=dict(e,subject=plan['subject'],keyshape=plan['keyshape'])
    (d/(slug+'.metadata.json')).write_text(json.dumps(meta,indent=2)+'\n')
    human=None
    if i in (5,6):
        human=dict(references=['icon_set/references/human_ref/user.svg','icon_set/references/human_ref/full_body_ref.png'],head_center=[15,12],head_radius=6,head_bottom=18,shoulder_apex=[15,26],centerline_gap=8,visible_ink_gap=4,proof='All shoulder/body geometry is at y>=26; the head bottom at (15,18) aligns with the shoulder apex (15,26). The nearest gap is exactly 8 minus two 2-unit stroke radii.',figure_type='Detached head with outlined torso/dress, not a stick figure.')
    review=dict(native_size=48,enlarged_size=240,themes=['light','dark'],findings=finding,visually_accepted=status['status']=='valid',human_construction=human)
    (d/'visual-review.json').write_text(json.dumps(review,indent=2)+'\n')
    required=[plan['python'],slug+'.svg',slug+'.metadata.json','reference.svg','reference.png','light-48.png','dark-48.png','light-240.png','dark-240.png','validation.txt','visual-review.json','plan.json']
    assert all((d/name).is_file() for name in required)
    alternate=None
    if (d/'diagonal-attempt').exists():
        alt=d/'diagonal-attempt'
        alternate=dict(directory='diagonal-attempt',status=json.loads((alt/'export-status.json').read_text())['status'],validation=(alt/'validation.txt').read_text(),finding='The diagonal orientation gives room to the strap loops but does not leave legal currency-to-case clearance; the upright version is retained as the more faithful failed drawing.')
    record=dict(batch=43,position=i,source_uuid=e['source_uuid'],source_path=e['reference_path'],reference_path=e['reference_path'],concept=e['concept'],icon_id=slug,author=AUTHOR,
                keyshape=plan['keyshape'],keyshape_reason=REASONS[plan['keyshape']],subject=plan['subject'],construction_references=plan['construction_reference'],omissions=plan['omissions'],
                validation_status=status['status'],validation_errors=status['errors'],validation_warnings=status['warnings'],validation_findings=(d/'validation.txt').read_text(),visual_review=review,
                diagonal_attempt=alternate,artifacts=required,result_dir=str(d),attempt_complete=True)
    records.append(record)

for start in (0,10):
    sheet=Image.new('RGB',(1200,600),'#e5e5e5');draw=ImageDraw.Draw(sheet)
    for j,r in enumerate(records[start:start+10]):
        d=Path(r['result_dir']);x=j%5*240;y=j//5*300
        for k,t in enumerate(('light','dark')):
            sheet.paste(Image.open(d/(t+'-240.png')).resize((120,120)),(x+k*120,y+10))
            sheet.paste(Image.open(d/(t+'-48.png')),(x+k*120+36,y+150))
        draw.text((x+4,y+208),f"{r['position']}. {r['concept']}".replace(' ','\n',2),fill='black')
        draw.text((x+4,y+264),r['validation_status'],fill='black')
    sheet.save(ROOT/f'final-overview-{start}.png')

counts={k:sum(r['validation_status']==k for r in records) for k in ('valid','invalid','review')}
report=['# Primitive make ray — batch 43 of 55','',f"All 20 inputs processed in requested order: {counts['valid']} valid, {counts['invalid']} invalid, {counts['review']} review. Every valid result has zero warnings. AUTHOR is `gpt-6`.",'',
        'All outputs are standalone run folders. No published, registered icon, gallery, metadata catalog, queue or runtime-state updates were made. Invalid attempts and rejected alternatives remain available for review.','',
        '| # | Input | Source UUID | Keyshape | Validation | Artifacts |','|---|---|---|---|---|---|']
for r in records:
    d=Path(r['result_dir']).resolve()
    report.append(f"| {r['position']} | {r['concept']} | {r['source_uuid']} | {r['keyshape']} | {r['validation_status']} | [Folder]({d}) · [SVG]({d/(r['icon_id']+'.svg')}) |")
for r in records:
    report+=['',f"## {r['position']}. {r['concept']}",'',r['subject'],'',r['visual_review']['findings'],'',f"Keyshape: {r['keyshape']}. {r['keyshape_reason']}",'',f"Construction: {r['construction_references']}",'',f"Omissions/reductions: {r['omissions']}",'','```text',r['validation_findings'].rstrip(),'```']
    if r['diagonal_attempt']:
        report+=['','Diagonal fit attempt:','',r['diagonal_attempt']['finding'],'','```text',r['diagonal_attempt']['validation'].rstrip(),'```']
(ROOT/'batch-report.md').write_text('\n'.join(report)+'\n')
(ROOT/'batch-summary.json').write_text(json.dumps(dict(batch=43,count=20,counts=counts,results=records),indent=2)+'\n')

# Completion records follow all source, export, provenance and visual checks.
for r in records:
    d=Path(r['result_dir']);assert not (d/'result.json').exists()
    (d/'result.json').write_text(json.dumps(r,indent=2)+'\n')
print(json.dumps(dict(count=20,counts=counts,report=str(ROOT/'batch-report.md')),indent=2))
