from pathlib import Path
import json,sys,io
ROOT=Path(__file__).resolve().parents[4];sys.path.insert(0,str(ROOT))
from icon_set.scripts.primitive_fix import load_icon,render_previews
from icon_set.scripts.build_gate import gate
import cairosvg
from PIL import Image,ImageDraw
HERE=Path(__file__).resolve().parent
items=json.loads((HERE/'items.json').read_text())
for i in map(int,sys.argv[1:]):
 it=items[i];run=ROOT/it['run'];module=ROOT/it['module'];icon=load_icon(module)
 report=icon.validate_icon();g=gate(module)
 (run/'validation.txt').write_text(report.describe())
 (run/'gate.json').write_text(json.dumps(g,indent=2))
 svg=icon.to_svg();(run/f"{it['id']}.svg").write_text(svg)
 render_previews(svg,it['id'],48,run)
 for name,key in [('reference','ref'),('before','before')]:
  cairosvg.svg2png(url=str(ROOT/it[key]),write_to=str(run/f'{name}.png'),output_width=192,output_height=192,background_color='white')
 print(i,it['id'],report.status,g['status'],len(g['errors']),len(g['warnings']))
 for e in (g['errors']+g['warnings'])[:8]:print(' ',e)
for start in range(0,20,5):
 selected=[(i,it) for i,it in enumerate(items[start:start+5],start) if 'run' in it and (ROOT/it['run']/'preview-light-384.png').exists()]
 if not selected:continue
 sheet=Image.new('RGB',(920,len(selected)*225),'#e9e9e9');d=ImageDraw.Draw(sheet)
 for j,(i,it) in enumerate(selected):
  run=ROOT/it['run'];d.text((8,j*225+4),f"{i}: {it['id']}",fill='black')
  for k,fn in enumerate(['reference.png','before.png','preview-light-384.png','preview-dark-384.png']):
   im=Image.open(run/fn).convert('RGB').resize((180,180));sheet.paste(im,(k*205+5,j*225+25))
  for k,theme in enumerate(['light','dark']):sheet.paste(Image.open(run/f'preview-{theme}-48.png'),(837,j*225+30+k*90))
 sheet.save(HERE/f'after-{start//5}.png')
