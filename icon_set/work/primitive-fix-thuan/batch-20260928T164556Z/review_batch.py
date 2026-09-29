from pathlib import Path
import sys,json
sys.path.insert(0,str(Path(__file__).resolve().parents[4]))
from icon_set.scripts.primitive_fix import load_icon,render_previews
from icon_set.scripts.build_gate import gate
from PIL import Image,ImageDraw
ROOT=Path(__file__).resolve().parent
rows=json.loads((ROOT/'batch.json').read_text())
selected=list(map(int,sys.argv[1:])) if len(sys.argv)>1 else list(range(len(rows)))
for i in selected:
 r=rows[i];run=Path(r['run']);module=Path(r['module'])
 try:
  icon=load_icon(module);report=icon.validate_icon();svg=icon.to_svg()
  (run/(r['icon_id']+'.svg')).write_text(svg)
  (run/'validation.txt').write_text(report.describe())
  render_previews(svg,r['icon_id'],48,run)
  qa=gate(module);(run/'gate.json').write_text(json.dumps(qa,indent=2))
  print(i,r['icon_id'],report.status,qa['status'],flush=True)
  for e in list(report.errors)+list(report.warnings)+qa['errors']+qa['warnings']:print(' ',e,flush=True)
 except Exception as e:print(i,'ERROR',str(e),flush=True)
for page in range(4):
 chunk=rows[page*5:(page+1)*5];im=Image.new('RGB',(1000,len(chunk)*220),'#eee');d=ImageDraw.Draw(im)
 for j,r in enumerate(chunk):
  y=j*220;d.text((10,y+3),str(page*5+j)+' '+r['icon_id'],fill='black');run=Path(r['run'])
  for n,p in enumerate([Path(r['fix_dir'])/'reference.png',Path(r['fix_dir'])/'before.png',run/'preview-light-384.png',run/'preview-dark-384.png']):
   if p.exists():im.paste(Image.open(p).convert('RGB').resize((192,192)),(10+n*200,y+24))
  for n,theme in enumerate(['light','dark']):
   p=run/f'preview-{theme}-48.png'
   if p.exists():im.paste(Image.open(p).convert('RGB'),(830+n*60,y+80))
 im.save(ROOT/f'revised-{page}.png')
