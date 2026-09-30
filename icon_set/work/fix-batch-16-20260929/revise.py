from author import *
D['police-avatar']['code']='''
poly('cap',(24,16),(22,6),(42,8),(40,16),(24,16))
path('jaw',(40,16),[('A',(24,16),8,8,True)]);join('cap','jaw')
path('body',(18,42),[('L',(18,34)),('A',(30,28),12,6,True),('A',(42,36),12,8,True),('L',(42,42))]);join('body','jaw')
path('arm',(18,34),[('C',(6,20),(10,30),(6,26)),('L',(6,14))]);join('arm','body')
'''
D['police-avatar']['omissions']='Simplify the raised arm to one coherent stroke; omit collar to preserve shoulder clearance.'
D['police-officer-with-sunglasses-and-pocket']['code']='''
path('hat',(16,12),[('L',(16,8)),('A',(20,4),4,4,True),('L',(28,4)),('A',(32,8),4,4,True),('L',(32,12))])
poly('brim',(8,12),(16,12),(24,12),(32,12),(40,12));join('hat','brim')
path('jaw',(32,12),[('A',(16,12),8,8,True)]);join('jaw','hat');join('jaw','brim')
for n,l,r in [('left',16,24),('right',24,32)]:
 path(n+'lens',(l,12),[('A',(r,12),4,4,False)]);join(n+'lens','brim');join(n+'lens','jaw');join(n+'lens','hat')
join('leftlens','rightlens')
path('body',(8,44),[('L',(8,32)),('A',(16,24),8,8,True),('L',(24,24)),('L',(32,24)),('A',(40,32),8,8,True),('L',(40,44))]);join('jaw','body')
box('pocket',24,34,32,42,1)
'''
D['real-estate-market-house-decrease']['shape']='HRECT_L'
D['real-estate-market-house-decrease']['code']='''
for i,(x,y) in enumerate(((4,20),(20,28),(36,32))):box('bar'+str(i),x,y,x+8,40)
line('trend',(12,8),(44,24));poly('arrow',(42,14),(44,24),(34,23));join('trend','arrow')
'''
D['smart-tv-and-phone']['code']='''
path('screen',(24,22),[('L',(10,22)),('A',(6,26),4,4,False),('L',(6,30)),('A',(10,34),4,4,False),('L',(28,34))])
line('stand',(20,34),(20,42));line('foot',(12,42),(28,42));join('stand','screen');join('stand','foot')
box('phone',34,14,42,34,2)
path('wifi',(6,10),[('A',(16,6),10,4,True),('A',(26,10),10,4,True)])
self.add_dot('wifi-inner',(16,14))
'''
D['smart-tv-and-phone']['omissions']='Inner Wi-Fi arc reduced to a dot; omit the phone lower divider.'
D['spotify-logo-1']['code']='''
oval('disc',24,24,20,20)
path('wave-top',(16,17),[('C',(33,19),(21,15),(28,16))])
path('wave-middle',(15,26),[('C',(31,28),(20,24),(26,25))])
path('wave-bottom',(19,34),[('C',(27,34),(22,33),(25,33))])
'''
D['stressed-person']['code']=D['stressed-person']['code'].replace("(24,4),(21,8),(25,11)","(24,4),(21,6),(25,8)")
D['three-balaclava-wearers']['code']='''
for n,cx in [('left',12),('right',36)]:
 path(n,(cx-8,28) if n=='left' else (cx+8,28), [('L',(cx-8,16) if n=='left' else (cx+8,16)),('A',(cx+8,16) if n=='left' else (cx-8,16),8,8,n=='left')])
 line(n+'band',(cx-8,16),(cx+8,16));join(n,n+'band')
path('front',(16,40),[('L',(16,32)),('A',(32,32),8,8,True),('L',(32,40))])
line('front-band',(16,32),(32,32));join('front','front-band')
'''
D['tooth-with-dental-floss-upload-79ce34090d76e090']['code']=D['tooth-with-dental-floss-upload-79ce34090d76e090']['code'].replace('(10,6)','(10,8)').replace('(28,6)','(28,8)')
D['traditional-japanese-mochi']['code']='''
path('dumpling',(12,40),[('A',(4,24),20,20,True),('A',(44,24),20,20,True),('A',(36,40),20,20,True)])
path('inset',(20,35),[('A',(14,28),10,7,True),('A',(34,28),10,7,True),('A',(28,35),10,7,True)])
'''
D['twisted-licorice-strands']['code']='''
path('strand',(6,34),[('C',(16,20),(6,28),(12,24)),('C',(30,12),(22,17),(27,17)),('C',(36,6),(32,9),(34,6)),('A',(42,12),6,6,True),('C',(32,28),(42,20),(36,25)),('C',(18,36),(26,31),(22,30)),('C',(12,42),(16,39),(14,42)),('A',(6,36),6,6,True),('L',(6,34))],True)
path('wrap',(6,34),[('C',(32,28),(14,34),(24,30))]);join('wrap','strand')
'''
D['twisted-rubber-band']['code']='''
path('loop',(6,34),[('C',(20,16),(6,28),(12,21)),('C',(34,6),(26,11),(30,6)),('A',(42,14),8,8,True),('C',(28,32),(42,20),(34,27)),('C',(14,42),(22,37),(18,42)),('A',(6,34),8,8,True)],True)
path('rear-top',(6,14),[('A',(14,6),8,8,True),('L',(18,6))])
path('rear-bottom',(42,34),[('A',(34,42),8,8,True),('L',(30,42))])
'''
D['two-eggs-in-decorated-bowl']['code']=D['two-eggs-in-decorated-bowl']['code'].replace("path('wave',(8,32),[('C',(24,32),(13,23),(19,40)),('C',(40,32),(30,24),(35,38))]);join('wave','bowl')","path('wave',(12,32),[('C',(24,32),(16,29),(20,35)),('C',(36,32),(28,29),(32,35))])")
D['two-finger-swipe-right-upload-27a8bf31fe0cadb0']['code']=D['two-finger-swipe-right-upload-27a8bf31fe0cadb0']['code'].replace('(18,8),(38,8)','(18,12),(38,12)').replace('(32,4),(38,8),(32,12)','(32,8),(38,12),(32,16)')
D['two-overlapping-document-sheets']['code']=D['two-overlapping-document-sheets']['code'].replace("('L',(14,12)),('A',(20,6),6,6,True)","('L',(14,10)),('A',(18,6),4,4,True)").replace("('L',(42,28)),('A',(36,34),6,6,True)","('L',(42,30)),('A',(38,34),4,4,True)")
D['two-person-group-batch-078']['code']=D['two-person-group-batch-078']['code'].replace("('A',(36,30),12,6,True)","('C',(36,30),(30,30),(34,30))")
D['vertical-swipe-gesture']['code']=D['vertical-swipe-gesture']['code'].replace("(38,base)","(40,base)").replace("(26,base)","(24,base)")
D['woman-with-halo']['code']='''
oval('halo',24,8,16,4)
path('jaw',(31,22),[('A',(17,22),7,7,True)])
path('fringe',(17,22),[('C',(24,20),(20,23),(22,22)),('C',(31,22),(26,22),(28,23))]);join('jaw','fringe')
path('body',(8,44),[('A',(24,33),16,11,True),('A',(40,44),16,11,True)]);join('body','jaw')
for n,x in [('left',8),('right',40)]:
 path(n+'hair',(x,21),[('L',(x,32)),('L',(x,44))]);join(n+'hair','body')
'''
D['worker-wearing-ridged-hard-hat']['code']=D['worker-wearing-ridged-hard-hat']['code'].replace("(20,16)","(20,12)").replace("(28,16)","(28,12)")
if __name__=='__main__':generate([k for k in D if k not in ('three-cell-row','two-coin-stacks')])
