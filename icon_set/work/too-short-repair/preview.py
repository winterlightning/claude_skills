from pathlib import Path
import json,io,sys
ROOT=Path(__file__).resolve().parents[3];sys.path.insert(0,str(ROOT))
from PIL import Image,ImageDraw,ImageFont
from icon_set.model.icons.registry import create
from icon_set.renderers.png import render_png
SOURCE_ICON_ID=None
SOURCE_PATH='icon_set/work/too-short-repair/queue.json'
AUTHOR='gpt-6'
W=Path(__file__).parent;rs=json.loads((W/'mapping.json').read_text());font=ImageFont.truetype('/System/Library/Fonts/Helvetica.ttc',11)
for theme,bg,ink in [('light','#f7f6f2','#17191d'),('dark','#17191d','#f7f6f2')]:
 for batch in range(6):
  im=Image.new('RGB',(1050,740),bg);d=ImageDraw.Draw(im)
  for k,r in enumerate(rs[batch*21:batch*21+21]):
   x=k%7*150;y=k//7*240;t=Image.open(io.BytesIO(render_png(create(r['original'] if r.get('blocked') else r['id']),scale=1,ink=ink)));im.paste(t,(x+50,y+15),t);t=Image.open(io.BytesIO(render_png(create(r['original'] if r.get('blocked') else r['id']),scale=2,ink=ink)));im.paste(t,(x+38,y+75),t)
   words=r['original'].split('-');line='';yy=y+180
   for word in words:
    if len(line)+len(word)>21:d.text((x+5,yy),line,font=font,fill=ink);line='';yy+=14
    line+=word+' '
   d.text((x+5,yy),line,font=font,fill=ink)
  im.save(W/f'after-{theme}-{batch+1}.png')
