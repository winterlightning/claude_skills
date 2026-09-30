from pathlib import Path
import json
from PIL import Image,ImageDraw
root=Path(__file__).parent;rows=json.loads((root/'batch.json').read_text())
for page in range(4):
 im=Image.new('RGB',(1000,340),'#ddd');d=ImageDraw.Draw(im)
 for j,r in enumerate(rows[page*5:page*5+5]):
  d.text((j*200,0),f"{page*5+j}: {r['id'][:25]}",fill='black');run=Path(r['run'])
  for k,theme in enumerate(['light','dark']):
   p=run/f'preview-{theme}-384.png'
   if p.exists():im.paste(Image.open(p).resize((140,140)),(j*200,k*155+25));im.paste(Image.open(run/f'preview-{theme}-48.png'),(j*200+145,k*155+70))
 im.save(root/f'after-{page}.png')
