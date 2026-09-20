import json,io,inspect,sys
from pathlib import Path
import xml.etree.ElementTree as ET
import cairosvg
from PIL import Image,ImageDraw
ROOT=Path(__file__).resolve().parents[3];sys.path.insert(0,str(ROOT))
from icon_set.model.icons.registry import create,factories
W=Path(__file__).parent
rows=json.loads((W/'batch.json').read_text());f=factories()
def paste(im,svg,x,y,size):
 try:
  png=cairosvg.svg2png(bytestring=svg.encode(),output_width=size,output_height=size)
  a=Image.open(io.BytesIO(png)).convert('RGBA');im.paste(a,(x,y),a)
 except Exception as e: print(e)
for off in range(0,50,10):
 im=Image.new('RGB',(1250,1150),'#ffffff');d=ImageDraw.Draw(im)
 for i,r in enumerate(rows[off:off+10]):
  x=(i%2)*625;y=(i//2)*230;uid=r['icon'];model=create(uid);svg=model.to_svg()
  mod=sys.modules[f[uid].__module__];src=Path(mod.SOURCE_PATH);src=src if src.is_absolute() else ROOT/src
  source=src.read_text() if src.exists() else svg
  r['source_path']=str(src);r['source_available']=src.exists()
  d.text((x+6,y+5),str(r['number'])+' '+uid,fill='black');d.text((x+10,y+25),'Original                  SUB32                    Centerline',fill='black')
  paste(im,source,x+10,y+50,145);paste(im,svg,x+190,y+50,145)
  root=ET.fromstring(svg)
  for e in root.iter():
   if 'stroke-width' in e.attrib:e.set('stroke-width','0.25')
  paste(im,ET.tostring(root).decode(),x+370,y+50,145)
  paste(im,svg,x+560,y+55,32)
  d.rectangle((x+550,y+105,x+604,y+160),fill='#17252a');paste(im,svg.replace('#000000','#ffffff').replace('stroke="black"','stroke="white"'),x+560,y+115,32)
 im.save(W/f'before-{off//10+1}.png')
(W/'batch.json').write_text(json.dumps(rows,indent=2))
(W/'sources.txt').write_text('\n\n'.join(f'#### {r["number"]} {r["icon"]}\n'+Path(r['python_source']).read_text() for r in rows))
