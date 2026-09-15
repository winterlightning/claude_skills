from pathlib import Path
import json,io,cairosvg
from PIL import Image,ImageDraw
OUT=Path(__file__).resolve().parent
rs=json.loads((OUT/'repairs.json').read_text())
for theme,bg,ink in [('light','#ffffff','#182736'),('dark','#132333','#f4f7fb')]:
 im=Image.new('RGB',(1440,((len(rs)+4)//5)*210),bg);dr=ImageDraw.Draw(im)
 for j,r in enumerate(rs):
  x=j%5*288;y=j//5*210
  for label,dx in [('before',8),('after',150)]:
   s=(OUT/label/f"{r['icon_id']}.svg").read_text().replace('currentColor',ink);pic=Image.open(io.BytesIO(cairosvg.svg2png(bytestring=s.encode(),output_width=112,output_height=112)));im.paste(pic,(x+dx,y+22),pic);dr.text((x+dx,y+4),label,fill=ink)
  dr.text((x+5,y+143),str(r['number'])+' '+r['icon_id'][:31],fill=ink);dr.text((x+5,y+162),r['after_qa']['status'],fill=ink)
  # actual native-scale after image
  s=(OUT/'after'/f"{r['icon_id']}.svg").read_text().replace('currentColor',ink);pic=Image.open(io.BytesIO(cairosvg.svg2png(bytestring=s.encode(),output_width=48,output_height=48)));im.paste(pic,(x+226,y+147),pic)
 im.save(OUT/f'comparison-{theme}.png')
