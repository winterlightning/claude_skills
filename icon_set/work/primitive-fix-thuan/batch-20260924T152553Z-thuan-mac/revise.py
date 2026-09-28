import json
from author_batch import DESIGNS,BATCH
changes={
'rhinoceros-facing-right': '''
path('rhino',(4,40),[(4,26),((18,12),14,14,True),(26,12),(31,8),(32,18),(36,22),(44,14),(44,26),((38,32),6,6,True),(32,30),(32,40),(24,40),(24,30),(12,30),(12,40),(4,40)],True)
''',
'right-facing-head-with-curled-breath-lines': '''
path('head',(6,42),[(6,18),((18,6),12,12,True),((30,18),12,12,True),(30,20),(32,23),(24,23),((24,33),5,5,False),((22,39),6,6,True),(22,42)])
path('breath-upper',(39,17),[((42,20),3,3,True),((39,23),3,3,True)])
path('breath-lower',(36,34),[(39,34),((42,37),3,3,True),((39,40),3,3,True)])
''',
'right-facing-human-profile': '''
path('profile',(24,44),[(24,32),(24,28),((12,16),12,12,True),((24,4),12,12,True),((36,16),12,12,True),(40,22),(34,24),(34,32),(32,32)])
path('shoulder',(8,44),[((24,32),16,12,True)]);join('profile','shoulder')
''',
'rocket-passing-above-a-globe': '''
path('rocket',(18,18),[(28,8),(42,6),(40,20),(30,30),(18,18)],True)
poly('fin-left',(18,18),(8,18),(12,10),(26,10));join('fin-left','rocket')
poly('fin-right',(30,30),(30,38),(38,34),(38,22));join('fin-right','rocket')
line('exhaust',(6,30),(10,26))
path('globe',(16,34),[((28,42),12,8,False),((42,28),14,14,False)])
''',
'rolled-parchment-wavy-mark': '''
path('sheet',(12,4),[(30,4),((36,10),6,6,True),(36,34),(40,34),(40,38),((34,44),6,6,True),(18,44),((12,38),6,6,True),(12,20)])
path('top-roll',(8,20),[(8,8),((12,4),4,4,True),((16,8),4,4,True),(16,20),(12,20),(8,20)],True);join('sheet','top-roll')
path('lower-curl',(24,34),[(24,38),((30,44),6,6,False)]);join('lower-curl','sheet')
line('lip',(24,34),(36,34));join('lip','sheet');join('lip','lower-curl')
path('wave',(22,26),[((25,25),3,3,True),((28,26),3,3,False)])
''',
'rolled-sheet-with-loose-end': '''
path('spiral',(17,23),[((13,19),4,4,True),((19,13),6,6,True),((27,21),8,8,True),((16,32),11,11,True),((4,20),12,12,True),((16,8),12,12,True)])
path('barrel',(16,8),[(32,8),((44,20),12,12,True),((32,32),12,12,True),(16,32)]);join('spiral','barrel')
poly('flap',(16,32),(24,40),(44,40),(32,32));join('flap','barrel');join('flap','spiral')
''',
'rotating-valve-handle': '''
path('handle',(19,14),[(29,14),((29,22),4,4,True),(24,22),(19,22),((19,14),4,4,True)],True)
line('stem',(24,22),(24,42));join('stem','handle')
poly('base',(14,42),(24,42),(34,42));join('base','stem')
path('left-arrow',(12,6),[((6,18),15,15,False),(6,30),(12,30)])
poly('left-head',(6,22),(6,30),(14,30));join('left-head','left-arrow')
path('right-arrow',(36,34),[((42,22),15,15,False),(42,6),(34,6)])
poly('right-head',(34,6),(42,6),(42,14));join('right-head','right-arrow')
''',
'round-antenna-on-splayed-legs': '''
circle('dish',24,22,9)
poly('divider',(15,22),(24,22),(33,22));join('divider','dish')
poly('legs',(16,42),(24,31),(32,42));join('legs','dish')
path('signal-left',(12,6),[((6,22),24,24,False),((12,38),24,24,False)])
path('signal-right',(36,6),[((42,22),24,24,True),((36,38),24,24,True)])
''',
'round-baby-head-with-one-curl': '''
path('head',(8,20),[((24,4),16,16,True),((40,20),16,16,True),((44,24),4,4,True),((40,28),4,4,True),((24,44),16,16,True),((8,28),16,16,True),((4,24),4,4,True),((8,20),4,4,True)],True)
path('curl',(24,4),[((30,10),6,6,True),((24,16),6,6,True),((18,10),6,6,True)]);join('curl','head')
''',
'round-bodied-hen': '''
path('hen',(4,12),[(12,20),(24,20),(24,16),((32,8),8,8,True),((40,16),8,8,True),(44,20),(40,24),((28,36),12,12,True),(20,36),((4,20),16,16,True),(4,12)],True)
line('foot-left',(20,36),(20,40));line('foot-right',(28,36),(28,40));join('foot-left','hen');join('foot-right','hen')
''',
'round-hatbox-with-loop-handle': '''
path('lid',(8,24),[((16,17),16,8,True),((32,17),16,8,True),((40,24),16,8,True),((24,32),16,8,True),((8,24),16,8,True)],True)
path('body',(8,24),[(8,36),((24,44),16,8,False),((40,36),16,8,False),(40,24)]);join('body','lid')
path('handle',(16,17),[(16,12),((32,12),8,8,True),(32,17)]);join('handle','lid')
''',
'round-lantern': '''
path('globe',(24,12),[((40,28),16,16,True),((24,44),16,16,True),((8,28),16,16,True),((24,12),16,16,True)],True)
poly('vertical',(24,12),(24,28),(24,44));poly('horizontal',(8,28),(24,28),(40,28));join('vertical','globe');join('horizontal','globe');join('vertical','horizontal')
path('handle',(16,12),[(16,8),((24,4),8,4,True),((32,8),8,4,True),(32,12)])
''',
'round-meatball-with-short-curved-marks': '''
circle('ball',24,24,20)
for i,(a,b) in enumerate([((15,21),(19,17)),((27,15),(31,19)),((33,27),(29,31)),((21,33),(17,29))]):
 self.add_arc(f'texture-{i}',a,b,radius_x=7,sweep=True)
''',
'rounded-armchair-with-inset-seat-cushion': '''
path('back',(14,22),[(14,12),((20,6),6,6,True),(28,6),((34,12),6,6,True),(34,22)])
path('chair',(14,28),[(14,22),((6,22),4,4,False),(6,34),((10,38),4,4,False),(38,38),((42,34),4,4,False),(42,22),((34,22),4,4,False),(34,28),(14,28)],True);join('back','chair')
line('foot-left',(10,38),(10,42));line('foot-right',(38,38),(38,42));join('foot-left','chair');join('foot-right','chair')
''',
'rounded-camping-caravan': '''
path('shell',(11,35),[(4,35),(4,20),((16,8),12,12,True),(28,8),((40,20),12,12,True),(40,35),(28,35),(21,35)])
circle('wheel',16,35,5);join('shell','wheel')
poly('door',(28,35),(28,20),(40,20));join('door','shell')
line('window',(13,19),(19,19))
line('tow',(40,35),(44,35));join('tow','shell')
'''}
for k,v in changes.items():
 key,plan,_=DESIGNS[k];DESIGNS[k]=(key,plan,v)
(BATCH/'revisions.json').write_text(json.dumps(DESIGNS,indent=2)+'\n')
