from pathlib import Path
import sys,json,io,hashlib,xml.etree.ElementTree as ET
sys.path.insert(0,str(Path.cwd()))
from PIL import Image,ImageDraw
import cairosvg
from icon_set.model.icons.registry import create
W=Path(__file__).parent
SOURCE_ICON_ID=None
SOURCE_PATH='plan.json'
AUTHOR='gpt-6'
plans=json.loads((W/'plan.json').read_text());select=set(sys.argv[1:]);plans=[r for r in plans if not select or r['icon_id'] in select or r['action'] in select]
results=[]
for r in plans:
 try:
  icon=create(r['new_id']);v=icon.validate_icon();svg=icon.to_svg();(W/(r['new_id']+'.svg')).write_text(svg);q={'icon_id':r['icon_id'],'new_id':r['new_id'],'status':v.status,'description':v.describe(),'sha256':hashlib.sha256(svg.encode()).hexdigest()};print(r['icon_id'],v.describe(),flush=True)
 except Exception as e:q={'icon_id':r['icon_id'],'new_id':r['new_id'],'status':'error','description':str(e)};print(q,flush=True)
 results.append(q)
(W/'latest-check.json').write_text(json.dumps(results,indent=2))
for page in range((len(plans)+7)//8):
 im=Image.new('RGB',(1400,1040),'#edf1f2');d=ImageDraw.Draw(im)
 for j,r in enumerate(plans[page*8:page*8+8]):
  x=j%2*700;y=j//2*260;d.text((x+8,y+8),r['icon_id'],fill='black')
  for k,p in enumerate([Path('icon_set/work/rejected-solo-review-50-sep15')/(r['icon_id']+'.svg'),W/(r['new_id']+'.svg')]):
   if not p.exists():continue
   svg=p.read_bytes();z=Image.open(io.BytesIO(cairosvg.svg2png(bytestring=svg,output_width=150,output_height=150))).convert('RGBA');im.paste(z,(x+10+k*165,y+35),z)
  p=W/(r['new_id']+'.svg')
  if not p.exists():continue
  root=ET.fromstring(p.read_text())
  for k,fg,bg in [(0,'black','white'),(1,'white','#18181b')]:
   for e in root.iter():
    if e.get('stroke') and e.get('stroke')!='none':e.set('stroke',fg)
   z=Image.open(io.BytesIO(cairosvg.svg2png(bytestring=ET.tostring(root),output_width=48,output_height=48,background_color=bg))).convert('RGBA');im.paste(z,(x+355+65*k,y+90),z)
  for e in root.iter():
   if e.get('stroke-width'):e.set('stroke-width','.45')
   if e.get('stroke') and e.get('stroke')!='none':e.set('stroke','#1786b0')
  z=Image.open(io.BytesIO(cairosvg.svg2png(bytestring=ET.tostring(root),output_width=150,output_height=150))).convert('RGBA');im.paste(z,(x+520,y+35),z)
  d.text((x+8,y+198),'Before                 After                48px light/dark          Centerline',fill='black')
 im.save(W/f'current-{page+1}.png')
