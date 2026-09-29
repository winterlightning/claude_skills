"""Visual reconstruction plans for only this batch's claimed source references."""
SOURCE_ICON_ID=None
SOURCE_PATH='icon_set/work/fix-batch-20260929T094854Z/claims.json'
AUTHOR='gpt-6'

EXTRA_HELPERS='''
    def rect(self, name, x, y, w, h, r=2):
        self.path(name,(x+r,y),[("L",(x+w-r,y)),("A",(x+w,y+r),r,r,True),("L",(x+w,y+h-r)),("A",(x+w-r,y+h),r,r,True),("L",(x+r,y+h)),("A",(x,y+h-r),r,r,True),("L",(x,y+r)),("A",(x+r,y),r,r,True)],True)

    def phone(self):
        self.rect('phone',10,4,28,40,4)
        self.add_line('screen-bottom',(10,36),(38,36))
        self.relate('connect','phone','screen-bottom')

    def wireless(self):
        self.add_arc('signal-outer',(8,9),(40,9),radius_x=24,radius_y=16,sweep=True)
        self.add_arc('signal-inner',(17,14),(31,14),radius_x=12,radius_y=9,sweep=True)
'''

SPECS=[
('SQUARE','The drone is a floating dumbbell and the operator has no hands or controller.','Restore twin rotor arms, landing legs and a person visibly holding a controller.', '''
self.rect('drone-body',12,14,16,8,4)
for side,x in enumerate((8,32)):
    self.line(f'propeller-{side}',(x-4,6),(x+4,6))
    self.path(f'arm-{side}',(x,6), [('L',(x,10)),('A',(12 if side==0 else 28,14),4,4,side==0)])
self.poly('landing',(16,22),(16,27),(12,29))
self.circle('head',35,24,4)
self.path('shoulders',(28,42), [('L',(28,39)),('A',(35,36),7,3,True),('A',(42,39),7,3,True),('L',(42,42))])
self.rect('controller',29,38,12,4,2)
'''),
('VRECT_L','The portrait dominates a generic frame and the device lacks a clear speaker or home control; feedback specifically asks for Phone.','Restore a recognizable smartphone with speaker, home dot and an inset woman portrait with hair.', '''
self.rect('phone',8,4,32,40,4)
self.line('speaker',(21,10),(27,10))
self.circle('face',24,22,5)
self.path('hair-left',(19,21), [('L',(18,26)),('L',(16,29))])
self.path('hair-right',(29,21), [('L',(30,26)),('L',(32,29))])
self.path('shoulders',(16,35), [('A',(32,35),8,4,True)])
self.add_dot('home',(24,40))
'''),
('VRECT_L','The open-top outline resembles a wallet under Wi-Fi; the phone top and bottom bezel are missing.','Restore a closed handset and bottom bezel below two wireless arcs, with a clear euro sign.', '''
self.wireless()
self.rect('phone',13,21,22,23,3)
self.line('bezel',(13,39),(35,39))
self.path('euro',(28,27), [('A',(28,35),6,5,False)])
self.line('euro-bar',(19,31),(26,31))
self.relate('connect','phone','bezel')
'''),
('VRECT_L','The plus touches the badge circle, turning the requested circle-add into a crosshair.','Separate the plus from its circular badge and retain a full phone frame with a bottom bezel.', '''
self.rect('phone',8,4,32,40,4)
self.circle('badge',24,22,10)
self.line('plus-horizontal',(20,22),(28,22))
self.line('plus-vertical',(24,18),(24,26))
self.line('bezel',(8,36),(40,36))
self.relate('connect','phone','bezel')
'''),
('SQUARE','The lock is an open G-shaped stroke with no separate lock body or recognizable raised shackle.','Draw a monitor and stand containing a rectangular padlock body and visibly open round shackle.', '''
self.rect('screen',6,6,36,29,3)
self.line('stand',(24,35),(24,42))
self.line('base',(16,42),(32,42))
self.rect('lock-body',16,23,16,8,2)
self.path('shackle',(19,23), [('L',(19,17)),('A',(29,17),5,5,True)])
self.relate('connect','screen','stand')
self.relate('connect','stand','base')
self.relate('connect','shackle','lock-body')
'''),
('SQUARE','The old headset has dots instead of earcups and a detached arc/dot resembling a person, losing wireless meeting context.','Restore two earcups, a headband, boom microphone and two nested wireless arcs.', '''
self.path('signal-outer',(12,10), [('A',(36,10),17,12,True)])
self.path('signal-inner',(19,15), [('A',(29,15),9,6,True)])
self.path('band',(9,31), [('A',(39,31),15,12,True)])
self.rect('cup-left',6,28,7,12,3)
self.rect('cup-right',35,28,7,12,3)
self.path('boom',(38,40), [('A',(30,44),8,4,True),('L',(24,44))])
self.line('mic',(21,44),(26,44))
'''),
('SQUARE','The rejected mecha head is a Y-shaped antenna above a rounded box with no eyes or mechanical cheek structure.','Restore V antennae, paired angular eyes, side ear housings and a tapered armored jaw.', '''
self.poly('crest',(6,6),(24,19),(42,6))
self.line('crest-stem',(24,19),(24,23))
self.poly('helmet',(12,19),(12,33),(18,40),(24,42),(30,40),(36,33),(36,19))
for side in (-1,1):
    x=lambda v:24+side*v
    self.poly(f'eye-{side}',(x(9),25),(x(3),27))
    self.poly(f'ear-{side}',(x(12),23),(x(18),23),(x(18),35),(x(12),35))
self.poly('mask',(19,34),(24,31),(29,34))
self.line('chin',(24,35),(24,40))
'''),
('VRECT_M','The old Merlion is a generic animal blob with a zigzag nose and no mane crescent or projecting lion muzzle.','Restore the lion muzzle, open mouth, sweeping mane and rounded fish-body base from the source.', '''
self.path('outline',(16,11), [('L',(26,4)),('L',(32,4)),('A',(38,14),10,10,True),('L',(38,33)),('A',(14,33),12,11,True),('L',(16,26)),('L',(12,26)),('A',(10,24),2,2,True),('L',(10,22)),('L',(16,22)),('A',(16,17),3,3,False),('L',(12,17)),('A',(10,15),2,2,True),('L',(10,13)),('A',(12,11),2,2,True),('L',(16,11))],True)
self.path('mane',(26,10), [('A',(24,27),11,11,True)])
self.poly('fish-collar',(15,30),(21,35),(27,30),(37,33))
'''),
('SQUARE','The old hair consists of four vertical flame-like stems, with no clearly outward-facing snakes.','Give Medusa a circular jaw, two eyes and four curling snakes with directional heads around the face.', '''
self.path('jaw',(12,24), [('L',(12,30)),('A',(36,30),12,12,False),('L',(36,24))])
self.add_dot('eye-left',(19,29))
self.add_dot('eye-right',(29,29))
self.line('mouth',(22,36),(26,36))
for side in (-1,1):
    x=lambda v:24+side*v
    self.path(f'snake-top-{side}',(x(3),22), [('L',(x(3),15)),('A',(x(8),10),5,5,side>0),('L',(x(12),10)),('A',(x(12),6),2,2,side<0),('L',(x(8),6))])
    self.path(f'snake-side-{side}',(x(9),22), [('L',(x(14),22)),('A',(x(18),18),4,4,side<0),('L',(x(18),16))])
    self.path(f'snake-low-{side}',(x(12),30), [('L',(x(17),30)),('A',(x(17),36),3,3,side>0),('L',(x(15),36))])
'''),
('SQUARE','The rejected RAM is horizontal with dots and dangling pins; it loses the reference diagonal board, chips and side notch.','Restore a diagonal memory board with two diamond-oriented chip outlines and an inset side notch.', '''
self.path('board',(6,30), [('L',(17,19)),('A',(21,15),3,3,False),('L',(30,6)),('L',(42,18)),('L',(18,42)),('L',(6,30))],True)
for n,(x,y) in enumerate(((17,31),(31,17))):
    self.poly(f'chip-{n}',(x,y-4),(x+4,y),(x,y+4),(x-4,y),closed=True)
'''),
('VRECT_M','The globe was reduced to an umbrella-like semicircle and the microphone lost its stand.','Restore the globe meridians and curved sides above a recognizable capsule microphone, yoke and stand.', '''
self.path('globe-upper',(10,18), [('A',(38,18),14,14,True)])
self.path('globe-left',(10,18), [('A',(13,26),14,14,False)])
self.path('globe-right',(38,18), [('A',(35,26),14,14,True)])
self.line('equator',(10,18),(38,18))
self.path('meridian-left',(24,4), [('A',(18,18),6,14,False)])
self.path('meridian-right',(24,4), [('A',(30,18),6,14,True)])
self.rect('microphone',20,23,8,12,4)
self.path('yoke',(14,29), [('L',(14,31)),('A',(34,31),10,8,False),('L',(34,29))])
self.line('stem',(24,39),(24,44))
self.line('base',(16,44),(32,44))
'''),
('SQUARE','The miner has a box-like jaw and hanging vertical hair, losing the female portrait and flared hair of the reference.','Restore a broad helmet brim, distinct headlamp, round jaw and outward-flaring hair.', '''
self.circle('lamp',24,10,4)
self.path('helmet-left',(9,23), [('A',(19,10),15,15,True)])
self.path('helmet-right',(29,10), [('A',(39,23),15,15,True)])
self.line('brim',(6,23),(42,23))
self.path('jaw',(14,24), [('A',(34,24),10,10,False)])
for side in (-1,1):
    x=lambda v:24+side*v
    self.path(f'hair-{side}',(x(13),26), [('A',(x(18),38),25,25,side<0),('A',(x(7),39),10,6,side<0)])
'''),
('VRECT_M','The old Merlion is a generic animal blob with a zigzag nose and no mane crescent or projecting lion muzzle.','Restore the lion muzzle, open mouth, sweeping mane and rounded fish-body base from the source.',''),
('SQUARE','The tablet is just an open angular bracket, so the pair reads as a phone beside an incomplete shape.','Restore rounded tablet edges and a bottom bezel behind an overlapping, fully outlined phone.', '''
self.path('tablet',(18,17), [('L',(18,10)),('A',(22,6),4,4,True),('L',(38,6)),('A',(42,10),4,4,True),('L',(42,32)),('A',(38,36),4,4,True),('L',(32,36))])
self.line('tablet-bezel',(32,29),(42,29))
self.rect('phone',6,22,19,20,3)
self.line('phone-bezel',(6,35),(25,35))
self.relate('connect','tablet','tablet-bezel')
self.relate('connect','phone','phone-bezel')
'''),
('VRECT_M','The currency mark is a thick C with one bar and the handset corners are square.','Restore a euro with two crossbars inside a rounded handset with a bottom bezel.', '''
self.phone()
self.path('euro',(29,15), [('A',(29,29),9,8,False)])
self.line('bar-top',(16,20),(26,20))
self.line('bar-bottom',(16,25),(26,25))
'''),
('VRECT_M','The wrench was reduced to a vertical bone-shaped mark; it loses the diagonal shaft and open jaws.','Restore a diagonal double-ended spanner inside a rounded phone frame.', '''
self.phone()
self.path('jaw-top',(28,13), [('A',(34,19),5,5,False)])
self.path('jaw-bottom',(14,28), [('A',(20,34),5,5,True)])
self.line('shaft',(28,19),(20,27))
'''),
('VRECT_L','The child is just a dot and T-shape inside a dress; the source shows a complete little person and maternal hair.','Restore the child head, torso, arms and legs within the mother silhouette, and add the mother hair tips.', '''
self.circle('mother-head',24,9,5)
self.path('hair-left',(19,10), [('A',(15,15),7,7,True)])
self.path('hair-right',(29,10), [('A',(33,15),7,7,False)])
self.path('mother-body',(8,44), [('L',(15,25)),('A',(33,25),10,7,True),('L',(40,44)),('L',(8,44))],True)
self.circle('child-head',24,28,3)
self.line('child-torso',(24,35),(24,39))
self.poly('child-arms',(20,37),(24,35),(28,37))
self.poly('child-legs',(20,43),(24,39),(28,43))
self.mark_human_figure('child',head='child-head',torso='child-torso',torso_junction='start')
self.relate('connect','child-torso','child-arms')
self.relate('connect','child-torso','child-legs')
'''),
('VRECT_L','The storefront fills the whole handset and has no home control; the drawing reads as a generic shop.','Restore a rounded mobile frame, scalloped shop awning, screen window and separate bottom home control.', '''
self.rect('phone',8,4,32,40,4)
self.path('awning',(10,16), [('L',(14,10)),('L',(34,10)),('L',(38,16)),('A',(31,16),4,4,True),('A',(24,16),4,4,True),('A',(17,16),4,4,True),('A',(10,16),4,4,True)],True)
self.poly('shop-front',(13,22),(13,33),(35,33),(35,22))
self.add_dot('home',(24,39))
'''),
('VRECT_L','The open-top phone resembles a wallet and the pound sign is an E-like mark.','Restore the closed handset below two wireless arcs and a pound sign with curved top, crossbar and baseline.', '''
self.wireless()
self.rect('phone',13,21,22,23,3)
self.line('bezel',(13,39),(35,39))
self.path('pound',(28,28), [('A',(22,28),3,3,False),('L',(22,35))])
self.line('pound-crossbar',(19,31),(26,31))
self.line('pound-base',(19,35),(29,35))
self.relate('connect','phone','bezel')
'''),
('VRECT_L','The mother and baby are detached rings above an open cradle line, losing the enclosing maternal body and nursing pose.','Restore a continuous seated maternal silhouette, baby head and diagonal baby body supported by a curved arm.', '''
self.circle('mother-head',20,10,6)
self.circle('baby-head',35,26,5)
self.path('body',(15,20), [('A',(8,31),13,13,False),('A',(24,44),16,13,False),('A',(40,34),16,12,False)])
self.path('arm',(15,31), [('A',(23,37),8,6,False),('L',(31,37))])
self.path('baby-body',(32,31), [('A',(23,37),13,13,False)])
self.line('shoulder',(25,20),(29,23))
'''),
]
SPECS[12]=(*SPECS[12][:3],SPECS[7][3])

def revise(i,body):
    SPECS[i]=(*SPECS[i][:3],body)

revise(0, '''
self.rect('drone-body',12,14,16,8,4)
for side,x in enumerate((8,32)):
    self.line(f'propeller-{side}',(x-4,6),(x+4,6))
    self.path(f'arm-{side}',(x,6), [('L',(x,10)),('A',(12 if side==0 else 28,14),4,4,side==0)])
self.poly('landing',(16,22),(16,27),(12,29))
self.circle('head',35,24,4)
self.path('shoulders',(26,44), [('L',(26,41)),('A',(35,36),9,5,True),('A',(44,41),9,5,True),('L',(44,44))])
self.line('controller',(31,43),(39,43))
''')
revise(2, '''
self.wireless()
self.rect('phone',12,20,24,24,3)
self.path('euro',(29,27), [('L',(27,27)),('A',(21,32),6,5,False),('A',(27,37),6,5,False),('L',(29,37))])
self.line('euro-bar',(19,32),(27,32))
''')
revise(3,SPECS[3][3].replace("'badge',24,22,10", "'badge',24,21,9").replace('(20,22),(28,22)','(21,21),(27,21)').replace('(24,18),(24,26)','(24,18),(24,24)'))
revise(4, '''
self.rect('screen',4,4,40,32,3)
self.line('stand',(24,36),(24,44))
self.line('base',(16,44),(32,44))
self.rect('lock-body',16,21,16,8,2)
self.path('shackle',(19,21), [('L',(19,15)),('A',(29,15),5,5,True)])
self.relate('connect','screen','stand')
self.relate('connect','stand','base')
self.relate('connect','shackle','lock-body')
''')
revise(5,SPECS[5][3].replace("(19,15), [('A',(29,15)","(19,13), [('A',(29,13)").replace("self.line('mic',(21,44),(26,44))",'').replace("('L',(24,44))","('L',(21,44))"))
for i in (7,12):
    revise(i,SPECS[i][3].replace("[('L',(26,4))", "[('A',(26,4),10,10,True)"))
revise(9,SPECS[9][3].replace('(x,y-4),(x+4,y),(x,y+4),(x-4,y)','(x,y-5),(x+5,y),(x,y+5),(x-5,y)'))
revise(14, '''
self.phone()
self.path('euro',(30,14), [('L',(28,14)),('A',(20,22),8,8,False),('A',(28,30),8,8,False),('L',(30,30))])
self.line('bar-top',(17,20),(27,20))
self.line('bar-bottom',(17,25),(27,25))
''')
revise(15, '''
self.rect('phone',8,4,32,40,4)
self.line('bezel',(8,36),(40,36))
self.path('jaw-top',(26,12), [('A',(32,18),4,4,False)])
self.path('jaw-bottom',(18,24), [('A',(24,30),4,4,True)])
self.line('shaft',(26,18),(24,24))
self.relate('connect','phone','bezel')
''')
revise(16, '''
self.circle('mother-head',24,8,4)
self.path('hair-left',(20,9), [('A',(16,14),7,7,True)])
self.path('hair-right',(28,9), [('A',(32,14),7,7,False)])
self.path('mother-body',(8,44), [('L',(15,25)),('A',(33,25),10,5,True),('L',(40,44)),('L',(8,44))],True)
self.circle('child-head',24,27,2)
self.line('child-torso',(24,34),(24,36))
self.line('child-arms',(20,34),(28,34))
self.poly('child-legs',(20,39),(24,36),(28,39))
self.mark_human_figure('child',head='child-head',torso='child-torso',torso_junction='start')
self.relate('connect','child-torso','child-arms')
self.relate('connect','child-torso','child-legs')
''')
revise(17, '''
self.rect('phone',8,4,32,40,4)
self.path('awning',(12,16), [('L',(16,10)),('L',(32,10)),('L',(36,16)),('A',(28,16),4,4,True),('A',(20,16),4,4,True),('A',(12,16),4,4,True)],True)
self.poly('shop-front',(15,23),(15,33),(33,33),(33,23))
self.add_dot('home',(24,39))
''')
revise(18, '''
self.wireless()
self.rect('phone',12,20,24,24,3)
self.path('pound',(29,29), [('A',(21,29),4,3,False),('L',(21,38))])
self.line('pound-crossbar',(18,32),(25,32))
self.line('pound-base',(18,38),(29,38))
''')

revise(9, '''
self.path('board',(6,28), [('L',(17,17)),('A',(21,13),3,3,False),('L',(28,6)),('L',(42,20)),('L',(20,42)),('L',(6,28))],True)
for n,(x,y) in enumerate(((19,29),(29,19))):
    self.poly(f'chip-{n}',(x,y-5),(x+5,y),(x,y+5),(x-5,y),closed=True)
''')
revise(13,SPECS[13][3].replace("(18,17)","(18,14)").replace("('L',(32,36))","('L',(33,36))").replace("(32,29),(42,29)","(33,28),(42,28)").replace("(6,35),(25,35)","(6,34),(25,34)"))
revise(16,SPECS[16][3].replace("self.circle('child-head',24,27,2)","self.add_dot('child-head',(24,28))"))
revise(13,SPECS[13][3].replace('(18,14)','(18,13)').replace('(33,36)','(34,36)').replace('(33,28)','(34,28)'))
revise(0,SPECS[0][3].replace("self.circle('head',35,24,4)","self.line('landing-right',(23,22),(23,27))\nself.circle('head',35,24,4)"))
SPECS[2]=(SPECS[2][0],SPECS[2][1],'Restore a closed handset below two wireless arcs and a clear euro sign; omit the crowded lower bezel.',SPECS[2][3])
SPECS[15]=('VRECT_L',*SPECS[15][1:])
