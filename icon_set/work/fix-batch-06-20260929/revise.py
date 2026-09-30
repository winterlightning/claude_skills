from author import author
author(1,'''
path('body',(6,32),[('A',(18,20),12,12,True),('A',(30,32),12,12,True),('L',(30,42)),('L',(6,42)),('L',(6,32))],True)
path('handle',(6,32),[('L',(6,14)),('A',(14,6),8,8,True),('L',(22,6)),('A',(30,14),8,8,True),('L',(30,32))]);join('body','handle')
path('spout',(30,32),[('L',(34,20)),('L',(42,20)),('L',(42,32)),('L',(30,42))]);join('spout','body')
''','The rejected kettle had a flat rectangular body and angular side loop. Restored the domed body, broad overhead handle and wide rising pouring spout; omitted the tiny lid knob.',lucide='Lucide cooking-pot: coherent vessel outline and attached handle')
author(2,'''
path('heart',(18,16),[('A',(6,16),6,6,False),('C',(18,34),(6,23),(12,30)),('C',(30,16),(24,30),(30,23)),('A',(18,16),6,6,False)],True)
poly('shaft',(18,34),(18,42),(42,42),(42,34));join('shaft','heart')
''','The rejected key had a very short shaft and pinched heart opening. Replaced the tiny nested heart with a clear heart bow, lengthened the key shaft and added a terminal tooth. The circular outer ring was simplified.',lucide='Lucide key-round: readable bow and toothed shaft')
author(3,'''
path('large',(28,10),[('C',(10,24),(16,10),(10,16)),('C',(28,38),(10,32),(16,38)),('L',(23,24)),('L',(28,10))],True)
poly('tail',(4,16),(10,24),(4,32));join('tail','large')
circle('small',40,24,4)
poly('small-tail',(33,20),(36,24),(33,28));join('small-tail','small')
''','The rejected large fish was a thin crescent. Broadened its body by making the open mouth shallower, and retained the distinct smaller fish with a tail. Omitted eye and gill details.','HRECT_M','Lucide fish: broad curved body with a simple tail')
author(4,'''
path('tooth',(6,16),[('C',(14,6),(6,6),(10,6)),('C',(22,6),(18,9),(18,9)),('C',(30,16),(26,6),(30,6)),('L',(30,36)),('A',(22,36),4,6,True),('L',(22,30)),('A',(14,30),4,4,False),('L',(14,36)),('A',(6,36),4,6,True),('L',(6,16))],True)
poly('brush',(42,42),(42,30),(42,22),(38,22))
line('bristle',(38,30),(42,30));join('brush','bristle')
''','The rejected tooth had angular roots and a sharp crown dip. Redrew a smooth crown and rounded separated roots with a wide central opening beside the upright toothbrush.')
