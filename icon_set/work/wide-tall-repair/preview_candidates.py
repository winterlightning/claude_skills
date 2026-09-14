from repair_geometry import *
from PIL import Image,ImageDraw,ImageFont
from icon_set.renderers.png import render_png
import io
SOURCE_ICON_ID=None
SOURCE_PATH='icon_set/work/wide-tall-repair/targets.json'
AUTHOR='gpt-6'
rows=[(f.stem,json.loads(f.read_text())) for f in sorted((W/'candidates').glob('*.json')) if f.stem!='figured-ceremonial-urn'];font=ImageFont.truetype('/System/Library/Fonts/Helvetica.ttc',11)
for theme,bg,fg in [('light','#faf9f6','#202226'),('dark','#17191d','#f1f2f5')]:
 for page in range((len(rows)+29)//30):
  batch=rows[page*30:(page+1)*30];im=Image.new('RGB',(1250,((len(batch)+4)//5)*185),bg);d=ImageDraw.Draw(im)
  for n,(id,x) in enumerate(batch):
   px=n%5*250;py=n//5*185;d.text((px+4,py+4),id,font=font,fill=fg);o=model(id,x['record'])
   for icon,dx,scale,dy in [(create(id),6,2,24),(o,132,2,24),(o,176,1,134)]:
    tile=Image.open(io.BytesIO(render_png(icon,ink=fg,scale=scale)));im.paste(tile,(px+dx,py+dy),tile)
   d.text((px+6,py+122),'Before',font=font,fill=fg);d.text((px+132,py+122),'After',font=font,fill=fg)
  im.save(W/f'preview-{theme}-{page+1}.png')
