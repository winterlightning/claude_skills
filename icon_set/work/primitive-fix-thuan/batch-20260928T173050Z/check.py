from pathlib import Path
import sys,json,cairosvg,io
from PIL import Image,ImageDraw
ROOT=Path(__file__).resolve().parents[4];sys.path.insert(0,str(ROOT))
from icon_set.scripts.primitive_fix import load_icon,render_previews
from icon_set.scripts.build_gate import gate
BATCH=Path(__file__).parent
runs=json.loads((BATCH/'runs.json').read_text())
for r in runs:
 run=ROOT/r['run'];m=ROOT/r['module']
 try:
  icon=load_icon(m);report=icon.validate_icon();svg=icon.to_svg()
  (run/(icon.icon_id+'.svg')).write_text(svg)
  (run/'validation.txt').write_text(report.describe())
  render_previews(svg,icon.icon_id,48,run)
  result=gate(m);(run/'gate.json').write_text(json.dumps(result,indent=2))
  print(r['n'],icon.icon_id,report.status,result['status'],str(result['errors']+result['warnings'])[:1500],flush=True)
 except Exception as e:print(r['n'],'ERROR',repr(e),flush=True)
for first in range(0,len(runs),5):
 s=Image.new('RGB',(1050,5*215),'#e4e4e4');d=ImageDraw.Draw(s)
 for j,r in enumerate(runs[first:first+5]):
  run=ROOT/r['run'];y=j*215
  d.text((8,y+5),f"{r['n']}. {run.parent.name}",fill='black')
  for k,theme in enumerate(['light','dark']):
   f=run/f'preview-{theme}-384.png'
   if f.exists():
    im=Image.open(f).convert('RGB').resize((168,168));s.paste(im,(20+270*k,y+30))
    im=Image.open(run/f'preview-{theme}-48.png').convert('RGB');s.paste(im,(202+270*k,y+90))
 s.save(BATCH/f'after-{first//5+1}.png')
