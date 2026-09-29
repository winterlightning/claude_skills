from pathlib import Path
import json,sys,shutil
sys.path.insert(0,str(Path.cwd()))
from icon_set.scripts.primitive_fix import load_icon,render_previews
B=Path('icon_set/work/primitive-fix-thuan/batch-20260929T085904Z-meaning');items=json.loads((B/'runs.json').read_text())
CHANGES={
0: '''
# Round face, two small strained eyes, and one open stream silhouette avoid the pinched mouth ring.
path(self,'face',(12,37),('C',(3,29),(4,16),(12,10)),('C',(19,4),(30,4),(37,12)),('C',(45,21),(43,30),(36,37)))
poly(self,'left-eye',(16,16),(19,19),(15,21))
poly(self,'right-eye',(32,16),(29,19),(33,21))
path(self,'stream',(14,30),('C',(14,25),(34,25),(34,30)),('L',(32,34)),('C',(32,37),(36,38),(36,41)),('C',(36,44),(31,43),(29,41)),('C',(25,44),(22,44),(19,41)),('C',(17,43),(12,44),(12,41)),('C',(12,38),(16,37),(16,34)),('L',(14,30)),closed=True)
''',
3: '''
# The cube is visibly behind the goggles; break the concealed wall instead of nearly touching it.
poly(self,'stylus',(6,5),(13,12),(15,17),(10,15),(3,8),closed=True)
poly(self,'cube-left',(6,23),(17,28),(17,40),(6,35),closed=True)
poly(self,'cube-top',(6,23),(17,18),(28,23),(17,28))
path(self,'goggles',(26,30),('L',(39,30)),('A',4,4,True,(43,34)),('L',(43,41)),('A',3,3,True,(40,44)),('L',(37,44)),('L',(33,40)),('L',(29,44)),('L',(26,44)),('A',4,4,True,(22,40)),('L',(22,34)),('A',4,4,True,(26,30)),closed=True)
self.add_dot('lens-left',(28,35));self.add_dot('lens-right',(38,35))
''',
4: '''
# The clock occupies the upper left; two opposed seated silhouettes preserve the source arrangement.
ellipse(self,'clock',12,12,8)
poly(self,'clock-hands',(12,9),(12,12),(15,12))
for x in (25,39):
 ellipse(self,f'head-{x}',x,23,3)
 line(self,f'torso-{x}',(x,34),(x,37))
 self.mark_human_figure(f'person-{x}',head=f'head-{x}',torso=f'torso-{x}',torso_junction='start')
poly(self,'legs-left',(25,37),(15,37),(11,44))
poly(self,'legs-right',(39,37),(44,37),(44,44))
# Seat lines meet the bodies at actual endpoints, without a second crowded backrest.
line(self,'seat-left',(25,37),(30,37))
line(self,'seat-right',(39,37),(34,37))
''',
5: '''
poly(self,'hat',(18,10),(19,4),(27,4),(30,10))
line(self,'brim',(15,10),(32,10))
path(self,'head',(20,10),('L',(20,12)),('A',4,4,False,(28,12)),('L',(28,10)))
line(self,'torso',(24,24),(21,32))
self.mark_human_figure('farmer',head='head',torso='torso',torso_junction='start')
poly(self,'hoe-shaft',(7,18),(37,24),(42,25))
poly(self,'hoe-blade',(7,18),(6,27),(12,28),(14,20))
poly(self,'supporting-arm',(24,24),(30,30),(37,24))
poly(self,'front-leg',(21,32),(29,38),(32,44))
poly(self,'back-leg',(21,32),(12,44))
''',
6: '''
ellipse(self,'head',29,9,5)
line(self,'torso',(24,21),(19,33))
self.mark_human_figure('walker',head='head',torso='torso',torso_junction='start')
poly(self,'back-arm',(24,21),(16,23),(8,29))
poly(self,'front-arm',(24,21),(31,28),(40,26))
poly(self,'front-leg',(19,33),(29,37),(33,44))
line(self,'back-leg',(19,33),(10,44))
''',
7: '''
path(self,'wallet',(40,23),('L',(40,18)),('A',4,4,False,(36,14)),('L',(8,14)),('A',4,4,False,(4,18)),('L',(4,38)),('A',4,4,False,(8,42)),('L',(36,42)),('A',4,4,False,(40,38)),('L',(40,33)))
poly(self,'banknote',(9,14),(32,6),(35,14))
path(self,'snap-tab',(44,23),('L',(33,23)),('A',5,5,False,(33,33)),('L',(44,33)),('L',(44,23)),closed=True)
self.add_dot('snap',(37,28))
''',
8: '''
# Two fingers are sufficient; delete the pinched third fingertip while retaining two hands.
path(self,'front-hand',(10,40),('C',(2,37),(4,29),(10,24)),('L',(21,17)),('A',3,3,True,(24,22)),('L',(18,28)),('L',(35,28)),('A',4,4,True,(35,36)),('L',(24,36)))
path(self,'fingers',(35,36),('L',(39,36)),('A',4,4,True,(39,44)),('L',(17,44)),('C',(14,44),(12,42),(10,40)))
path(self,'back-hand',(22,11),('C',(25,9),(28,12),(31,14)),('L',(40,22)),('C',(43,25),(44,28),(43,30)))
ellipse(self,'bubble-left',10,10,3)
ellipse(self,'bubble-right',37,6,3)
''',
9: '''
ellipse(self,'head',20,15,5)
ellipse(self,'ball',38,8,4)
line(self,'torso',(20,28),(22,38))
self.mark_human_figure('player',head='head',torso='torso',torso_junction='start')
poly(self,'throwing-arm',(20,28),(32,27),(39,18),(38,12))
path(self,'reaching-arm',(20,28),('C',(12,28),(8,30),(5,34)))
path(self,'water',(4,39),('C',(10,34),(16,43),(22,38)),('C',(29,33),(35,43),(44,38)))
''',
10: '''
ellipse(self,'head',13,9,5)
line(self,'torso',(13,22),(16,29))
self.mark_human_figure('skier',head='head',torso='torso',torso_junction='start')
poly(self,'arms',(13,22),(24,24),(31,20))
line(self,'tow-rope',(31,20),(44,15))
poly(self,'legs',(16,29),(26,31),(29,36))
path(self,'ski',(6,36),('L',(37,36)),('A',5,5,False,(42,31)))
path(self,'water',(6,45),('C',(12,41),(18,47),(24,44)),('C',(30,41),(37,47),(43,43)))
''',
11: '''
ellipse(self,'head',12,9,5)
path(self,'torso',(12,22),('C',(12,27),(13,29),(18,31)))
self.mark_human_figure('skier',head='head',torso='torso-1',torso_junction='start')
poly(self,'arm',(12,22),(26,22),(29,18))
line(self,'rope',(29,18),(44,18))
poly(self,'leg',(18,31),(24,31),(27,36))
path(self,'ski',(5,36),('L',(36,36)),('A',5,5,False,(41,31)))
path(self,'water',(5,45),('C',(13,41),(19,47),(26,44)),('C',(33,40),(38,47),(44,42)))
''',
13: '''
path(self,'bill',(4,9),('C',(17,1),(31,15),(44,8)),('L',(44,39)),('C',(31,46),(17,32),(4,40)),('L',(4,9)),closed=True)
path(self,'dollar',(29,19),('C',(21,13),(15,23),(24,24)),('C',(34,25),(27,35),(19,29)))
line(self,'dollar-bar',(24,14),(24,34))
''',
14: '''
path(self,'worm',(10,34),('C',(14,34),(8,10),(18,10)),('C',(30,10),(22,34),(32,34)),('C',(39,34),(25,6),(38,6)),('A',4,4,True,(38,14)),('C',(32,14),(45,42),(32,42)),('C',(15,42),(24,18),(18,18)),('C',(14,18),(24,42),(10,42)),('A',4,4,True,(10,34)),closed=True)
''',
15: '''
# Open the handle/body junction and use a single larger grip window with a round lower turn.
path(self,'handle',(6,29),('L',(15,21)),('L',(25,31)),('C',(25,36),(21,41),(16,44)),('C',(13,46),(10,43),(8,41)),('L',(4,37)),('C',(2,34),(3,32),(6,29)),closed=True)
path(self,'grip',(10,33),('L',(14,29)),('L',(19,34)),('L',(15,38)),('A',3,3,True,(11,37)),('L',(10,33)),closed=True)
poly(self,'blade',(16,22),(36,4),(44,11),(39,14),(39,18),(34,20),(33,25),(28,27),(25,31))
''',
17: '''
ellipse(self,'head',16,8,4)
line(self,'torso',(16,20),(16,28))
self.mark_human_figure('rider',head='head',torso='torso',torso_junction='start')
line(self,'arm',(16,20),(25,22))
poly(self,'leg',(16,28),(24,28),(28,34),(31,34))
path(self,'wheel',(10,23),('A',10,10,False,(22,39)))
poly(self,'ramp',(27,44),(44,36),(44,44))
''',
18: '''
# Mouse capsule and scroll wheel follow Lucide construction, independently fitted to SOLO48.
path(self,'mouse',(15,31),('A',9,9,True,(33,31)),('L',(33,35)),('A',9,9,True,(15,35)),('L',(15,31)),closed=True)
line(self,'scroll-wheel',(24,31),(24,35))
path(self,'signal-outer',(10,7),('A',14,3,True,(38,7)))
path(self,'signal-inner',(18,15),('A',6,2,True,(30,15)))
'''
}
for i,body in CHANGES.items():
 item=items[i];old=Path(item['result_dir']);run=old.with_name('20260929T085904Z-meaning-v2');run.mkdir(exist_ok=False)
 oldmodule=Path(item['module']);module=run/oldmodule.name;code=oldmodule.read_text().split('    def build(self):')[0]
 code+='    def build(self):\n'+'\n'.join('        '+s for s in body.strip().splitlines())+'\n        contacts(self)\n';module.write_text(code)
 for f in ['reference.png','before.png',item['icon_id']+'.metadata.json']:shutil.copyfile(old/f,run/f)
 icon=load_icon(module);report=icon.validate_icon();svg=icon.to_svg();(run/(item['icon_id']+'.svg')).write_text(svg);(run/'validation.txt').write_text(report.describe());render_previews(svg,item['icon_id'],48,run)
 item.update(result_dir=str(run),module=str(module),validation_status=report.status,errors=report.errors,warnings=report.warnings)
 (run/'review.json').write_text(json.dumps(item,indent=2));print(i,report.status,len(report.errors),len(report.warnings),flush=True)
(B/'runs.json').write_text(json.dumps(items,indent=2))
