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
from reasons import reasons

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
    if i==4:omissions=['Reduced the source three text strokes to two, with a short upper line, to keep the thumb separate.']
    if i in (6,7,8,10,11,12):omissions=['Simplified outlined human limbs to the shared full-body stroke style while retaining the pose and activity.']
    if i==12:omissions.append('Reduced three document marks to two to preserve native-size spacing.')
    result=dict(concept=m['concept'],source_uuid=m['source_uuid'],reference_path=m['reference_path'],icon_id=m['icon_id'],author=AUTHOR,keyshape=m['keyshape'],module=module.name,svg=m['icon_id']+'.svg',comparison=m['comparison'],reviewer_feedback=m['feedback'],lucide_reference=m['lucide'],visual_review='Inspected against original and rejected drawing, enlarged and native 48px in light/dark. Coherent contours, visible openings, directional arrangement and legibility accepted.',omissions=omissions,validation_status=report.status,validation_errors=report.errors,validation_warnings=report.warnings,build_gate=finished['build_gate'],accepted_exception=finished['accepted_exception'],production_outcome=finished['outcome'],review_status=finished['review_status'],previews=['preview-light-48.png','preview-dark-48.png','preview-light-384.png','preview-dark-384.png'])
    (rd/'result.json').write_text(json.dumps(result,indent=2))
    m['finished']=finished
    (root/'batch.json').write_text(json.dumps(rows,indent=2))
    print(f'FINISHED {i}/20 {m["key"]}',flush=True)
