from author import make,ROOT
import json,textwrap
N=json.loads((ROOT/'comparison-plan.json').read_text())
make(2,'SQUARE',N[1]+ ' Restore smooth three-lobed body and four bearing marks; small holes simplify to dots for spacing.','''
path('spinner',(15,15),[('A',(33,15),9,9,True),('C',(35,24),(30,19),(31,23)),('C',(42,33),(41,24),(42,29)),('A',(33,42),9,9,True),('C',(24,37),(29,42),(27,39)),('C',(15,42),(21,39),(19,42)),('A',(6,33),9,9,True),('C',(13,24),(6,29),(7,24)),('C',(15,15),(17,23),(18,19))],True)
for n,x,y in [('top',24,15),('left',15,33),('right',33,33),('hub',24,26)]:self.add_dot(n,(x,y))
''','Mirrored smooth lobes and spaced bearing marks; no useful exact Lucide match.')
make(4,'HRECT_L',N[3]+ ' Restore three centered trunks, with a tall narrow foreground tree and smaller rear canopies.','''
poly('front',(24,8),(28,24),(30,32),(24,32),(18,32),(20,24),closed=True)
poly('left',(20,24),(4,24),(10,12),(20,24))
poly('right',(28,24),(44,24),(38,12),(28,24));join('left','front');join('right','front')
for n,x,top in [('mid',24,32),('left',10,24),('right',38,24)]:
 line(f'trunk-{n}',(x,top),(x,40));join(f'trunk-{n}','front' if n=='mid' else n)
''','Lucide trees original/atoms: staggered pointed canopies and three centered trunks; branch steps omitted.')
make(5,'HRECT_L',N[4]+ ' Restore long curved horns and taper the brow and muzzle around three separated eyes.','''
path('head',(16,12),[('C',(24,8),(18,8),(21,8)),('C',(32,12),(27,8),(30,8)),('C',(37,22),(34,16),(37,19)),('L',(37,28)),('C',(31,35),(37,32),(31,32)),('A',(17,35),7,5,True),('C',(11,28),(17,32),(11,32)),('L',(11,22)),('C',(16,12),(11,19),(14,16))],True)
for side in [-1,1]:
 p=lambda x,y:(24+side*x,y)
 path(f'horn-{side}',p(8,12),[('C',p(20,14),p(15,6),p(20,8)),('L',p(20,18))]);join('head',f'horn-{side}')
self.add_dot('third-eye',(24,17));self.add_dot('eye-l',(20,26));self.add_dot('eye-r',(28,26))
''')
make(8,'SQUARE',N[7]+ ' Add short swept hairlines and a curved ponytail while keeping the circular heads at a shared tangent.','''
path('upper-head',(22,24),[('A',(6,16),10,10,True),('A',(16,6),10,10,True),('A',(26,16),10,10,True),('A',(22,24),10,10,True)],True)
path('lower-head',(22,24),[('A',(34,24),10,10,True),('A',(38,32),10,10,True),('A',(28,42),10,10,True),('A',(18,32),10,10,True),('A',(22,24),10,10,True)],True)
join('upper-head','lower-head')
line('upper-hair',(6,16),(19,16));join('upper-hair','upper-head')
line('lower-hair',(25,32),(38,32));join('lower-hair','lower-head')
path('ponytail',(34,24),[('C',(42,18),(34,14),(42,12))]);join('ponytail','lower-head')
''','human_ref/user.svg circular jaws; original diagonal pair and ponytail. Hairlines shortened to keep heads clear.')
make(13,'HRECT_L',N[12]+ ' Restore a slim hanging bag and recognizable dog back and upright head.','''
circle('head',20,13,5)
line('torso',(20,26),(20,31));poly('legs',(20,40),(20,31),(28,40));join('legs','torso')
poly('bag-arm',(20,26),(15,26),(8,22));join('bag-arm','torso')
path('bag',(8,22),[('C',(4,35),(7,27),(4,32)),('A',(12,35),4,5,False),('C',(8,22),(12,31),(9,27))],True);join('bag','bag-arm')
poly('leash',(20,26),(26,26),(36,32));join('leash','torso');join('leash','bag-arm')
poly('dog',(36,40),(36,32),(44,32),(44,24),(40,20));join('dog','leash')
line('foreleg',(44,32),(44,40));join('foreleg','dog')
self.mark_human_figure('person',head='head',torso='torso',torso_junction='start')
''','human_ref/full_body_ref.png: radius5 head bottom18 and neck26 gives exact4 ink gap.')
make(15,'CIRCLE',N[14]+ ' Restore curved inner neck and pointed beak while opening the narrow wing-to-neck gap.','''
path('dragon',(24,4),[('A',(44,24),20,20,True),('A',(24,44),20,20,True),('A',(4,24),20,20,True),('C',(14,8),(4,17),(9,11)),('C',(18,25),(11,19),(12,25)),('C',(32,21),(24,30),(32,28)),('L',(25,20)),('C',(24,4),(24,14),(22,8))],True)
''','Original circular curled wing and pointed head; neck moved with its owner to enlarge the opening.')
make(17,'SQUARE',N[16]+ ' Restore arcing crop rows and a separate hillside, joining at a shared node.','''
path('row-outer',(6,42),[('C',(18,18),(6,32),(10,26)),('C',(42,6),(26,10),(32,6))])
path('row-middle',(18,42),[('A',(42,18),24,24,True)])
path('row-inner',(30,42),[('A',(42,30),12,12,True)])
path('hill',(6,8),[('C',(18,18),(10,8),(15,13))]);join('hill','row-outer')
''','Concentric crop arcs and opposing hill with a shared junction. Small left-side row fragment omitted for clarity.')
