from pathlib import Path
import sys,json,io
ROOT=Path(__file__).resolve().parents[3];sys.path.insert(0,str(ROOT))
from icon_set.model.icons.registry import create
from icon_set.renderers.png import render_png
from PIL import Image,ImageDraw,ImageFont
W=Path(__file__).parent
SOURCE_ICON_ID=None
SOURCE_PATH='icon_set/work/neck-tail-repair/results.json'
AUTHOR='gpt-6'
rows=json.loads((W/'results.json').read_text());font=ImageFont.truetype('/System/Library/Fonts/Helvetica.ttc',14)
for theme,bg,fg in [('light','#f7f6f2','#22262c'),('dark','#17191d','#f1f2f5')]:
 im=Image.new('RGB',(1050,320),bg);d=ImageDraw.Draw(im)
 for i,r in enumerate(rows):
  x=i*350;d.text((x+12,12),r['id'],font=font,fill=fg)
  for ident,dx in [(r['original'],12),(r['id'],180)]:
   obj=create(ident);tile=Image.open(io.BytesIO(render_png(obj,ink=fg,scale=3)));im.paste(tile,(x+dx,48),tile)
  d.text((x+12,205),'Before',font=font,fill=fg);d.text((x+180,205),'After',font=font,fill=fg)
  tile=Image.open(io.BytesIO(render_png(create(r['id']),ink=fg)));im.paste(tile,(x+150,245),tile)
 im.save(W/f'preview-{theme}.png')
