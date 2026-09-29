from pathlib import Path
import json,sys
from PIL import Image,ImageDraw
ROOT=Path('icon_set/work/meaning-fixes-20260928')
R=json.loads((ROOT/'runs.json').read_text())
for a in range(0,20,5):
 s=Image.new('RGB',(1100,5*260),'#eee');d=ImageDraw.Draw(s)
 for j in range(5):
  n=a+j+1;r=R[str(n)];out=Path(r['result_dir']);y=j*260
  d.text((10,y+5),f'{n}. {r["id"]}',fill='black')
  for k,theme in enumerate(('light','dark')):
   im=Image.open(out/f'preview-{theme}-384.png').convert('RGB').resize((210,210))
   s.paste(im,(10+k*540,y+30));s.paste(Image.open(out/f'preview-{theme}-48.png').convert('RGB'),(250+k*540,y+100))
 s.save(ROOT/f'after-{a//5+1}.png')
