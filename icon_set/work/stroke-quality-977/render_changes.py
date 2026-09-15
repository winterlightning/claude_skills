import sys,json,io,math
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3];sys.path.insert(0,str(ROOT))
from icon_set.model.icons.registry import create
from PIL import Image,ImageDraw
import cairosvg
H=Path(__file__).parent
before={r['id']:r for r in json.loads((H/'before.json').read_text())}
changes=json.loads((H/'changes.json').read_text())
for b in range(math.ceil(len(changes)/20)):
 im=Image.new('RGB',(1500,1000),'white');d=ImageDraw.Draw(im)
 for k,r in enumerate(changes[b*20:(b+1)*20]):
  x=k%5*300;y=k//5*250
  for j,s in enumerate([before[r['id']]['svg'],create(r['id']).to_svg()]):
   p=Image.open(io.BytesIO(cairosvg.svg2png(bytestring=s.replace('currentColor','#101820').encode(),output_width=128,output_height=128)));im.paste(p,(x+6+j*145,y+20),p)
  d.text((x+8,y+2),'BEFORE                       AFTER',fill='gray');d.text((x+8,y+152),r['id'][:40],fill='black')
  d.rectangle((x+155,y+179,x+220,y+244),fill='#101820')
  for xx,color in [(84,'#101820'),(164,'white')]:
   p=Image.open(io.BytesIO(cairosvg.svg2png(bytestring=create(r['id']).to_svg().replace('currentColor',color).encode(),output_width=48,output_height=48)));im.paste(p,(x+xx,y+187),p)
 im.save(H/f'changes-{b:02d}.png')
print('Rendered',len(changes),'changes')
