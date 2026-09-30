from author import make,ROOT
import json,textwrap
N=json.loads((ROOT/'comparison-plan.json').read_text())
make(4,'HRECT_L',N[3]+ ' Restore separate trunks and shorten the central canopy to leave room for all three trees.','''
poly('front',(24,8),(34,32),(24,32),(14,32),closed=True)
poly('left',(17,25),(4,25),(10,12),(19,20));poly('right',(31,25),(44,25),(38,12),(29,20));join('left','front');join('right','front')
line('trunk-mid',(24,32),(24,40));join('trunk-mid','front')
line('trunk-left',(6,25),(6,38));line('trunk-right',(42,25),(42,38));join('trunk-left','left');join('trunk-right','right')
''','Lucide trees original/atoms: three staggered canopies and separate trunks; fine branch steps omitted.')
m=json.loads((ROOT/'latest-5.json').read_text());s=(ROOT.parents[2]/m['result_dir']/m['module']).read_text();body=textwrap.dedent("        path('head'"+s.split("        path('head'",1)[1]);body=body.replace("p(20,22)","p(20,18)")
make(5,'HRECT_L',m['comparison'],body,m['construction_reference'])
make(14,'SQUARE',N[13]+ ' Restore rounded snout and a smooth open S body with two distinct horns.','''
path('head',(18,10),[('C',(27,12),(22,9),(25,10)),('L',(37,12)),('A',(37,22),5,5,True),('L',(22,22)),('C',(18,10),(10,22),(10,10))],True)
path('body',(22,22),[('C',(36,34),(22,27),(36,28)),('C',(24,42),(36,40),(30,42)),('C',(6,34),(14,42),(6,42)),('C',(10,25),(6,29),(11,28))]);join('head','body')
line('horn-left',(18,10),(12,6));line('horn-right',(27,12),(27,6));join('horn-left','head');join('horn-right','head')
''','Original horned dragon; rounded muzzle and coherent S curve. Tail interior outline omitted for spacing.')
make(15,'CIRCLE',N[14]+ ' Enlarge the negative space under the head and restore a pointed beak inside the curled outer wing.','''
path('dragon',(24,4),[('A',(44,24),20,20,True),('A',(24,44),20,20,True),('A',(4,24),20,20,True),('C',(14,8),(4,17),(9,11)),('C',(18,25),(11,19),(12,25)),('C',(32,21),(24,30),(32,28)),('L',(23,20)),('C',(24,4),(20,14),(20,8))],True)
''','Original circular wing and pointed inner head; smooth few curves, fine tail notches omitted.')
make(16,'VRECT_L',N[15]+ ' Restore a pointed fox ear and snout at the opening of the curled flame.','''
path('flame',(8,22),[('L',(8,28)),('A',(24,44),16,16,False),('A',(40,28),16,16,False),('A',(24,4),16,24,False),('L',(28,16)),('A',(20,24),8,8,False),('A',(32,24),6,6,False)])
poly('fox-head',(8,22),(12,12),(16,22),(21,24));join('fox-head','flame')
''','Original fox/flame: pointed ear and snout restored; open curling contour keeps interior clear.')
make(19,'VRECT_M',N[18]+ ' Widen the waist around a visible soundhole, and smooth the body and headstock.','''
path('outline',(20,8),[('A',(24,4),4,4,True),('A',(28,8),4,4,True),('L',(28,18)),('C',(36,24),(32,18),(36,20)),('C',(35,30),(36,27),(35,28)),('C',(38,37),(35,32),(38,33)),('A',(31,44),7,7,True),('L',(17,44)),('A',(10,37),7,7,True),('C',(13,30),(10,33),(13,32)),('C',(12,24),(13,28),(12,27)),('C',(20,18),(12,20),(16,18)),('L',(20,8))],True)
circle('soundhole',24,32,3)
''','Lucide guitar original/atoms: smooth waist curves, round soundhole and rounded headstock; strings and bridge omitted for spacing.')
make(20,'VRECT_L',N[19]+ ' Round the head shoulders and lengthen the handle below the wide open jaw.','''
path('wrench',(16,4),[('L',(16,12)),('A',(32,12),8,8,False),('L',(32,4)),('A',(40,16),8,12,True),('L',(40,20)),('C',(30,29),(40,23),(33,27)),('L',(30,38)),('A',(18,38),6,6,True),('L',(18,29)),('C',(8,20),(15,27),(8,23)),('L',(8,16)),('A',(16,4),8,12,True)],True)
''','Lucide wrench original/atoms: rounded jaw shoulders and long grip; preserve upright original.')
