from author import *
runs=json.loads((BATCH/'runs.json').read_text())
current={i+1:(ROOT/r['run']/r['module']).read_text().split('        s=self\n',1)[1] for i,r in enumerate(runs)}
updates={}
for i in [3,4]:
 updates[i]=textwrap.dedent(current[i]).replace("(20,33),('C',(26,31),(22,31),(24,30))","(21,33),('C',(26,31),(23,31),(24,30))")
updates[2]=textwrap.dedent(current[2]).replace("s.add_line('torso',(28,20),(22,30))","s.add_line('torso',(28,20),(28,23))\ns.add_line('lower-torso',(28,23),(22,30))\ns.relate('connect','torso','lower-torso')").replace('(19,18)','(19,20)').replace("s.relate('connect','torso',part)","s.relate('connect','torso' if part=='arms' else 'lower-torso',part)")
updates[13]=textwrap.dedent(current[13]).replace("(13,32),(28,32),(32,44)","(13,32),(29,32),(32,44)").replace("'child-head',28,16,3","'child-head',29,13,3").replace('(28,27),(28,32)','(29,24),(29,32)').replace('(28,32),(37,33)','(29,32),(37,33)').replace('(13,22),(18,28),(28,27)','(13,22),(19,25),(29,24)')
updates[15]=textwrap.dedent(current[15]).replace('(22,28),(21,33)','(23,28),(21,33)')
updates[16]=textwrap.dedent(current[16]).replace('((14,24),(10,29),(10,35))','((15,33),(10,29),(10,35))').replace('(34,26),(23,28)','(34,27),(23,29)')
updates[20]='''
 # Plan: upright shoulders, lowered arms, two hooked knees and crossed single-stroke legs.
 circle(s,'head',24,9,5)
 s.add_line('torso',(24,22),(24,33))
 path(s,'shoulders',(12,34),('L',(12,30)),('A',(20,22),8,8,True),('L',(28,22)),('A',(36,30),8,8,True),('L',(36,34)));s.relate('connect','torso','shoulders')
 path(s,'leg-front',(12,34),('C',(7,39),(6,32),(2,37)),('L',(38,44)))
 path(s,'leg-back',(36,34),('C',(41,39),(42,32),(46,37)),('L',(10,44)))
 s.relate('connect','shoulders','leg-front');s.relate('connect','shoulders','leg-back')
 s.mark_human_figure('person',head='head',torso='torso',torso_junction='start')
'''
for i,body in updates.items():
 old=DESIGNS[i-1];DESIGNS[i-1]=(*old[:4],body)
author(sorted(updates))
