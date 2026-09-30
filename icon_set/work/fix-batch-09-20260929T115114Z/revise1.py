from author import make,ROOT
import json,textwrap
N=json.loads((ROOT/'comparison-plan.json').read_text())
# Fresh run with the head and neck moved together to leave room for the racket.
m=json.loads((ROOT/'latest-1.json').read_text());s=(ROOT.parents[2]/m['result_dir']/m['module']).read_text();body=textwrap.dedent("        circle('head'"+s.split("        circle('head'",1)[1]);body=body.replace("'head',21,11","'head',20,11").replace('(21,24)','(20,24)').replace('(21,26)','(20,26)').replace('(21,29)','(20,29)')
make(1,'SQUARE',m['comparison'],body,m['construction_reference'])
make(2,'SQUARE',N[1]+ ' Rebuild as three circular bearing lobes joined to a central axle, omitting the crowded extra rim.','''
for n,x,y in [('top',24,12),('left',12,36),('right',36,36)]:circle(n,x,y,6)
line('top-arm',(24,18),(24,24));line('left-arm',(24,24),(12,30));line('right-arm',(24,24),(36,30))
join('top-arm','top');join('left-arm','left');join('right-arm','right')
join('top-arm','left-arm');join('top-arm','right-arm');join('left-arm','right-arm')
''','Three equal circular bearings with shared central axle; no useful exact Lucide match.')
make(3,'SQUARE',N[2]+ ' Rebuild blades with smooth rounded ends and a smaller central hub.','''
circle('hub',24,24,7)
path('top-blade',(17,24),[('L',(18,12)),('A',(30,12),6,6,True),('L',(31,24))]);join('top-blade','hub')
path('left-blade',(17,24),[('L',(8,32)),('C',(6,36),(6,33),(6,34)),('A',(12,42),6,6,False),('L',(24,31))]);join('left-blade','hub');join('left-blade','top-blade')
path('right-blade',(31,24),[('L',(40,32)),('C',(42,36),(42,33),(42,34)),('A',(36,42),6,6,True),('L',(24,31))]);join('right-blade','hub');join('right-blade','top-blade');join('left-blade','right-blade')
''','Lucide fan original/atoms: coherent rounded blades about a round hub; mirrored lower blades.')
make(4,'HRECT_L',N[3]+ ' Restore three trunks and stagger the foliage to make three distinct trees.','''
poly('front',(24,8),(36,32),(24,32),(12,32),closed=True)
poly('left',(16,24),(4,24),(10,12),(18,20));poly('right',(32,24),(44,24),(38,12),(30,20));join('left','front');join('right','front')
line('trunk-mid',(24,32),(24,40));join('trunk-mid','front')
line('trunk-left',(8,24),(8,36));line('trunk-right',(40,24),(40,36));join('trunk-left','left');join('trunk-right','right')
''','Lucide trees original/atoms: staggered canopies with separate trunks. Small foliage steps omitted for spacing.')
make(5,'HRECT_L',N[4]+ ' Extend the horns downward and give the skull a longer rounded muzzle while preserving three eyes.','''
path('head',(16,12),[('C',(24,8),(18,8),(21,8)),('C',(32,12),(27,8),(30,8)),('C',(37,20),(36,14),(37,17)),('L',(37,28)),('C',(31,35),(37,32),(31,32)),('A',(17,35),7,5,True),('C',(11,28),(17,32),(11,32)),('L',(11,20)),('C',(16,12),(11,17),(12,14))],True)
for side in [-1,1]:
 p=lambda x,y:(24+side*x,y)
 path(f'horn-{side}',p(8,12),[('C',p(20,14),p(15,6),p(20,8)),('L',p(20,22))]);join('head',f'horn-{side}')
self.add_dot('third-eye',(24,17));self.add_dot('eye-l',(20,26));self.add_dot('eye-r',(28,26))
''')
