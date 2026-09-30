from author import make,ROOT
import json
N=json.loads((ROOT/'comparison-plan.json').read_text())
make(16,'VRECT_L',N[15]+ ' Restore closed curling flame with fox ear and snout notch.','''
path('flame',(8,27),[('C',(16,13),(8,21),(12,17)),('C',(21,22),(15,18),(18,21)),('L',(27,24)),('L',(21,28)),('A',(32,29),6,6,False),('C',(24,16),(35,23),(31,18)),('C',(26,4),(23,10),(24,7)),('C',(37,20),(32,8),(36,14)),('L',(39,16)),('C',(40,28),(40,20),(40,24)),('A',(24,44),16,16,True),('A',(8,28),16,16,True),('L',(8,27))],True)
''','Original Firefox fox/flame silhouette; no useful direct Lucide match.')
make(17,'SQUARE',N[16]+ ' Rebuild concentric crop rows against a distinct opposing hill contour.','''
path('row-outer',(6,42),[('A',(42,6),36,36,True)])
path('row-middle',(18,42),[('A',(42,18),24,24,True)])
path('row-inner',(30,42),[('A',(42,30),12,12,True)])
path('hill',(6,8),[('C',(17,17),(10,8),(15,13))]);join('hill','row-outer')
path('hill-row',(6,22),[('C',(9,27),(8,23),(9,25))]);join('hill-row','row-outer')
''','Three concentric circular field arcs and opposing hillside; no useful direct Lucide match.')
make(18,'HRECT_L',N[17]+ ' Make the rolled paper span the full height and restore a top paper lip.','''
path('sheet',(36,8),[('L',(4,8)),('L',(4,40)),('L',(36,40)),('A',(44,32),8,8,False),('L',(44,16)),('A',(36,8),8,8,False)],True)
path('roll',(36,8),[('A',(28,16),8,8,False),('L',(28,32)),('L',(36,32)),('A',(44,32),4,4,False)]);join('roll','sheet')
line('lip',(4,16),(28,16));join('lip','sheet');join('lip','roll')
''','Original rolled right edge and top lip; use shared radii and broad paper interior.')
make(19,'VRECT_M',N[18]+ ' Restore a smooth guitar body with a visible circular soundhole and rounded headstock.','''
path('outline',(20,8),[('A',(24,4),4,4,True),('A',(28,8),4,4,True),('L',(28,18)),('C',(35,24),(32,18),(35,20)),('C',(33,30),(35,27),(33,28)),('C',(38,37),(33,32),(38,33)),('A',(31,44),7,7,True),('L',(17,44)),('A',(10,37),7,7,True),('C',(15,30),(10,33),(15,32)),('C',(13,24),(15,28),(13,27)),('C',(20,18),(13,20),(16,18)),('L',(20,8))],True)
circle('soundhole',24,31,3)
''','Lucide guitar original and atoms: smooth waist transitions and round soundhole; upright proportions from original.')
make(20,'VRECT_L',N[19]+ ' Soften the head shoulders and extend the handle while retaining the open U jaw.','''
path('wrench',(16,4),[('L',(16,12)),('A',(32,12),8,8,False),('L',(32,4)),('A',(40,16),8,12,True),('C',(30,26),(40,21),(35,24)),('L',(30,38)),('A',(18,38),6,6,True),('L',(18,26)),('C',(8,16),(13,24),(8,21)),('A',(16,4),8,12,True)],True)
''','Lucide wrench original and atoms: rounded head transitions and long round-ended handle; upright source orientation preserved.')
