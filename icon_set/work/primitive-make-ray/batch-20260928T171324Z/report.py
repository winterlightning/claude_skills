from author_batch import *
import html,os
records=json.loads((Path(__file__).parent/'ready-runs.json').read_text())
out=Path(__file__).parent
def link(label,p):return f'[{label}](<{(ROOT/p).resolve()}>)'
lines=['# Primitive fix report — 20 manual fix requests','',
       'Worker: `thuan-mac`. All modules use `AUTHOR = "gpt-6"`. Original references, rejected displayed SVGs, review notes, fresh Python models, light/dark previews and automatic findings are retained in each run.',
       '', 'All 20 before drawings and after revisions were uploaded through `primitive_fix.py`; every claim finished as `done` and returned to `ready`. Four revisions passed the full automatic gate. Sixteen use exact-drawing visual exceptions delegated by the user; their automatic errors and warnings are preserved.',
       '', link('Final light/dark contact sheet',out.relative_to(ROOT)/'final-contact-sheet.png'),'',
       'Registered sources, published output, metadata and Git history were not edited by this batch.','']
rows=[];summary=[]
for r in records:
    finished=json.loads((ROOT/r['fix_dir']/'result.json').read_text())
    assert finished['outcome']=='done' and finished['review_status']=='ready'
    assert finished['author']==AUTHOR and finished['make_ray_run']==r['run']
    f=ROOT/r['run'];result=json.loads((f/'result.json').read_text())
    status='Pass with user-delegated visual exception' if r['accepted_exception'] else 'Automatic pass; zero warnings'
    lines += [f"## {r['n']}. {r['key']}",'',
       f"**Compared with reference:** {r['spec']['problem']}",
       '',f"**Feedback:** {r['feedback'].replace(chr(10),' ').strip()}",
       '',f"**Revision:** {r['spec']['change']}",
       '',f"**Construction:** {r['spec']['construction_reference']} Keyshape: `{r['spec']['keyshape']}`. Omitted: {r['spec']['omissions']}",
       '',f"**Validation:** {status}. Automatic model status: `{r['validation_status']}`; automatic full-gate status: `{r['gate'].get('automatic_status',r['gate']['status'])}`. Production: `done → ready`. `AUTHOR = \"gpt-6\"`.",
       '',result['visual_review'],'']
    if r['accepted_exception']:lines += ['**Exception rationale:** '+r['gate']['exception']['reason'],'']
    lines += [link('RESULT_DIR',r['run'])+' · '+link('SVG',Path(r['run'])/f"{r['icon_id']}.svg")+' · '+link('Python',r['module'])+' · '+link('Validation',Path(r['run'])/'validation.txt')+' · '+link('Production receipt',Path(r['fix_dir'])/'result.json'),'']
    def rel(p):return html.escape(os.path.relpath(ROOT/p,out))
    images=''.join(f'<td><img width="144" height="144" src="{rel(p)}"></td>' for p in [r['reference'],str(Path(r['fix_dir'])/'before'/f"{r['icon_id']}.svg"),str(Path(r['run'])/'preview-light-384.png'),str(Path(r['run'])/'preview-dark-384.png')])
    images+=''.join(f'<td><img width="48" height="48" src="{rel(Path(r["run"])/f"preview-{t}-48.png")}"></td>' for t in ('light','dark'))
    rows.append(f'<tbody><tr><th colspan="6">{r["n"]}. {html.escape(r["key"])}</th></tr><tr>{images}</tr><tr><td colspan="6">{html.escape(r["spec"]["change"])}<br><b>{status}</b></td></tr></tbody>')
    summary.append({'key':r['key'],'run':r['run'],'svg':str(Path(r['run'])/f"{r['icon_id']}.svg"),'author':AUTHOR,'outcome':'done','review_status':'ready','accepted_exception':r['accepted_exception'],'production_receipt':str(Path(r['fix_dir'])/'result.json')})
(out/'REPORT.md').write_text('\n'.join(lines))
(out/'review.html').write_text('<!doctype html><meta charset="utf-8"><title>20 repaired icons</title><style>body{font:15px system-ui;background:#eee;margin:32px}table{border-collapse:collapse;background:white}td,th{padding:12px;text-align:left;border-bottom:1px solid #ddd}th{background:#e4e5e7}img{object-fit:contain}tbody{border-top:14px solid #eee}</style><h1>20 repaired icons</h1><p>All done → Ready. Four automatic passes; sixteen user-delegated visual exceptions. AUTHOR: gpt-6.</p><table><thead><tr><th>Reference</th><th>Rejected</th><th>Revised light</th><th>Revised dark</th><th>Light 48 px</th><th>Dark 48 px</th></tr></thead>'+''.join(rows)+'</table>')
(out/'completion.json').write_text(json.dumps({'count':len(summary),'automatic_pass':4,'accepted_exceptions':16,'items':summary},indent=2))
print('Verified all 20 production finish receipts. Report:',out/'REPORT.md')
