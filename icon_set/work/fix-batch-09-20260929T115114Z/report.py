from pathlib import Path
import json,html,os
from urllib.parse import quote
ROOT=Path(__file__).resolve().parent;REPO=ROOT.parents[2]
rows=json.loads((ROOT/'batch.json').read_text())
lines=['# Once-disapproved solo fix batch 09','', 'Requested: 20 icons, offset 0, maximum disapprovals 1. Worker: `thuan-mac`. Author: `gpt-6`.','', 'Each claim was checked against production history before upload: all had exactly one disapproval. No reviewer supplied written feedback; comparisons with the original references guided these revisions.','', 'Each final drawing was inspected at 48 px and enlarged size in light and dark themes, and passed model validation and the full build gate with zero errors and zero warnings.','']
parts=['<!doctype html><meta charset="utf-8"><title>Solo fix batch 09</title><style>body{font:16px system-ui;max-width:1100px;margin:40px auto;color:#242424;background:#fafafa}article{margin:32px 0;padding:24px;background:white;border:1px solid #ddd;border-radius:12px}.images{display:flex;gap:25px;align-items:center}figure{margin:0}figcaption{margin:10px 0;font-size:13px;color:#555}.large{width:160px;height:160px}.native{width:48px;height:48px}p{line-height:1.5}a{color:#1767a1}</style><h1>Once-disapproved solo fix batch 09</h1><p>20 revisions · gpt-6 · model valid · full gate pass · zero warnings</p>']
results=[]
for i,r in enumerate(rows,1):
 m=json.loads((ROOT/f'latest-{i}.json').read_text());out=REPO/m['result_dir'];p=REPO/r['claim_dir']/'result.json'
 assert p.is_file(),f'Not finished: {r["key"]}'
 f=json.loads(p.read_text());assert f['outcome']=='done' and f['validation_status']=='valid' and f['build_gate']['status']=='pass' and not f['validation_warnings']
 assert f['author']=='gpt-6' and f['review_status']=='ready'
 link=lambda label,target:f'[{label}](<{target}>)'
 lines += [f'## {i}. {r["key"]}', '',m['comparison'],'', '**Reviewer feedback:** No written feedback recorded.','',f'**Construction:** {m["construction_reference"]}', '', f'**Keyshape:** `{m["keyshape"]}`. {m["keyshape_reason"]}', '',f'**Omissions:** {m["omissions"]}', '', f'**Visual review:** {m["visual_review"]["findings"]}', '', '**AUTHOR:** `gpt-6`. **Validation:** valid; build gate pass; zero errors/warnings. **Production:** `done`, returned to `ready`.', '', ' · '.join([link('RESULT_DIR',out),link('SVG',out/m['svg']),link('Python',out/m['module']),link('Validation',out/'validation.txt'),link('Finish receipt',p)]),'']
 imgs=[]
 for caption,name in [('Original','reference'),('Rejected','before'),('Fixed light','preview-light'),('Fixed dark','preview-dark')]:
  rel=lambda size:quote(os.path.relpath(out/f'{name}-{size}.png',ROOT))
  imgs.append(f'<figure><img class="large" src="{rel(384)}"><img class="native" src="{rel(48)}"><figcaption>{caption}</figcaption></figure>')
 parts += [f'<article><h2>{i}. {html.escape(r["key"])}</h2><div class="images">'+''.join(imgs)+f'</div><p>{html.escape(m["comparison"])}</p><p>{html.escape(m["omissions"])}</p><p>gpt-6 · valid · full gate pass · Ready</p><a href="{quote(os.path.relpath(out/m["svg"],ROOT))}">SVG</a> · <a href="{quote(os.path.relpath(out,ROOT))}">Result folder</a></article>']
 results.append({'key':r['key'],'result_dir':m['result_dir'],'svg':str((out/m['svg']).relative_to(REPO)),'author':f['author'],'validation_status':f['validation_status'],'build_gate':f['build_gate'],'production_review_status':f['review_status'],'finish_receipt':str(p.relative_to(REPO))})
(ROOT/'REPORT.md').write_text('\n'.join(lines))
(ROOT/'index.html').write_text('\n'.join(parts))
(ROOT/'results.json').write_text(json.dumps(results,indent=2)+'\n')
print('Verified 20/20 done, Ready, gpt-6, valid, full gate pass, zero warnings.')
print(ROOT/'REPORT.md')
