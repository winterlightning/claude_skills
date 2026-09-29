from pathlib import Path
import json,sys,shutil
sys.path.insert(0,str(Path.cwd()))
from icon_set.scripts.primitive_fix import load_icon,render_previews
B=Path('icon_set/work/primitive-fix-thuan/batch-20260929T085904Z-meaning');items=json.loads((B/'runs.json').read_text())
changes={
4: '''
# Two distinct seated people, with enough torso length to read the posture.
ellipse(self,'clock',10,9,6)
poly(self,'clock-hands',(10,7),(10,9),(12,9))
for x in (26,40):
 ellipse(self,f'head-{x}',x,17,4)
 line(self,f'torso-{x}',(x,29),(x,36))
 self.mark_human_figure(f'person-{x}',head=f'head-{x}',torso=f'torso-{x}',torso_junction='start')
poly(self,'legs-left',(26,36),(16,36),(12,44))
poly(self,'legs-right',(40,36),(44,36),(44,44))
''',
14: '''
# Wide bends retain an open lumen through the tube; endpoint radii match.
path(self,'worm',(8,34),('C',(12,34),(8,10),(18,10)),('C',(30,10),(22,34),(32,34)),('C',(39,34),(29,6),(40,6)),('A',4,4,True,(40,14)),('C',(36,14),(45,42),(32,42)),('C',(15,42),(24,18),(18,18)),('C',(14,18),(22,42),(8,42)),('A',4,4,True,(8,34)),closed=True)
''',
15: '''
path(self,'handle',(15,21),('L',(25,31)),('C',(28,37),(19,45),(14,44)),('C',(9,43),(3,38),(4,33)),('C',(5,29),(10,25),(15,21)),closed=True)
ellipse(self,'grip',14,34,5)
poly(self,'blade',(16,22),(36,4),(44,11),(39,14),(39,18),(34,20),(33,25),(28,27),(25,31))
'''
}
for i,body in changes.items():
 r=items[i];old=Path(r['result_dir']);run=old.with_name('20260929T085904Z-meaning-v3');run.mkdir();module=run/Path(r['module']).name
 code=Path(r['module']).read_text().split('    def build(self):')[0]+'    def build(self):\n'+'\n'.join('        '+s for s in body.strip().splitlines())+'\n        contacts(self)\n';module.write_text(code)
 for f in ['reference.png','before.png',r['icon_id']+'.metadata.json']:shutil.copyfile(old/f,run/f)
 icon=load_icon(module);rep=icon.validate_icon();svg=icon.to_svg();(run/(r['icon_id']+'.svg')).write_text(svg);(run/'validation.txt').write_text(rep.describe());render_previews(svg,r['icon_id'],48,run)
 r.update(result_dir=str(run),module=str(module),validation_status=rep.status,errors=rep.errors,warnings=rep.warnings);(run/'review.json').write_text(json.dumps(r,indent=2))
 print(i,rep.status,flush=True)
(B/'runs.json').write_text(json.dumps(items,indent=2))
