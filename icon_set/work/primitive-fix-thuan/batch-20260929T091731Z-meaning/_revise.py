from pathlib import Path
import sys,json,shutil
sys.path.insert(0,str(Path.cwd()))
from icon_set.scripts.primitive_fix import load_icon,render_previews
B=Path('icon_set/work/primitive-fix-thuan/batch-20260929T091731Z-meaning');rs=json.loads((B/'runs.json').read_text())
CHANGES={
3: '''
# Exact VRECT_M extremes: x10/38, y4/44. The bowl has short tines and a long handle.
path(self,'spork-outline',(14,4),('C',(11,7),(10,11),(10,14)),('C',(10,21),(15,24),(20,25)),('L',(20,40)),('A',4,4,False,(28,40)),('L',(28,25)),('C',(33,24),(38,21),(38,14)),('C',(38,11),(37,7),(34,4)))
path(self,'tines',(14,4),('L',(14,12)),('A',5,5,False,(24,12)),('L',(24,4)),('L',(24,12)),('A',5,5,False,(34,12)),('L',(34,4)))
''',
4: '''
# The cab frame is itself the window; avoid nesting a second tiny rectangle inside it.
line(self,'cab-roof',(4,7),(21,7))
poly(self,'cab',(6,26),(6,7),(19,7),(19,27))
path(self,'boiler',(19,18),('L',(39,18)),('A',3,3,True,(42,21)),('L',(42,30)),('L',(23,30)))
poly(self,'stack',(31,18),(31,12),(29,7),(39,7),(37,12),(37,18))
ellipse(self,'driver',12,35,9)
ellipse(self,'driver-hub',12,35,3)
for x in (28,40):
 ellipse(self,f'wheel-{x}',x,39,3)
 line(self,f'axle-{x}',(x,30),(x,36))
''',
7: '''
path(self,'head',(12,14),('C',(12,6),(17,4),(24,4)),('C',(40,4),(48,20),(40,30)),('C',(37,35),(42,39),(44,44)))
poly(self,'nose-lip',(12,14),(6,22),(11,24),(11,29))
path(self,'palate',(11,24),('C',(29,17),(36,27),(36,44)))
path(self,'mouth-floor',(11,29),('C',(23,25),(28,30),(28,44)))
path(self,'chin',(12,34),('C',(12,39),(21,37),(21,40)),('L',(21,44)))
''',
19: '''
ellipse(self,'head',28,8,4)
path(self,'torso',(28,20),('C',(28,24),(24,26),(22,30)))
self.mark_human_figure('person',head='head',torso='torso-1',torso_junction='start')
poly(self,'leg',(22,30),(34,26),(34,34),(29,34))
poly(self,'tank',(4,34),(4,23),(12,23),(12,34))
path(self,'bowl',(4,34),('L',(37,34)),('C',(37,40),(19,41),(16,41)),('L',(16,44)))
line(self,'base',(14,44),(22,44))
line(self,'cross-a',(39,4),(45,10));line(self,'cross-b',(39,10),(45,4))
'''
}
for i in [3,4,7,8,9,11,19]:
 r=rs[i];old=Path(r['result_dir']);run=old.with_name('20260929T091731Z-meaning-v2');run.mkdir();module=run/Path(r['module']).name;code=Path(r['module']).read_text()
 if i in CHANGES:code=code.split('    def build(self):')[0]+'    def build(self):\n'+'\n'.join('        '+s for s in CHANGES[i].strip().splitlines())+'\n        contacts(self)\n'
 elif i in [8,9]:
  code=code.replace("(12,28),('C',(1,28),(1,14),(12,14))", "(12,25),('C',(1,25),(1,13),(12,13))").replace("(48,21),(44,28),(37,28)","(48,20),(44,25),(37,25)").replace("('L',(12,28))", "('L',(12,25))").replace("(28,33),(21,39),(28,39),(23,45)","(27,30),(20,38),(28,38),(22,46)")
  code=code.replace('(12,35),(7,42)','(12,33),(7,41)').replace('(41,35),(36,42)','(41,33),(36,41)')
 else:code=code.replace("        line(self,'ball-diagonal',(5,10),(25,25))\n",'')
 module.write_text(code)
 for f in ['reference.png','before.png',r['icon_id']+'.metadata.json']:shutil.copyfile(old/f,run/f)
 icon=load_icon(module);rep=icon.validate_icon();svg=icon.to_svg();(run/(r['icon_id']+'.svg')).write_text(svg);(run/'validation.txt').write_text(rep.describe());render_previews(svg,r['icon_id'],48,run)
 r.update(result_dir=str(run),module=str(module),validation_status=rep.status,errors=rep.errors,warnings=rep.warnings);(run/'review.json').write_text(json.dumps(r,indent=2));print(i,rep.status,len(rep.errors),len(rep.warnings),flush=True)
(B/'runs.json').write_text(json.dumps(rs,indent=2))
from PIL import Image,ImageDraw
im=Image.new('RGB',(900,7*190),'#ddd');d=ImageDraw.Draw(im)
for n,i in enumerate([3,4,7,8,9,11,19]):
 p=Path(rs[i]['result_dir']);d.text((10,n*190+5),rs[i]['icon_id'],fill='black')
 for j,t in enumerate(['light','dark']):
  im.paste(Image.open(p/f'preview-{t}-384.png').resize((150,150)),(j*440+10,n*190+30));im.paste(Image.open(p/f'preview-{t}-48.png'),(j*440+190,n*190+70))
im.save(B/'revised.png')
