import sys,json,io,math
from pathlib import Path
H=Path(__file__).resolve().parent;ROOT=H.parents[3];sys.path.insert(0,str(ROOT))
from icon_set.model.icons.registry import create
from PIL import Image,ImageDraw
import cairosvg
before={r['id']:r for r in json.loads((H/'baseline.json').read_text())}
phase=sys.argv[1] if len(sys.argv)>1 else 'changes';changes=json.loads((H/(phase+'.json')).read_text())
for b in range(math.ceil(len(changes)/16)):
 im=Image.new('RGB',(1440,1200),'white');d=ImageDraw.Draw(im)
 for k,r in enumerate(changes[b*16:(b+1)*16]):
  x=k%4*360;y=k//4*300
  for j,s in enumerate([before[r['id']]['svg'],create(r['id']).to_svg()]):
   pic=Image.open(io.BytesIO(cairosvg.svg2png(bytestring=s.replace('currentColor','#152333').encode(),output_width=148,output_height=148)));im.paste(pic,(x+12+j*175,y+25),pic)
   pic=Image.open(io.BytesIO(cairosvg.svg2png(bytestring=s.replace('currentColor','#0872c9').replace('stroke-width="4"','stroke-width=".35"').encode(),output_width=76,output_height=76)));im.paste(pic,(x+15+j*175,y+190),pic)
  d.text((x+12,y+6),'BEFORE                              AFTER',fill='gray');d.text((x+8,y+176),r['id'][:49],fill='black')
  d.rectangle((x+295,y+210,x+353,y+268),fill='#152333')
  for xx,color in [(239,'#152333'),(300,'white')]:
   pic=Image.open(io.BytesIO(cairosvg.svg2png(bytestring=create(r['id']).to_svg().replace('currentColor',color).encode(),output_width=48,output_height=48)));im.paste(pic,(x+xx,y+215),pic)
 im.save(H/f'{phase}-{b:02d}.png')
print('Rendered',phase,len(changes))
