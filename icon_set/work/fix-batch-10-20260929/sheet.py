from pathlib import Path
from PIL import Image,ImageDraw
import json
root=Path(__file__).parent
for g in range(4):
 sheet=Image.new('RGB',(1000,460),'#ddd');d=ImageDraw.Draw(sheet)
 for j in range(5):
  i=g*5+j+1;m=json.loads((root/f'latest-{i}.json').read_text());out=Path(m['result_dir'])
  d.text((j*200+4,4),f'{i} {m["icon_id"][:23]}',fill='black')
  for k,theme in enumerate(('light','dark')):
   im=Image.open(out/f'preview-{theme}-384.png').resize((160,160));sheet.paste(im,(j*200+4,k*220+24))
   im=Image.open(out/f'preview-{theme}-48.png');sheet.paste(im,(j*200+144,k*220+160))
 sheet.save(root/f'review-{g}.png')
