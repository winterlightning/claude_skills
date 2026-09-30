import author_claimed as a
from author import *
D=a.D
D['bow-tie-suit']['code']=D['bow-tie-suit']['code'].replace("(x(10),44),(x(16),27),(x(12),38)","(x(15),44),(x(16),27),(x(16),38)")
D['cat-head-affection-component']['code']='''
path('cat',(6,28),[('L',(12,32)),('L',(18,32)),('L',(24,28)),('L',(24,33)),('A',(15,42),9,9,True),('A',(6,33),9,9,True),('L',(6,28))],True)
path('heart',(32,11),[('A',(42,11),5,5,True),('C',(32,23),(42,15),(36,20)),('C',(22,11),(28,20),(22,15)),('A',(32,11),5,5,True)],True)
'''
D['circular-emblem-with-banner']['code']=D['circular-emblem-with-banner']['code'].replace('(10,28)','(10,26)').replace('(38,28)','(38,26)').replace('24,20,7,6','24,20,7,5')
D['curved-showerhead-water-jets']['code']='''
path('pipe',(42,42),[('L',(42,18)),('A',(30,6),12,12,False),('L',(24,6)),('L',(20,10))])
path('head',(10,14),[('C',(20,10),(13,11),(16,10)),('C',(28,14),(23,10),(26,11)),('C',(28,28),(32,19),(32,24)),('L',(10,14))],True);join('head','pipe')
for j,(x,y) in enumerate([(12,28),(20,36)]):line(f'jet-{j}',(x,y),(x-6,y+6))
'''
D['diagonal-harpoon-spear']['code']=D['diagonal-harpoon-spear']['code'].replace('(29,10),(42,6),(38,19)','(30,10),(42,6),(38,18)')
D['space-station-with-paired-solar-wings']['shape']='HRECT_L'
D['space-station-with-paired-solar-wings']['code']='''
for x in (4,36):
 box(f'wing{x}',x,16,x+8,40)
 line(f'row{x}',(x,28),(x+8,28));join(f'row{x}',f'wing{x}')
box('upper',20,8,28,16)
box('core',20,24,28,36)
line('spine',(24,16),(24,24));join('spine','upper');join('spine','core')
line('link-left',(12,28),(20,28));line('link-right',(28,28),(36,28))
for n,a,b in [('link-left','wing4','core'),('link-right','wing36','core')]:join(n,a);join(n,b)
'''
D['square-wristwatch-solo-ac5e07e4']['code']='''
box('face',8,7,40,41,4)
line('strap-upper',(24,4),(24,7));join('strap-upper','face')
line('strap-lower',(24,41),(24,44));join('strap-lower','face')
poly('euro',(30,16),(20,16),(20,24),(20,32),(30,32))
line('euro-bar',(17,24),(27,24));join('euro-bar','euro')
'''
D['tilted-square-paint-bucket']['code']='''
poly('bucket',(6,26),(22,10),(34,22),(18,38),closed=True)
path('handle',(10,22),[('L',(10,12)),('A',(22,12),6,6,True)]);join('handle','bucket')
path('drop',(38,31),[('C',(42,38),(40,34),(42,36)),('A',(34,38),4,4,True),('C',(38,31),(34,36),(36,34))],True)
'''
D['traveler-beside-suitcase']['code']=D['traveler-beside-suitcase']['code'].replace('(24,31),(23,25),(24,27)','(23,31),(23,25),(23,27)').replace('(24,42)','(23,42)')
D['treehouse-with-ladder-solo-b016-r02']['code']=D['treehouse-with-ladder-solo-b016-r02']['code'].replace("path('canopy',(12,28),[('C',(6,20),(7,28),(6,25))","path('canopy',(6,28),[('L',(6,20))")
D['two-hands-cupping-a-house']['code']='''
poly('house',(15,16),(24,6),(33,16),(33,23),(15,23),closed=True)
for s in (-1,1):
 x=lambda a:24+s*a
 path(f'hand{s}',(x(6),42),[('L',(x(6),39)),('L',(x(12),33)),('C',(x(18),33),(x(15),30),(x(18),30)),('L',(x(18),25)),('L',(x(18),34)),('C',(x(17),42),(x(18),37),(x(18),40))])
'''
D['two-linked-wifi-routers']['code']='''
box('router-a',6,18,18,26,2)
box('router-b',30,34,42,42,2)
line('antenna-a',(12,14),(12,18));join('antenna-a','router-a')
line('antenna-b',(36,30),(36,34));join('antenna-b','router-b')
path('wifi-a',(6,9),[('A',(18,9),6,3,True)])
path('wifi-b',(30,25),[('A',(42,25),6,3,True)])
line('link',(12,35),(20,40))
'''
D['two-piece-bikini-set']['code']=D['two-piece-bikini-set']['code'].replace("('C',(40,35),(18,37),(30,37))","('L',(40,35))")
D['two-wheel-cart-with-a-marked-suitcase']['code']=D['two-wheel-cart-with-a-marked-suitcase']['code'].replace('(14,27)','(14,26)').replace('(18,31)','(18,30)').replace('(42,31)','(42,30)').replace('(22,31)','(22,30)').replace('(30,23),(34,23)','(31,22),(33,22)')
D['upright-skeleton-key']['code']=D['upright-skeleton-key']['code'].replace("24,15,3,3","24,16,3,3").replace('(30,38)','(34,42)').replace('(35,y)','(35,y)')
if __name__=='__main__':
 import author
 author.D=D
 keys=sys.argv[1:] or [k for k in D if not json.loads((B/'runs.json').read_text())[k]['valid']]
 generate(keys)
