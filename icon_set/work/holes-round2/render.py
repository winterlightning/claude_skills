from pathlib import Path
import json,io
from PIL import Image,ImageDraw
import cairosvg
SOURCE_ICON_ID=None
SOURCE_PATH='icon_set/work/holes-round2/results.json'
AUTHOR='gpt-6'
w=Path(__file__).parent;rows=json.loads((w/'results.json').read_text())
for b in range(3):
 im=Image.new('RGB',(1080,960),'#efefea');d=ImageDraw.Draw(im)
 for j,r in enumerate(rows[b*9:b*9+9]):
  x=j%3*360;y=j//3*320;d.text((x+10,y+5),r['original'],fill='black')
  for k,path in enumerate([w/(r['original']+'-before.svg'),w/(r['candidate']+'.svg')]):
   s=path.read_text().replace('currentColor','#242521');png=Image.open(io.BytesIO(cairosvg.svg2png(bytestring=s.encode(),output_width=155,output_height=155)));im.paste(png,(x+10+k*175,y+40),png)
   sm=Image.open(io.BytesIO(cairosvg.svg2png(bytestring=s.encode(),output_width=48,output_height=48)));im.paste(sm,(x+65+k*175,y+215),sm)
  d.text((x+10,y+286),r['qa']['status']+' / holes '+r['qa']['negative_space']['status'],fill='black')
 im.save(w/f'preview-{b+1}.png')
