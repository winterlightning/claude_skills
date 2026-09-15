from pathlib import Path
import sys,json
from io import BytesIO
from PIL import Image,ImageDraw
ROOT=Path(__file__).resolve().parents[3];sys.path.insert(0,str(ROOT))
from icon_set.model.icons.registry import create
from icon_set.renderers.png import render_png
SOURCE_ICON_ID=None
SOURCE_PATH='icon_set/work/solo-ai-full-set/pending.json'
AUTHOR='gpt-6'
w=Path(__file__).parent
names=json.loads((w/'focus.json').read_text())
for theme in ['light','dark']:
 bg,fg=('white','#111111') if theme=='light' else ('#191d24','#f3f4f6')
 im=Image.new('RGB',(1200,((len(names)+5)//6)*150),bg);d=ImageDraw.Draw(im)
 for k,n in enumerate(names):
  i=create(n);x=k%6*200;y=k//6*150
  for scale,dx in [(2,4),(1,122)]:
   p=Image.open(BytesIO(render_png(i,scale=scale,ink=fg))).convert('RGBA');im.paste(p,(x+dx,y+3),p)
  d.text((x+4,y+108),n[:29],fill=fg)
 im.save(w/f'focus-{theme}.png')
