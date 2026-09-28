from pathlib import Path
import json,sys
from icon_set.scripts.primitive_fix import load_icon,render_previews
from icon_set.scripts.build_gate import gate
from PIL import Image,ImageDraw
root=Path('icon_set/work/primitive-make-ray/fix-batch-20260924')
items=json.loads((root/'manifest.json').read_text());selected=set(map(int,sys.argv[1:]))
for e in items:
 if selected and e['index'] not in selected:continue
 p=Path(e['module']);r=Path(e['run']);icon=load_icon(p);report=icon.validate_icon();g=gate(p)
 (r/'validation.txt').write_text(report.describe()+'\n'+json.dumps(g,indent=2))
 (r/'gate.json').write_text(json.dumps(g,indent=2));svg=icon.to_svg();(r/(e['icon_id']+'.svg')).write_text(svg);render_previews(svg,e['icon_id'],48,r)
 print(e['index'],e['icon_id'],report.status,g['status'],flush=True)
 for err in g['errors']+g['warnings']:print(err,flush=True)
c=Image.new('RGB',(900,180*len(items)),'#ddd');d=ImageDraw.Draw(c)
for n,e in enumerate(items):
 r=Path(e['run']);d.text((5,n*180+4),str(e['index'])+' '+e['icon_id'],fill='black')
 for j,f in enumerate([r/'reference.png',Path(e['fix_dir'])/'before.png',r/'preview-light-384.png',r/'preview-dark-384.png']):
  if f.exists():
   im=Image.open(f).convert('RGBA').resize((140,140));c.paste(im,(210+j*170,n*180+30),im)
 for j,t in enumerate(['light','dark']):
  f=r/f'preview-{t}-48.png'
  if f.exists():c.paste(Image.open(f),(50+j*65,n*180+65))
c.save(root/'review.png')
