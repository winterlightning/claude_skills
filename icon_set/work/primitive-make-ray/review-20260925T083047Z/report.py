"""Write a reviewable batch index, including production outcome for every claim."""
import json,ast,html
from pathlib import Path
HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[3]
rows=json.loads((HERE/'batch.json').read_text())
def link(p,label):return f'[{label}](<{(ROOT/p).resolve()}>)'
done=sum(r.get('production_outcome')=='done' for r in rows)
lines=['# Primitive fix batch — thuan-mac','',
       'Requested: 20 icons, offset 0, reason `manual-fix-request`. Claimed: 20.',
       f'Production: **{done} done**, **{20-done} blocked by concurrent reviewer approvals**. The approved production drawings were preserved.',
       'Local validation: **12 strict passes**, **8 accepted exact-SVG visual exceptions**. Automatic errors and warnings remain in each run.',
       'All feedback was exactly “Manual fix request”; there were no more specific reviewer instructions.',
       'Every icon received a fresh standalone `primitive-make-ray` run, visual review at 48px in light and dark, and a `primitive-fix-thuan finish` call. The production API refused attempts to finish superseded claims; those are not reported as done or cannot-fix.',
       '',link(HERE.relative_to(ROOT)/'final-before-after.png','Before / after comparison sheet'),'',
       '| Icon key | RESULT_DIR | SVG | Validation | Production outcome |',
       '|---|---|---|---|---|']
for r in rows:
    ident=r['key'].split('/')[1]
    val='Pass · exception (automatic '+r['automatic_status']+')' if r['exception'] else 'Strict pass'
    lines.append(f'| `{r["key"]}` | {link(Path(r["run"]),"run")} | {link(Path(r["run"])/(ident+".svg"),"SVG")} | {val} | {r["production_outcome"]} |')
lines+=['','## Revision notes','']
for r in rows:
    doc=ast.get_docstring(ast.parse((ROOT/r['module']).read_text())).split('\n')[0]
    lines += [f'### {r["key"]}','',doc,
              f'Keyshape: `{r["keyshape"]}`, chosen for the subject’s orientation and outline. '+('The narrow tie intentionally retains a smaller horizontal envelope.' if 'necktie' in r['key'] else ''),
              'Construction reference: '+r['construction_reference'],
              'Omissions: '+('; '.join(r['omissions']) if r['omissions'] else 'none beyond stroke-level simplification.'),
              'Visual review: native 48px and enlarged light/dark previews; coherent contour flow and legible negative space.',
              'Exception: '+(r['exception']['reason'] if r['exception'] else 'none.'),
              'Validation: '+link(Path(r['run'])/'validation.txt','automatic and effective findings')+'.',
              'Production: '+r['production_outcome']+'.',
              link(Path(r['fix'])/('result.json' if r['production_outcome']=='done' else 'production-blocked.json'),'production response'), '']
(HERE/'REPORT.md').write_text('\n'.join(lines)+'\n')
parts=['<!doctype html><meta charset="utf-8"><title>Primitive fix batch</title><style>body{font:15px system-ui;margin:32px;background:#eee;color:#222}article{background:white;padding:20px;margin:16px 0;border-radius:12px}section{display:flex;gap:18px;align-items:center}img{width:144px;height:144px;object-fit:contain}img.native{width:48px;height:48px}code{font-size:14px}a{color:#1453ad}h2{font-size:18px}</style>',f'<h1>{done} uploaded; {20-done} concurrent approvals preserved</h1><p>20 locally reviewed revisions: 12 strict passes, 8 drawing-bound visual exceptions.</p><p><a href="REPORT.md">Full report and artifacts</a></p>']
for r in rows:
    run=ROOT/r['run'];fix=ROOT/r['fix'];ident=r['key'].split('/')[1]
    parts.append('<article><h2>'+html.escape(r['key'])+'</h2><p>'+html.escape(r['production_outcome'])+' · '+('visual exception' if r['exception'] else 'strict pass')+'</p><section>')
    for label,file in [('Reference','reference.png'),('Before','before.png'),('After light','preview-light-384.png'),('After dark','preview-dark-384.png')]:
        parts.append(f'<figure><img src="{html.escape(str(run/file))}"><figcaption>{label}</figcaption></figure>')
    parts.append(f'<img class="native" src="{run}/preview-light-48.png"><img class="native" src="{run}/preview-dark-48.png"></section>')
    parts.append(f'<p><a href="{run}">RESULT_DIR</a> · <a href="{run}/{ident}.svg">SVG</a> · <a href="{run}/validation.txt">Validation</a></p></article>')
(HERE/'index.html').write_text('\n'.join(parts))
print('Report:',HERE/'REPORT.md')
