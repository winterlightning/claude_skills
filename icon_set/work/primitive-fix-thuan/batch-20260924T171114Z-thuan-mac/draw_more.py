from draw import *
put('pipe-wrench','SQUARE','wrench','A diagonal wrench with a rounded open jaw and broad rounded handle replaces the rejected upright block; diagonal perspective follows the original.', '''
path('wrench',(22,22),[('L',(8,36)),('C',(6,39),(6,38),(6,38)),('C',(14,42),(6,41),(10,42)),('C',(19,40),(16,42),(18,41)),('L',(32,27)),('C',(42,16),(37,28),(42,22)),('C',(32,6),(42,10),(38,6)),('C',(25,8),(29,6),(27,7)),('L',(32,15)),('L',(25,22)),('L',(18,15)),('C',(22,22),(17,18),(19,21))],True)
''','Fine screw ridges and jaw seam omitted to leave a readable open jaw and handle.')
put('plumbing-pipe-repair-with-wrench','HRECT_L','wrench','An elbow pipe, teardrop and diagonal repair wrench retain the three-part composition; rounded elbows and smooth drop replace polygonal bends.', '''
path('pipe',(44,12),[('L',(18,12)),('L',(18,8)),('L',(8,8)),('A',(4,12),4,4,False),('L',(4,16)),('A',(8,20),4,4,False),('L',(44,20))])
path('drop',(10,28),[('C',(16,35),(13,31),(16,33)),('C',(10,40),(16,38),(13,40)),('C',(4,35),(7,40),(4,38)),('C',(10,28),(4,33),(7,31))],True)
path('jaw',(24,29),[('L',(24,31)),('A',(30,37),6,6,False),('C',(36,30),(34,37),(36,33))])
line('handle',(30,37),(44,40));join('jaw','handle')
''','Tiny jaw screw and handle outline reduced to clean centerline strokes.')
put('question-and-exclamation-speech-bubbles','HRECT_L','messages-square','Two overlapping rectangular speech bubbles retain an open question hook and a vertical warning mark, with clean round joins and exact spacing.', '''
poly('back',(32,20),(32,8),(4,8),(4,32),(10,32),(10,38),(18,32))
poly('front',(28,20),(32,20),(44,20),(44,38),(38,38),(38,40),(36,38),(28,38),closed=True);join('back','front')
path('question',(13,20),[('A',(19,20),3,3,True),('C',(17,24),(19,22),(17,22))])
line('exclamation',(36,28),(36,30))
''','Separate punctuation dots omitted, matching the supplied thin-line marks.')
put('seated-teddy-bear','VRECT_L','none','A vertically symmetric teddy with rounded ears, broad head and paired seated feet is built from mirrored curves.', '''
path('head',(14,14),[('C',(10,8),(11,14),(10,11)),('C',(14,4),(10,6),(12,4)),('C',(18,8),(16,4),(18,6)),('C',(30,8),(22,7),(26,7)),('C',(34,4),(30,6),(32,4)),('C',(38,8),(36,4),(38,6)),('C',(34,14),(38,11),(37,14)),('C',(24,26),(34,21),(30,26)),('C',(14,14),(18,26),(14,21))],True)
path('body',(24,26),[('L',(34,26)),('C',(40,34),(38,26),(40,30)),('L',(40,38)),('A',(28,38),6,6,True),('L',(28,36)),('L',(20,36)),('L',(20,38)),('A',(8,38),6,6,True),('L',(8,34)),('C',(14,26),(8,30),(10,26)),('L',(24,26))],True);join('body','head')
''','Inner ear loops and finger seams omitted; two rounded feet retained.')
put('stack-unstack-column','VRECT_L','blocks','Five repeated square cells descend in three staggered columns; two smooth return arrows repeat alongside them.', '''
# Single boundary and dividers: no duplicated cell edges.
poly('stack',(8,4),(16,4),(16,20),(20,20),(20,36),(24,36),(24,44),(16,44),(16,36),(12,36),(12,20),(8,20),closed=True)
for name,a,b in [('first',(8,12),(16,12)),('second',(12,28),(20,28)),('join-first',(12,20),(16,20)),('join-second',(16,36),(20,36))]:
    line(name,a,b);join(name,'stack')
path('turn-upper',(25,4),[('C',(40,11),(34,4),(40,6)),('C',(28,18),(40,16),(34,18))])
poly('head-upper',(32,14),(28,18),(32,22));join('turn-upper','head-upper')
path('turn-lower',(33,31),[('C',(40,37),(37,31),(40,33)),('C',(33,42),(40,40),(37,42))])
poly('head-lower',(37,38),(33,42),(39,44));join('turn-lower','head-lower')
''')
if __name__=='__main__':write()
