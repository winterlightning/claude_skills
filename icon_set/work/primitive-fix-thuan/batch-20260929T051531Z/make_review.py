from PIL import Image,ImageDraw
from pathlib import Path
import json
b=Path(__file__).parent;rs=json.loads((b/'batch.json').read_text())
for page in range(4):
 im=Image.new('RGB',(1060,5*212+32),'#eeeeee');d=ImageDraw.Draw(im)
 for x,label in [(16,'Original reference'),(216,'Rejected'),(416,'Revision light'),(616,'Revision dark'),(826,'Native 48px')]:d.text((x,8),label,fill='black')
 for row,i in enumerate(range(page*5,page*5+5)):
  r=rs[i];y=32+row*212;d.text((10,y+2),f'{i+1}. {r["id"]}',fill='black');p=Path(r['run'])
  files=[b/f'{i}-reference.png',b/f'{i}-before.png',p/'preview-light-384.png',p/'preview-dark-384.png']
  for col,f in enumerate(files): im.paste(Image.open(f).convert('RGB').resize((160,160)),(16+col*200,y+28))
  for col,t in enumerate(['light','dark']):im.paste(Image.open(p/f'preview-{t}-48.png').convert('RGB'),(836+col*70,y+80))
 im.save(b/f'final-review-{page+1}.png')
