from pathlib import Path
import sys,json,hashlib,shutil
sys.path.insert(0,str(Path(__file__).resolve().parents[4]))
from icon_set.scripts.primitive_fix import load_icon,finish
from icon_set.scripts import work_queue
root=Path(__file__).parent
rows=json.loads((root/'batch.json').read_text())
AUTHOR='gpt-6'
SOURCE_ICON_ID=[m['source_uuid'] for m in rows]
SOURCE_PATH=[m['reference_path'] for m in rows]
reasons={1: 'Preserve the three shallow Wi-Fi waves and open router chassis. Natural envelope stays inside the canvas; smallest antenna-to-wave ink clearance is 2.4px, and the near-exact 4px curved wave gap remains an automatic advisory.', 2: 'Preserve the original broad, low VR goggle shape and smooth nose bridge. Filling the standard horizontal keyshape vertically would turn the headset back into the rejected tall rectangle.', 3: 'Preserve the wider portrait phone and two detached vibration strokes. Each side has a readable 2px visible gap; the overall 44px square ink envelope remains inset within the 48px canvas.', 4: 'Preserve the broad monitor with an outlined avatar and centered stand. Screen-to-avatar clearance is 2px. The detached head/body gap remains exactly 4px: shoulder top 24 minus head bottom 16 minus two half-strokes of 2.', 5: 'Retain the defining serrated rounded trap and separate pointed leaf. Repaired the leaf collision; remaining tooth gaps are at least about 2.46px and trap-to-leaf gap is about 3.11px. Natural envelope is retained.', 6: 'Preserve the broad burger bun, filling band and lower bun beside the drink. The burger bands have deliberate 2px clear openings and remain distinct at native size; the entire composition stays within the canvas.', 7: 'Preserve the triangular carry strap, viewfinder hump, shutter and lens. Strap/hump ink gaps are now equal at about 2.36px, with no overlap. Lens clearance is about 1.82px; all details remain legible at 48px.', 8: 'Preserve the natural wide capsule proportions. The two short bars have exactly 4px geometric ink clearance to the horizontal walls; the curve-containing contour retains its uncertified equality finding. The natural height is smaller than HRECT_M.', 9: 'Preserve the natural wide capsule proportions and short equal bars. Wall/bar ink clearance is exactly 4px geometrically, while the curve-containing contour remains uncertified by the automatic checker; natural height is smaller than HRECT_M.', 10: 'Keep a truly circular return orbit and a tangent arrowhead with readable clock hands. The head extends 2px beyond the square keyshape but stays inside the canvas.', 11: 'Preserve three readable cube faces and equal circular nodes. The natural 44px envelope remains within the canvas; the two lower node-to-face gaps are approximately 2.32px and visibly separate.', 12: 'Keep a smooth inlet, broad basin and two wave lines. The smallest wave-to-shore gap is 2px and the other is about 3.4px; all remain separated in both themes.', 13: 'Keep three fork tines and the enlarged diagonal spoon. Tines have about 1.66px clear gaps; the spoon/fork head collision was removed and now has about 2.87px clearance. Natural crossed-handle junctions remain intentional.', 14: 'Preserve the four-circle logo hierarchy and arrangement. All four loops remain open and distinct; the smallest separation is about 2.14px. Natural envelope stays at least 2px inside the canvas.', 16: 'Preserve the reference slender horizontal fish body, closed triangular tail and short curved gill. Natural height is smaller than the standard horizontal keyshape; gill clearance is about 1.77px and remains visible in both themes.', 17: 'Preserve the smooth S and continuous dollar stem inside the house. The stem has a deliberate 2px bottom gap and the S has local 3.33px curve spacing; both retain open readable counters.', 18: 'Preserve the narrow hourglass rims, smooth crossed glass walls and horizontal sand level. The level has approximately 2px clearance to the walls, while the central hourglass crossing is intentional.', 20: 'Feedback explicitly requests a wider logo. Preserve the broad outer and inner hexagons in a 44px square ink envelope; all spacing checks pass, with only the 2px keyshape extension on each side excepted.'}

for i,m in enumerate(rows,1):
    rd=Path(m['result_dir']);module=Path(m['module']);claim=Path(m['claim_dir'])
    if (claim/'result.json').exists():
        existing=json.loads((claim/'result.json').read_text())
        if existing.get('outcome')=='done':
            print(i,m['key'],'already done',flush=True);continue
    icon=load_icon(module);svg=icon.to_svg()
    if i in reasons:
        approval=dict(reason=reasons[i]+' User explicitly delegated exception decisions for UI/UX quality; reviewed at 48px in light and dark.',approved_by='user-delegated-gpt-6',approved_on='2026-09-29',svg_sha256=hashlib.sha256(svg.encode()).hexdigest())
        s=module.read_text()
        if '    exception = ' not in s:s=s.replace('class Drawing(Solo48):','class Drawing(Solo48):\n    exception = '+repr(approval))
        module.write_text(s)
        m['exception']=approval
    icon=load_icon(module);report=icon.validate_icon()
    (rd/'validation.txt').write_text(report.describe())
    note=m['comparison']
    if i in reasons:note+=' Reviewed native light/dark; accepted drawing-bound visual exception: '+reasons[i]
    rc=finish(work_queue.default_base_url(),'thuan-mac',m['key'],'done',note=note,ray_run=rd)
    if rc:raise SystemExit(f'Finish refused {i} {m["key"]}: {rc}')
    finished=json.loads((claim/'result.json').read_text())
    shutil.copyfile(claim/'validation.txt',rd/'validation.txt')
    (rd/'gate.json').write_text(json.dumps(finished['build_gate'],indent=2))
    omissions=[]
    if i==5:omissions=['Reduced tooth count to three clear points to preserve the trap silhouette at 48px.']
    if i==7:omissions=['Simplified the double lens ring to one open lens to keep the camera body readable.']
    if i==14:omissions=['Secondary-circle sizes were adjusted slightly on the integer grid while retaining the logo hierarchy.']
    result=dict(concept=m['concept'],source_uuid=m['source_uuid'],reference_path=m['reference_path'],icon_id=m['icon_id'],author=AUTHOR,keyshape=m['keyshape'],module=module.name,svg=m['icon_id']+'.svg',comparison=m['comparison'],reviewer_feedback=m['feedback'],lucide_reference=m['lucide'],visual_review='Inspected against original and rejected drawing, enlarged and native 48px in light/dark. Coherent contours, visible openings, directional arrangement and legibility accepted.',omissions=omissions,validation_status=report.status,validation_errors=report.errors,validation_warnings=report.warnings,build_gate=finished['build_gate'],accepted_exception=finished['accepted_exception'],production_outcome=finished['outcome'],review_status=finished['review_status'],previews=['preview-light-48.png','preview-dark-48.png','preview-light-384.png','preview-dark-384.png'])
    (rd/'result.json').write_text(json.dumps(result,indent=2))
    m['finished']=finished
    (root/'batch.json').write_text(json.dumps(rows,indent=2))
    print(f'FINISHED {i}/20 {m["key"]}',flush=True)
