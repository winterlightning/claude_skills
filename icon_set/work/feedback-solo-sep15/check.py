from pathlib import Path
import sys,json,hashlib
ROOT=Path(__file__).resolve().parent/'snapshot';sys.path.insert(0,str(ROOT))
from icon_set.model.icons.registry import create
from icon_set.renderers.svg import render_svg
from icon_set.renderers.png import render_png
from PIL import Image,ImageDraw
from io import BytesIO
W=Path(__file__).parent;rs=json.loads((W/'revisions.json').read_text());done={}
for k,r in rs.items():
 if r['id'] in done:continue
 icon=create(r['id']);q=icon.validate_icon();done[r['id']]={'status':q.status,'description':q.describe(),'keyshape':icon.keyshape.name,'svg':render_svg(icon)}
 if q.status!='valid':print(k,r['id'],q.describe(),flush=True)
(W/'validation.json').write_text(json.dumps(done,indent=2))
items=list({r['id']:r for r in rs.values()}.values())
for start in range(0,len(items),25):
 for theme,ink,bg in [('light','#111111','#ffffff'),('dark','#f5f5f5','#17191d')]:
  batch=items[start:start+25];im=Image.new('RGB',(1200,((len(batch)+4)//5)*165),bg);d=ImageDraw.Draw(im)
  for j,r in enumerate(batch):
   x=(j%5)*240;y=(j//5)*165
   for id,dx,scale in [(r['parent'],3,1),(r['id'],62,1),(r['id'],127,2)]:
    try:png=Image.open(BytesIO(render_png(create(id),ink=ink,scale=scale)));im.paste(png,(x+dx,y+8),png)
    except Exception as e:print(id,e)
   d.text((x+4,y+111),str(r['brief_numbers'])+' '+r['parent'][:25],fill=ink)
   d.text((x+4,y+131),done[r['id']]['status'],fill=ink)
  im.save(W/f'comparison-{start//25+1}-{theme}.png')
print('RESULT',len(done),{s:sum(v['status']==s for v in done.values()) for s in ['valid','invalid','review']})
