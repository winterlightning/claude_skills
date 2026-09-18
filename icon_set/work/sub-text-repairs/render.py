import json,io
from pathlib import Path
import cairosvg
from PIL import Image,ImageDraw,ImageFont
D=Path('icon_set/work/sub-text-repairs');rs=json.loads((D/'repairs.json').read_text());font=ImageFont.truetype('/System/Library/Fonts/Supplemental/Arial.ttf',16)
for offset in range(0,len(rs),9):
 out=Image.new('RGB',(1500,1440),'white');draw=ImageDraw.Draw(out)
 for i,a in enumerate(rs[offset:offset+9]):
  y=i*160;draw.text((10,y+2),f"{offset+i+1}. {a['name']}",fill='black',font=font)
  for x,p in [(10,D/'before'/Path(a['old']).name),(600,Path(a['repair_svg']))]:
   im=Image.open(io.BytesIO(cairosvg.svg2png(url=str(p),scale=4))).convert('RGBA');ratio=min(2/4,(880 if x==600 else 560)/im.width);im=im.resize((round(im.width*ratio),round(im.height*ratio)),Image.Resampling.LANCZOS);out.paste(im,(x,y+32),im)
   native=Image.open(io.BytesIO(cairosvg.svg2png(url=str(p)))).convert('RGBA');out.paste(native,(x,y+108),native)
  draw.line((0,y+159,1500,y+159),fill='#dddddd')
 out.save(D/f'repairs-{offset//9+1}.png')
