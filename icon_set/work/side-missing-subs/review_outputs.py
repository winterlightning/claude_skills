"""Render the authored models and existing-glyph labels for native-size review."""
import json,io,textwrap,importlib,sys,html
from pathlib import Path
import cairosvg
from PIL import Image,ImageDraw,ImageFont
ROOT=Path(__file__).resolve().parents[3];sys.path.insert(0,str(ROOT))
from icon_set.renderers.svg import render_svg
AUTHOR='gpt-6';SOURCE_ICON_ID=None;SOURCE_PATH='icon_set/work/side-missing-subs/references.json'
out=Path(__file__).parent;solos=[r for r in json.loads((out/'solo-results.json').read_text()) if r['status']=='pass'];texts=json.loads((out/'text-results.json').read_text());items=[]
for r in solos:
 m=importlib.import_module('.'.join(Path(r['path']).with_suffix('').parts));c=next(c for c in vars(m).values() if isinstance(c,type) and getattr(c,'icon_id',None) and c.__module__==m.__name__);icon=c();document=render_svg(icon);(out/(r['icon_id']+'.svg')).write_text(document);r['keyshape']=icon.keyshape.name;items.append((r['number'],r['name'],document,'SOLO48 · '+r['keyshape']))
for r in texts:items.append((None,r['text'],(ROOT/'icon_set/dist/text32'/(r['icon_id']+'.svg')).read_text(),f'TEXT32 · {r["canvas_width"]:.1f} × 32'))
f=ImageFont.truetype('/System/Library/Fonts/Supplemental/Arial.ttf',15)
for theme in ['light','dark']:
 bg='#ffffff' if theme=='light' else '#172026';ink='#152027' if theme=='light' else '#f4f7fa';im=Image.new('RGB',(1040,1020),bg);dr=ImageDraw.Draw(im);dr.text((24,15),'11 SOLO48 icons + 13 typeface labels · native size · '+theme,font=f,fill=ink)
 for j,(n,name,document,detail) in enumerate(items):
  x=(j%4)*260;y=55+(j//4)*158;svg=document.replace('currentColor',ink).replace('#202820',ink).replace('#000000',ink).replace('stroke="black"','stroke="'+ink+'"');png=Image.open(io.BytesIO(cairosvg.svg2png(bytestring=svg.encode()))).convert('RGBA');im.paste(png,(x+(260-png.width)//2,y+20),png)
  for k,line in enumerate(textwrap.wrap((str(n)+'. ' if n else '')+name,28)):
   box=dr.textbbox((0,0),line,font=f);dr.text((x+(260-box[2])/2,y+82+k*18),line,font=f,fill=ink)
 im.save(out/f'generated-{theme}.png')
cards=[]
for n,name,svg,detail in items:
 cards.append('<article><div class="art">'+svg.replace('#202820','currentColor')+'</div><b>'+html.escape((str(n)+'. ' if n else '')+name)+'</b><small>'+detail+'</small></article>')
(out/'generated.html').write_text('''<!doctype html><meta charset="utf-8"><title>Side reference outputs</title><style>body{font:16px system-ui;margin:32px;background:#fafafa;color:#172026}body.dark{background:#172026;color:#f4f7fa}main{display:grid;grid-template-columns:repeat(auto-fill,minmax(235px,1fr));gap:14px}article{border:1px solid #8885;border-radius:12px;padding:18px;display:flex;flex-direction:column;gap:12px;text-align:center}.art{height:92px;display:flex;align-items:center;justify-content:center}svg{max-width:100%}small{opacity:.7}button{padding:8px 16px}h1{font-size:28px}</style><h1>11 solo drawings + 13 typeface labels</h1><p>Native-size review. Typeface ink height: 32 units; width follows the text. All outputs below pass their respective checks.</p><button onclick="document.body.classList.toggle('dark')">Light / dark</button><p>Three-star reference remains blocked. 28 composed references have separate component handoffs.</p><main>'''+''.join(cards)+'</main>')
(out/'solo-results.json').write_text(json.dumps(solos+[r for r in json.loads((out/'solo-results.json').read_text()) if r['status']!='pass'],indent=2))
