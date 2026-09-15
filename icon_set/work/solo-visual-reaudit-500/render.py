from pathlib import Path
import sys,json,io
ROOT=Path(__file__).resolve().parents[3];sys.path.insert(0,str(ROOT))
from icon_set.model.icons.registry import create
from icon_set.renderers.svg import render_svg
from PIL import Image,ImageDraw
import cairosvg
W=Path(__file__).parent
rows=json.loads((W/'repairs.json').read_text())
for page in range((len(rows)+11)//12):
 im=Image.new('RGB',(1200,900),'white');pen=ImageDraw.Draw(im)
 for j,r in enumerate(rows[page*12:page*12+12]):
  x=j%4*300;y=j//4*300
  pen.text((x+5,y+5),f"{r['number']} {r['icon_id'][:36]}",fill='black')
  for ident,dy,size in [(r['icon_id'],25,144),(r['parent'],192,72)]:
   svg=render_svg(create(ident))
   v=Image.open(io.BytesIO(cairosvg.svg2png(bytestring=svg.encode(),output_width=size,output_height=size)));im.paste(v,(x+5,y+dy),v)
  for dx,dark in [(170,False),(234,True)]:
   svg=render_svg(create(r['icon_id']))
   if dark:
    svg=svg.replace('currentColor','#ffffff');pen.rectangle((x+dx,y+45,x+dx+48,y+93),fill='#17191d')
   v=Image.open(io.BytesIO(cairosvg.svg2png(bytestring=svg.encode(),output_width=48,output_height=48)));im.paste(v,(x+dx,y+45),v)
 im.save(W/f'new-{page+1}.png')
