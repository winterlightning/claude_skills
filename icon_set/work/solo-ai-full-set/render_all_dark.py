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
w=Path(__file__).parent;rows=json.loads((w/'pending.json').read_text())
for off in range(0,len(rows),48):
 im=Image.new('RGB',(1200,1200),'#191d24');d=ImageDraw.Draw(im)
 for k,r in enumerate(rows[off:off+48]):
  x=k%6*200;y=k//6*150;i=create(r['icon_id'])
  for scale,dx in [(2,4),(1,122)]:
   p=Image.open(BytesIO(render_png(i,scale=scale,ink='#f3f4f6'))).convert('RGBA');im.paste(p,(x+dx,y+3),p)
  d.text((x+4,y+108),f"{off+k+1} {r['icon_id']}"[:33],fill='#f3f4f6')
 im.save(w/f'before-dark-{off//48+1:02}.png')
print('Rendered all dark sheets')
