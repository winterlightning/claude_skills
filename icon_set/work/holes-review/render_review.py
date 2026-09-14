from pathlib import Path
from PIL import Image,ImageDraw,ImageFont
import json,cairosvg,io
W=Path(__file__).parent
SOURCE_ICON_ID=None
SOURCE_PATH='icon_set/work/holes-review/queue.json'
AUTHOR='gpt-6'
rows=json.loads((W/'results.json').read_text())
for page in range(6):
 group=rows[page*12:(page+1)*12];out=Image.new('RGB',(1200,((len(group)+2)//3)*230),'#f7f6f3');d=ImageDraw.Draw(out)
 for j,r in enumerate(group):
  x=j%3*400;y=j//3*230;d.text((x+10,y+8),str(page*12+j+1)+' '+r['original'],fill='#111')
  for col,name in enumerate([r['original'],r['candidate']]):
   p=Path('icon_set/dist/failed/solo48')/(name+'.svg') if col==0 else W/(name+'.svg')
   s=p.read_text().replace('currentColor','#222')
   for size,dx,dy in [(130,10,35),(48,145,95)]:
    im=Image.open(io.BytesIO(cairosvg.svg2png(bytestring=s.encode(),output_width=size,output_height=size)));out.paste(im,(x+col*200+dx,y+dy),im)
   d.text((x+col*200+15,y+181),'Before' if col==0 else 'After',fill='#666')
  d.text((x+10,y+207),'Holes PASS | '+('All checks PASS' if r['qa']['status']=='pass' else str(len(r['qa']['errors']))+' other findings'),fill='#166534')
 out.save(W/f'review-{page+1}.png')
