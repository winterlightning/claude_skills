import sys,json,io,xml.etree.ElementTree as E
from pathlib import Path
from PIL import Image,ImageDraw
import cairosvg
W=Path(__file__).resolve().parent;ROOT=W.parents[2];sys.path.insert(0,str(ROOT))
from icon_set.model.icons.registry import create
rows=json.loads((W/'batch.json').read_text());cs=json.loads((W/'candidates.json').read_text());assets=W/'review-assets';assets.mkdir(exist_ok=True)
for start in range(0,32,8):
 im=Image.new('RGB',(1440,1000),'#eeeeee');d=ImageDraw.Draw(im)
 for j,r in enumerate(rows[start:start+8]):
  i=r['number'];m=create(cs[str(i)]['icon']);docs={'original':(ROOT/r['source_path']).read_text(),'after':m.to_svg()};t=E.fromstring(docs['after'])
  for e in t.iter():
   if 'stroke-width' in e.attrib:e.set('stroke-width','.4')
  docs['center']=E.tostring(t).decode()
  x=(j%2)*720;y=(j//2)*250
  d.text((x+10,y+5),f'{i}. {r["icon"]} ({m.canvas_width} x {m.canvas_height})',fill='black')
  for k,(key,svg) in enumerate(docs.items()):
   (assets/f'{i}-{key}.svg').write_text(svg)
   png=cairosvg.svg2png(bytestring=svg.encode(),output_width=180,output_height=180);img=Image.open(io.BytesIO(png));im.paste(img,(x+10+k*235,y+40),img);d.text((x+10+k*235,y+25),key,fill='black')
 im.save(W/f'review-{start//8+1}.png')
print('Rendered all32')
