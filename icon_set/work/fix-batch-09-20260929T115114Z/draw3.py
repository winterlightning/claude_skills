from author import make,ROOT
import json
N=json.loads((ROOT/'comparison-plan.json').read_text())
make(11,'VRECT_L',N[10]+ ' Give the cap a domed crown over a longer circular jaw and shape the book around a central fold.','''
path('head',(16,12),[('A',(32,12),8,8,True),('L',(32,16)),('A',(16,16),8,8,True),('L',(16,12))],True)
line('cap',(16,12),(32,12));join('head','cap')
path('shoulders',(8,32),[('A',(24,28),16,4,True),('A',(40,32),16,4,True)])
join('head','shoulders')
poly('book',(8,32),(24,36),(40,32),(40,40),(24,44),(8,40),closed=True)
line('fold',(24,36),(24,44));join('fold','book');join('shoulders','book')
''','human_ref/user.svg circular jaw lower24 touches shoulder ink at28; original cap and open book.',extra='    human_construction = "bust"')
make(12,'HRECT_L',N[11]+ ' Broaden the tent roof and restore a longer tent body beside the crowned bust.','''
poly('tent-roof',(4,20),(12,8),(20,20),closed=True)
poly('tent-body',(8,20),(6,38),(18,38),(16,20));join('tent-body','tent-roof')
poly('crown',(28,8),(32,12),(36,8),(40,12),(44,8),(42,20),(30,20),closed=True)
path('jaw',(30,20),[('A',(42,20),6,6,False)]);join('jaw','crown')
path('shoulders',(26,40),[('A',(36,30),10,10,True),('A',(44,34),10,10,True),('L',(44,40))]);join('jaw','shoulders')
''','human_ref/user.svg: circular jaw and close shoulders; crown and tent retain original layout.',extra='    human_construction = "bust"')
make(13,'HRECT_L',N[12]+ ' Reshape the bag as a hanging teardrop and give the dog a recognizable muzzle and upright ear.','''
circle('head',19,13,5)
line('torso',(19,26),(19,31));poly('legs',(15,40),(19,31),(25,40));join('legs','torso')
poly('bag-arm',(19,26),(15,26),(8,22));join('bag-arm','torso')
path('bag',(8,22),[('C',(4,35),(7,27),(4,32)),('A',(12,35),4,5,False),('C',(8,22),(12,31),(9,27))],True);join('bag','bag-arm')
poly('leash',(19,26),(26,26),(32,32));join('leash','torso');join('leash','bag-arm')
poly('dog',(32,40),(32,32),(39,32),(40,23),(44,27),(44,32),(44,40));join('dog','leash')
self.mark_human_figure('person',head='head',torso='torso',torso_junction='start')
''','human_ref/full_body_ref.png: radius5 head lower18 and neck26 exact4 ink gap; original bag and dog silhouette.')
make(14,'SQUARE',N[13]+ ' Round the snout and carry a smooth S-curve from the jaw through the curled tail.','''
path('dragon',(18,12),[('C',(29,14),(23,10),(27,12)),('L',(38,14)),('A',(38,22),4,4,True),('L',(27,22)),('C',(26,28),(20,22),(20,25)),('C',(36,35),(31,30),(36,32)),('C',(24,42),(36,41),(30,42)),('L',(16,42)),('A',(6,32),10,10,True),('C',(8,23),(6,29),(10,26)),('C',(14,29),(13,23),(15,26)),('C',(14,34),(14,31),(11,32)),('L',(23,34)),('C',(20,25),(29,34),(20,29)),('C',(18,12),(12,19),(13,14))],True)
line('horn-left',(18,12),(13,6));line('horn-right',(25,12),(25,6));join('horn-left','dragon');join('horn-right','dragon')
''','Original horned dragon: rounded horizontal snout, two horns and flowing S body; no useful direct Lucide match.')
make(15,'CIRCLE',N[14]+ ' Restore pointed beak and sweeping upper wing in a round curled dragon silhouette.','''
path('dragon',(24,4),[('A',(44,24),20,20,True),('A',(24,44),20,20,True),('A',(4,24),20,20,True),('C',(12,9),(4,18),(8,12)),('C',(20,26),(7,22),(12,27)),('C',(32,16),(28,28),(32,21)),('L',(22,16)),('C',(24,4),(17,12),(18,6))],True)
''','Original pointed inner head, large circular wing and curled tail; no useful direct Lucide match.')
