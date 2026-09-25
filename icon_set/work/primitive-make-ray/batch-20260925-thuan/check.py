from pathlib import Path
import json,sys,io
sys.path.insert(0,str(Path.cwd()))
from icon_set.scripts.primitive_fix import load_icon
from icon_set.scripts.build_gate import gate
from PIL import Image,ImageDraw
import cairosvg
root=Path('icon_set/work/primitive-make-ray/batch-20260925-thuan'); rows=json.loads((root/'manifest.json').read_text())
for row in rows:
 p=Path(row['module']);run=p.parent;icon=load_icon(p);svg=icon.to_svg();ident=icon.icon_id
 (run/f'{ident}.svg').write_text(svg)
 report=icon.validate_icon();(run/'validation.txt').write_text(report.describe())
 result=gate(p);(run/'gate.json').write_text(json.dumps(result,indent=2))
 print(row['index'],ident,report.status,result['status'],flush=True)
 print('\n'.join((result['errors']+result['warnings'])[:8]),flush=True)
 for theme,bg,fg in [('light','#ffffff','#111111'),('dark','#171b22','#f5f7fa')]:
  for size in (48,192):
   cairosvg.svg2png(bytestring=svg.replace('currentColor',fg).replace('#000000',fg).replace('black',fg).encode(),write_to=str(run/f'{theme}-{size}.png'),output_width=size,output_height=size,background_color=bg)
 cairosvg.svg2png(url=row['reference_path'],write_to=str(run/'reference.png'),output_width=192,output_height=192)
for group in range(4):
 im=Image.new('RGB',(900,5*230),'#e1e4e8');d=ImageDraw.Draw(im)
 for j,row in enumerate(rows[group*5:group*5+5]):
  run=Path(row['run']);d.text((10,j*230+6),str(row['index'])+'. '+row['key'],fill='black')
  for k,(name,size) in enumerate([('reference',192),('light-192',192),('dark-192',192),('light-48',48),('dark-48',48)]):
   a=Image.open(run/(name+'.png')).convert('RGBA');im.paste(a,([10,230,450,680,760][k],j*230+30),a)
 im.save(root/f'after-{group}.png')
