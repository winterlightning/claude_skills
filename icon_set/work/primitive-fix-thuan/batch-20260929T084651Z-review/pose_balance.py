from author import *
updates={
15: '''
 # Plan: HRECT_M extremes (4,10)-(44,38), low fold centered at y24; r6 head, 14u to neck.
 circle(s,'head',10,16,6)
 s.add_bezier('torso',(24,16),((33,16),(44,15),(44,26)))
 path(s,'hip-leg',(44,26),('C',(26,38),(44,35),(37,38)),('L',(4,38)));s.relate('connect','torso','hip-leg')
 path(s,'arm',(24,16),('C',(17,30),(24,24),(21,30)),('L',(4,30)));s.relate('connect','arm','torso')
 s.mark_human_figure('person',head='head',torso='torso',torso_junction='start')
 ''',
16: '''
 # Plan: VRECT_M extremes (10,4)-(38,44), bowed head follows shoulder tangent (5,-12).
 circle(s,'head',25,9,5)
 s.add_bezier('torso',(20,21),((15,33),(10,29),(10,35)))
 path(s,'hips',(10,35),('C',(21,41),(10,42),(16,44)),('L',(29,30)),('L',(38,44)));s.relate('connect','torso','hips')
 s.add_polyline('embracing-arm',(20,21),(34,27),(23,29));s.relate('connect','torso','embracing-arm')
 s.mark_human_figure('person',head='head',torso='torso',torso_junction='start')
 '''
}
for i,body in updates.items():
 old=DESIGNS[i-1];DESIGNS[i-1]=(old[0],'VRECT_M' if i==16 else old[1],old[2],old[3],body)
author(sorted(updates))
