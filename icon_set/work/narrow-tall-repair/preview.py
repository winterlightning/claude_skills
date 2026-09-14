from pathlib import Path
import sys,json,io,html
ROOT=Path(__file__).resolve().parents[3];sys.path.insert(0,str(ROOT))
from PIL import Image,ImageDraw,ImageFont
from icon_set.model.icons.registry import create
from icon_set.renderers.png import render_png
SOURCE_ICON_ID=None
SOURCE_PATH='icon_set/work/narrow-tall-repair/results.json'
AUTHOR='gpt-6'
W=Path(__file__).parent;rows=json.loads((W/'results.json').read_text());font=ImageFont.truetype('/System/Library/Fonts/Helvetica.ttc',12)
for theme,bg,fg in [('light','#faf9f6','#202226'),('dark','#17191d','#f1f2f5')]:
 im=Image.new('RGB',(1250,((len(rows)+4)//5)*190),bg);d=ImageDraw.Draw(im)
 for n,r in enumerate(rows):
  x=n%5*250;y=n//5*190;d.text((x+6,y+5),r['original'],font=font,fill=fg)
  for ident,dx in [(r['original'],12),(r['id'],135)]:
   o=create(ident);tile=Image.open(io.BytesIO(render_png(o,ink=fg,scale=2)));im.paste(tile,(x+dx,y+26),tile)
  d.text((x+12,y+126),'Before',font=font,fill=fg);d.text((x+135,y+126),'After',font=font,fill=fg)
  tile=Image.open(io.BytesIO(render_png(create(r['id']),ink=fg)));im.paste(tile,(x+174,y+140),tile)
 im.save(W/f'preview-{theme}.png')
