from pathlib import Path
import json,io,xml.etree.ElementTree as E
import cairosvg
from PIL import Image,ImageDraw
from icon_set.model.icons.registry import create
from icon_set.scripts.container_placement import root_svg,Artwork,artwork_group
OUT=Path(__file__).parent;baseline=json.loads((OUT/'baseline.json').read_text());variants=json.loads((OUT/'variants.json').read_text())
for theme in ['light','dark']:
 bg='#ffffff' if theme=='light' else '#202833';fg='#171b22' if theme=='light' else '#f5f7fb';im=Image.new('RGB',(1100,((len(variants)+4)//5)*170),bg);d=ImageDraw.Draw(im)
 for i,r in enumerate(variants):
  row=next(a for a in baseline['rows'] if baseline['hosts'][a[0]]['name']==r['parent'] and a[7]=='fail');sub=Artwork.read(baseline['subs'][row[1]]['svg32'],32);old=baseline['hosts'][row[0]]['svg'];new=create(r['variant'] if Path(r['module']).exists() else r['parent']).to_svg()
  xx=i%5*220;yy=i//5*170
  for k,(doc,center) in enumerate([(old,row[3:5]),(new,r['center'])]):
   root=root_svg();root.set('color',fg);root.append(artwork_group(Artwork.read(doc,64),'host',1,0,0,stroke=4));root.append(artwork_group(sub,'sub',1,center[0]-16,center[1]-16,stroke=4));svg=E.tostring(root,encoding='unicode');pic=Image.open(io.BytesIO(cairosvg.svg2png(bytestring=svg.encode(),output_width=80,output_height=80)));im.paste(pic,(xx+k*108+10,yy+5),pic)
   native=Image.open(io.BytesIO(cairosvg.svg2png(bytestring=svg.encode(),output_width=64,output_height=64)));im.paste(native,(xx+k*108+18,yy+88),native)
  d.text((xx+3,yy+153),str(i)+' '+r['parent'][:29],fill=fg)
 im.save(OUT/(theme+'-review.png'))
