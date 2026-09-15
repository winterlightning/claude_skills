from pathlib import Path
import json,io,xml.etree.ElementTree as ET
import cairosvg
from PIL import Image,ImageDraw
AUTHOR='gpt-6'
SOURCE_ICON_ID=None
SOURCE_PATH='icon_set/work/latest-variant-cleanup/additional-needs-repair.json'
W=Path(__file__).parent
names=[g['root'] for g in json.loads((W/'additional-needs-repair.json').read_text())]+['aircraft-releasing-bomb']
im=Image.new('RGB',(1200,600),'#eee');d=ImageDraw.Draw(im)
for j,n in enumerate(names):
 x=j%4*300;y=j//4*300;p=W/(n+'.svg');s=p.read_bytes()
 tile=Image.open(io.BytesIO(cairosvg.svg2png(bytestring=s,output_width=170,output_height=170))).convert('RGBA');im.paste(tile,(x+65,y+5),tile)
 d.text((x+10,y+182),n,fill='black')
 for k,(bg,fg) in enumerate([('white','black'),('#18181b','white')]):
  root=ET.fromstring(s)
  for e in root.iter():
   if e.get('stroke') and e.get('stroke')!='none':e.set('stroke',fg)
   if e.get('fill')=='black':e.set('fill',fg)
  tile=Image.open(io.BytesIO(cairosvg.svg2png(bytestring=ET.tostring(root),output_width=48,output_height=48,background_color=bg))).convert('RGB');im.paste(tile,(x+15+k*60,y+220))
 for e in root.iter():
  if e.get('stroke-width'):e.set('stroke-width','0.5')
  if e.get('stroke') and e.get('stroke')!='none':e.set('stroke','#1687c2')
 tile=Image.open(io.BytesIO(cairosvg.svg2png(bytestring=ET.tostring(root),output_width=95,output_height=95))).convert('RGBA');im.paste(tile,(x+175,y+205),tile)
im.save(W/'additional-after.png')
