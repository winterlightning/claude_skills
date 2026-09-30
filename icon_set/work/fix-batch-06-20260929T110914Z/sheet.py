from pathlib import Path
import json,sys,io,cairosvg
from PIL import Image,ImageDraw
out=Path(__file__).parent;rows=json.loads((out/'claims.json').read_text());ids=list(map(int,sys.argv[1:])) if len(sys.argv)>1 else list(range(20))
for part in range((len(ids)+4)//5):
 chunk=ids[part*5:part*5+5];sheet=Image.new('RGB',(1050,len(chunk)*230),'#ddd');d=ImageDraw.Draw(sheet)
 for j,i in enumerate(chunk):
  r=rows[i];p=out/f'latest-{i}.txt'
  if not p.exists():continue
  run=Path(p.read_text());d.text((5,j*230+3),str(i)+' '+r['id'],fill='black')
  for k,s in enumerate([r['reference'],r['before'],str(run/(r['id']+'.svg'))]):
   img=Image.open(io.BytesIO(cairosvg.svg2png(url=s,output_width=180,output_height=180,background_color='white'))).convert('RGB');sheet.paste(img,(5+k*205,j*230+24))
  for k,t in enumerate(['light','dark']):
   im=Image.open(run/f'preview-{t}-48.png').convert('RGB');sheet.paste(im,(635+k*80,j*230+75))
 sheet.save(out/f'after-{part}.png')
