from pathlib import Path
from PIL import Image,ImageDraw
import cairosvg,io
SOURCE_ICON_ID=None
SOURCE_PATH='icon_set/references/lucide'
AUTHOR='gpt-6'
w=Path(__file__).parent;root=Path(SOURCE_PATH);names=['castle','church','house','disc','bird','fish','feather','baby','bug','dog','cat','sword','shopping-bag','moon','landmark','shell'];im=Image.new('RGB',(1000,((len(names)+3)//4)*170),'white');d=ImageDraw.Draw(im)
for i,n in enumerate(names):
 x=i%4*250;y=i//4*170;d.text((x+8,y+2),n,fill='black')
 for j,t in enumerate(['original','atomic-debug']):
  p=root/t/(n+'.svg')
  if p.exists():
   png=Image.open(io.BytesIO(cairosvg.svg2png(url=str(p),output_width=112,output_height=112)));im.paste(png,(x+j*120+8,y+24),png)
  else:d.text((x+j*120+8,y+40),'Unavailable',fill='black')
im.save(w/'round2-lucide.png')
