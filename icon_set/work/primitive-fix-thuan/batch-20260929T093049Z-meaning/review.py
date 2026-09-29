from pathlib import Path
from PIL import Image,ImageDraw
import json,sys
b=Path(__file__).parent;rows=json.loads((b/'items.json').read_text())
indices=[int(x) for x in sys.argv[1:]] or list(range(1,len(rows)+1))
for page in range((len(indices)+4)//5):
 s=Image.new('RGB',(1120,850),'#ddd');d=ImageDraw.Draw(s)
 for j,n in enumerate(indices[page*5:page*5+5]):
  r=rows[n-1];y=j*170;d.text((10,y+10),str(n)+' '+r['icon_id'],fill='black')
  for k,t in enumerate(('light','dark')):
   run=Path(r['run']);im=Image.open(run/f'preview-{t}-384.png').convert('RGB').resize((144,144));s.paste(im,(530+k*245,y+20))
   im=Image.open(run/f'preview-{t}-48.png').convert('RGB');s.paste(im,(685+k*245,y+70))
 s.save(b/f'candidate-{page+1}.png')
