from author import *
runs=json.loads((BATCH/'runs.json').read_text())
current={i+1:(ROOT/r['run']/r['module']).read_text().split('        s=self\n',1)[1] for i,r in enumerate(runs)}
updates={}
for i in [3,4]:
 updates[i]=textwrap.dedent(current[i]).replace("(21,33),('C',(26,31),(23,31),(24,30))","(21,32),('C',(26,30),(23,30),(24,29))")
updates[18]='''
 # Plan: SQUARE extremes (6,6)-(42,42); head r5 and neck distance 13u.
 circle(s,'head',35,11,5)
 s.add_line('torso',(35,24),(35,36))
 s.add_polyline('arm',(35,24),(30,28),(24,28));s.relate('connect','torso','arm')
 s.add_polyline('leg',(35,36),(25,36),(22,42));s.relate('connect','torso','leg')
 s.add_polyline('laptop',(9,14),(13,28),(24,28));s.relate('connect','arm','laptop')
 s.add_line('desk',(6,28),(13,28));s.relate('connect','laptop','desk')
 s.add_line('desk-leg',(10,28),(10,42));s.relate('connect','desk','desk-leg')
 s.add_polyline('chair',(35,36),(42,36),(42,42));s.relate('connect','chair','torso');s.relate('connect','chair','leg')
 s.mark_human_figure('worker',head='head',torso='torso',torso_junction='start')
'''
updates[14]='''
 # Plan: SQUARE extremes (6,6)-(42,42), ellipse fish and fork tail; seated torso right.
 circle(s,'head',35,11,5)
 s.add_line('torso',(35,24),(35,33))
 s.add_polyline('leg',(35,33),(25,33),(24,42));s.relate('connect','torso','leg')
 s.add_polyline('arm',(35,24),(29,28),(22,24));s.relate('connect','torso','arm')
 path(s,'rod',(22,24),('C',(10,6),(20,14),(16,6)))
 s.add_line('line',(10,6),(10,25));s.relate('connect','line','rod')
 path(s,'fish',(10,25),('A',(10,35),4,5,True),('A',(10,25),4,5,True),closed=True);s.relate('connect','line','fish')
 s.add_polyline('tail',(6,41),(10,35),(14,41));s.relate('connect','tail','fish')
 s.add_polyline('stool',(35,33),(42,33),(42,42));s.relate('connect','stool','torso');s.relate('connect','stool','leg')
 s.mark_human_figure('angler',head='head',torso='torso',torso_junction='start')
'''
for i,body in updates.items():
 old=DESIGNS[i-1];DESIGNS[i-1]=(*old[:4],body)
author(sorted(updates))
