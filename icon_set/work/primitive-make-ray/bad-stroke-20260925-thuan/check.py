from pathlib import Path
import sys,json,importlib.util,cairosvg
from PIL import Image,ImageDraw
sys.path.insert(0,str(Path.cwd()))
from icon_set.scripts.primitive_fix import load_icon
from icon_set.scripts.build_gate import gate
ROOT=Path(__file__).parent
rows=json.loads((ROOT/'batch.json').read_text())
chosen=[int(x) for x in sys.argv[1:]] or list(range(len(rows)))
for i in chosen:
 r=rows[i];d=Path(r['dir']);p=next(d.glob('*.py'))
 try:
  icon=load_icon(p);report=icon.validate_icon();(d/'validation.txt').write_text(report.describe());svg=icon.to_svg();(d/(r['id']+'.svg')).write_text(svg)
  for name,ink,bg in [('light','#141413','#ffffff'),('dark','#f5f4ef','#1c1c19')]:
   for size in [48,192]:cairosvg.svg2png(bytestring=svg.replace('currentColor',ink).encode(),write_to=str(d/f'{name}-{size}.png'),output_width=size,output_height=size,background_color=bg)
  g=gate(p);(d/'gate.json').write_text(json.dumps(g,indent=2));print(i,r['id'],report.status,json.dumps(g),flush=True)
 except Exception as e:print(i,type(e).__name__,str(e),flush=True)
im=Image.new('RGB',(1000,5*240),'#bbb');draw=ImageDraw.Draw(im)
for i,r in enumerate(rows):
 x=i%2*500;y=i//2*240;draw.text((x+3,y+3),f"{i} {r['id']}",fill='black');d=Path(r['dir'])
 for j,theme in enumerate(['light','dark']):
  for size in [192,48]:
   p=d/f'{theme}-{size}.png'
   if p.exists():im.paste(Image.open(p).convert('RGB'),(x+j*250+(0 if size==192 else 195),y+30))
im.save(ROOT/'review.png')
