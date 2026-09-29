from pathlib import Path
import sys,json,shutil
sys.path.insert(0,str(Path.cwd()))
from icon_set.scripts.primitive_fix import load_icon,render_previews
B=Path('icon_set/work/primitive-fix-thuan/batch-20260929T085904Z-meaning');rs=json.loads((B/'runs.json').read_text())
changes={14: '''
# Construct the tube with concentric 10/2 radii: a constant 8-unit boundary width.
path(self,'worm',(8,32),('L',(8,20)),('A',10,10,True,(28,20)),('L',(28,30)),('A',2,2,False,(32,30)),('L',(32,10)),('A',4,4,True,(40,10)),('L',(40,30)),('A',10,10,True,(20,30)),('L',(20,20)),('A',2,2,False,(16,20)),('L',(16,32)),('A',8,8,True,(8,40)),('A',4,4,True,(8,32)),closed=True)
''',15: '''
path(self,'handle',(14,19),('L',(28,33)),('L',(19,42)),('C',(16,46),(12,44),(9,41)),('L',(4,36)),('C',(1,33),(4,29),(7,26)),('L',(14,19)),closed=True)
path(self,'grip',(9,31),('L',(14,26)),('L',(22,34)),('L',(17,39)),('L',(9,31)),closed=True)
poly(self,'blade',(15,20),(36,4),(44,11),(39,14),(39,18),(34,20),(33,25),(28,27),(28,33))
'''}
for i in [4,14,15]:
 r=rs[i];old=Path(r['result_dir']);run=old.with_name('20260929T085904Z-meaning-v4');run.mkdir();module=run/Path(r['module']).name;code=Path(r['module']).read_text()
 if i==4:code=code.replace("'clock',10,9,6","'clock',10,10,7").replace("(10,7),(10,9),(12,9)","(10,7),(10,10),(13,10)")
 else:code=code.split('    def build(self):')[0]+'    def build(self):\n'+'\n'.join('        '+s for s in changes[i].strip().splitlines())+'\n        contacts(self)\n'
 module.write_text(code)
 for f in ['reference.png','before.png',r['icon_id']+'.metadata.json']:shutil.copyfile(old/f,run/f)
 icon=load_icon(module);rep=icon.validate_icon();svg=icon.to_svg();(run/(r['icon_id']+'.svg')).write_text(svg);(run/'validation.txt').write_text(rep.describe());render_previews(svg,r['icon_id'],48,run)
 r.update(result_dir=str(run),module=str(module),validation_status=rep.status,errors=rep.errors,warnings=rep.warnings);(run/'review.json').write_text(json.dumps(r,indent=2));print(i,rep.status)
(B/'runs.json').write_text(json.dumps(rs,indent=2))
from PIL import Image,ImageDraw
im=Image.new('RGB',(800,660),'#ddd');d=ImageDraw.Draw(im)
for n,i in enumerate([4,14,15]):
 p=Path(rs[i]['result_dir']);d.text((10,n*220+5),rs[i]['icon_id'],fill='black')
 for j,t in enumerate(['light','dark']):
  im.paste(Image.open(p/f'preview-{t}-384.png').resize((180,180)),(j*400+10,n*220+30));im.paste(Image.open(p/f'preview-{t}-48.png'),(j*400+220,n*220+90))
im.save(B/'final-refinement.png')
