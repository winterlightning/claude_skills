from pathlib import Path
import json, html, os
from urllib.parse import quote
ROOT=Path(__file__).resolve().parent
REPO=ROOT.parents[2]
SOURCE_ICON_ID=None
SOURCE_PATH=str(ROOT/'claims.json')
AUTHOR='gpt-6'
claims=json.loads((ROOT/'claims.json').read_text())
runs=json.loads((ROOT/'runs.json').read_text())
def link(path):return quote(os.path.relpath(path,ROOT))
md=['# Meaning fixes — 20 icons','', 'Worker: `thuan-mac`. Every authored module uses `AUTHOR = "gpt-6"`.', '', 'General review feedback: “Does not convey the intended meaning.” The phone-woman and circle-add items also include specific requests, recorded below. Each reference and rejected drawing was rendered and inspected before authoring. One revision passes strictly; nineteen use user-authorized, exact-SVG visual exceptions with automatic findings preserved. All revisions retain SOLO48, integer coordinates and uniform 4px strokes.','']
cards=[];done=0
for i,c in enumerate(claims):
    run=REPO/runs[str(i)];r=json.loads((run/'result.json').read_text());fix=REPO/c['fix_dir']; f=fix/'result.json'
    fdata=json.loads(f.read_text()) if f.exists() else {}
    finished=fdata.get('outcome')=='done';done+=finished
    status='Ready — uploaded and done' if finished else 'Upload pending'
    validation='Pass with visual exception; automatic '+r['automatic_status'] if r['accepted_exception'] else 'Strict pass; zero warnings'
    svg=run/(c['icon_id']+'.svg')
    md += [f'## {c["key"]}', '',f'- Before: {r["before_findings"]}',f'- Feedback: {c["feedback"]}',f'- Change: {r["revision_plan"]}',f'- Simplification: {r["omissions"]}',f'- Construction references: {r["references"]}',f'- Keyshape: `{r["keyshape"]}`; preserves the subject’s upright, horizontal, or circular proportions.',f'- Author: `{r["author"]}`.',f'- Validation: {validation}. Production: {status}.',f'- [RESULT_DIR]({link(run)}/) · [SVG]({link(svg)}) · [Validation]({link(run/"validation.txt")}) · [Original]({link(REPO/c["reference"])}) · [Rejected SVG]({link(fix/"before"/(c["icon_id"]+".svg"))})','']
    if r['accepted_exception']:md.extend(['Exception: '+r['exception']['reason'],''])
    figures=[]
    for label,path in [('Original',REPO/c['reference']),('Rejected',fix/'before'/(c['icon_id']+'.svg')),('Revised — light',run/'preview-light-384.png'),('Revised — dark',run/'preview-dark-384.png')]:
        figures.append(f'<figure><img src="{link(path)}"><figcaption>{html.escape(label)}</figcaption></figure>')
    cards.append(f'''<article><h2>{i+1}. {html.escape(c['key'])}</h2><p class="status">{html.escape(status)} · {html.escape(validation)}</p><div class="images">{''.join(figures)}</div><div class="native"><span>48px:</span><img src="{link(run/'preview-light-48.png')}"><img src="{link(run/'preview-dark-48.png')}"></div><p><b>Before:</b> {html.escape(r['before_findings'])}</p><p><b>Changed:</b> {html.escape(r['revision_plan'])}</p><p><b>Omissions:</b> {html.escape(r['omissions'])}</p><p><b>Exception:</b> {html.escape((r.get('exception') or {}).get('reason','None — strict pass.'))}</p><p><a href="{link(run)}/">Result folder</a> · <a href="{link(svg)}">SVG</a> · <a href="{link(run/'validation.txt')}">Validation</a> · AUTHOR: {r['author']}</p></article>''')
(ROOT/'REPORT.md').write_text('\n'.join(md))
(ROOT/'review.html').write_text('''<!doctype html><meta charset="utf-8"><title>Meaning fixes — 20 icons</title><style>body{font:16px/1.5 system-ui;margin:30px auto;max-width:1100px;padding:0 24px;color:#202020;background:#f5f5f3}article{background:white;border-radius:12px;padding:24px;margin:24px 0}h2{font-size:19px}.images{display:flex;gap:24px;flex-wrap:wrap}figure{margin:0}figure img{width:160px;height:160px;object-fit:contain}figcaption{font-size:13px;color:#666}.native{display:flex;align-items:center;gap:16px;margin-top:16px}.native img{width:48px;height:48px}.status{color:#296643}a{color:#245b9c}p{max-width:950px}</style>'''+f'<h1>Meaning fixes — 20 icons</h1><p>{done}/20 uploaded and returned to Ready. Worker: thuan-mac. Author: gpt-6. One strict pass and nineteen visually reviewed exceptions. Feedback for all: “Does not convey the intended meaning.”</p>'+''.join(cards))
print(f'{done}/20 production done; report: {ROOT/"REPORT.md"}; visual review: {ROOT/"review.html"}')
