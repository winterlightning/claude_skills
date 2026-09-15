import json,sys,io,math
from pathlib import Path
H=Path(__file__).resolve().parent;ROOT=H.parents[3];sys.path.insert(0,str(ROOT))
from icon_set.model.icons.registry import create
from PIL import Image,ImageDraw
import cairosvg
rows=json.loads((H/'baseline.json').read_text())
rows.sort(key=lambda r:(-sum(max(1,len(p.get('segments',[]))) for p in r['primitives']),r['id']))
ledger=[]
for b in range(math.ceil(len(rows)/24)):
 im=Image.new('RGB',(1440,1440),'white');d=ImageDraw.Draw(im)
 for k,r in enumerate(rows[b*24:(b+1)*24]):
  x=k%6*240;y=k//6*360;icon=create(r['id']);s=icon.to_svg()
  for size,xx,yy,col,thin in [(150,40,32,'#152333',False),(130,8,204,'#0872c9',True),(48,172,247,'#152333',False)]:
   src=s.replace('currentColor',col)
   if thin:src=src.replace('stroke-width="4"','stroke-width=".3"')
   pic=Image.open(io.BytesIO(cairosvg.svg2png(bytestring=src.encode(),output_width=size,output_height=size)));im.paste(pic,(x+xx,y+yy),pic)
  name=r['id'];d.text((x+8,y+8),name[:36],fill='black')
  if len(name)>36:d.text((x+8,y+20),name[36:],fill='black')
  d.text((x+8,y+188),f'{len(icon.primitives)} parts / {sum(max(1,len(getattr(p,'segments',()))) for p in icon.primitives)} segments',fill='gray')
  ledger.append(dict(id=r['id'],sheet=f'sweep-{b:02d}.png',cell=k+1,primitives=len(icon.primitives),segments=sum(max(1,len(getattr(p,'segments',()))) for p in icon.primitives)))
 im.save(H/f'sweep-{b:02d}.png');print('sheet',b,flush=True)
(H/'sweep-index.json').write_text(json.dumps(ledger,indent=2))
