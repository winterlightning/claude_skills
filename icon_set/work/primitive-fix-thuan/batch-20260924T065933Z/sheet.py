from pathlib import Path
from PIL import Image,ImageDraw
runs=sorted(Path('icon_set/work/primitive-make-ray').glob('*/20260924T071000Z-thuan-mac'),key=lambda p:next(p.glob('*.svg')).name)
for b in range(2):
 im=Image.new('RGB',(1100,1250),'#eeeeee');d=ImageDraw.Draw(im)
 for j,p in enumerate(runs[b*10:b*10+10]):
  x=j%2*550;y=j//2*250;name=next(p.glob('*.svg')).stem
  d.text((x+5,y+3),name,fill='black')
  for k,theme in enumerate(['light','dark']):
   pic=Image.open(p/f'{theme}-240.png').convert('RGB');im.paste(pic.resize((185,185)),(x+k*270,y+25))
   im.paste(Image.open(p/f'{theme}-48.png'),(x+k*270+195,y+90))
 im.save(Path(__file__).parent/f'candidates-{b}.png')
