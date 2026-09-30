from author import make,ROOT
import json
N=json.loads((ROOT/'comparison-plan.json').read_text())
make(1,'SQUARE',N[0]+ ' Rebuilt with a larger head, oval racket and curved torso.','''
circle('head',21,11,5)
line('torso',(21,24),(21,26))
path('lower-torso',(21,26),[('C',(18,33),(21,29),(19,31))]);join('torso','lower-torso')
poly('back-arm',(21,24),(12,26),(8,31));join('back-arm','torso')
poly('racket-arm',(21,24),(28,30),(34,30));join('racket-arm','torso');join('racket-arm','back-arm')
poly('legs',(6,42),(14,38),(18,33),(26,38),(26,42));join('legs','lower-torso')
path('racket',(32,20),[('A',(42,20),5,7,True),('A',(32,20),5,7,True)],True)
line('shaft',(37,27),(34,30));join('shaft','racket');join('shaft','racket-arm')
self.mark_human_figure('player',head='head',torso='torso',torso_junction='start')
''','human_ref/full_body_ref.png: circular head radius5, lower edge16 to neck24 gives exact4 ink gap; tangent follows head.')
make(2,'SQUARE',N[1]+ ' Restore three smooth lobes and three small bearings; center bearing becomes a dot.','''
path('spinner',(15,15),[('A',(33,15),9,9,True),('C',(35,24),(30,19),(31,23)),('C',(42,33),(41,24),(42,29)),('A',(33,42),9,9,True),('C',(24,37),(29,42),(27,39)),('C',(15,42),(21,39),(19,42)),('A',(6,33),9,9,True),('C',(13,24),(6,29),(7,24)),('C',(15,15),(17,23),(18,19))],True)
for n,x,y in [('top',24,15),('left',15,33),('right',33,33)]:circle(n,x,y,2)
self.add_dot('hub',(24,26))
''','Three mirrored lobes share circular bearings; no useful direct Lucide match.')
make(3,'SQUARE',N[2]+ ' Round all three tips and use a smaller hub with long smoothly widening blades.','''
circle('hub',24,25,6)
path('top-blade',(19,22),[('L',(18,12)),('A',(30,12),6,6,True),('L',(29,22))]);join('top-blade','hub')
path('left-blade',(18,25),[('L',(8,33)),('A',(14,42),6,6,False),('L',(23,31))]);join('left-blade','hub')
path('right-blade',(30,25),[('L',(40,33)),('A',(34,42),6,6,True),('L',(25,31))]);join('right-blade','hub')
''','Lucide fan original and atoms: few coherent rounded blade contours around a central hub; three blades per source.')
make(4,'HRECT_L',N[3]+ ' Restore three trunks and wider tiered evergreen silhouettes.','''
poly('front',(24,8),(34,24),(30,24),(36,32),(24,32),(12,32),(18,24),(14,24),closed=True)
poly('left',(14,24),(10,14),(4,26),(8,26),(4,34),(12,34))
poly('right',(34,24),(38,14),(44,26),(40,26),(44,34),(36,34))
join('left','front');join('right','front')
line('trunk-mid',(24,32),(24,40));join('trunk-mid','front')
line('trunk-left',(8,34),(8,40));line('trunk-right',(40,34),(40,40));join('trunk-left','left');join('trunk-right','right')
''','Lucide trees original and atoms: tiered evergreen edges and independent trunks, central tree taller.')
make(5,'HRECT_L',N[4]+ ' Lengthen curved horns and taper the face; emphasize third eye with a short stroke.','''
path('head',(16,15),[('C',(24,10),(18,10),(21,10)),('C',(32,15),(27,10),(30,10)),('C',(34,26),(36,19),(36,23)),('L',(29,34)),('A',(19,34),5,6,True),('L',(14,26)),('C',(16,15),(12,23),(12,19))],True)
for side in [-1,1]:
 p=lambda x,y:(24+side*x,y)
 path(f'horn-{side}',p(8,15),[('C',p(20,16),p(16,3),p(20,8)),('C',p(20,24),p(20,19),p(18,22))]);join('head',f'horn-{side}')
line('third-eye',(22,19),(26,19))
self.add_dot('eye-l',(20,28));self.add_dot('eye-r',(28,28))
''')
