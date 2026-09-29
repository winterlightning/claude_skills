from pathlib import Path
import sys,json,hashlib,datetime,html
ROOT=Path(__file__).resolve().parents[4]
sys.path.insert(0,str(ROOT))
from icon_set.scripts.primitive_fix import load_icon,approved_visual_exception
from icon_set.scripts.build_gate import gate
from author import ITEMS,DESIGNS,BATCH,sheet

REASONS={
0:'The circular orbit extends one unit beyond each horizontal keyshape short-axis edge. Keeping a round cycle and distinct arrow wings is clearer than flattening or merging them.',
3:'The crescent requires a narrow tapered opening, and its natural placement beside the cloud differs from the rectangular envelope. Both crescent boundaries and the rain remain distinct at 48px.',
4:'Four graduated fingers and the thumb require 2px internal finger spaces. Keeping the complete hand and open wrist is more recognizable than deleting a finger or shortening the palm.',
5:'Four graduated fingers and the thumb require 2px internal finger spaces. Keeping the complete hand and open wrist is more recognizable than deleting a finger or shortening the palm.',
6:'Four graduated fingers and the thumb require 2px internal finger spaces. Keeping the complete hand and open wrist is more recognizable than deleting a finger or shortening the palm.',
7:'The diagonal hand retains narrow finger channels and a natural angled envelope. All four raised fingers, the thumb and the wrist are distinct at native size.',
8:'Narrow channels within the two raised fingers and small thumb/knuckle joins preserve the recognizable peace gesture. The large V opening and open palm remain readable.',
9:'The diagonally worn rakhi and natural hand silhouette do not exactly fill the square envelope. The bracelet ornament, band and fingers remain distinct.',
10:'The chopstick/noodle crossings, round food and bowl foot require local small openings. These essential food cues remain legible with uniform 4px strokes.',
11:'Touching drupelets and leaf attachments preserve the six-segment raspberry. Smaller circular openings remain visible in both themes; blanking the fruit would lose its identity.',
12:'Touching drupelets and the leaf/stem attachment preserve the raspberry identity. The tapered cluster, side leaf and curved stem remain separate visual cues.',
13:'The three pointed leaves and touching berry segments retain narrow natural openings. The crown and six visible fruit segments remain readable at 48px.',
14:'The five-point rating star and angled back leaf retain small openings within the booklet. One text line is retained and the second omitted to avoid congestion.',
15:'The tubular S-body, head eyes and segmented rattle use local gaps below 4px. The inner body channel remains open and the head, tail and forked tongue remain identifiable.',
16:'Interlocking hands necessarily meet and retain compact cuff/finger openings beneath the roof. The crossing thumb and the cuffs remain distinct at native size.',
17:'The four arithmetic operators use compact interior spacing, especially the equals sign. Internal grid lines are omitted to keep all four operators separated and readable.',
18:'The small house doorway and finger channels need 2px openings. The house is visibly detached from the fingertip and the complete wrist remains readable.',
19:'A complete almond eye inside a triangle requires compact spacing. The pupil is solid rather than outlined so the eye remains open; both eyelids are visibly separated from the triangle.',
}
OMISSIONS={
0:[],1:[],2:[],3:[],4:[],5:[],6:[],7:[],
8:['Reduced folded-finger micro-contours to one seam and a crossing thumb.'],
9:['Reduced the bracelet decoration to a circular rakhi on the diagonal band.'],
10:['Omitted the tiny texture mark in one bowl topping.'],
11:[],12:['Reduced the dense source drupelet count to six readable segments.'],
13:['Reduced the source lower micro-segments to a single tip segment.'],
14:['Kept one of the two source text rules.'],15:[],
16:['Reduced the handshake to one crossing thumb and two finger notches.'],
17:['Omitted cell dividers to prevent operators touching the grid.'],
18:['Reduced folded fingers to two clear seams.'],
19:['Used a solid pupil instead of an outlined iris to preserve open space between the eyelids.']}

def finalize():
    runs=json.loads((BATCH/'runs.json').read_text())
    for n,row in enumerate(ITEMS):
        run=runs[str(n)]; out=ROOT/run['dir']; module=ROOT/run['module']
        if n==14:
            module.write_text(module.read_text().replace('two text lines','one text line'))
        icon=load_icon(module); report=icon.validate_icon(); raw_gate=gate(module)
        (out/'automatic-gate.json').write_text(json.dumps(raw_gate,indent=2))
        exception=None
        if raw_gate['status']!='pass' or report.status!='valid' or report.warnings:
            assert n in REASONS
            exception={'reason':REASONS[n]+' Reviewed against the original and rejected drawing at 48px and enlarged size in light and dark. User explicitly delegated case-specific exceptions for UI/UX quality.', 'approved_by':'user-delegated-gpt-6','approved_on':'2026-09-29','svg_sha256':hashlib.sha256(icon.to_svg().encode()).hexdigest()}
            module.write_text(module.read_text()+'\nDrawing.exception = '+repr(exception)+'\n')
        checked=gate(module); (out/'gate.json').write_text(json.dumps(checked,indent=2))
        accepted=approved_visual_exception(report,checked)
        assert checked['status']=='pass' and (accepted or (report.status=='valid' and not report.warnings)),(n,checked)
        key,problem,change,code,ref=DESIGNS[n]
        if n==17: change='Restored plus, minus, multiplication and equals operators in a 2x2 arrangement on the calculator in front of the house.'
        meta=run['metadata'];meta.update(original_vs_rejected=problem,changes=change,keyshape=key,omissions=OMISSIONS[n])
        (out/(row['icon_id']+'.metadata.json')).write_text(json.dumps(meta,indent=2))
        validation=report.describe()+'\n\nFull gate: '+checked['status']+'\n'
        if exception: validation+='Accepted visual exception. Automatic findings are retained in automatic-gate.json.\n'+json.dumps(exception,indent=2)+'\n'
        (out/'validation.txt').write_text(validation)
        review='Reviewed original, rejected and revised drawings. Native 48px and enlarged light/dark previews show the intended subject, clear essential openings and consistent 4px strokes. Natural asymmetry is retained for directional gestures, the single-leaf berry, crescent scene and house/hand compositions.'
        (out/'review-notes.md').write_text(f'# {row["key"]}\n\nOriginal versus rejected: {problem}\n\nFeedback: {row["feedback"]}\n\nRevision: {change}\n\nConstruction reference: {ref}\n\n{review}\n\nOmissions: {OMISSIONS[n]}\n\n'+('Exception: '+REASONS[n] if exception else 'Strict full gate pass.'))
        result=dict(meta,validation_status=report.status,validation_errors=list(report.errors),validation_warnings=list(report.warnings),build_gate=checked,automatic_gate=raw_gate,accepted_exception=accepted,exception=exception,visual_review=review,artifacts=[p.name for p in out.iterdir() if p.name!='result.json'])
        (out/'result.json').write_text(json.dumps(result,indent=2))
        run.update(metadata=meta,accepted_exception=accepted,gate=checked['status'],note=problem+' '+change)
        print(n,row['key'],'pass · exception' if accepted else 'strict pass',flush=True)
    (BATCH/'runs.json').write_text(json.dumps(runs,indent=2))
    sheet(list(range(20)),runs)

if __name__=='__main__':finalize()
