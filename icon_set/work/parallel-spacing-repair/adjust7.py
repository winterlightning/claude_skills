from author import write,ROOT,TARGETS,WORK
import shutil
for i in (11,51,74):shutil.copy2(ROOT/TARGETS[i]['source_path'],WORK/('pre-final-'+str(i)+'.py'))
write(11,'VRECT_L','''
p('body',(8,14),(40,14),(40,44),(8,44),(8,14))
p('terminal',(16,14),(16,4),(32,4),(32,14))
link('connect','terminal','body')
p('charge',(24,23),(16,29),(32,29),(24,35))
''','Charging battery: a centered broad lightning stroke with open turns and a clear terminal.')
write(51,'SQUARE','''
p('hammer',(6,6),(32,6),(32,14),(24,14))
a('outer-body',(24,14),(42,32),18)
p('tail',(42,32),(34,42),(26,42),(32,32))
a('inner-body',(32,32),(16,22),16,10,sweep=False)
p('head-return',(16,22),(6,14),(6,6))
link('connect','hammer','outer-body')
link('connect','outer-body','tail')
link('connect','tail','inner-body')
link('connect','inner-body','head-return')
link('connect','head-return','hammer')
l('splash-high',(6,32),(8,34))
l('splash-low',(6,42),(8,42))
''','Leaping hammerhead: broad hammer-shaped head, smooth arcing body and an open tail with separated splash marks.')
write(74,'HRECT_L','''
p('plane',(38,8),(26,14),(20,8),(12,12),(22,22),(10,26),(4,16),(4,32),(14,32),(38,20))
a('nose',(38,20),(38,8),6,sweep=False)
link('connect','plane','nose')
l('runway',(4,40),(44,40))
''','Departing plane: broad clear wing and tail, a smooth circular nose and a straight runway.')
