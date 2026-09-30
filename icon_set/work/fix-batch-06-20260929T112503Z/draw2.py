from author import make
make(6,'HRECT_L','Rejected pie became a plain half-disc and lost the connected rising zigzag. Restore an open circular pie with a radial sector and a continuous growth arrow.','''
path('chart',(32,16),[('C',(20,8),(30,10),(26,8)),('A',(4,24),16,16,False),('A',(20,40),16,16,False),('L',(28,32)),('L',(34,36)),('L',(44,20))])
poly('sector',(20,8),(20,24),(32,16));join('sector','chart')
poly('arrow',(36,20),(44,20),(44,28));join('arrow','chart')
''','Lucide chart-pie original and atomic geometry: radial sector, circular outline; original connected growth line.')
make(7,'SQUARE','Rejected piggy bank was a boxy animal without a rounded back. Restore a round belly, arched rump, ear and two short feet beneath the separate coin. Tail and coin denomination omitted for spacing.','''
circle('coin',29,11,5)
path('pig',(6,27),[('L',(11,27)),('L',(13,19)),('L',(21,25)),('L',(30,25)),('A',(42,37),12,12,True),('L',(42,38)),('L',(37,42)),('L',(30,42)),('L',(30,38)),('L',(20,38)),('L',(20,42)),('L',(12,42)),('L',(12,35)),('L',(6,35)),('L',(6,27))],True)
''','Lucide piggy-bank original and atomic geometry: rounded body, snout, ear and paired feet; left facing per original.')
make(8,'SQUARE','Rejected Pikachu resembled a generic round mouse with antenna strokes. Restore a single pointed-ear silhouette and broad cheeks; keep paired eyes and a short mouth. Omit ear-tip divisions and tiny cheek patches.','''
path('outline',(12,24),[('L',(6,6)),('C',(19,20),(13,9),(16,15)),('A',(29,20),13,13,True),('C',(42,6),(32,15),(35,9)),('L',(36,24)),('A',(38,32),13,13,True),('C',(24,42),(38,39),(31,42)),('C',(10,32),(17,42),(10,39)),('A',(12,24),13,13,True)],True)
self.add_dot('eye-l',(18,29));self.add_dot('eye-r',(30,29))
line('mouth',(22,37),(26,37))
''')
make(9,'SQUARE','Rejected Poseidon lost the crown and reduced the robe to a traffic-sign triangle. Restore a crowned open face and draped body beside the three-prong trident.','''
path('head',(6,6),[('L',(6,10)),('A',(18,10),6,6,False),('L',(18,6))])
line('crown',(12,6),(12,10));join('head','crown')
path('robe',(6,42),[('L',(8,29)),('A',(12,24),5,5,True),('L',(14,24)),('L',(24,42)),('L',(6,42))],True)
poly('arm',(14,24),(24,30),(34,30));join('arm','robe')
path('trident',(26,6),[('L',(26,14)),('A',(34,22),8,8,False),('A',(42,14),8,8,False),('L',(42,6))])
poly('shaft',(34,6),(34,22),(34,30),(34,42));join('shaft','trident');join('shaft','arm')
''','human_ref/full_body_ref.png for head and coherent robe; crown and trident follow original.')
make(10,'SQUARE','Rejected runner had an undersized head and stiff flat shoulders. Enlarge head, curve the torso through the hip and give both arms a clear elbow while retaining opposed legs.','''
circle('head',28,11,5)
path('torso',(28,24),[('C',(22,32),(28,27),(24,30))])
poly('rear-arm',(28,24),(17,20),(10,27));poly('front-arm',(28,24),(34,30),(42,27))
poly('rear-leg',(22,32),(15,40),(6,40));poly('front-leg',(22,32),(32,36),(29,42))
for a in ['rear-arm','front-arm','rear-leg','front-leg']:join('torso',a)
join('rear-arm','front-arm');join('rear-leg','front-leg')
self.mark_human_figure('runner',head='head',torso='torso-0',torso_junction='start')
''','human_ref/full_body_ref.png: radius5 head, torso at24, exact4 ink gap; curved upper torso has vertical neck tangent.')
