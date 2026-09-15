from pathlib import Path
import json,sys,io
from PIL import Image,ImageDraw
ROOT=Path(__file__).resolve().parents[3];sys.path.insert(0,str(ROOT))
from icon_set.model.icons.registry import create
from icon_set.renderers.png import render_png
w=Path(__file__).parent;rows=json.loads((w/'batch.json').read_text())
for theme,bg,ink in [('light','#fff','#111'),('dark','#171a1c','#f4f4f4')]:
 for start in (0,6):
  sheet=Image.new('RGB',(1020,600),bg);d=ImageDraw.Draw(sheet)
  for j,r in enumerate(rows[start:start+6]):
   x=j%2*510;y=j//2*200;d.text((x+8,y+5),r['parent'],fill=ink)
   for col,(n,label) in enumerate([(r['parent'],'Original'),(r['previous'],'Previous'),(r['icon_id'],'New')]):
    for scale,dx,dy in [(2,0,30),(1,105,60)]:
     p=Image.open(io.BytesIO(render_png(create(n),scale=scale,ink=ink)));sheet.paste(p,(x+col*170+dx,y+dy),p)
    d.text((x+col*170+15,y+145),label,fill=ink)
  sheet.save(w/f'{theme}-{start//6+1}.png')
