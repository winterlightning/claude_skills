import sys,json,hashlib,io,math
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3];sys.path.insert(0,str(ROOT))
from icon_set.model.icons.registry import create
from icon_set.model.primitives import Arc,Bezier
from PIL import Image,ImageDraw
import cairosvg
HERE=Path(__file__).parent
rows=json.loads((ROOT/'icon_set/work/intersection-review-977/cohort.json').read_text())
if __name__=='__main__':
 records=[]
 for row in rows:
  p=ROOT/row['python_source']['path'];b=HERE/'before'/p.name
  if not b.exists():b.write_bytes(p.read_bytes())
  icon=create(row['icon_id']);records.append(dict(id=row['icon_id'],source=row['python_source']['path'],sha256=hashlib.sha256(p.read_bytes()).hexdigest(),svg=icon.to_svg(),curved=any(isinstance(p,(Arc,Bezier)) for p in icon.primitives)))
 (HERE/'before.json').write_text(json.dumps(records))
 curved=[r for r in records if r['curved']]
 for batch in range(math.ceil(len(curved)/36)):
  im=Image.new('RGB',(1440,1080),'#fff');d=ImageDraw.Draw(im)
  for k,r in enumerate(curved[batch*36:(batch+1)*36]):
   x=k%6*240;y=k//6*180;s=r['svg'];pic=Image.open(io.BytesIO(cairosvg.svg2png(bytestring=s.replace('currentColor','#101820').encode(),output_width=128,output_height=128)));im.paste(pic,(x+6,y+4),pic)
   line=s.replace('stroke-width="4"','stroke-width="0.5"').replace('currentColor','#176ee6');pic=Image.open(io.BytesIO(cairosvg.svg2png(bytestring=line.encode(),output_width=96,output_height=96)));im.paste(pic,(x+139,y+20),pic)
   label=f'{batch*36+k+1} '+r['id'];d.text((x+5,y+140),label[:33],fill='black');d.text((x+5,y+154),label[33:66],fill='black')
  im.save(HERE/f'curves-{batch:02d}.png')
 print('Curved:',len(curved),'of',len(records))
