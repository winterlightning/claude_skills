import json,sys
from pathlib import Path
from PIL import Image,ImageDraw
root=Path(__file__).parent;rows=json.loads((root/'claims.json').read_text())
ids=list(map(int,sys.argv[1:])) if sys.argv[1:] else list(range(len(rows)))
for page in range((len(ids)+4)//5):
 im=Image.new('RGB',(600,1100),'white');d=ImageDraw.Draw(im)
 for n,i in enumerate(ids[page*5:page*5+5]):
  r=rows[i];d.text((5,n*220),str(i)+' '+r['key'],fill='black')
  for j,t in enumerate(('light','dark')):
   p=Path(r['run']);im.paste(Image.open(p/f'preview-{t}-384.png').resize((175,175)),(j*300,n*220+25));im.paste(Image.open(p/f'preview-{t}-48.png'),(j*300+200,n*220+70))
 im.save(root/f'after-{page}.png')
