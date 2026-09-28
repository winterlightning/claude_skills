from author import *
D.clear()
add('red-blood-cell-strem-1','SQUARE','A tilted red blood cell with a smooth outer disc and a central depression.', '''
# Alternating quarter circles are tangent at all four joins; diagonal mass is intentional.
self.path('cell',(6,30),[('A',(18,42),12,12,False),('A',(42,18),24,24,False),('A',(30,6),12,12,False),('A',(6,30),24,24,False)],True)
self.path('depression',(16,27),[('A',(21,32),5,5,False),('A',(32,21),11,11,False),('A',(27,16),5,5,False),('A',(16,27),11,11,False)],True)
''','No useful exact Lucide match; tangent quarter-circle construction')
add('red-blood-cell-three','HRECT_L','Three separate red blood cells in a triangular arrangement.', '''
# Three oval definitions retain the source count and broad triangular arrangement.
self.oval('upper-left',12,12,8,4)
self.oval('upper-right',36,18,8,5)
self.oval('lower',17,33,11,7)
''','No useful exact Lucide match; coherent elliptical contours','Small source tilts reduced to horizontal ovals to avoid fragmented curves.')
add('person-silhouette-wavy','SQUARE','Continuous head, short neck and sloping shoulders with a smooth crown.', '''
# Shared x24 axis and radius10 crown; intentional neck is part of the source silhouette.
self.path('silhouette',(6,42),[('A',(8,38),5,5,True),('L',(20,29)),('L',(20,26)),('A',(14,17),10,10,True),('L',(14,16)),('A',(34,16),10,10,True),('L',(34,17)),('A',(28,26),10,10,True),('L',(28,29)),('L',(40,38)),('A',(42,42),5,5,True)])
''','human_ref/user.svg and user-round: circular head and coherent shoulders','Tiny ripples in the source head edge removed at 48px.')
add('person-using-laptop','SQUARE','A seated person reaches toward the keyboard of an open laptop.', '''
# user.svg: head bottom16, shoulder top24 gives exactly8 centerline /4 ink gap.
self.oval('head',14,11,5)
self.path('back',(14,24),[('A',(6,32),8,8,False),('L',(6,36)),('A',(12,42),6,6,False),('L',(24,42))])
self.add_polyline('arm',(14,24),(14,32),(27,32))
self.add_polyline('screen',(24,42),(27,32),(30,22),(42,22),(36,42),closed=True)
self.relate('connect','back','arm');self.relate('connect','screen','back');self.relate('connect','screen','arm')
''','human_ref/user.svg and full_body_ref.png: round head, bent arm and coherent torso','No omitted defining features; laptop keeps the source perspective.')
add('person-with-jagged-open-head','VRECT_L','Stressed person with a jagged open head and a detached broad shoulder arch.', '''
# Open cranium zigzag retained; smooth semicircular jaw; body apex36 minus jaw28=8.
self.path('head',(14,18),[('L',(14,16)),('L',(14,4)),('L',(19,9)),('L',(24,4)),('L',(29,9)),('L',(34,4)),('L',(34,16)),('L',(34,18)),('A',(14,18),10,10,True)],True)
self.add_line('opening',(14,16),(34,16));self.relate('connect','opening','head')
self.path('shoulders',(8,44),[('A',(40,44),16,8,True)])
''','human_ref/user.svg: broad shoulders and detached head','Peripheral stress rays and center shirt mark removed to preserve clear head and body.')
add('radiating-gear','SQUARE','A rounded cog surrounded by four radial emphasis marks.', '''
# Rounded teeth share a 24,24 center. Cardinal dots sit 9 units beyond the cog.
self.path('gear',(21,15),[('L',(27,15)),('L',(28,18)),('L',(31,17)),('L',(34,22)),('L',(31,24)),('L',(34,26)),('L',(31,31)),('L',(28,30)),('L',(27,33)),('L',(21,33)),('L',(20,30)),('L',(17,31)),('L',(14,26)),('L',(17,24)),('L',(14,22)),('L',(17,17)),('L',(20,18)),('L',(21,15))],True)
for n,p in [('top',(24,6)),('bottom',(24,42)),('left',(6,24)),('right',(42,24))]:self.add_dot(n,p)
''','settings: repeated rounded teeth','Tiny source specks removed; radial marks retained.')
add('people-giving-high-five','SQUARE','Two people raise their inner arms to meet in a high five.', '''
# Shared human head radius4; shoulder y28 minus head bottom20 gives exact 4 ink gap.
for i,x in enumerate([10,38]):self.oval('head-'+str(i),x,16,4)
for i in range(2):
    def q(x,y):return (x if i==0 else 48-x,y)
    self.path('shoulder-'+str(i),q(6,42),[('L',q(6,32)),('A',q(10,28),4,4,i==0),('L',q(14,28))])
    self.path('arm-'+str(i),q(14,28),[('A',q(24,18),10,10,i!=0)])
    self.add_line('torso-'+str(i),q(14,28),q(14,42))
    self.relate('connect','torso-'+str(i),'shoulder-'+str(i))
    self.relate('connect','arm-'+str(i),'shoulder-'+str(i))
    self.relate('connect','arm-'+str(i),'torso-'+str(i))
self.relate('connect','arm-0','arm-1')
self.add_dot('contact-ray',(24,6))
''','human_ref/user.svg and full_body_ref.png: paired round heads and raised limbs','Three contact rays reduced to one dot to keep the upper gap clear.')
add('recycle-arrows','SQUARE','Three bent arrows form a continuous clockwise recycling cycle.', '''
# Three distinct arrows with real endpoint joins; preserve triangular flow.
self.path('top',(18,12),[('L',(20,8)),('A',(28,8),5,5,True),('L',(36,22))])
self.add_polyline('top-head',(28,20),(36,22),(38,14));self.relate('connect','top','top-head')
self.path('right',(42,28),[('L',(42,32)),('A',(38,36),4,4,True),('L',(24,36))])
self.add_polyline('bottom-head',(30,30),(24,36),(30,42));self.relate('connect','right','bottom-head')
self.path('left',(15,36),[('L',(10,36)),('A',(6,32),4,4,True),('L',(12,20))])
self.add_polyline('left-head',(6,22),(12,20),(14,28));self.relate('connect','left','left-head')
''','recycle: three separate strokes and attached open arrowheads')
add('oval-stadium-with-two-flags','SQUARE','Oval stadium bowl with a broad opening and two raised flags.', '''
# Capsule rim and elliptical wall retain an open bowl; poles end on explicit rim nodes.
self.path('rim',(12,21),[('L',(34,21)),('L',(36,21)),('A',(42,27),6,6,True),('A',(36,33),6,6,True),('L',(12,33)),('A',(6,27),6,6,True),('A',(12,21),6,6,True)],True)
self.path('wall',(6,27),[('L',(6,35)),('A',(42,35),18,7,False),('L',(42,27))])
self.relate('connect','wall','rim')
for i,x in enumerate([12,34]):
    self.add_polyline('flag-'+str(i),(x,6),(x+8,10),(x,14),closed=True)
    self.add_line('pole-'+str(i),(x,14),(x,21))
    self.relate('connect','pole-'+str(i),'flag-'+str(i));self.relate('connect','pole-'+str(i),'rim')
''','No useful exact Lucide match; shared elliptical bowl and repeated flags','Inner field arc omitted because an additional nested opening cannot fit with 8-unit centerline spacing.')
add('pear-with-two-crossbars-on-diagonal-mark','VRECT_L','Pear with a diagonal genetic mark and two crossing bars.', '''
# The pear owns symmetric shoulder transitions and two equal crossbars.
self.path('pear',(24,8),[('A',(32,16),8,8,True),('A',(36,22),4,6,False),('A',(40,28),4,6,True),('A',(24,44),16,16,True),('A',(8,28),16,16,True),('A',(12,22),4,6,True),('A',(16,16),4,6,False),('A',(24,8),8,8,True)],True)
self.add_line('stem',(24,4),(24,8));self.relate('connect','stem','pear')
self.add_polyline('mark',(21,27),(27,33))
for i,(x,y) in enumerate([(21,27),(27,33)]):
    self.add_polyline('bar-'+str(i),(x-2,y+2),(x,y),(x+2,y-2));self.relate('connect','bar-'+str(i),'mark')
''','No useful exact Lucide match; coherent pear silhouette and repeated crossbars','Leaf omitted to preserve space for the identifying genetic mark.')
if __name__=='__main__':
 for name in sys.argv[1:] or D:export(write(name))
