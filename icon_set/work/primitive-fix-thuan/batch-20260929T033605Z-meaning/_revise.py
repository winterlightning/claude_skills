import _author as a
import json
def replace(i,x,y):
 assert x in a.DESIGNS[i]['code'],(i,x)
 a.DESIGNS[i]['code']=a.DESIGNS[i]['code'].replace(x,y)
a.DESIGNS[0]['code']='''
path('back',(4,32),[('C',(14,27),(5,28),(9,27))])
path('horse',(29,23),[('L',(33,15)),('L',(35,12)),('L',(35,17)),('L',(43,24)),('C',(41,27),(45,26),(43,28)),('L',(35,25)),('L',(30,34)),('L',(35,39)),('L',(34,44))])
poly('foreleg',(30,34),(26,39),(25,44));join('horse','foreleg')
circle('head',20,7,3)
path('torso',(20,18),[('C',(14,27),(20,22),(16,23))])
poly('arm',(20,18),(25,23),(29,23));join('arm','horse')
poly('rider-leg',(14,27),(18,32),(15,38))
join('torso','arm');join('torso','rider-leg');join('back','rider-leg')
self.mark_human_figure('rider',head='head',torso='torso-0',torso_junction='start')
'''
replace(2,"(11,39)","(11,40)");replace(2,"('L',(17,40))","('L',(11,40)),('L',(17,40))")
replace(2,"(32,25)","(32,26)")
replace(2,"join('arm','tow-rope');join('horse','belly')","join('arm','tow-rope');join('horse','belly');join('tow-rope','horse');join('skier-leg','ski')")
replace(3,"path('tail',(10,28),[('C',(4,34),(5,26),(5,29))])","path('tail',(14,26),[('C',(4,34),(6,24),(5,29))])")
replace(3,"(25,23),(30,23)","(26,20),(31,19)")
a.DESIGNS[4]['code']='''
oval('rim',24,23,20,7)
path('bowl',(4,23),[('C',(24,38),(5,33),(12,38)),('C',(44,23),(36,38),(43,33))]);join('rim','bowl')
line('foot',(16,44),(32,44))
path('bean-left',(15,24),[('C',(19,22),(14,22),(17,20))])
path('bean-right',(28,22),[('C',(33,24),(28,25),(31,25))])
for j,x in enumerate((18,30)):
    path(f'steam-{j}',(x,4),[('C',(x,10),(x-3,6),(x+3,8))])
'''
a.DESIGNS[4]['omissions']='Reduced steam count to two and used solid curved bean marks instead of tiny outlined counters.'
a.DESIGNS[8]['code']='''
path('glass',(6,12),[('L',(32,12)),('L',(42,12)),('L',(41,20)),('L',(38,42)),('A',(34,46),4,4,True),('L',(14,46)),('A',(10,42),4,4,True),('L',(7,20)),('L',(6,12))],True)
path('liquid',(7,20),[('C',(24,20),(13,17),(18,23)),('C',(41,20),(30,17),(35,23))]);join('glass','liquid')
poly('straw',(30,20),(32,12),(34,6),(40,4));join('glass','straw')
poly('ice-upper',(19,23),(23,27),(19,31),(15,27),closed=True)
poly('ice-lower',(27,32),(31,36),(27,40),(23,36),closed=True)
'''
a.DESIGNS[9]['code']='''
path('top-leaf',(24,8),[('C',(17,8),(18,1),(15,4)),('C',(24,18),(17,12),(20,15)),('C',(31,8),(28,15),(31,12)),('C',(24,8),(33,4),(30,1))],True)
path('left-leaf',(10,21),[('C',(4,21),(6,15),(3,17)),('C',(16,28),(4,25),(12,28)),('C',(16,18),(19,22),(19,18)),('C',(10,21),(13,16),(12,17))],True)
path('right-leaf',(38,21),[('C',(44,21),(42,15),(45,17)),('C',(32,28),(44,25),(36,28)),('C',(32,18),(29,22),(29,18)),('C',(38,21),(35,16),(36,17))],True)
line('stem',(24,18),(24,34));line('stem-left',(16,28),(20,34));line('stem-right',(32,28),(28,34))
path('pot',(12,34),[('L',(36,34)),('L',(33,42)),('A',(30,44),3,3,True),('L',(18,44)),('A',(15,42),3,3,True),('L',(12,34))],True)
for leaf,stem in [('top-leaf','stem'),('left-leaf','stem-left'),('right-leaf','stem-right')]:join(leaf,stem);join('pot',stem)
'''
replace(10,"(22,22),(27,25)","(25,21),(28,23)")
replace(10,"(20,27),(24,30)","(20,25),(23,27)")
replace(11,"(38,18)","(38,16)");replace(11,"('C',(44,25),(41,19),(43,23))","('C',(44,23),(41,17),(43,21))")
replace(11,"path('stream-two',(35,27),[('C',(39,31),(37,28),(38,30))])","path('stream-two',(38,26),[('C',(41,29),(39,27),(40,28))])")
replace(11,"[('wave-top',33),('wave-bottom',42)]","[('wave-top',35),('wave-bottom',44)]")
replace(12,"path('glass',(18,10),[('C',(12,29),(14,16),(12,23)),('C',(24,38),(12,35),(17,38)),('C',(36,29),(31,38),(36,35)),('C',(30,10),(36,23),(34,16))])", "path('glass',(18,10),[('C',(16,32),(15,20),(13,26)),('C',(24,38),(18,36),(20,38)),('C',(32,32),(28,38),(30,36)),('C',(30,10),(35,26),(33,20))])")
replace(12,"path('flame',(24,20),[('C',(18,30),(25,25),(18,26)),('A',(30,30),6,6,False),('C',(24,20),(30,26),(26,22))],True)", "path('flame',(24,19),[('C',(20,28),(25,24),(20,24)),('A',(28,28),4,4,False),('C',(24,19),(28,24),(26,22))],True)")
a.DESIGNS[15]['code']='''
circle('face',24,24,20)
for j,cx in enumerate((16,32)):
    path(f'spiral-{j}',(cx-3,26),[('C',(cx,15),(cx-8,24),(cx-8,15)),('C',(cx+1,25),(cx+8,15),(cx+8,25)),('C',(cx+2,20),(cx-2,25),(cx-2,20))])
line('mouth',(20,35),(28,35))
'''
replace(16,"(22,", "(20,");replace(16,"(26,", "(28,")
replace(18,"line('back-boot',(5,35),(12,37))", "line('back-boot',(6,35),(13,37))")
replace(18,"circle(f'wheel-{j}',x,y,2)","self.add_dot(f'wheel-{j}',(x,y))")
a.DESIGNS[18]['omissions']='Simplified clothing and used two 4px solid wheels under each small boot; full outline wheels overwhelmed the scene.'
selected=[0,2,3,4,8,9,10,11,12,15,16,18]
for i in selected:a.write(i,'02')
(a.HERE/'items.json').write_text(json.dumps(a.ITEMS,indent=2))
