from pathlib import Path
import json,io,html,sys
ROOT=Path(__file__).resolve().parents[3]
sys.path.insert(0,str(ROOT))
from PIL import Image,ImageDraw,ImageFont
from icon_set.model.icons.registry import create
from icon_set.renderers.png import render_png
SOURCE_ICON_ID=None
SOURCE_PATH='icon_set/work/broken-geometry-repair/queue.json'
AUTHOR='gpt-6'
W=Path(__file__).parent
rows=json.loads((W/'queue.json').read_text())
font=ImageFont.truetype('/System/Library/Fonts/Helvetica.ttc',13)
small=ImageFont.truetype('/System/Library/Fonts/Helvetica.ttc',11)
results=[]
for row in rows:
 obj=create(row['id']);svg=obj.to_svg();report=obj.validate_icon();desc=report.describe()
 assert not any(s in desc for s in ['not contiguous','does not return to its start','unknown element','duplicate element ids','coincident endpoints']),desc
 (W/(row['id']+'.svg')).write_text(svg)
 results.append({'id':row['id'],'file':row['file'],'valid':desc.splitlines()[0]=='status: valid','validation':desc})
for theme,bg,fg,muted in [('light','#f7f6f2','#202226','#686b70'),('dark','#17191d','#f1f2f5','#a7abb3')]:
 sheet=Image.new('RGB',(1250,1150),bg);draw=ImageDraw.Draw(sheet)
 draw.text((22,16),'BROKEN GEOMETRY REPAIRS — 25 icons now render',font=font,fill=fg)
 for index,row in enumerate(results):
  x=(index%5)*250;y=(index//5)*220+45;obj=create(row['id'])
  for scale,dx,dy in [(2,28,20),(1,159,60)]:
   im=Image.open(io.BytesIO(render_png(obj,ink=fg,scale=scale)))
   sheet.paste(im,(x+dx,y+dy),im)
  draw.text((x+18,y+130),row['id'],font=font,fill=fg)
  draw.text((x+18,y+154),'All checks pass' if row['valid'] else 'Renders • other findings remain',font=small,fill=muted)
  draw.text((x+18,y+174),'2× preview                         48px',font=small,fill=muted)
 sheet.save(W/f'preview-{theme}.png')
(W/'results.json').write_text(json.dumps(results,indent=2))
cards=[]
for r in results:
 svg=(W/(r['id']+'.svg')).read_text()
 cards.append(f'<article><div class="icons">{svg}{svg}</div><h2>{r["id"]}</h2><p>{"All checks pass" if r["valid"] else "Renders; other findings remain"}</p><details><summary>Validation details</summary><pre>{html.escape(r["validation"])}</pre></details></article>')
(W/'index.html').write_text('''<!doctype html><meta charset="utf-8"><title>25 repaired icons</title><style>body{font:15px system-ui;background:#f7f6f2;color:#202226;margin:32px}h1{font-size:25px}main{display:grid;grid-template-columns:repeat(auto-fit,minmax(230px,1fr));gap:16px}article{border:1px solid #8885;border-radius:12px;padding:18px}h2{font-size:15px}p,summary{font-size:13px;color:#797d84}.icons{display:flex;align-items:center;gap:35px;height:120px}.icons svg:first-child{width:96px;height:96px}.icons svg:last-child{width:48px;height:48px}pre{white-space:pre-wrap;font-size:11px}@media(prefers-color-scheme:dark){body{background:#17191d;color:#f1f2f5}}</style><h1>25 repaired icons</h1><p>All 25 render. 7 pass all checks; 18 retain findings outside Broken geometry. Previews shown at 2× and native 48px.</p><main>'''+''.join(cards)+'</main>')
print('Emission checks: 25/25. Fully valid:',sum(r['valid'] for r in results))
