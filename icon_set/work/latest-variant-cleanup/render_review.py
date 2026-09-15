from pathlib import Path
import json,io,xml.etree.ElementTree as ET
import cairosvg
from PIL import Image,ImageDraw
SOURCE_ICON_ID=None
SOURCE_PATH='icon_set/work/latest-variant-cleanup/needs-repair.json'
AUTHOR='gpt-6'
W=Path(__file__).parent
names=[g['root'] for g in json.loads((W/'needs-repair.json').read_text())]+['hermes-with-winged-helmet','jet-ski-rider-jumping-a-wave','sledding-person']
for page in range((len(names)+8)//9):
 im=Image.new('RGB',(1350,1050),'#eee');d=ImageDraw.Draw(im)
 for j,n in enumerate(names[page*9:(page+1)*9]):
  x=j%3*450;y=j//3*350;p=W/(n+'.svg');old=W/'before'/(n+'.svg')
  if not old.exists():old=Path('icon_set/dist/failed/solo48')/(n+'-v2.svg')
  if n=='hermes-with-winged-helmet':old=W/'hermes-before.svg'
  for k,f in enumerate([old,p]):
   if not f.exists():continue
   tile=Image.open(io.BytesIO(cairosvg.svg2png(url=str(f),output_width=170,output_height=170))).convert('RGBA');im.paste(tile,(x+25+k*210,y+5),tile)
  d.text((x+10,y+183),n,fill='black');d.text((x+25,y+203),'Latest version before repair       Final canonical',fill='black')
  for k,(bg,fg) in enumerate([('white','black'),('#18181b','white')]):
   root=ET.fromstring(p.read_text())
   for e in root.iter():
    if e.get('stroke') and e.get('stroke')!='none':e.set('stroke',fg)
    if e.get('fill')=='black':e.set('fill',fg)
   tile=Image.open(io.BytesIO(cairosvg.svg2png(bytestring=ET.tostring(root),output_width=48,output_height=48,background_color=bg))).convert('RGB');im.paste(tile,(x+25+k*68,y+245))
  for e in root.iter():
   if e.get('stroke-width'):e.set('stroke-width','0.5')
   if e.get('stroke') and e.get('stroke')!='none':e.set('stroke','#1687c2')
  tile=Image.open(io.BytesIO(cairosvg.svg2png(bytestring=ET.tostring(root),output_width=110,output_height=110))).convert('RGBA');im.paste(tile,(x+250,y+225),tile)
 im.save(W/f'after-{page}.png')
