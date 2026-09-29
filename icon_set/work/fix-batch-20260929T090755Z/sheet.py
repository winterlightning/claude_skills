from pathlib import Path
import json
from PIL import Image,ImageDraw
root=Path(__file__).parent;rows=json.loads((root/'batch.json').read_text())
for b in range(4):
 out=Image.new('RGB',(980,5*205),'#dedede');d=ImageDraw.Draw(out)
 for j,row in enumerate(rows[b*5:b*5+5]):
  dest=Path(row['result_dir']);y=j*205;d.text((4,y+3),f'{b*5+j}: {row["icon_id"]}',fill='black')
  for k,name in enumerate(['reference.png','rejected.png','preview-light-384.png','preview-dark-384.png']):
   im=Image.open(dest/name).convert('RGB').resize((160,160));out.paste(im,(k*210+6,y+28))
  for k,t in enumerate(['light','dark']):out.paste(Image.open(dest/f'preview-{t}-48.png').convert('RGB'),(850,y+30+70*k))
 out.save(root/f'after-{b}.png')
