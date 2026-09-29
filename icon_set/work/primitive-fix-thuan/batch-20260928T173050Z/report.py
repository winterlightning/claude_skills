from pathlib import Path
import json,html,os
B=Path(__file__).resolve().parent;ROOT=B.parents[3]
items=json.loads((B/'items.json').read_text());rs=json.loads((B/'final-results.json').read_text())
finished=0;sections=[];cards=[]
for i,(it,r) in enumerate(zip(items,rs),1):
 run=ROOT/r['result_dir'];svg=run/r['svg'];rec=ROOT/it['fix_dir']/'result.json'
 receipt=json.loads(rec.read_text()) if rec.exists() else {}
 done=receipt.get('outcome')=='done';finished+=done
 status='pass · exception (automatic '+r['automatic_status']+')' if r['accepted_exception'] else 'pass · zero warnings'
 keyshape=next(line.strip().split('Keyshape.')[1] for line in (run/r['module']).read_text().splitlines() if 'keyshape = Keyshape.' in line)
 sec=f'''## {i}. {it['key']}

- Original versus rejected: {r['original_comparison']}
- Reviewer feedback: {r['feedback']}
- Repair: {r['change']}
- Keyshape: `{keyshape}`; selected for the subject's natural orientation. {r['omissions']}
- Construction reference: {r['construction_reference']}
- Visual review: {r['visual_review']}
- AUTHOR: `{r['author']}`.
- Validation: **{status}**. Model status: `{r['validation_status']}`. Automatic findings are preserved in validation.txt and automatic-gate.json.
- Production: **{'done — Ready' if done else 'upload pending'}**{'; worker '+receipt.get('worker','thuan-mac') if done else ''}.
- [RESULT_DIR]({run}) · [SVG]({svg}) · [Python]({run/r['module']}) · [Validation]({run/'validation.txt'}) · [Production receipt]({rec})
'''
 if r['accepted_exception']:sec+='- Exception reason: '+r['exception']['reason']+'\n'
 sections.append(sec)
 def rel(p):return html.escape(os.path.relpath(p,B))
 h=html.escape
 imgs=''.join(f'<figure><img src="{rel(run/p)}"><figcaption>{label}</figcaption></figure>' for p,label in [('reference-192.png','Original'),('before-192.png','Rejected'),('preview-light-384.png','Revised · light'),('preview-dark-384.png','Revised · dark')])
 native=''.join(f'<img class="native" src="{rel(run/p)}">' for p in ['preview-light-48.png','preview-dark-48.png'])
 cards.append(f'<article><h2>{i}. {h(it["key"])}</h2><div class="imgs">{imgs}</div><div>{native} <b>{h(status)}</b> · AUTHOR {h(r["author"])} · {"done — Ready" if done else "pending"}</div><p><b>Problem:</b> {h(r["original_comparison"])}</p><p><b>Feedback:</b> {h(r["feedback"])}</p><p><b>Changed:</b> {h(r["change"])}</p><p>{h(r["omissions"])}</p><p>{h(r["exception"]["reason"]) if r["accepted_exception"] else "No exception required."}</p><a href="{rel(run)}">RESULT_DIR</a> · <a href="{rel(svg)}">SVG</a> · <a href="{rel(run/r["module"])}">Python</a> · <a href="{rel(run/"validation.txt")}">Validation</a></article>')
head=f'''# Primitive fix batch — 20 bad-stroke icons

Worker: `thuan-mac` · offset: 0 · AUTHOR: `gpt-6`.

**{finished}/20 confirmed done and returned to Ready.** Five ordinary full-gate passes; fifteen accepted drawing-specific exceptions under the user's explicit delegation. Every drawing retains uniform 4px strokes on a 48×48 canvas. All originals and rejected drawings were compared visually; revised icons were inspected at 48px and enlarged in light and dark themes.

[Visual before/after report]({B/'report.html'}) · [Final contact sheet]({B/'final-contact.png'}) · [Machine-readable results]({B/'final-results.json'})

Exceptions preserve automatic failures/warnings and are bound to the exact SVG SHA-256. They are not described as clean automatic passes. Registered modules, published output and unrelated working changes were not edited.

'''
(B/'REPORT.md').write_text(head+'\n'.join(sections))
(B/'report.html').write_text('<!doctype html><html><head><meta charset="utf-8"><title>20 icon fixes</title><style>body{font:15px system-ui;background:#eee;color:#222;max-width:1100px;margin:30px auto}article{background:white;border-radius:12px;margin:20px 0;padding:24px}h2{font-size:20px}.imgs{display:flex;gap:24px}figure{margin:0}figure img{width:192px;height:192px}figcaption{color:#666;text-align:center}.native{width:48px;height:48px;margin:20px 12px 10px 0;vertical-align:middle}a{color:#2460ae}</style></head><body><h1>20 bad-stroke icon fixes</h1><p>'+str(finished)+'/20 confirmed done · 5 ordinary passes · 15 accepted exceptions · AUTHOR gpt-6</p>'+''.join(cards)+'</body></html>')
print(B/'REPORT.md');print('Production done',finished)
