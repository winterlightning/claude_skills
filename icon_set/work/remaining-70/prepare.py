from pathlib import Path
import json,inspect,io
import cairosvg
from PIL import Image,ImageDraw
from icon_set.model.icons.registry import factories
AUTHOR='gpt-6';SOURCE_ICON_ID=None;SOURCE_PATH='icon_set/dist/failed/solo48/manifest.json'
W=Path(__file__).parent;R=factories();rows=json.loads(Path(SOURCE_PATH).read_text())['icons'];out=[]
for i,r in enumerate(rows,1):
 n=r['icon_id'];c=R[n];f=Path(inspect.getsourcefile(c));s=c().to_svg();(W/'before'/f'{n}.py').write_bytes(f.read_bytes());(W/'before'/f'{n}.svg').write_text(s);out.append(dict(number=i,root=n,target_file=str(f),findings=r))
(W/'plan.json').write_text(json.dumps(out,indent=2))
for k in range(0,len(out),15):
 im=Image.new('RGB',(1500,900),'white');d=ImageDraw.Draw(im)
 for i,g in enumerate(out[k:k+15]):
  x=i%5*300;y=i//5*300;n=g['root'];tile=Image.open(io.BytesIO(cairosvg.svg2png(url=str(W/'before'/f'{n}.svg'),output_width=240,output_height=240))).convert('RGBA');im.paste(tile,(x+30,y+10),tile);d.text((x+5,y+260),f"{g['number']} {n}",fill='black')
 im.save(W/f'before-{k//15}.png')
refs=['hand','handshake','hand-heart','hand-metal','person-standing','bike','sailboat','fish','atom','heart','cake','car','flag','bed','camera']
im=Image.new('RGB',(1200,((len(refs)+3)//4)*210),'white');d=ImageDraw.Draw(im)
for i,n in enumerate(refs):
 x=i%4*300;y=i//4*210;d.text((x+5,y+5),n,fill='black')
 for j,kind in enumerate(['original','atomic-debug']):
  f=Path('icon_set/references/lucide')/kind/(n+'.svg')
  if f.exists():
   tile=Image.open(io.BytesIO(cairosvg.svg2png(url=str(f),output_width=140,output_height=170))).convert('RGBA');im.paste(tile,(x+j*150,y+30),tile)
im.save(W/'references.png')
cairosvg.svg2png(url='icon_set/references/human_ref/user.svg',write_to=str(W/'avatar-reference.png'),output_width=240,output_height=240,background_color='white')
