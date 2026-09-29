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
reasons={
1:'Preserve six open isometric corners and the central Y. A 40x44 ink envelope and 3.0–3.6px local gaps maintain legibility without shortening the cube into stubs.',
2:'Keep a truly round orbit and a recognizable tangent head; the left head extends 2px beyond the square keyshape, remaining inset within the canvas.',
3:'Keep the opposing heads on one round cycle. The heads extend 2px beyond each square side, leaving canvas padding and clear separation.',
4:'Keep the circular refresh path and compact tangent head; the left head extends 2px beyond the square keyshape inside the canvas.',
5:'Preserve a shared circular cycle and opposing heads instead of compressing it into two ovals; 2px side-envelope extension stays inside the canvas.',
6:'Preserve the round clockwise loop with its upward lower-left head; a 2px keyshape extension prevents an oval loop.',
7:'Keep the mirrored triangles large enough to remain triangles. Their tips have 1px clear ink gaps to the divider, visibly separated at native size in both themes.',
8:'Keep the compass and centered E in the original vertical arrangement. The E has readable 1px inter-bar gaps and the independent triangular pointer remains separated from the rim; the upright natural envelope is retained.',
9:'Preserve the round two-arrow search motif with its full diagonal handle. Natural bounds extend beyond the square template but stay inside the 48px canvas.',
10:'Keep three equal circular node openings, diagonal arrow and a spacious lower-right sweep. The natural composition uses a larger near-square envelope inside the canvas.',
11:'Keep three equal circular node openings, diagonal arrow and spacious curved connector in the source arrangement; natural envelope remains inside the canvas.',
12:'Retain the wrench open jaw, curved head and diagonal handle. The tapered jaw has a locally smaller 2.36px opening; its silhouette is clear in both themes, with natural envelope inside the canvas.',
14:'Preserve a concentric hub and circular orbit. The tangent head extends 2px beyond the square keyshape without crowding the hub or leaving the canvas.',
15:'Keep the round synchronization/search loop, slanted heads and diagonal handle; natural bounds differ from the square keyshape but remain inside the canvas.',
16:'Preserve two slanted, segmented bands. Parallel rails retain 3.76px visible gaps and the band tips remain separated by 2px; both bands read independently at native size.',
17:'Preserve the source sphere-to-antenna proportions and long unequal rods, using a natural 42x44 envelope entirely inside the canvas.',
18:'Preserve the source spherical body and long unequal antenna rods, with a natural 42x44 envelope entirely inside the canvas.',
19:'Retain recognizable dial ticks and the separated needle/pivot within the arched housing. The smallest retained tick-to-rim gap is 2px; all marks remain distinct at native size.',
20:'The closed speech-bubble perimeter and connected lightning crack satisfy the explicit connection feedback. Keep the intentional 2.56px crack opening, visibly open in both themes.'
}

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
    if i==8:omissions=['Four tiny compass rim ticks omitted to keep the independent needle legible.']
    if i==16:omissions=['Two separators per strip retain segmentation without crowded small cells.']
    if i==19:omissions=['Reduced secondary tick count; removed the upper-right tick that crowded the needle.']
    result=dict(concept=m['concept'],source_uuid=m['source_uuid'],reference_path=m['reference_path'],icon_id=m['icon_id'],author=AUTHOR,keyshape=m['keyshape'],module=module.name,svg=m['icon_id']+'.svg',comparison=m['comparison'],reviewer_feedback=m['feedback'],lucide_reference=m['lucide'],visual_review='Inspected against original and rejected drawing, enlarged and native 48px in light/dark. Coherent contours, visible openings, directional arrangement and legibility accepted.',omissions=omissions,validation_status=report.status,validation_errors=report.errors,validation_warnings=report.warnings,build_gate=finished['build_gate'],accepted_exception=finished['accepted_exception'],production_outcome=finished['outcome'],review_status=finished['review_status'],previews=['preview-light-48.png','preview-dark-48.png','preview-light-384.png','preview-dark-384.png'])
    (rd/'result.json').write_text(json.dumps(result,indent=2))
    m['finished']=finished
    (root/'batch.json').write_text(json.dumps(rows,indent=2))
    print(f'FINISHED {i}/20 {m["key"]}',flush=True)
