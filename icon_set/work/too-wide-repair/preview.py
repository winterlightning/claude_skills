from pathlib import Path
import json,sys,io,html
ROOT=Path(__file__).resolve().parents[3];sys.path.insert(0,str(ROOT))
from icon_set.model.icons.registry import create
from icon_set.renderers.png import render_png
from icon_set.renderers.svg import render_svg
from PIL import Image,ImageDraw,ImageFont
SOURCE_ICON_ID=None
SOURCE_PATH='icon_set/work/too-wide-repair/queue.json'
AUTHOR='gpt-6'
W=Path(__file__).parent;rows=json.loads((W/'mapping.json').read_text());font=ImageFont.truetype('/System/Library/Fonts/Helvetica.ttc',12)
for theme,bg,ink in [('light','#f7f6f2','#171717'),('dark','#17191d','#f6f6f2')]:
 im=Image.new('RGB',(1250,6*165),bg);d=ImageDraw.Draw(im)
 for i,r in enumerate(rows):
  x=i%5*250;y=i//5*165
  try:
   t=Image.open(io.BytesIO(render_png(create(r['id']),ink=ink,scale=2)));im.paste(t,(x+75,y+10),t)
   native=Image.open(io.BytesIO(render_png(create(r['id']),ink=ink)));im.paste(native,(x+190,y+55),native)
  except Exception:pass
  d.text((x+10,y+122),r['original'],font=font,fill=ink)
 im.save(W/f'after-{theme}.png')
