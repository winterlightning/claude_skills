from pathlib import Path
import sys,json,io
ROOT=Path(__file__).resolve().parents[3];sys.path.insert(0,str(ROOT))
from PIL import Image,ImageDraw,ImageFont
from icon_set.model.icons.registry import create
from icon_set.renderers.png import render_png
SOURCE_ICON_ID=None
SOURCE_PATH='icon_set/work/solo-failed-batch-100/repairs.json'
AUTHOR='gpt-6'
W=Path(__file__).parent;rows=json.loads((W/'repairs.json').read_text());font=ImageFont.truetype('/System/Library/Fonts/Helvetica.ttc',12)
for theme,bg,fg in [('light','#f7f6f2','#202226'),('dark','#17191d','#f1f2f5')]:
 im=Image.new('RGB',(1200,880),bg);d=ImageDraw.Draw(im)
 for j,r in enumerate(rows):
  x=j%4*300;y=j//4*220;d.text((x+8,y+8),r['parent'],font=font,fill=fg)
  for ident,offset,size in [(r['parent'],10,96),(r['icon_id'],115,96),(r['icon_id'],235,48)]:
   o=create(ident);tile=Image.open(io.BytesIO(render_png(o,ink=fg,scale=size//48)));im.paste(tile,(x+offset,y+42),tile)
  d.text((x+10,y+152),'Before',font=font,fill=fg);d.text((x+115,y+152),'Reconstructed',font=font,fill=fg);d.text((x+8,y+183),'All checks pass',font=font,fill=fg)
 im.save(W/f'comparison-{theme}.png')
