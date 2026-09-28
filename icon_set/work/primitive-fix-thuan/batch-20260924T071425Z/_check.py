from pathlib import Path
import json,sys
sys.path.insert(0,str(Path.cwd()))
from icon_set.scripts.primitive_fix import load_icon,render_previews
from PIL import Image,ImageDraw
root=Path(__file__).parent
rows=json.loads((root/'inputs.json').read_text())
selected=set(map(int,sys.argv[1:])) if sys.argv[1:] else set(range(20))
for i,r in enumerate(rows):
 if i not in selected or not Path(r['module']).exists():continue
 icon=load_icon(r['module']);report=icon.validate_icon();out=Path(r['run'])
 (out/'validation.txt').write_text(report.describe());svg=icon.to_svg();(out/(r['icon_id']+'.svg')).write_text(svg)
 render_previews(svg,r['icon_id'],48,out)
 print(i,r['icon_id'],report.status,report.describe() if report.status!='valid' or report.warnings else '')
for batch in range(4):
 im=Image.new('RGB',(800,5*180),'#eeeeee');d=ImageDraw.Draw(im)
 for k in range(5):
  i=batch*5+k;r=rows[i];out=Path(r['run']);d.text((5,k*180+3),f'{i}: '+r['icon_id'],fill='black')
  for j,(f,size) in enumerate([(root/f'{i}-ref.png',144),(out/'preview-light-384.png',144),(out/'preview-dark-384.png',144),(out/'preview-light-48.png',48),(out/'preview-dark-48.png',48)]):
   if not f.exists():continue
   pic=Image.open(f).convert('RGBA').resize((size,size));im.paste(pic,(10+j*155,k*180+25),pic)
 im.save(root/f'after-{batch}.png')
