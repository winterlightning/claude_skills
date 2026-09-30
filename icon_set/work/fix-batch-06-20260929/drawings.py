author(0,'''
poly('head',(18,14),(26,6),(42,22),(34,30),(26,22),(18,14))
poly('cap-upper',(22,6),(26,6),(42,22),(42,26))
poly('cap-lower',(14,14),(18,14),(34,30),(34,34))
join('head','cap-upper');join('head','cap-lower')
line('handle',(26,22),(6,42));join('handle','head');join('handle','cap-lower')
line('block',(28,42),(42,42))
''','The rejected head was a plain diamond and lacked the reference striking caps. Rebuilt the diagonal gavel with projecting caps and a long handle above the sound block.',lucide='Lucide gavel: projecting end bars and diagonal handle')
author(1,'''
path('body',(6,32),[('A',(18,20),12,12,True),('A',(30,32),12,12,True),('L',(30,42)),('L',(6,42)),('L',(6,32))],True)
path('handle',(6,32),[('L',(6,14)),('A',(14,6),8,8,True),('L',(22,6)),('A',(30,14),8,8,True),('L',(30,32))])
join('body','handle')
path('spout',(30,32),[('L',(38,22)),('L',(42,22)),('L',(40,34)),('L',(30,42))]);join('spout','body')
''','The rejected kettle had a flat rectangular body and angular side loop. Restored the domed body, broad overhead handle and rising pouring spout; omitted the tiny lid knob.',lucide='Lucide cooking-pot: coherent vessel outline and attached handle')
author(2,'''
path('heart',(22,20),[('A',(6,20),8,8,False),('C',(22,42),(6,28),(14,36)),('C',(38,20),(30,36),(38,28)),('A',(22,20),8,8,False)],True)
poly('shaft',(34,12),(40,6),(42,6));join('shaft','heart')
''','The rejected key had a very short upright shaft and a pinched tiny heart. Enlarged the heart-shaped opening into the bow and restored a diagonal shaft. Simplified the outer circular ring.',lucide='Lucide key-round: diagonal shaft attached to a rounded bow')
author(3,'''
path('large',(28,10),[('C',(10,24),(16,10),(10,16)),('C',(28,38),(10,32),(16,38)),('L',(20,24)),('L',(28,10))],True)
poly('tail',(4,16),(10,24),(4,32));join('tail','large')
circle('small',40,24,4)
line('small-tail',(32,24),(36,24));join('small-tail','small')
''','The rejected large fish was a thin crescent and the small tail crowded its ring. Broadened the large fish body and simplified the small fish tail while retaining the pursuing arrangement. Omitted eye and gill details.','HRECT_M','Lucide fish: broad curved body with a simple tail')
author(4,'''
path('tooth',(6,16),[('C',(14,6),(6,6),(10,6)),('C',(22,6),(18,9),(18,9)),('C',(30,16),(26,6),(30,6)),('C',(27,38),(30,24),(29,34)),('C',(21,38),(26,44),(23,42)),('C',(18,29),(20,34),(21,29)),('C',(15,38),(15,29),(16,34)),('C',(9,38),(13,42),(10,44)),('C',(6,16),(7,34),(6,24))],True)
poly('brush',(42,42),(42,30),(42,22),(38,22))
line('bristle',(38,30),(42,30));join('brush','bristle')
''','The rejected tooth roots were angular and the crown dip was sharp. Redrew a smooth crown, curved sides and rounded divergent roots beside the upright toothbrush.')
