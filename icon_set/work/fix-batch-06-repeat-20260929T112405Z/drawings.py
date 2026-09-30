H='Human full_body_ref.png: circular head, coherent limbs and exact 4-unit detached head gap'
author(0,'''
circle('head',16,12,6)
line('torso',(16,26),(16,32))
path('seat',(16,32),[('A',(24,42),10,10,False)]);join('seat','torso')
poly('legs',(24,42),(32,30),(40,42));join('legs','seat')
poly('arm',(16,26),(28,26),(32,30));join('arm','torso');join('arm','legs')
''','The rejected pose had a rigid rectangular arm and a low detached head far left of the knees. Moved the aligned head and torso toward the folded knees and softened the seated back, with the arm wrapping toward the knee.','VRECT_L',H)
author(1,'''
circle('head',28,9,5)
line('torso',(28,22),(28,30))
path('body-leg',(28,30),[('A',(24,34),4,4,True),('L',(17,34)),('A',(13,38),4,4,False),('L',(10,44))]);join('body-leg','torso')
poly('arm',(28,22),(22,26),(14,26));join('arm','torso')
poly('screen',(8,14),(12,26),(14,26));join('screen','arm')
path('chair',(40,20),[('L',(40,34)),('A',(32,42),8,8,True),('L',(28,42))])
line('seat',(24,34),(40,34));join('seat','chair');join('seat','body-leg')
self.mark_human_figure('person',head='head',torso='torso',torso_junction='start')
''','The rejected seated user had an angular chair and square hip. Restored the rounded hip, bent leg and curved chair support while retaining the open laptop and left-facing working pose.','VRECT_L',H+'; Lucide armchair: rounded seat transitions; laptop: open screen/base')
author(2,'''
path('body',(6,42),[('L',(6,32)),('C',(10,24),(6,28),(8,26)),('L',(10,20)),('A',(24,6),14,14,True),('A',(38,20),14,14,True),('L',(38,24)),('C',(42,32),(40,26),(42,28)),('L',(42,42)),('L',(6,42))],True)
path('muzzle',(24,17),[('C',(18,20),(20,14),(18,16)),('L',(18,24)),('A',(30,24),6,6,False),('L',(30,20)),('C',(24,17),(30,16),(28,14))],True)
poly('left-arm',(14,32),(14,42));join('left-arm','body')
poly('right-arm',(34,32),(34,42));join('right-arm','body')
''','The rejected orangutan had a single circular muzzle resembling one eye and tiny knee rings. Restored the broad two-lobed muzzle and long seated arms. Omitted ear loops and tiny knee rings to give the face room.',lucide='No useful direct Lucide ape match; original pear-shaped muzzle and long-arm silhouette')
author(3,'''
path('pastry',(4,32),[('C',(12,14),(4,24),(8,18)),('C',(27,8),(16,10),(23,8)),('C',(40,18),(34,8),(39,12)),('C',(44,30),(43,22),(44,26)),('A',(38,34),5,5,True),('C',(29,25),(34,32),(33,26)),('C',(19,28),(25,23),(22,25)),('C',(14,40),(18,31),(18,40)),('C',(4,32),(8,40),(4,38))],True)
path('seam-left',(12,14),[('C',(19,28),(18,16),(21,22))]);join('seam-left','pastry')
path('seam-right',(34,10),[('C',(29,25),(36,15),(34,22))]);join('seam-right','pastry')
''','The rejected pastry was a thin symmetric arch with pointed tips. Restored a plump asymmetric crescent with rounded tapered ends and curved segment seams, following the reference tilt.','HRECT_L','Lucide croissant: plump segmented body and rounded tapered ends')
author(4,'''
for j,x in enumerate((7,21,40)):
 circle(f'wheel-{j}',x,37,3)
path('cab',(26,29),[('L',(26,8)),('L',(32,8)),('A',(38,14),6,6,True),('L',(40,16)),('L',(44,24)),('L',(44,29)),('L',(40,29)),('L',(26,29))],True)
poly('chassis',(4,29),(7,29),(21,29),(26,29));join('chassis','cab')
for j,x in enumerate((7,21,40)):
 line(f'axle-{j}',(x,29),(x,34));join(f'axle-{j}',f'wheel-{j}');join(f'axle-{j}','cab' if j==2 else 'chassis')
poly('window',(34,16),(34,24),(44,24));join('window','cab')
''','The rejected tractor cab was undersized and its wheels hung on long stalks. Enlarged and rounded the cab, lowered the chassis toward the wheels and rebuilt the side window. Retained all three axles.','HRECT_L','Lucide truck: rounded cab corners and wheels close to the chassis')
