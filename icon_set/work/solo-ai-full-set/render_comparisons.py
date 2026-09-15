from pathlib import Path
import sys,json
from io import BytesIO
from PIL import Image,ImageDraw
ROOT=Path(__file__).resolve().parents[3];sys.path.insert(0,str(ROOT))
from icon_set.model.icons.registry import create
from icon_set.renderers.png import render_png
SOURCE_ICON_ID=None
SOURCE_PATH='icon_set/work/solo-ai-full-set/batch.json'
AUTHOR='gpt-6'
w=Path(__file__).parent;rows=json.loads((w/'batch.json').read_text())
for theme in ['light','dark']:
 bg,fg=('white','#111111') if theme=='light' else ('#191d24','#f3f4f6')
 for off in range(0,len(rows),20):
  im=Image.new('RGB',(1200,800),bg);d=ImageDraw.Draw(im)
  for k,r in enumerate(rows[off:off+20]):
   x=k%4*300;y=k//4*160
   for n,dx in [(r['parent'],0),(r['icon_id'],150)]:
    i=create(n)
    for scale,sx in [(2,0),(1,98)]:
     p=Image.open(BytesIO(render_png(i,scale=scale,ink=fg))).convert('RGBA');im.paste(p,(x+dx+sx,y+8),p)
   d.text((x+4,y+113),f"{off+k+1}. {r['parent']}"[:43],fill=fg)
   d.text((x+4,y+133),'Original                       Revised',fill=fg)
  im.save(w/f'compare-{theme}-{off//20+1:02}.png')
