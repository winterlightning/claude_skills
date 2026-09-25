from pathlib import Path
import sys,json,io
sys.path.insert(0,str(Path(__file__).resolve().parents[4]))
from icon_set.scripts.primitive_fix import load_icon,run_module,render_previews
from icon_set.scripts.build_gate import gate
import cairosvg
from PIL import Image,ImageDraw
root=Path(__file__).parent
rows=json.loads((root/'batch.json').read_text())
chosen=[r for r in rows if not sys.argv[1:] or r['icon_id'] in sys.argv[1:]]
for r in chosen:
 out=Path(r['run'])
 try:
  module=run_module(out);icon=load_icon(module);v=icon.validate_icon();g=gate(module)
  (out/'validation.txt').write_text(v.describe()+'\n'+json.dumps(g,indent=2))
  svg=icon.to_svg();(out/(r['icon_id']+'.svg')).write_text(svg)
  render_previews(svg,r['icon_id'],48,out)
  cairosvg.svg2png(url=r['reference_path'],write_to=str(out/'reference.png'),output_width=192,output_height=192,background_color='white')
  result=dict(model=v.status,errors=list(v.errors),warnings=list(v.warnings),gate=g)
  (out/'checks.json').write_text(json.dumps(result,indent=2))
  print(r['icon_id'],v.status,g['status'],v.errors,v.warnings,g['errors'],g['warnings'],flush=True)
 except Exception as e:print(r['icon_id'],type(e).__name__,str(e),flush=True)
im=Image.new('RGB',(1000,((len(rows)+3)//4)*270),'#eee');d=ImageDraw.Draw(im)
for i,r in enumerate(rows):
 x=(i%4)*250;y=(i//4)*270;out=Path(r['run']);d.text((x+3,y+2),r['icon_id'][:32],fill='black')
 for j,theme in enumerate(['light','dark']):
  p=out/f'preview-{theme}-384.png'
  if p.exists():
   a=Image.open(p).resize((120,120));im.paste(a,(x+j*125,y+25))
   a=Image.open(out/f'preview-{theme}-48.png');im.paste(a,(x+j*125+35,y+160))
im.save(root/'review.png')
