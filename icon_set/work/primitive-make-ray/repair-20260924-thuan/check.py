from pathlib import Path
import json,sys
sys.path.insert(0,str(Path.cwd()))
from icon_set.scripts.primitive_fix import load_icon
import cairosvg
from PIL import Image,ImageDraw
root=Path(__file__).parent;rows=json.loads((root/'batch.json').read_text())
for i,r in enumerate(rows):
 run=Path(r['result_dir']);p=next(run.glob('*.py'));icon=load_icon(p);report=icon.validate_icon();s=report.describe();(run/'validation.txt').write_text(s)
 print(i,r['icon_id'],report.status,len(report.errors),len(report.warnings),flush=True)
 if report.errors or report.warnings:print(s,flush=True)
 svg=icon.to_svg();(run/(r['icon_id']+'.svg')).write_text(svg)
 for theme,fg,bg in [('light','#141413','#ffffff'),('dark','#f5f4ef','#1c1c19')]:
  for size in (48,192):
   cairosvg.svg2png(bytestring=svg.replace('currentColor',fg).encode(),write_to=str(run/f'{theme}-{size}.png'),output_width=size,output_height=size,background_color=bg)
 cairosvg.svg2png(url=r['reference_path'],write_to=str(run/'reference.png'),output_width=192,output_height=192,background_color='white')
for batch in range(4):
 sheet=Image.new('RGB',(700,1100),'#eeeeee');d=ImageDraw.Draw(sheet)
 for row,r in enumerate(rows[batch*5:batch*5+5]):
  run=Path(r['result_dir']);y=row*220;d.text((5,y),f'{batch*5+row}: '+r['icon_id'],fill='black')
  for x,n in [(0,'reference.png'),(200,'light-192.png'),(400,'dark-192.png'),(600,'light-48.png'),(650,'dark-48.png')]:sheet.paste(Image.open(run/n),(x,y+24))
 sheet.save(root/f'candidates-{batch}.png')
