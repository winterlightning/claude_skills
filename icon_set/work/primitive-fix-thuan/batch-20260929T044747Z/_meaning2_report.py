from pathlib import Path
import json,os,html
b=Path('icon_set/work/primitive-fix-thuan/batch-20260929T044747Z');xs=json.loads((b/'final.json').read_text());cs=json.loads((b/'claims.json').read_text());assert len(xs)==20
rows=[];strict=sum(not x['result']['accepted_exception'] for x in xs);summary=f'{strict} automatic QA pass; {20-strict} accepted visual exceptions. All retain SOLO48 and uniform 4 px strokes. Automatic findings are preserved.'
lines=['# Meaning fixes — thuan-mac','', '20 icons claimed at offset 0, reason `meaning`. Every authored module uses `AUTHOR = "gpt-6"`.', '', summary,'','[Visual comparisons](comparison.html)',''];done=0
for x,c in zip(xs,cs):
 def rel(p):return os.path.relpath(p,b)
 r=x['result'];run=Path(x['run']);status='pass · exception' if r['accepted_exception'] else 'automatic pass';prod=Path(c['dir'])/'result.json';p=json.loads(prod.read_text()) if prod.exists() else {};done+=p.get('outcome')=='done' and p.get('review_status')=='ready'
 reflabel='Current drawing fallback' if r.get('reference_is_current') else 'Original'
 prodstatus=f"{p.get('outcome','pending')} / {p.get('review_status','pending')}"
 rows.append(f'''<article><h2>{html.escape(x['key'])}</h2><div class="pair"><figure><img src="{rel(c['ref'])}"><figcaption>{reflabel}</figcaption></figure><figure><img src="{rel(c['before'])}"><figcaption>Rejected</figcaption></figure><figure><img src="{rel(run/r['svg'])}"><figcaption>Revised</figcaption></figure><figure class="dark"><img src="{rel(run/'preview-dark-384.png')}"><figcaption>Dark</figcaption></figure><figure><img width="48" height="48" src="{rel(run/'preview-light-48.png')}"><figcaption>Native 48 px</figcaption></figure></div><p>{html.escape(r['comparison'])}</p><p>Feedback: {html.escape(r['feedback'])}</p><p>AUTHOR: gpt-6 · {status} · Production: {prodstatus}</p><p><a href="{rel(run)}">RESULT_DIR</a> · <a href="{rel(run/r['svg'])}">SVG</a> · <a href="{rel(run/'validation.txt')}">Validation</a></p><p>{html.escape((r.get('exception') or {}).get('reason','All automatic checks passed without warnings.'))}</p></article>''')
 absrun=run.resolve();lines+=['## '+x['key'],'',r['comparison'],'','Reviewer feedback: '+r['feedback'].replace('\n',' '),'',f'Author: `gpt-6`. Validation: **{status}**. Production: **{prodstatus}**.','',f'[RESULT_DIR]({absrun}) · [SVG]({absrun/r["svg"]}) · [Validation]({absrun/"validation.txt"})','']
 if r.get('reference_is_current'):lines+=['Reference: no original was available; the rejected current drawing was used.','']
 if r.get('exception'):lines+=['Exception: '+r['exception']['reason'],'']
(b/'REPORT.md').write_text('\n'.join(lines))
(b/'comparison.html').write_text('''<!doctype html><html><head><meta charset="utf-8"><title>20 meaning fixes · thuan-mac</title><style>body{font:15px system-ui;max-width:1200px;margin:32px auto;background:#f5f5f5;color:#222}article{background:white;padding:24px;margin:24px 0;border-radius:12px}h2{font-size:18px}.pair{display:flex;align-items:center;gap:12px}figure{margin:0;padding:12px;text-align:center}img{width:150px;height:150px}img[width]{width:48px;height:48px}.dark{background:#1c1c19;color:white}figcaption{font-size:12px;margin-top:8px}p{line-height:1.5}</style></head><body><h1>20 meaning fixes · thuan-mac</h1><p>'''+summary+'</p>'+''.join(rows)+'</body></html>')
print('Production done/ready:',done,'of 20;',summary)
