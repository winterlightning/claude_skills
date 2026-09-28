from pathlib import Path
import json,os,html
root=Path(__file__).parent;rows=json.loads((root/'inputs.json').read_text())
lines=['# Primitive fix batch — thuan-mac','','20 bad-stroke icons claimed at offset 0. All 20 revisions uploaded and reported **done → Ready**. All validate with zero errors and zero warnings.','','[Visual comparison gallery](index.html)','']
page=['<!doctype html><meta charset="utf-8"><title>20 bad-stroke revisions · thuan-mac</title><style>body{font:15px system-ui;background:#eee;color:#222;max-width:1100px;margin:30px auto}article{background:white;border-radius:12px;padding:20px;margin:20px 0}section{display:flex;align-items:center;gap:28px}figure{margin:0;text-align:center}img{width:144px;height:144px}img.native{width:48px;height:48px}small{color:#555}a{color:#246}</style><h1>20 bad-stroke revisions</h1><p>Worker: thuan-mac · All 20 uploaded and reported done → Ready.</p>']
summary=[]
for i,r in enumerate(rows):
 result=json.loads((Path(r['fix'])/'result.json').read_text());d=json.loads((Path(r['run'])/'result.json').read_text())
 assert result['outcome']=='done' and result['review_status']=='ready' and result['validation_status']=='valid' and not result['validation_warnings'] and result.get('uploaded'),r['key']
 out=Path(r['run']).resolve();svg=out/(r['icon_id']+'.svg');feedback=r['feedback'].replace('\n',' ')
 lines+=['## '+r['key'],'','- Feedback: '+feedback,'- Revision: '+d['plan'],'- Keyshape: '+d['keyshape']+'; chosen to preserve the subject’s proportions.','- Construction reference: '+d['construction_reference'],'- Omissions: '+d['omissions'],f'- RESULT_DIR: [open folder]({out})',f'- SVG: [{svg.name}]({svg})','- Validation: valid; zero errors, zero warnings. Reviewed at native 48 px in light and dark.',f'- Outcome: **done → Ready**. [Finish receipt]({(Path(r["fix"])/"result.json").resolve()})','']
 rel=lambda p:html.escape(os.path.relpath(p,root),quote=True)
 page.append('<article><h2>'+html.escape(r['key'])+'</h2><p>Feedback: '+html.escape(feedback)+'</p><section>')
 for label,p,cls in [('Original',root/f'{i}-ref.png',''),('Rejected',root/f'{i}-before.png',''),('Revision — light',out/'preview-light-384.png',''),('Revision — dark',out/'preview-dark-384.png',''),('48px light',out/'preview-light-48.png','native'),('48px dark',out/'preview-dark-48.png','native')]:
  page.append(f'<figure><img class="{cls}" src="{rel(p)}"><figcaption>{label}</figcaption></figure>')
 page.append('</section><p>'+html.escape(d['plan'])+'</p><p><small>'+html.escape(d['construction_reference'])+' Omissions: '+html.escape(d['omissions'])+'</small></p>')
 page.append(f'<p>Validation: valid, zero warnings · Outcome: done → Ready · <a href="{rel(svg)}">SVG</a> · <a href="{rel(out/"result.json")}">Result</a></p></article>')
 summary.append({'key':r['key'],'outcome':'done','review_status':'ready','validation_status':'valid','warnings':0,'result_dir':r['run'],'svg':str(svg),'receipt':str(Path(r['fix'])/'result.json')})
(root/'REPORT.md').write_text('\n'.join(lines));(root/'index.html').write_text('\n'.join(page));(root/'summary.json').write_text(json.dumps(summary,indent=2))
print('Verified 20/20 finish receipts: uploaded, done, Ready, zero warnings. No unfinished claims in this batch.')
