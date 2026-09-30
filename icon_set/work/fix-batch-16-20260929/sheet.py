from pathlib import Path
import json
from PIL import Image,ImageDraw
B=Path(__file__).parent;rows=json.loads((B/'runs.json').read_text())
for page in range(4):
 c=Image.new('RGB',(850,1000),'#ccc');d=ImageDraw.Draw(c)
 for i,(k,r) in enumerate(list(rows.items())[page*5:page*5+5]):
  y=i*200;d.text((8,y+3),k+' '+str(r['valid']),fill='black')
  for j,t in enumerate(['light','dark']):
   p=Path(r['run'])/f'preview-{t}-384.png'
   im=Image.open(p);im.thumbnail((156,156));c.paste(im,(j*400+20,y+25))
   c.paste(Image.open(Path(r['run'])/f'preview-{t}-48.png'),(j*400+190,y+80))
 c.save(B/f'candidates-{page}.png')
