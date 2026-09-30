import json
from pathlib import Path
from PIL import Image,ImageDraw
B=Path(__file__).parent
rows=list(json.loads((B/'runs.json').read_text()).items())
for page in range((len(rows)+4)//5):
 im=Image.new('RGB',(850,1050),'#ddd');d=ImageDraw.Draw(im)
 for n,(key,r) in enumerate(rows[page*5:page*5+5]):
  y=n*210;d.text((8,y+4),key,fill='black')
  run=Path(r['run'])
  for k,theme in enumerate(('light','dark')):
   im.paste(Image.open(run/f'preview-{theme}-48.png').convert('RGB'),(k*420+5,y+55))
   im.paste(Image.open(run/f'preview-{theme}-384.png').convert('RGB').resize((180,180)),(k*420+80,y+25))
 im.save(B/f'candidates-{page}.png')
