import io
from pathlib import Path
import cairosvg
from PIL import Image,ImageDraw
W=Path(__file__).parent;R=W.resolve().parents[2]/'icon_set/references'
names=['plane','venetian-mask','bike','link','ruler','wallet','award','syringe','rocket','battery-charging']
for off in range(0,len(names),10):
 im=Image.new('RGB',(1100,1050),'white');d=ImageDraw.Draw(im)
 for j,name in enumerate(names[off:off+10]):
  x=j%2*550;y=j//2*210;d.text((x+5,y+5),name,fill='black')
  for k,folder in enumerate(['original','atomic-debug']):
   p=R/'lucide'/folder/(name+'.svg')
   if not p.exists():continue
   a=Image.open(io.BytesIO(cairosvg.svg2png(url=str(p),output_width=180,output_height=180))).convert('RGBA');im.paste(a,(x+10+k*240,y+25),a)
 im.save(W/f'references-{off//10+1}.png')
cairosvg.svg2png(url=str(R/'human_ref/user.svg'),write_to=str(W/'human.png'),output_width=300,output_height=300)
