from pathlib import Path
import sys,json,io,textwrap
ROOT=Path(__file__).resolve().parents[3];sys.path.insert(0,str(ROOT))
import cairosvg
from PIL import Image,ImageDraw
from icon_set.model.icons.registry import create
OUT=Path(__file__).resolve().parent;draft=OUT/'draft-svg';draft.mkdir(exist_ok=True)
rows=json.loads((OUT/'complete-models.json').read_text());rows.sort(key=lambda r:r['number']);im=Image.new('RGB',(1200,((len(rows)+5)//6)*180),'#eef1e9');d=ImageDraw.Draw(im)
for i,r in enumerate(rows):
 s=create(r['icon_id']).to_svg();(draft/(r['icon_id']+'.svg')).write_text(s);x=i%6*200;y=i//6*180
 d.rectangle((x+4,y+4,x+196,y+174),fill='white')
 for scale,dx in [(1,10),(2,78)]:
  a=Image.open(io.BytesIO(cairosvg.svg2png(bytestring=s.encode(),scale=scale))).convert('RGBA');im.paste(a,(x+dx,y+8),a)
 for j,line in enumerate(textwrap.wrap(str(r['number'])+'. '+r['icon_id'],26)):d.text((x+9,y+112+j*15),line,fill='black')
im.save(OUT/'all-models-review.png')
