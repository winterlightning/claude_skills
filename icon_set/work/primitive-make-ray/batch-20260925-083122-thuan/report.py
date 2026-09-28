from pathlib import Path
import json,html,os
root=Path('icon_set/work/primitive-make-ray/batch-20260925-083122-thuan');rows=json.loads((root/'manifest.json').read_text());claims=json.loads((root/'claims.json').read_text())
lines=['# Primitive fix batch — thuan-mac','', 'Request: 20 icons, offset 0, reason manual-fix-request. The claim command returned 8 icons; only those 8 were revised.','', 'All reviewer feedback was exactly “Manual fix request”; no more specific instructions accompanied these claims. The original reference and rejected drawing guided each revision.','', '8 revisions uploaded and reported done; all returned to Ready. 3 strict passes, 5 drawing-bound visual exceptions authorized by the user. Every exception preserves the 48×48 canvas and 4px strokes, with automatic findings retained.','', '[Visual review gallery](review.html)','']
parts=['<!doctype html><meta charset="utf-8"><title>8 icon revisions · thuan-mac</title><style>body{font:15px system-ui;margin:32px;background:#edf0f4;color:#15202b}article{background:white;padding:20px;margin:18px 0;border-radius:12px}img{vertical-align:middle;margin:12px}code{font-size:12px}a{color:#145bc0}</style><h1>8 icon revisions · thuan-mac</h1><p>20 requested; 8 claimed. All returned to Ready. Native light/dark and enlarged previews reviewed. Three strict passes; five drawing-specific exceptions with automatic findings retained.</p>']
for row,claim in zip(rows,claims):
 run=Path(row['run']).resolve();r=json.loads((run/'result.json').read_text());finish=json.loads((Path(claim)/'result.json').read_text());assert finish['outcome']=='done' and finish['review_status']=='ready'
 ident=r['icon_id'];svg=run/(ident+'.svg');val='Strict pass (valid, zero warnings)' if not r['exception'] else 'Pass with authorized exception; automatic '+r['automatic_status']
 lines += [f'## {row["index"]}. {row["key"]}','', 'Feedback: Manual fix request.', '', row['note'], '', f'Validation: **{val}**. Outcome: **done · Ready**.', '', f'[RESULT_DIR]({run}) · [SVG]({svg}) · [Validation]({run / "validation.txt"})', '', f'Keyshape: {r["keyshape"]}, selected for the subject’s natural orientation and proportions. Construction: {row["reference"]}', '', 'Reduction: '+r['omissions'], '']
 if r['exception']:lines += ['Exception: '+r['exception']['reason'],'']
 parts.append(f'<article><h2>{row["index"]}. {html.escape(row["key"])}</h2><p>{html.escape(row["note"])}</p>')
 for file in ['reference.png','light-192.png','dark-192.png','light-48.png','dark-48.png']:
  parts.append(f'<img src="{os.path.relpath(run/file,root.resolve())}" alt="{file}">')
 parts.append(f'<p>Validation: {html.escape(val)}. Outcome: done · Ready.</p>')
 if r['exception']:parts.append('<p>'+html.escape(r['exception']['reason'])+'</p>')
 parts.append(f'<p><a href="{os.path.relpath(svg,root.resolve())}">SVG</a> · <a href="{os.path.relpath(run,root.resolve())}/">Result directory</a> · <a href="{os.path.relpath(run/"validation.txt",root.resolve())}">Validation</a></p></article>')
(root/'REPORT.md').write_text('\n'.join(lines));(root/'review.html').write_text('\n'.join(parts));print('Verified 8 completed production finish records; report:',root/'REPORT.md')
