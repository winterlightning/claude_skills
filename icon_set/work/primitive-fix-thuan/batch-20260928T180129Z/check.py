from pathlib import Path
import sys,json,shutil
from PIL import Image,ImageDraw
sys.path.insert(0,str(Path.cwd()))
from icon_set.scripts.primitive_fix import load_icon,render_previews
from icon_set.scripts.build_gate import gate
ROOT=Path(__file__).resolve().parent
items=json.loads((ROOT/'authored.json').read_text())
for d in items:
 r=Path(d['run']);p=Path(d['module'])
 try:
  icon=load_icon(p);svg=icon.to_svg();report=icon.validate_icon();g=gate(p)
  (r/(d['icon_id']+'.svg')).write_text(svg);(r/'validation.txt').write_text(report.describe());(r/'gate.json').write_text(json.dumps(g,indent=2));render_previews(svg,d['icon_id'],48,r)
  shutil.copyfile(Path(d['fix_dir'])/'reference.png',r/'reference.png')
  print(d['n'],report.status,g['status'],len(g['errors']),len(g['warnings']),flush=True)
 except Exception as e:print(d['n'],'ERROR',str(e),flush=True)
for a in range(0,20,5):
 im=Image.new('RGB',(940,5*250),'#ddd');dr=ImageDraw.Draw(im)
 for j,d in enumerate(items[a:a+5]):
  y=j*250;dr.text((10,y+2),str(d['n'])+'. '+d['icon_id'],fill='black')
  for k,(p,size) in enumerate([(Path(d['fix_dir'])/'reference.png',192),(Path(d['fix_dir'])/'before.png',192),(Path(d['run'])/'preview-light-384.png',192),(Path(d['run'])/'preview-dark-384.png',192)]):
   if p.exists():
    pic=Image.open(p).convert('RGBA').resize((size,size));im.paste(pic,(k*230+5,y+25),pic)
  for k,t in enumerate(['ref','before','after light','after dark']):dr.text((k*230+10,y+224),t,fill='black')
  for k,t in enumerate(['light','dark']):
   p=Path(d['run'])/f'preview-{t}-48.png'
   if p.exists():im.paste(Image.open(p),(k*70+580,y+193))
 im.save(ROOT/f'after-{a//5+1}.png')
