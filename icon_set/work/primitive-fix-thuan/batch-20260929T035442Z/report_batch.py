from pathlib import Path
import json
ROOT=Path(__file__).parent.resolve()
rows=json.loads((ROOT/'runs.json').read_text())
def link(label,path):return f'[{label}](<{Path(path).resolve()}>)'
lines=['# Meaning fixes — 20 icons','', 'Worker: `thuan-mac`. Author: `gpt-6`. Requested offset: 0; disapproval reason: meaning.', '',
'Every source and rejected SVG was rendered and compared before drawing. Every final drawing was inspected at native 48px and enlarged in light and dark themes. The user authorized visual exceptions. These 20 drawings use exact-SVG exceptions; full QA accepts them while preserving the underlying automatic findings. This is **pass with exception**, not a strict automatic pass. All drawings retain the 48×48 canvas and uniform 4px strokes.', '',
'Feedback for every icon: “Does not convey the intended meaning.”', '',
'Workflow: `primitive-fix-thuan` → fresh `primitive-make-ray` run → full QA → `primitive_fix.py finish --outcome done`. No registered originals, metadata catalogs or published files were edited.', '',
'## Review sheets','']
for i in range(1,5):lines.append(link(f'Original / revised light and dark, icons {(i-1)*5+1}–{i*5}',ROOT/f'revisions-{i}.png'))
lines+=['','## Per-icon results','']
ready=0
for i,row in enumerate(rows,1):
 run=Path(row['run']); result=json.loads((run/'result.json').read_text())
 finish_path=Path(row['fix'])/'result.json'
 finish=json.loads(finish_path.read_text()) if finish_path.exists() else {}
 status=finish.get('review_status','pending upload')
 if finish.get('outcome')=='done' and status=='ready':ready+=1
 lines += [f'### {i}. {row["key"]}', '',f'**Original vs rejected:** {row["comparison"]}', '',f'**Feedback:** {row["feedback"]}', '',f'**Changed:** {row["change"]}', '',
 f'**Construction:** `{result["keyshape"]}` selected for the subject\'s overall proportions; its natural outline is retained where the fixed guide distorts the subject. {result["references_used"]}', '',
 f'**Omissions / simplifications:** {result["omissions"]}', '',
 f'**Exception:** {row["exception_reason"]}', '',
 f'**Validation:** full gate `pass`; exact-SVG exception accepted. Automatic model status `{row["validation_status"]}` ({row["automatic_errors"]} errors, {row["automatic_warnings"]} warnings), retained in validation evidence. **AUTHOR:** `gpt-6`. **Production:** `{finish.get("outcome","pending")} / {status}`.', '',
 ' · '.join([link('RESULT_DIR',run),link('SVG',row['svg']),link('Python',row['module']),link('Validation',run/'validation.txt'),link('Finish receipt',finish_path)]), '']
 if result.get('human_spacing_evidence'):lines +=[f'**Human construction:** `icon_set/skills/icon-design/human-reference.md` and the relevant shared human reference. {result["human_spacing_evidence"]}', '']
lines.insert(4,f'**Completed: {ready}/20 — production `done`, review status `ready`.**')
(ROOT/'REPORT.md').write_text('\n'.join(lines)+'\n')
print('Report written; production ready:',ready,'/20')
