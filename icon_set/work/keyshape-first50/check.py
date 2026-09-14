"""Validate and render the frozen sample from its current Python models."""
SOURCE_ICON_ID = None
SOURCE_PATH = 'selection.json'
AUTHOR = 'gpt-6'
import sys,json,io
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3];sys.path.insert(0,str(ROOT));W=Path(__file__).parent
from icon_set.model.icons.registry import create
from icon_set.validation.envelope import visible_bounds
from icon_set.renderers.png import render_png
from PIL import Image,ImageDraw
rows=[];s=json.loads((W/'selection.json').read_text())
for theme in ['light','dark']:
 bg,ink=('#ffffff','#151719') if theme=='light' else ('#17191d','#f0f2f5')
 im=Image.new('RGB',(1000,1200),bg);d=ImageDraw.Draw(im)
 for n,i in enumerate(s):
  o=create(i['id'])
  if theme=='light':
   r=o.validate_icon();row={'number':n+1,'id':i['id'],'keyshape':o.keyshape.name,'bounds':visible_bounds(o.primitives),'status':r.status,'report':r.describe()};rows.append(row)
   if r.status!='valid':print(n+1,i['id'],r.describe(),flush=True)
  x=(n%5)*200;y=(n//5)*120
  pic=Image.open(io.BytesIO(render_png(o,ink=ink,scale=1)))
  im.paste(pic,(x+14,y+22),pic)
  pic=Image.open(io.BytesIO(render_png(o,ink=ink,scale=2)))
  im.paste(pic,(x+88,y),pic)
  d.text((x+4,y+99),str(n+1)+' '+i['id'],fill=ink)
 im.save(W/f'after-{theme}.png')
(W/'results.json').write_text(json.dumps(rows,indent=2))
print('VALID',sum(r['status']=='valid' for r in rows),'/',len(rows))
