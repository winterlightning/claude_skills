from author import make,ROOT
import json
N=json.loads((ROOT/'comparison-plan.json').read_text())
make(6,'VRECT_L',N[5]+ ' Rebalance bow to a wider, shallower form and give the long lapels clear space inside the jacket.','''
poly('bow-left',(8,4),(24,10),(8,16),closed=True)
poly('bow-right',(40,4),(24,10),(40,16),closed=True);join('bow-left','bow-right')
poly('lapels',(8,16),(24,36),(40,16));join('lapels','bow-left');join('lapels','bow-right')
poly('jacket',(8,16),(8,44),(24,44),(40,44),(40,16));join('jacket','bow-left');join('jacket','bow-right');join('jacket','lapels')
line('seam',(24,36),(24,44));join('seam','jacket');join('seam','lapels')
''','Shared center axis and mirrored bow/lapels; tiny jacket taper omitted for clear spacing.')
make(8,'SQUARE',N[7]+ ' Restore two child hairlines and a curved ponytail; use touching circular faces at shared tangent point.','''
path('upper-head',(22,24),[('A',(6,16),10,10,True),('A',(16,6),10,10,True),('A',(26,16),10,10,True),('A',(22,24),10,10,True)],True)
path('lower-head',(22,24),[('A',(34,24),10,10,True),('A',(38,32),10,10,True),('A',(28,42),10,10,True),('A',(18,32),10,10,True),('A',(22,24),10,10,True)],True)
join('upper-head','lower-head')
line('upper-hair',(6,16),(26,16));join('upper-hair','upper-head')
line('lower-hair',(18,32),(38,32));join('lower-hair','lower-head')
path('ponytail',(34,24),[('C',(42,18),(34,14),(42,12))]);join('ponytail','lower-head')
''','human_ref/user.svg: circular jaws; two hairlines restore the children, with original diagonal arrangement.')
make(9,'HRECT_M',N[8]+ ' Rebuild equal rounder lobes and a wide central lens, meeting at two shared intersection nodes.','''
for side in [-1,1]:
 p=lambda x,y:(24+side*x,y)
 path(f'outer-{side}',p(0,12),[('C',p(6,10),p(2,10),p(4,10)),('A',p(20,24),14,14,side>0),('A',p(6,38),14,14,side>0),('C',p(0,36),p(4,38),p(2,38))])
 path(f'inner-{side}',p(0,12),[('C',p(8,24),p(5,15),p(8,19)),('C',p(0,36),p(8,29),p(5,33))])
for a,b in [('outer--1','outer-1'),('inner--1','inner-1'),('outer--1','inner--1'),('outer--1','inner-1'),('outer-1','inner--1'),('outer-1','inner-1')]:join(a,b)
''','Two matched circle-like contours. Round outer quarter arcs and smooth cubic intersection spans preserve horizontal Venn layout on the integer grid.')
make(11,'VRECT_L',N[10]+ ' Give the cap a domed crown over a circular jaw and deepen the book pages around a central fold.','''
path('head',(16,12),[('A',(32,12),8,8,True),('L',(32,16)),('A',(16,16),8,8,True),('L',(16,12))],True)
line('cap',(16,12),(32,12));join('head','cap')
path('shoulders',(8,31),[('A',(24,28),16,3,True),('A',(40,31),16,3,True)]);join('head','shoulders')
poly('book',(8,31),(24,35),(40,31),(40,40),(24,44),(8,40),closed=True)
line('fold',(24,35),(24,44));join('fold','book');join('shoulders','book')
''','human_ref/user.svg circular jaw lower24 and shoulder28 touching ink; source cap and open book.',extra='    human_construction = "bust"')
make(13,'HRECT_L',N[12]+ ' Reshape bag as a hanging teardrop and restore a low dog back with upright ear and muzzle.','''
circle('head',19,13,5)
line('torso',(19,26),(19,31));poly('legs',(19,40),(19,31),(27,40));join('legs','torso')
poly('bag-arm',(19,26),(15,26),(8,22));join('bag-arm','torso')
path('bag',(8,22),[('C',(4,35),(7,27),(4,32)),('A',(12,35),4,5,False),('C',(8,22),(12,31),(9,27))],True);join('bag','bag-arm')
poly('leash',(19,26),(26,26),(34,32));join('leash','torso');join('leash','bag-arm')
poly('dog',(34,40),(34,32),(44,32),(44,24),(40,20));join('dog','leash')
line('foreleg',(44,32),(44,40));join('foreleg','dog')
self.mark_human_figure('person',head='head',torso='torso',torso_junction='start')
''','human_ref/full_body_ref.png: radius5 head bottom18 to neck26 exact4 ink gap; original hanging bag and dog.')
