from pathlib import Path
import json,io,cairosvg
from PIL import Image,ImageDraw
B=Path(__file__).parent
rows=json.loads((B/'staged.json').read_text())
for page in range((len(rows)+4)//5):
 c=Image.new('RGB',(760,1000),'#dddddd');d=ImageDraw.Draw(c)
 for n,r in enumerate(rows[page*5:page*5+5]):
  i=r['item'];y=n*200;d.text((5,y+2),i['key'],fill='black');d.text((5,y+18),'Original                            Rejected',fill='black')
  for j,p in enumerate([Path(r['reference']),Path(r['result_dir'])/'before'/(i['icon_id']+'.svg')]):
   raw=cairosvg.svg2png(url=str(p),output_width=160,output_height=160,background_color='white')
   im=Image.open(io.BytesIO(raw)).convert('RGB');c.paste(im,(j*370+30,y+38))
 c.save(B/f'comparison-{page}.png')
for n,r in enumerate(rows):print(n,r['key'],repr(r['item'].get('feedback')))
