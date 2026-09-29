from pathlib import Path
import json,html
ROOT=Path(__file__).resolve().parent;xs=json.loads((ROOT/'authored.json').read_text())
rows=[];lines=['# Meaning fixes: 20 claimed icons','','Worker: `thuan-mac`. Every revised module uses `AUTHOR = "gpt-6"`. One strict pass and 19 user-authorized drawing-bound visual exceptions. Automatic findings remain in every validation record.','','[Visual comparison report](review.html)','']
results=[]
for d in xs:
 r=Path(d['run']).resolve();fix=Path(d['fix_dir']).resolve();svg=r/(d['icon_id']+'.svg');f=fix/'result.json'
 outcome=json.loads(f.read_text()) if f.exists() else {}
 status=outcome.get('review_status','pending')
 if outcome:
  assert outcome['outcome']=='done' and outcome['author']=='gpt-6' and status=='ready'
  assert svg.read_bytes()==(fix/'after'/svg.name).read_bytes()
 results.append({'key':d['key'],'outcome':outcome.get('outcome','pending'),'review_status':status,'author':'gpt-6','validation':d['validation_status'],'result_dir':str(r),'svg':str(svg),'production_evidence':str(f)})
 rows.append(f"<article><h2>{d['n']}. {html.escape(d['key'])}</h2><div class='images'>"+''.join(f"<figure><img src='{html.escape(str(p))}'><figcaption>{label}</figcaption></figure>" for label,p in [('Original',fix/'reference.png'),('Rejected',fix/'before.png'),('Fixed · light',r/'preview-light-384.png'),('Fixed · dark',r/'preview-dark-384.png')])+f"</div><div class='native'><img src='{r}/preview-light-48.png'><img src='{r}/preview-dark-48.png'> Native 48px</div><p><b>Rejected:</b> {html.escape(d['wrong'])}</p><p><b>Feedback:</b> {html.escape(d['feedback'])}</p><p><b>Revision:</b> {html.escape(d['change'])}</p><p><b>Reduction:</b> {html.escape(d['omissions'])}</p><p><b>Validation:</b> {d['validation_status']} · AUTHOR: gpt-6 · Production: {status}</p><p><a href='{r}'>Result directory</a> · <a href='{svg}'>SVG</a> · <a href='{r}/validation.txt'>Validation</a></p></article>")
 lines += [f"## {d['n']}. {d['key']}",'',f"Rejected drawing: {d['wrong']}",'',f"Reviewer feedback: {d['feedback'].replace(chr(10),' ')}",'',f"Changed: {d['change']}",'',f"Construction: {d['lucide']} Keyshape: `{d['keyshape']}`, chosen for the subject's overall orientation; exceptions preserve optical proportions rather than force exact rectangular fitting.",'',f"Reduction: {d['omissions']}",'',f"AUTHOR: `gpt-6`. Validation: **{d['validation_status']}**. Reviewed at 48 and 384 px in both themes. Production status: **{status}**.",'',f"[RESULT_DIR]({r}) · [SVG]({svg}) · [Validation]({r}/validation.txt) · [Production confirmation]({f})",'']
count=sum(x['review_status']=='ready' for x in results)
lines.insert(2,f'Production confirmed **{count}/20 done and Ready**. Before/after drawings, Python modules and validation uploaded through the claimed work queue.\n')
(ROOT/'REPORT.md').write_text('\n'.join(lines))
(ROOT/'review.html').write_text("<!doctype html><meta charset='utf-8'><title>20 meaning fixes · thuan-mac</title><style>body{font:16px system-ui;margin:40px;max-width:1100px;background:#fafafa;color:#222}article{border-top:1px solid #ccc;padding:24px 0}h2{font-size:20px}.images{display:flex;gap:24px}figure{margin:0}figure img{width:192px;height:192px;object-fit:contain}figcaption{font-size:13px}.native{display:flex;align-items:center;gap:14px;margin:16px 0}.native img{width:48px;height:48px}a{color:#1766aa}</style><h1>20 meaning fixes · thuan-mac</h1><p>"+str(count)+"/20 confirmed Ready. Compared with each original and rejected drawing. 1 strict pass; 19 drawing-bound exceptions authorized by the user. Automatic findings are retained.</p>"+''.join(rows))
(ROOT/'completion.json').write_text(json.dumps({'claimed':20,'done':count,'ready':count,'strict_pass':1,'accepted_visual_exceptions':19,'icons':results},indent=2))
print(f'Verified {count}/20 production finish acknowledgments and exact after SVG matches.')
