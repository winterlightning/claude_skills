from pathlib import Path
from PIL import Image,ImageDraw
import json
root=Path(__file__).resolve().parent
rows=json.loads((root/'batch.json').read_text())
for page in range(2):
 im=Image.new('RGB',(1000,1100),'#ddd');d=ImageDraw.Draw(im)
 for j,row in enumerate(rows[page*10:page*10+10]):
  if not row['result_dir']:continue
  x=(j%2)*500;y=(j//2)*220;p=Path(row['result_dir'])
  d.text((x+4,y+3),row['icon_id'],fill='black')
  for i,theme in enumerate(['light','dark']):
   f=p/f'preview-{theme}-384.png'
   if f.exists():im.paste(Image.open(f).resize((160,160)),(x+10+i*245,y+25))
   f=p/f'preview-{theme}-48.png'
   if f.exists():im.paste(Image.open(f),(x+185+i*245,y+75))
 im.save(root/f'review-{page}.png')
