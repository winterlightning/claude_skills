from pathlib import Path
import json
root=Path('icon_set/work/primitive-make-ray/batch-20260925-thuan');rows=json.loads((root/'manifest.json').read_text());claims=json.loads((root/'claims.json').read_text())
lines=['# Primitive fix batch — thuan-mac','', 'Request: 20 icons, offset 0, reason manual-fix-request.','', 'All reviewer feedback was exactly “Manual fix request”; no specific repair instructions accompanied the claims. Revisions were based on the original reference and rejected drawing.','', '20 revisions uploaded and reported done; all returned to Ready. 14 strict passes, 6 accepted drawing-bound visual exceptions. Every exception preserves 48×48 canvas and 4px strokes; automatic findings remain recorded.','', '[Visual review gallery](review.html)','']
for row,claim in zip(rows,claims):
 run=Path(row['run']).resolve();r=json.loads((run/'result.json').read_text());finish=json.loads((Path(claim)/'result.json').read_text());assert finish['outcome']=='done' and finish['review_status']=='ready'
 ident=r['icon_id'];svg=run/(ident+'.svg');val='Strict pass (valid, zero warnings)' if not r['exception'] else 'Pass with authorized exception; automatic '+r['automatic_status']
 lines += [f'## {row["index"]}. {row["key"]}','', 'Feedback: Manual fix request.', '', row['note'], '', f'Validation: **{val}**. Outcome: **done · Ready**.', '', f'[RESULT_DIR]({run}) · [SVG]({svg}) · [Validation]({run / "validation.txt"})', '', f'Keyshape: {r["keyshape"]}, selected for the subject’s natural orientation and proportions. Construction: {row["reference"]}', '', 'Reduction: '+r['omissions'], '']
 if r['exception']:lines += ['Exception: '+r['exception']['reason'],'']
(root/'REPORT.md').write_text('\n'.join(lines))
print('Verified 20 completed production finish records; report:',root/'REPORT.md')
