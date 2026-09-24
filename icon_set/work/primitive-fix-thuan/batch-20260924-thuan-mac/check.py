from pathlib import Path
import sys,json,io
sys.path.insert(0,str(Path.cwd()))
from icon_set.scripts.primitive_fix import load_icon
import cairosvg
from PIL import Image,ImageDraw
rows=json.loads(Path('icon_set/work/primitive-fix-thuan/batch-20260924-thuan-mac/runs.json').read_text())
sheet=Image.new('RGB',(1000,150*len(rows)),'white');d=ImageDraw.Draw(sheet)
for i,row in enumerate(rows):
 out=Path(row['run']); icon=load_icon(row['module']);r=icon.validate_icon();svg=icon.to_svg()
 (out/'validation.txt').write_text(r.describe());(out/(icon.icon_id+'.svg')).write_text(svg)
 print(icon.icon_id,r.status,len(r.errors),len(r.warnings))
 if r.errors or r.warnings:print(r.describe())
 d.text((2,i*150+4),icon.icon_id+' '+r.status,fill='black')
 for theme,fg,bg in [('light','#141413','#ffffff'),('dark','#f5f4ef','#1c1c19')]:
  for size in (48,384):
   raw=cairosvg.svg2png(bytestring=svg.replace('currentColor',fg).encode(),output_width=size,output_height=size,background_color=bg)
   (out/f'{theme}-{size}.png').write_bytes(raw)
  j=0 if theme=='light' else 1
  im=Image.open(out/f'{theme}-384.png').convert('RGB').resize((120,120));sheet.paste(im,(600+150*j,i*150+20))
  sheet.paste(Image.open(out/f'{theme}-48.png').convert('RGB'),(900,i*150+15+65*j))
 for size in (48,384):cairosvg.svg2png(url=row['reference_path'],write_to=str(out/f'reference-{size}.png'),output_width=size,output_height=size)
 sheet.paste(Image.open(out/'reference-384.png').convert('RGBA').resize((120,120)),(430,i*150+20),Image.open(out/'reference-384.png').convert('RGBA').resize((120,120)))
sheet.save('icon_set/work/primitive-fix-thuan/batch-20260924-thuan-mac/review.png')
