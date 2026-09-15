import json,io,math
from pathlib import Path
from PIL import Image,ImageDraw
import cairosvg
H=Path(__file__).resolve().parent; data=json.loads((H.parent/'report.json').read_text())
rows=[r for r in data['rows'] if r['status']=='retained']
# Count real SVG drawing runs separately from their constituent geometry.
import xml.etree.ElementTree as ET
for r in rows:
 r['strokes']=len(ET.fromstring(r['current']['svg']).findall('{http://www.w3.org/2000/svg}path'))
 r['segments']=sum(p['d'].count('C')+p['d'].count('L')+p['d'].count('A') for p in r['current']['paths'])
rows.sort(key=lambda r:(-r['segments'],r['id']))
(H/'baseline.json').write_text(json.dumps(rows))
for b in range(math.ceil(len(rows)/48)):
 im=Image.new('RGB',(1440,1200),'white');d=ImageDraw.Draw(im)
 for k,r in enumerate(rows[b*48:(b+1)*48]):
  x=k%6*240;y=k//6*150;s=r['current']['svg']
  for xx,sz,sw in [(4,112,'4'),(130,92,'.4')]:
   pic=Image.open(io.BytesIO(cairosvg.svg2png(bytestring=s.replace('currentColor','#142330').replace('stroke-width="4"',f'stroke-width="{sw}"').encode(),output_width=sz,output_height=sz)));im.paste(pic,(x+xx,y+4),pic)
  label=f'{b*48+k+1} {r["id"]}'
  d.text((x+4,y+118),label[:37],fill='black');d.text((x+4,y+132),label[37:]+f'  [{r["strokes"]} strokes / {r["segments"]} segments]',fill='#465d70')
 im.save(H/f'remaining-{b:02d}.png')
print(len(rows),'remaining, rendered',b+1,'sheets')
