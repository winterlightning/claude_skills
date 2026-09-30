from pathlib import Path
import json
from PIL import Image,ImageDraw
p=Path(__file__).parent;rows=json.loads((p/'runs.json').read_text());claims=json.loads((p/'claims.json').read_text())
for start in range(0,20,5):
 sh=Image.new('RGB',(740,1100),'#ddd');d=ImageDraw.Draw(sh)
 for i in range(start,start+5):
  r=Path(rows[str(i)]);y=(i-start)*220;d.text((4,y+4),str(i+1)+' '+claims[i]['key'],fill='black')
  for j,t in enumerate(['light','dark']):
   im=Image.open(r/f'preview-{t}-384.png').resize((170,170));sh.paste(im,(20+j*350,y+25));im=Image.open(r/f'preview-{t}-48.png');sh.paste(im,(210+j*350,y+90))
 sh.save(p/f'drafts-{start//5+1}.png')
