from pathlib import Path
import json
from PIL import Image,ImageDraw
b=Path(__file__).parent
rows=json.loads((b/'claims.json').read_text());runs=json.loads((b/'runs.json').read_text())
for page in range(4):
 c=Image.new('RGB',(720,900),'#dddddd');d=ImageDraw.Draw(c)
 for j,r in enumerate(rows[page*5:page*5+5]):
  k=r['key'].split('/')[-1];v=runs[k];y=j*180
  d.text((2,y),k+' '+str(v['valid']),fill='black')
  for i,theme in enumerate(['light','dark']):
   p=Path(v['run'])/f'preview-{theme}-384.png'
   im=Image.open(p).convert('RGB');c.paste(im.resize((140,140)),(i*350+5,y+25))
   c.paste(Image.open(Path(v['run'])/f'preview-{theme}-48.png').convert('RGB'),(i*350+180,y+60))
 c.save(b/f'after-{page}.png')
