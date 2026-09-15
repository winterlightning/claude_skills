exec(open(__file__.replace('rebuild.py','repair.py')).read().split('edit(3,')[0])
H='from ._symmetry_curves import path, ellipse, line, poly, contacts\n'
for i in (1,2):
 redraw(i,H+f'''
for j,cx in enumerate((8,24,40)):
    front = {i==2} and j == 1
    cy = 15 if front else 11
    bottom = 36 if {i==2} and not front else 40
    top = cy+7
    ellipse(self,f'head-{{j}}',cx,cy,3)
    ellipse(self,f'body-{{j}}',cx,(top+bottom)//2,4,(bottom-top)//2)
    self.relate('connect',f'head-{{j}}',f'body-{{j}}')
''','Rebalance three pin heads and bodies as repeated rounded shapes; their painted head/body contours meet tangentially.',key='HRECT_L')
redraw(10,H+'''
ellipse(self,'head',29,11,5)
ellipse(self,'ball',39,39,3)
path(self,'body',(24,23),('C',(22.5,26.6),(18.5,28.25),(17,30)))
poly(self,'left-arm',(24,23),(14,22),(8,26))
poly(self,'right-arm',(24,23),(34,28),(42,28))
poly(self,'back-leg',(17,30),(12,36),(6,36))
poly(self,'front-leg',(17,30),(28,36),(26,42))
contacts(self)
self.mark_human_figure('person',head='head',torso='body-1',torso_junction='start')
''','Preserve the approved head at (29,11) and shoulder (24,23); use a coherent torso curve tangent to the head axis. Gap 13-5=8 centerline units.')
redraw(17,H+'''
path(self,'hand',(42,6),('L',(30,6)),('L',(16,16)),('A',4,4,False,(22,22)),('L',(30,16)),('C',(34,16),(37,19),(40,14)))
ellipse(self,'head',24,34,2)
path(self,'shoulders',(6,42),('A',18,2,True,(24,40)),('A',18,2,True,(42,42)))
self.relate('connect','head','shoulders')
''','Focus the selecting hand on one clear avatar. Retain the pointing fingertip; remove the two redundant background people to open the composition.')
edit(11,[('(14, 34)','(16, 34)'),('(14, 15)','(16, 15)'),('(14, 21)','(16, 21)'),('(27, 34)','(28, 34)'),('(27, 15)','(28, 15)'),('(27, 21)','(28, 21)'),('(8, 18)','(6, 20)'),('(34, 18)','(36, 20)'),('(35, 29)','(36, 30)'),('radius_x=13, radius_y=12','radius_x=15, radius_y=14'),("'chin', p_27_21, p_14_21, radius_x=7, radius_y=8", "'chin', p_27_21, p_14_21, radius_x=6, radius_y=6")],'Widen the headdress around a circular jaw and retain the reclining lion body.')
for i in (20,22):
 front="('L',(36,44))" if i==22 else "('L',(40,40)),('L',(38,44))"
 redraw(i,H+f'''
ellipse(self,'head',16,8,4)
path(self,'torso',(16,20),('C',(16,24),(16,28),(16,30)))
poly(self,'arm',(16,20),(24,20),(26,18))
path(self,'horse',(8,44),('L',(8,38)),('L',(8,30)),('L',(16,30)),('L',(24,30)),('L',(26,18)),('L',(28,10)),('L',(40,18)),('L',(40,26)),('L',(36,26)),('L',(36,38)),{front})
poly(self,'belly',(8,38),(16,38),(36,38))
poly(self,'rider-leg',(16,30),(16,38),(16,40))
line(self,'tail',(8,30),(8,22))
contacts(self)
self.mark_human_figure('rider',head='head',torso='torso-1',torso_junction='start')
''','Reconstruct the horse neck and saddle together; preserve circular rider head, reins and distinct horse/rider legs. Human reference full_body_ref.png; head gap 12-4=8.',key='VRECT_L')
redraw(49,H+'''
ellipse(self,'head',24,11,5)
path(self,'shoulders',(10,28),('C',(13,24),(19,24),(24,24)),('C',(29,24),(35,24),(38,28)))
line(self,'arm-l',(10,28),(6,34))
line(self,'arm-r',(38,28),(42,34))
line(self,'torso',(24,24),(24,38))
poly(self,'leg-l',(6,34),(24,38),(42,42))
poly(self,'leg-r',(42,34),(24,38),(6,42))
contacts(self)
self.mark_human_figure('person',head='head',torso='torso',torso_junction='start')
''','Rest both hands directly on the crossed knees. Preserve the broad smooth shoulders and exact 8-unit head gap.')
redraw(50,H+'''
ellipse(self,'head',24,8,4)
poly(self,'torso',(24,20),(24,28),(24,44))
poly(self,'left-arm',(24,20),(8,32),(24,28))
poly(self,'right-arm',(24,20),(40,32),(24,28))
poly(self,'knees',(8,40),(24,44),(40,40))
contacts(self)
self.mark_human_figure('person',head='head',torso='torso-1',torso_junction='start')
''','Open both prayer-arm counters above broad seated knees; remove the redundant crossing leg stroke to keep the seated prayer readable.',key='VRECT_L')
for i in (30,31):
 outline="ellipse(self,'frame',24,24,20)" if i==31 else "path(self,'frame',(6,6),('L',(24,6)),('A',18,18,True,(42,24)),('L',(42,42)),('L',(24,42)),('A',18,18,True,(6,24)),('L',(6,6)),closed=True)"
 redraw(i,H+outline+'''
poly(self,'l',(16,16),(16,24),(16,32),(24,32),(32,32))
path(self,'m',(16,32),('L',(16,24)),('A',4,4,True,(24,24)),('A',4,4,True,(32,24)),('L',(32,32)))
line(self,'middle',(24,24),(24,32))
contacts(self)
''','Retain the LM monogram, with the L sharing the left stem and baseline. Equal 8-unit m arches fit the enclosing brand shape.',key='CIRCLE' if i==31 else 'SQUARE')
redraw(34,H+'''
poly(self,'main',(8,24),(8,44),(40,28),(40,18),(8,4),(8,14),(22,22))
line(self,'fold',(40,18),(16,34))
contacts(self)
''','Preserve the Dynamics folded ribbon; shorten its internal diagonal before it creates a narrow triangular pinch at the lower corner.',key='VRECT_L')
redraw(65,H+'''
path(self,'head',(6,24),('A',18,18,True,(42,24)))
poly(self,'eye-left',(18,17),(20,19),(18,21))
poly(self,'eye-right',(30,17),(28,19),(30,21))
path(self,'flow',(16,30),('L',(32,30)),('L',(32,34)),('C',(32,38),(39,39),(40,42)),('L',(8,42)),('C',(9,39),(16,38),(16,34)),('L',(16,30)),closed=True)
''','Replace the pinched vomit puddle zigzags with one smooth widening stream and broad bottom opening.')
(W/'rebuild-changes.json').write_text(json.dumps(CHANGED,indent=2))
