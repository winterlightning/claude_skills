from pathlib import Path
import json,os,html
from urllib.parse import quote
B=Path(__file__).parent
ROOT=B.resolve().parents[3]
rows=json.loads((B/'items.json').read_text())
runs=json.loads((B/'runs.json').read_text())
def link(label,path):return f'[{label}]({Path(path).resolve()})'
def url(path):return quote(os.path.relpath(path,B))
md=['# Meaning fixes — 20 icons', '', 'Worker: `thuan-mac`. Model author in all 20 modules: `gpt-6`.', '', 'All 20 were claimed for meaning review, compared with their originals and rejected drawings, revised, reviewed at 48px and enlarged in light/dark themes, and finished through the production queue. All returned to Ready.', '', 'Validation: **2 strict passes; 18 pass with user-authorized visual exceptions**. The automatic errors and warnings are preserved for every exception and must not be mistaken for strict passes.', '', 'All reviewers supplied: “Does not convey the intended meaning.”', '', link('Visual comparison gallery',B/'report.html'), '']
cards=[]
summary=[]
for n,item in enumerate(rows):
 r=runs[str(n)]; out=ROOT/r['dir']; result=json.loads((out/'result.json').read_text()); fix=ROOT/item['fix']; uploaded=json.loads((fix/'result.json').read_text())
 assert uploaded['outcome']=='done' and uploaded['review_status']=='ready'
 assert uploaded['author']=='gpt-6' and uploaded['build_gate']['status']=='pass'
 status='pass · exception' if uploaded['accepted_exception'] else 'strict pass'
 meta=result; svg=out/(item['icon_id']+'.svg')
 md += [f'## {item["key"]}', '', '**Before:** '+meta['original_vs_rejected'], '', '**Feedback:** '+item['feedback'], '', '**Changed:** '+meta['changes'], '', f'**AUTHOR:** `gpt-6`. **Validation:** {status}; automatic model status `{uploaded["validation_status"]}`. **Production:** done → Ready.', '', f'**Keyshape:** `{meta["keyshape"]}` — chosen for the subject’s proportions; accepted deviations are documented below.' ,'', '**References:** '+link('Original',ROOT/item['ref'])+'; '+meta['lucide_reference']+'.', '', '**Omissions:** '+('; '.join(meta['omissions']) or 'No defining feature omitted.'), '']
 if result['accepted_exception']:md+=['**Exception:** '+result['exception']['reason'],'']
 md += [link('RESULT_DIR',out)+' · '+link('SVG',svg)+' · '+link('Python module',ROOT/r['module'])+' · '+link('Validation',out/'validation.txt')+' · '+link('Production finish record',fix/'result.json'),'']
 imgs=[]
 for label,path in [('Original',ROOT/item['ref']),('Rejected',fix/'before'/(item['icon_id']+'.svg')),('Revised light',out/'preview-light-384.png'),('Revised dark',out/'preview-dark-384.png')]:
  imgs.append(f'<figure><figcaption>{label}</figcaption><img class="large" src="{url(path)}"><img class="native" src="{url(path)}"></figure>')
 cards.append(f'<article><h2>{html.escape(item["key"])}</h2><p class="status">Ready · {status} · AUTHOR gpt-6</p><div class="images">'+''.join(imgs)+f'</div><p><b>Before:</b> {html.escape(meta["original_vs_rejected"])}</p><p><b>Changed:</b> {html.escape(meta["changes"])}</p><p><a href="{url(svg)}">SVG</a> · <a href="{url(out/"validation.txt")}">Validation</a> · <a href="{url(fix/"result.json")}">Production finish</a></p></article>')
 summary.append(dict(key=item['key'],outcome=uploaded['outcome'],review_status=uploaded['review_status'],author=uploaded['author'],validation=status,result_dir=str(out),svg=str(svg)))
(B/'report.md').write_text('\n'.join(md))
(B/'summary.json').write_text(json.dumps(summary,indent=2))
(B/'report.html').write_text('''<!doctype html><meta charset="utf-8"><title>20 meaning fixes</title><style>body{font:15px system-ui;max-width:1000px;margin:40px auto;background:#eee;color:#191919}h1{font-size:28px}h2{font-size:18px}article{background:white;padding:24px;margin:20px 0;border-radius:12px}.images{display:flex;gap:24px}figure{margin:0;width:190px}figcaption{margin-bottom:10px;color:#555}.large{display:block;width:144px;height:144px;object-fit:contain}.native{display:block;width:48px;height:48px;object-fit:contain;margin:16px 0}.status{color:#357441}a{color:#2459a5}p{line-height:1.55}</style><h1>20 meaning fixes — all returned to Ready</h1><p>Worker thuan-mac · AUTHOR gpt-6 · 2 strict passes · 18 accepted visual exceptions. Every exception retains its automatic findings. Each comparison includes an enlarged view and a native 48px view.</p>'''+''.join(cards))
print('Verified:',len(summary),'done / ready; author gpt-6; full gate pass')
print(B/'report.md')
