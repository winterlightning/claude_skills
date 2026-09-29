from pathlib import Path
from PIL import Image,ImageDraw
import json
r=Path(__file__).parent;a=json.loads((r/'runs.json').read_text())
for g in range(4):
 s=Image.new('RGB',(1050,650),'#ddd');d=ImageDraw.Draw(s)
 for j,i in enumerate(range(g*5,g*5+5)):
  v=a[str(i)];run=Path(v['run']);y=j*130;d.text((4,y+8),str(i)+' '+v['icon_id'],fill='black')
  for k,theme in enumerate(['light','dark']):
   im=Image.open(run/f'preview-{theme}-384.png').convert('RGB');s.paste(im.resize((112,112)),(520+k*250,y+8))
   s.paste(Image.open(run/f'preview-{theme}-48.png').convert('RGB'),(650+k*250,y+35))
 s.save(r/f'after-{g}.png')
