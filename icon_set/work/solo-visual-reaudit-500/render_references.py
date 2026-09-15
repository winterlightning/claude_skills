from pathlib import Path
import json,ast,io
from PIL import Image,ImageDraw
import cairosvg
W=Path(__file__).parent
rows=json.load(open('icon_set/work/solo-remaining-repair/review-decisions.json'))
nums=json.load(open(W/'human-numbers.json'))
for page in range((len(nums)+19)//20):
 im=Image.new('RGB',(1100,880),'white');pen=ImageDraw.Draw(im)
 for j,n in enumerate(nums[page*20:page*20+20]):
  r=rows[n-1];t=ast.parse(Path(r['file']).read_text());p=next(x.value.value for x in t.body if isinstance(x,ast.Assign) and any(getattr(y,'id',None)=='SOURCE_PATH' for y in x.targets));x=j%5*220;y=j//5*220
  pen.text((x+3,y),f'{n} {r["selected"][:29]}',fill='black')
  if p and Path(p).exists():
   v=Image.open(io.BytesIO(cairosvg.svg2png(url=p,output_width=190,output_height=190)));im.paste(v,(x+10,y+24),v)
 im.save(W/f'human-refs-{page+1}.png')
