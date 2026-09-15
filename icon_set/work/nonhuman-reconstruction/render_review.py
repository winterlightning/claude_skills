"""Render before/after, native themes and centerline evidence for human review."""
from pathlib import Path
import json,io,xml.etree.ElementTree as ET
from PIL import Image,ImageDraw
import cairosvg
W=Path(__file__).parent
items=[i for i in json.loads((W/'audit.json').read_text()) if i['audit_status']=='reconstructed']
(W/'before-svg').mkdir(exist_ok=True)
for page in range((len(items)+11)//12):
 s=Image.new('RGB',(1400,990),'#ededed');d=ImageDraw.Draw(s)
 for j,i in enumerate(items[page*12:(page+1)*12]):
  p=W/(i['icon_id']+'.svg');old=W/'before-svg'/i['svg'];dist=Path('icon_set/dist/failed/solo48')/i['svg']
  if not old.exists() and dist.exists():old.write_bytes(dist.read_bytes())
  if not p.exists():continue
  x=j%4*350;y=j//4*330
  for k,path in enumerate([old,p]):
   if not path.exists():continue
   im=Image.open(io.BytesIO(cairosvg.svg2png(url=str(path),output_width=150,output_height=150))).convert('RGBA');s.paste(im,(x+8+k*170,y+10),im)
  d.text((x+5,y+170),i['icon_id'],fill='black');d.text((x+5,y+188),'Before                     Reconstructed',fill='black')
  for k,(bg,fg) in enumerate([('white','black'),('#18181b','white')]):
   root=ET.fromstring(p.read_text())
   for e in root.iter():
    if e.get('stroke') and e.get('stroke')!='none':e.set('stroke',fg)
   im=Image.open(io.BytesIO(cairosvg.svg2png(bytestring=ET.tostring(root),output_width=48,output_height=48,background_color=bg))).convert('RGB');s.paste(im,(x+5+k*60,y+215))
  for e in root.iter():
   if e.get('stroke-width'):e.set('stroke-width','0.5')
   if e.get('stroke') and e.get('stroke')!='none':e.set('stroke','#1687c2')
  im=Image.open(io.BytesIO(cairosvg.svg2png(bytestring=ET.tostring(root),output_width=110,output_height=110))).convert('RGBA');s.paste(im,(x+190,y+210),im)
 s.save(W/f'after-{page+1}.png')
print(len(items),'icons rendered')
