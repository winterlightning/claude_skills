from pathlib import Path
import sys,json,io,html
ROOT=Path(__file__).resolve().parents[3];sys.path.insert(0,str(ROOT))
from PIL import Image,ImageDraw,ImageFont
from icon_set.model.icons.registry import create
from icon_set.renderers.png import render_png
W=Path(__file__).parent
SOURCE_ICON_ID=None
SOURCE_PATH='icon_set/work/shifted-bounds-repair/results.json'
AUTHOR='gpt-6'
rows=json.loads((W/'results.json').read_text());font=ImageFont.truetype('/System/Library/Fonts/Helvetica.ttc',13)
for theme,bg,fg in [('light','#f7f6f2','#202226'),('dark','#17191d','#f1f2f5')]:
 im=Image.new('RGB',(1250,370),bg);d=ImageDraw.Draw(im);d.text((16,12),'KEYSHAPE BOUNDS CORRECTED — parent / revised / native 48px',font=font,fill=fg)
 for i,r in enumerate(rows):
  x=i*250;d.text((x+8,47),r['original'],font=font,fill=fg)
  for ident,dx in [(r['original'],8),(r['id'],135)]:
   o=create(ident);tile=Image.open(io.BytesIO(render_png(o,ink=fg,scale=2)));im.paste(tile,(x+dx,80),tile)
   a,b,c,e=o.keyshape_bounds();d.rectangle((x+dx+2*a,80+2*b,x+dx+2*c,80+2*e),outline='#559abb',width=1)
  d.text((x+8,186),'Before',font=font,fill=fg);d.text((x+135,186),'After',font=font,fill=fg)
  o=create(r['id']);tile=Image.open(io.BytesIO(render_png(o,ink=fg)));im.paste(tile,(x+100,215),tile)
  d.text((x+8,280),'Bounds PASS',font=font,fill=fg);d.text((x+8,304),'Other validation findings remain',font=font,fill=fg)
 im.save(W/f'preview-{theme}.png')
for r in rows:(W/(r['id']+'.svg')).write_text(create(r['id']).to_svg())
cards=[]
for r in rows:cards.append('<article><h2>'+r['original']+'</h2><img width="96" height="96" src="'+r['id']+'.svg"><p>New variant: '+r['id']+'</p><p>'+r['note']+'</p><pre>'+html.escape(r['validation'])+'</pre></article>')
(W/'index.html').write_text('<!doctype html><meta charset="utf-8"><title>Shifted bounds repairs</title><style>body{font:15px system-ui;background:#f7f6f2;color:#24272d;margin:28px}main{display:grid;grid-template-columns:repeat(auto-fit,minmax(300px,1fr));gap:18px}article{padding:18px;border:1px solid #ddd;border-radius:12px;background:white}h2{font-size:17px}pre{white-space:pre-wrap;font-size:12px}</style><h1>Five keyshape-bounds corrections</h1><p>All five revised variants have exact bounds. Existing spacing and other design findings remain; these are not full-validation passes. Parents are preserved. The two sharks had tiny arc overshoots, miscategorized as a shift by rounded report values.</p><p><a href="preview-light.png">Light comparison</a> · <a href="preview-dark.png">Dark comparison</a></p><main>'+''.join(cards)+'</main>')
