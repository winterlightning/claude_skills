import json,sys,io
from pathlib import Path
from PIL import Image,ImageDraw
ROOT=Path(__file__).resolve().parents[4]
sys.path.insert(0,str(ROOT))
from icon_set.scripts.primitive_fix import load_icon,render_previews
from icon_set.scripts.build_gate import gate
BATCH=Path(__file__).resolve().parent
rows=json.loads((BATCH/'batch.json').read_text())
indices=list(map(int,sys.argv[1:])) or list(range(1,21))
for index in indices:
 row=rows[index-1]
 if 'module' not in row: continue
 out=ROOT/row['result_dir']; icon=load_icon(ROOT/row['module']); report=icon.validate_icon()
 svg=icon.to_svg();(out/(icon.icon_id+'.svg')).write_text(svg)
 render_previews(svg,icon.icon_id,48,out)
 (out/'validation.txt').write_text(report.describe()+'\n')
 result=gate(ROOT/row['module']);(out/'gate.json').write_text(json.dumps(result,indent=2)+'\n')
 print(index,icon.icon_id,report.status,'gate',result['status'],len(result['errors']),len(result['warnings']),flush=True)
 for e in (report.errors+report.warnings)[:2]:print(' ',e,flush=True)
for page in range(4):
 sheet=Image.new('RGB',(950,5*200),'#dededb');d=ImageDraw.Draw(sheet)
 for i,row in enumerate(rows[page*5:page*5+5]):
  y=i*200;d.text((8,y+3),f'{page*5+i+1}. '+row['icon_id'],fill='black')
  if 'result_dir' not in row:continue
  out=ROOT/row['result_dir']
  if not (out/'preview-light-384.png').exists():continue
  for x,theme in [(10,'light'),(240,'dark')]:
   im=Image.open(out/f'preview-{theme}-384.png').convert('RGB').resize((160,160))
   sheet.paste(im,(x,y+26));sheet.paste(Image.open(out/f'preview-{theme}-48.png').convert('RGB'),(x+168,y+72))
  import cairosvg
  for x,key in [(500,'reference'),(720,'before')]:
   png=cairosvg.svg2png(url=str(ROOT/row[key]),output_width=150,output_height=150,background_color='white')
   sheet.paste(Image.open(io.BytesIO(png)).convert('RGB'),(x,y+28));d.text((x,y+180),key,fill='black')
 sheet.save(BATCH/f'review-{page+1}.png')
