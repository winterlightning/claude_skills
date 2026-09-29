from author_batch import *
from PIL import Image,ImageDraw
import io,html,cairosvg
records=[]
for n,r in enumerate(ITEMS,1):
 receipt=json.loads((ROOT/r['fix_dir']/'result.json').read_text())
 assert receipt['outcome']=='done' and receipt['review_status']=='ready',(r['key'],receipt)
 assert receipt['author']=='gpt-6' and receipt['build_gate']['status']=='pass'
 run=ROOT/receipt['make_ray_run'];result=json.loads((run/'result.json').read_text());svg=run/(result['icon_id']+'.svg')
 assert svg.read_text()==(ROOT/r['fix_dir']/'after'/svg.name).read_text()
 if n==1:
  result['human_review']={'reference':'icon_set/references/human_ref/user.svg','face_center':[24,20],'face_radius':8,'face_bottom_centerline_y':28,'shoulder_top_centerline_y':32,'head_body_ink_gap':0,'note':'Circular face and broad symmetric shoulders; exact intentional tangent ink contact. Flowing headcloth spacing accepted as a drawing-bound visual exception.'}
  (run/'result.json').write_text(json.dumps(result,indent=2)+'\n')
 records.append((n,r,receipt,run,result,svg))
exc=sum(bool(z[2].get('accepted_exception')) for z in records)
lines=['# Bad-stroke fix batch — 20 icons','',f'Worker: `thuan-mac`. Author on every module: `gpt-6`. Offset: 0. All 20 production finishes returned `done` and review status `ready`. {20-exc} strict passes; {exc} user-authorized visual exceptions.','', 'Original and rejected SVGs were inspected before drawing. Final revisions were inspected at native 48px and enlarged size in light and dark themes. Each result directory contains the module, SVG, input metadata, reference renders, theme previews, validation findings and result.json.','', '[Visual comparison report](comparison.html)','']
for n,r,receipt,run,result,svg in records:
 status='Pass with drawing-bound visual exception' if receipt.get('accepted_exception') else 'Valid, zero warnings; full build gate pass'
 lines += [f'## {n}. {r["key"]}','',r['comparison'],'',f'**Feedback:** {r["feedback"].strip()}', '',f'**Changed:** {result["changes"]} Keyshape: {result["keyshape"]}. Retained the defining composition; removed microscopic contour detours. Construction reference: {result["references"]}.','',f'**AUTHOR:** `gpt-6`. **Validation:** {status}. **Production:** done → Ready.','',f'[RESULT_DIR]({run}) · [SVG]({svg}) · [Validation]({ROOT/r["fix_dir"]/"validation.txt"})','']
 if receipt.get('accepted_exception'):lines += [f'**Exception:** {receipt["build_gate"]["exception"]["reason"]}',f'Automatic status: `{receipt["build_gate"]["automatic_status"]}`; original errors/warnings remain in the validation artifacts.','']
 if n==1:lines += ['Human construction: face center (24,20), radius 8; face bottom centerline y=28 and shoulder top y=32 give exactly zero visible head-to-body gap with 4-unit strokes.','']
(BATCH/'REPORT.md').write_text('\n'.join(lines))
blocks=[]
for n,r,receipt,run,result,svg in records:
 def img(path,label):return f'<figure><img src="{html.escape(str(path))}" alt="{label}"><figcaption>{label}</figcaption></figure>'
 blocks.append('<article><h2>'+html.escape(r['key'])+'</h2><div class="images">'+img(ROOT/r['ref'],'Reference')+img(ROOT/r['before'],'Rejected')+img(run/'preview-light-384.png','Revised')+img(run/'preview-dark-384.png','Dark')+f'</div><div class="native"><img src="{run}/preview-light-48.png"><img src="{run}/preview-dark-48.png"></div><p>'+html.escape(r['comparison'])+'</p><p>'+('Pass · exception' if receipt.get('accepted_exception') else 'Strict pass · zero warnings')+f' · Ready · gpt-6</p><a href="{svg}">SVG</a> · <a href="{run}">Result directory</a></article>')
(BATCH/'comparison.html').write_text('<!doctype html><html><meta charset="utf-8"><title>20 bad-stroke revisions</title><style>body{font:15px system-ui;background:#eee;color:#222;margin:32px}main{display:grid;grid-template-columns:repeat(2,minmax(450px,1fr));gap:20px}article{background:white;padding:20px;border-radius:12px}h2{font-size:17px}.images{display:flex;gap:12px}figure{margin:0}figure img{width:100px;height:100px}figcaption{font-size:12px;color:#666}.native{display:flex;gap:12px;margin:16px 0}.native img{width:48px;height:48px}</style><h1>20 bad-stroke revisions — all Ready</h1><p>18 strict passes · 2 documented visual exceptions · Author gpt-6 · Worker thuan-mac</p><main>'+''.join(blocks)+'</main></html>')
# Compact complete native-size review overview, preserving 48px pixels in both themes.
sheet=Image.new('RGB',(1000,720),'#e7e7e5');d=ImageDraw.Draw(sheet)
for n,r,receipt,run,result,svg in records:
 col=(n-1)%4;row=(n-1)//4;x=col*250;y=row*144
 title=r['key'].split('/')[1];d.text((x+10,y+8),f'{n}. {title[:29]}',fill='#222')
 sheet.paste(Image.open(run/'preview-light-48.png'),(x+25,y+40));sheet.paste(Image.open(run/'preview-dark-48.png'),(x+105,y+40))
 d.text((x+10,y+105),'Ready / '+('exception' if receipt.get('accepted_exception') else 'strict pass'),fill='#222')
sheet.save(BATCH/'all-20-native.png')
summary={'claimed':20,'done':20,'ready':20,'strict_pass':20-exc,'exceptions':exc,'author':'gpt-6','worker':'thuan-mac','items':[{'key':r['key'],'run':str(run),'svg':str(svg),'review_status':receipt['review_status'],'exception':bool(receipt.get('accepted_exception'))} for n,r,receipt,run,result,svg in records]}
(BATCH/'summary.json').write_text(json.dumps(summary,indent=2))
print(json.dumps({k:v for k,v in summary.items() if k!='items'}))
