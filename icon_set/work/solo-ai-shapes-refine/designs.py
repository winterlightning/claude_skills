SOURCE_ICON_ID=None
SOURCE_PATH='icon_set/work/solo-ai-next100/batch.json'
AUTHOR='gpt-6'
design('casino-clover','SQUARE','Three heart-shaped leaves','clover','Restore the three heart-shaped leaves and gently curved stem from the original, with balanced side leaves and smooth curves.', """
path('clover',(24,30),[('C',(10,36),(17,35),(12,38)),('C',(6,30),(6,36),(6,33)),('C',(9,26),(6,28),(8,27)),('C',(6,21),(7,25),(6,23)),('C',(16,18),(6,15),(12,15)),('C',(15,11),(13,15),(13,13)),('C',(19,6),(15,8),(16,6)),('C',(24,9),(21,6),(23,7)),('C',(29,6),(25,7),(27,6)),('C',(33,11),(32,6),(33,8)),('C',(32,18),(35,13),(35,15)),('C',(42,21),(36,15),(42,15)),('C',(39,26),(42,23),(41,25)),('C',(42,30),(40,27),(42,28)),('C',(38,36),(42,33),(42,36)),('C',(24,30),(36,38),(31,35))],True)
path('stem',(24,30),[('L',(24,37)),('C',(29,42),(24,40),(26,42))]);join('stem','clover')
""")
design('cog-4c6e5052','SQUARE','Eight-tooth gear','cog','Restore eight distinct teeth around the gear rather than the four-armed shape. One repeated quadrant owns all tooth widths and root transitions.', """
quarter=[(24,6),(28,6),(28,12),(30,12),(34,8),(40,14),(36,18),(36,20),(42,20),(42,24)]
turn=lambda p,n:p if n==0 else turn((48-p[1],p[0]),n-1)
poly('gear',*[turn(p,n) for n in range(4) for p in quarter[:-1]],closed=True)
""")
design('corn','VRECT_L','Broad cob and overlapping husks',None,'Restore a broad rounded cob with an overlapping right husk, preserving the original ear-of-corn proportions rather than a narrow central stalk.', """
path('cob',(15,27),[('L',(16,12)),('C',(24,4),(16,7),(20,4)),('C',(32,12),(28,4),(32,7)),('L',(33,27))])
path('husk',(8,22),[('C',(24,31),(14,22),(20,26)),('C',(40,22),(29,26),(34,22)),('C',(24,44),(37,35),(38,44)),('C',(8,22),(10,44),(11,35))],True)
path('overlap',(24,31),[('C',(20,43),(21,35),(20,39))]);join('overlap','husk');join('husk','cob')
""")
design('corn','VRECT_L','Broad cob and overlapping husks',None,'Restore a broad rounded cob tapering behind overlapping husks. The wider crown and asymmetric leaf overlap preserve the original ear-of-corn reading.', """
path('cob',(18,25),[('L',(16,12)),('A',(32,12),8,8,True),('L',(30,25))])
path('husk',(8,22),[('C',(18,25),(12,22),(15,23)),('C',(24,31),(20,27),(22,29)),('C',(30,25),(26,29),(28,27)),('C',(40,22),(33,23),(36,22)),('C',(24,44),(37,35),(38,44)),('C',(20,43),(22,44),(21,44)),('C',(8,22),(11,40),(11,32))],True)
path('overlap',(24,31),[('C',(20,43),(21,35),(20,39))]);join('overlap','husk');join('husk','cob')
""")
