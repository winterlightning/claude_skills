from pathlib import Path
import sys,json,io,shutil
sys.path.insert(0,str(Path.cwd()))
from icon_set.scripts.primitive_fix import load_icon
from icon_set.scripts.build_gate import gate
import cairosvg
from PIL import Image,ImageDraw
root=Path('icon_set/work/primitive-make-ray/review-20260925T060624Z');rows=json.loads((root/'batch.json').read_text())
indices=list(map(int,sys.argv[1:])) if len(sys.argv)>1 else list(range(20))
for i in indices:
 r=rows[i];run=Path(r['run']);icon=load_icon(Path(r['module']));report=icon.validate_icon();svg=icon.to_svg();(run/(r['id']+'.svg')).write_text(svg);(run/'validation.txt').write_text(report.describe())
 for theme,fg,bg in [('light','#111111','#ffffff'),('dark','#eeeeee','#171717')]:
  for size in [48,192]:
   cairosvg.svg2png(bytestring=svg.replace('currentColor',fg).encode(),write_to=str(run/f'{theme}-{size}.png'),output_width=size,output_height=size,background_color=bg)
 cairosvg.svg2png(url=r['ref'],write_to=str(run/'reference.png'),output_width=192,output_height=192,background_color='white')
 print(i,r['id'],report.status,flush=True)
 if report.status!='valid' or report.warnings:print(report.describe(),flush=True)
 if '--gate' in []:pass
for part in range(2):
 sheet=Image.new('RGB',(1200,1050),'#ddd');d=ImageDraw.Draw(sheet)
 for j,r in enumerate(rows[part*10:part*10+10]):
  run=Path(r['run']);x=j%2*600;y=j//2*210;d.text((x+5,y+2),str(part*10+j)+' '+r['id'],fill='black')
  for k,t in enumerate(['light','dark']):
   p=run/f'{t}-192.png'
   if p.exists():sheet.paste(Image.open(p),(x+k*260,y+18));sheet.paste(Image.open(run/f'{t}-48.png'),(x+k*260+200,y+80))
 sheet.save(root/f'after-{part}.png')
