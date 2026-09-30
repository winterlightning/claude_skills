from author import make
make(16,'HRECT_L','Rejected guinea pig looked like a short-legged dog with a square haunch. Restore a full rounded seated rump, tiny round ear and short front foot. Omit small mouth and inner haunch line for spacing.','''
path('body',(18,40),[('A',(4,26),14,14,True),('A',(18,12),14,14,True),('L',(28,12)),('A',(34,12),3,4,True),('C',(44,24),(40,12),(44,18)),('C',(36,31),(44,28),(40,30)),('L',(39,36)),('A',(36,40),3,4,True),('L',(18,40))],True)
self.add_dot('eye',(34,23))
''')
make(17,'SQUARE','Rejected rocking figure sat as a right-angle glyph attached to the base. Restore a curved seated back and bent forward arm, with a distinct rising rocker.','''
circle('head',19,11,5)
path('torso',(19,24),[('C',(17,30),(19,26),(17,28)),('A',(21,34),4,4,False)])
poly('leg',(21,34),(29,34),(36,40));join('torso','leg')
poly('arm',(19,24),(25,26),(30,26));join('arm','torso')
path('rocker',(6,32),[('C',(24,42),(9,39),(16,42)),('C',(36,40),(29,42),(33,42)),('C',(42,30),(40,38),(42,33))])
join('leg','rocker')
self.mark_human_figure('person',head='head',torso='torso-0',torso_junction='start')
''','human_ref/full_body_ref.png circular head, curved seated torso. Head bottom16 to torso24 gives exact4 ink gap.')
make(18,'SQUARE','Rejected kangaroo had a rectangular head and no long ears. Restore a long upright ear, sloping muzzle, round haunch and a long raised tail; omit tiny eye and forepaw.','''
path('outline',(6,20),[('L',(14,12)),('L',(14,6)),('A',(22,6),4,4,True),('L',(22,16)),('C',(32,30),(29,19),(31,24)),('C',(42,28),(36,33),(40,30)),('C',(28,40),(41,37),(35,40)),('L',(28,42)),('L',(12,42)),('A',(12,34),4,4,True),('L',(20,34)),('C',(14,24),(12,33),(12,29)),('L',(6,20))],True)
''')
make(19,'VRECT_L','Rejected meditator was a flat trapezoid over a narrow oval. Restore a taller upright body, sloping relaxed arms and a broad rounded crossed-leg base.','''
circle('head',24,10,6)
line('torso',(24,24),(24,32))
poly('arms',(8,32),(14,32),(18,24),(24,24),(30,24),(34,32),(40,32));join('torso','arms')
path('legs',(24,32),[('L',(13,35)),('A',(14,44),5,5,False),('L',(34,44)),('A',(35,35),5,5,False),('L',(24,32))],True)
join('torso','legs')
self.mark_human_figure('person',head='head',torso='torso',torso_junction='start')
''','human_ref/full_body_ref.png: circular head radius6, neck24 exact4 ink gap and mirrored relaxed arms.')
make(20,'SQUARE','Rejected car was a pentagonal box and the person a rigid chair shape. Restore the sloped windshield, front bumper, paired wheels and a curved seated torso with reaching forearm.','''
circle('head',11,11,5)
path('torso',(11,24),[('L',(11,30)),('A',(16,35),5,5,False)])
poly('legs',(16,35),(22,35),(28,42));join('torso','legs')
poly('arm',(11,24),(17,27),(20,27));join('arm','torso')
poly('roof',(26,14),(29,6),(39,6),(42,14))
box('car',26,14,42,24,2);join('roof','car')
line('wheel-l',(28,24),(28,27));line('wheel-r',(40,24),(40,27));join('wheel-l','car');join('wheel-r','car')
''','human_ref/full_body_ref.png: radius5 head lower16 to torso24; Lucide car-front original and atomic geometry: windshield over bumper and two wheels.')
