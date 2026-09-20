import json,sys,io
from pathlib import Path
import xml.etree.ElementTree as ET
import cairosvg
from PIL import Image,ImageDraw
W=Path(__file__).parent;ROOT=W.resolve().parents[2];sys.path.insert(0,str(ROOT))
from icon_set.model.icons.registry import create
rows=json.loads((W/'candidates.json').read_text());results={}
for k,r in rows.items():
 m=create(r['icon']);q=m.validate_icon();results[k]=dict(r,status=q.status,findings=q.describe());print(k,q.describe(),flush=True)
 (W/'svg').mkdir(exist_ok=True);(W/'svg'/f'{k}.svg').write_text(m.to_svg())
(W/'results.json').write_text(json.dumps(results,indent=2))
for offset in range(0,50,10):
 im=Image.new('RGB',(1400,1100),'white');d=ImageDraw.Draw(im)
 for j in range(10):
  k=str(offset+j+1);x=(j%2)*700;y=(j//2)*220
  if k not in results:continue
  r=results[k];svg=(W/'svg'/f'{k}.svg').read_text();d.text((x+6,y+5),k+' '+r['icon'],fill='black');d.text((x+6,y+25),r['status'],fill='green' if r['status']=='valid' else 'red')
  root=ET.fromstring(svg)
  for e in root.iter():
   if 'stroke-width' in e.attrib:e.set('stroke-width','0.25')
  center=ET.tostring(root).decode()
  for doc,xx,sz,dark in [(svg,x+10,150,False),(center,x+210,150,False),(svg,x+425,32,False),(svg,x+555,32,True)]:
   if dark:
    tree=ET.fromstring(doc)
    for el in tree.iter():
     if el.get('stroke') and el.get('stroke')!='none':el.set('stroke','white')
    doc=ET.tostring(tree).decode();d.rectangle((xx-10,y+70,xx+int(ET.fromstring(doc).get('width','32'))+10,y+122),fill='#15252a')
   native_width=int(ET.fromstring(doc).get('width','32')) if sz==32 else sz
   png=cairosvg.svg2png(bytestring=doc.encode(),output_width=native_width,output_height=sz);p=Image.open(io.BytesIO(png)).convert('RGBA');im.paste(p,(xx,y+80 if sz==32 else y+50),p)
 im.save(W/f'after-{offset//10+1}.png')
