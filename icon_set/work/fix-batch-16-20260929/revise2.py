from revise import *
keys=[]
def change(k,code=None):
 keys.append(k)
 if code is not None:D[k]['code']=code
change('police-avatar',D['police-avatar']['code'].replace("(18,42)","(22,42)").replace("(18,34)","(22,36)").replace("('A',(30,28),12,6,True),('A',(42,36),12,8,True)","('A',(32,28),10,8,True),('A',(42,36),10,8,True)"))
change('police-officer-with-sunglasses-and-pocket','''
path('hat',(12,16),[('L',(14,8)),('A',(18,4),4,4,True),('L',(30,4)),('A',(34,8),4,4,True),('L',(36,16))])
poly('brim',(8,16),(12,16),(24,16),(36,16),(40,16));join('hat','brim')
path('jaw',(36,16),[('A',(12,16),12,12,True)]);join('jaw','hat');join('jaw','brim')
for n,l,r in [('left',12,24),('right',24,36)]:
 path(n+'lens',(l,16),[('A',(r,16),6,6,False)]);join(n+'lens','brim');join(n+'lens','jaw');join(n+'lens','hat')
join('leftlens','rightlens')
path('body',(8,44),[('A',(24,32),16,12,True),('A',(40,44),16,12,True)]);join('jaw','body')
''')
D['police-officer-with-sunglasses-and-pocket']['omissions']='Omit the chest pocket and central seam: a separate readable pocket cannot fit below the full-width sunglass face with required spacing.'
change('real-estate-market-house-decrease',D['real-estate-market-house-decrease']['code'].replace('(34,23)','(35,23)'))
change('smart-tv-and-phone',D['smart-tv-and-phone']['code'].replace("('L',(28,34))","('L',(25,34))").replace("(16,14)","(16,15)").replace("(24,22)","(24,24)").replace("(10,22)","(10,24)").replace("(6,26),4,4","(6,28),4,4"))
change('spotify-logo-1','''
oval('disc',24,24,20,20)
path('wave-top',(16,16),[('C',(33,19),(21,14),(28,16))])
path('wave-middle',(15,25),[('C',(31,27),(20,23),(26,24))])
path('wave-bottom',(20,34),[('C',(27,34),(22,33),(25,34))])
''')
change('two-eggs-in-decorated-bowl','''
path('bowl',(6,20),[('A',(42,20),18,22,False),('L',(30,20)),('L',(18,20)),('L',(6,20))],True)
for n,l,r in [('left',6,20),('right',28,42)]:
 path(n+'egg',(l,20),[('L',(l,16)),('A',(r,16),7,10,True),('L',(r,20))]);join(n+'egg','bowl')
path('wave',(16,30),[('C',(24,30),(19,27),(21,33)),('C',(32,30),(27,27),(29,33))])
''')
change('two-finger-swipe-right-upload-27a8bf31fe0cadb0',D['two-finger-swipe-right-upload-27a8bf31fe0cadb0']['code'].replace("(l,28)","(l,34)").replace("(r,28)","(r,34)"))
change('stressed-person',D['stressed-person']['code'].replace("poly('stress-left',(8,4),(12,8),(8,12));poly('stress-middle',(24,4),(21,6),(25,8));poly('stress-right',(40,4),(36,8),(40,12))","poly('stress-left',(8,4),(12,8),(8,10),(12,14));poly('stress-right',(40,4),(36,8),(40,10),(36,14))"))
D['stressed-person']['omissions']='Reduce three stress marks to two lightning zigzags so each remains readable.'
if __name__=='__main__':generate(keys)
