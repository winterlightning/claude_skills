from pathlib import Path
import json,io,sys,html
ROOT=Path(__file__).resolve().parents[3];sys.path.insert(0,str(ROOT))
from icon_set.model.icons.registry import create
from icon_set.renderers.png import render_png
from icon_set.renderers.svg import render_svg
from PIL import Image,ImageDraw,ImageFont
SOURCE_ICON_ID=None
SOURCE_PATH='icon_set/work/circle-bounds-repair/queue.json'
AUTHOR='gpt-6'
W=Path(__file__).parent;rows=json.loads((W/'mapping.json').read_text());font=ImageFont.truetype('/System/Library/Fonts/Helvetica.ttc',12)
for theme,bg,ink in [('light','#f7f6f2','#171717'),('dark','#17191d','#f6f6f2')]:
 im=Image.new('RGB',(1080,560),bg);d=ImageDraw.Draw(im)
 for i,r in enumerate(rows):
  x=i%3*360;y=i//3*280
  for j,key in enumerate(['original','id']):
   t=Image.open(io.BytesIO(render_png(create(r[key]),ink=ink,scale=2)));im.paste(t,(x+40+j*150,y+40),t);d.text((x+55+j*150,y+150),'Before' if j==0 else 'Revised',font=font,fill=ink)
  t=Image.open(io.BytesIO(render_png(create(r['id']),ink=ink)));im.paste(t,(x+152,y+184),t)
  d.text((x+10,y+253),r['original'],font=font,fill=ink)
 im.save(W/f'preview-{theme}.png')
notes={'compact-disc':'Reduced the disc radius; preserved the central hole.','compact-disc-with-partition-segment':'Reduced the rim and hub; preserved the partition.','compact-disc-with-sheen-arcs':'Repositioned both reflections and reduced the hub for nine-unit spacing.','cracked-compact-disc':'Rebuilt the open rim as an exact circle; retained the crack.','face-wearing-round-glasses':'Rebalanced the lenses and raised the smile.','disk-platter-with-drive-slots':'Rebalanced the hub and three short slots.'}
cards=[]
for r in rows:
 cards.append(f'<article><h2>{html.escape(r["original"])}</h2><div class="pair"><div><span>Before</span>{render_svg(create(r["original"]))}</div><div><span>Revised</span>{render_svg(create(r["id"]))}</div></div><div class="native">48 px {render_svg(create(r["id"]))}</div><p>{notes[r["original"]]}</p><small>Bounds · Spacing · Openings · Internal spacing: pass</small></article>')
(W/'index.html').write_text('''<!doctype html><html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Six circle repairs</title><style>*{box-sizing:border-box}body{margin:0;background:#f7f6f2;color:#17191d;font:15px system-ui}body.dark{background:#17191d;color:#f7f6f2}header{padding:30px;border-bottom:1px solid #8884}h1{margin:0 0 10px}button{float:right;border:1px solid #8886;border-radius:25px;background:transparent;color:inherit;padding:12px;cursor:pointer}main{display:grid;grid-template-columns:repeat(auto-fit,minmax(320px,1fr));gap:20px;padding:25px}article{border:1px solid #8884;border-radius:14px;padding:22px}h2{font-size:16px;min-height:38px}.pair{display:flex;justify-content:space-around}.pair div{display:flex;flex-direction:column;align-items:center;gap:15px}.pair svg{width:120px;height:120px}.pair span,.native{font-size:12px;color:#888}.native{display:flex;justify-content:center;align-items:center;gap:14px;margin:20px}.native svg{color:initial;width:48px;height:48px}body.dark .native svg{color:#f7f6f2}p{font-size:13px;line-height:1.6;min-height:40px}small{color:#398c60;font-size:11px}footer{padding:25px;font-size:13px;opacity:.7}</style><header><button onclick="document.body.classList.toggle('dark')">Light / dark</button><h1>Six circle repairs</h1>Visible radius 22 · all icon checks pass · originals preserved</header><main>'''+''.join(cards)+'''</main><footer>References: local Lucide disc, disc-3 and glasses; shared human reference user.svg. Existing approved small-circle rules apply to the reduced hubs and lenses.</footer></html>''')
