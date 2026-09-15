from edit_batch import *
revise([16,126,138],'Remove the short inner wing return so the swan reads as a broad curved body above a calm waterline.',patch=lambda s:s.replace("        self.add_bezier('wing-top',(16,24),((16,23),(16,22),(16,21)))\n",'').replace("    self.add_bezier('wing-top',(16,24),((16,23),(16,22),(16,21)))\n",'').replace(", 'wing-top'",''),ref='Lucide bird: a reduced continuous neck and body')
revise([30,152],'Simplify the canyon to two stepped cliffs, distant mountain slopes, and one curved river.',body='''
poly('left-cliff',(6,42),(6,18),(16,18),(16,26))
poly('right-cliff',(42,42),(42,18),(34,18),(34,26))
poly('mountain',(6,10),(16,6),(25,12),(34,6),(42,10))
path('river',(25,23),[('C',(23,33),(25,28),(23,30)),('C',(29,42),(23,37),(27,40))])
''')
revise(45,'Smooth the belly using matched vertical tangents and balance the arm curve across the torso.',patch=lambda s:s.replace("self.add_arc('arm-left', (8,8), (17,13), radius_x=9, radius_y=5, sweep=False)","self.add_arc('arm-left',(8,8),(20,13),radius_x=12,radius_y=5,sweep=False)").replace("self.add_arc('arm-right', (17,13), (32,8), radius_x=15, radius_y=5, sweep=False)","self.add_arc('arm-right',(20,13),(32,8),radius_x=12,radius_y=5,sweep=False)"))
revise([70,86],'Open the pot rim and simplify the cactus to a tall center stem with larger mirrored branches.',body='''
poly('rim',(8,28),(24,28),(40,28),(40,38),(8,38),closed=True)
poly('pot',(13,38),(16,44),(32,44),(35,38));join('pot','rim')
poly('stem',(24,4),(24,18),(24,28));join('stem','rim')
path('left-arm',(8,8),[('L',(8,12)),('A',(14,18),6,6,False),('L',(24,18))])
path('right-arm',(40,8),[('L',(40,12)),('A',(34,18),6,6,True),('L',(24,18))])
join('left-arm','stem');join('right-arm','stem');join('left-arm','right-arm')
''',keyshape='VRECT_L')
revise(54,'Move the two bells inward symmetrically; widen the round clock face to preserve the vertical envelope.',body='''
oval('clock',24,30,16,14)
path('bell-left',(11,8),[('A',(21,8),5,4,True)])
path('bell-right',(27,8),[('A',(37,8),5,4,True)])
poly('hands',(24,25),(24,30),(20,32))
''')
revise(102,'Rebuild the snake as a clear open coil with a broad rounded head.',body='''
path('coil',(18,36),[('A',(6,24),12,12,True),('A',(24,6),18,18,True),('A',(42,24),18,18,True),('L',(42,34)),('A',(34,42),8,8,True),('A',(26,34),8,8,True),('L',(26,25))])
path('head',(26,25),[('A',(34,17),8,8,True),('L',(39,17))]);join('head','coil')
''',ref='Lucide shell: coherent spiral strokes')
revise([90,112],'Simplify the crocodile snout to one horizontal stroke and keep a low toothed back above the water.',body='''
poly('back',(4,18),(8,14),(12,18),(18,18))
path('brow',(18,18),[('A',(36,18),9,10,True),('L',(44,18))]);join('back','brow')
dot('eye',(27,18))
path('water',(4,37),[('A',(18,37),7,3,False),('A',(30,37),6,3,False),('A',(44,37),7,3,False)])
''',keyshape='HRECT_L')
revise(113,'Shorten the four legs and replace the angular claws with opposing curves.',body='''
oval('body',24,27,6,7)
for side in (-1,1):
 x=lambda d:24+side*d
 line(f'upper-leg-{side}',(x(6),27),(x(14),25));join(f'upper-leg-{side}','body')
 line(f'lower-leg-{side}',(24,34),(x(14),34));join(f'lower-leg-{side}','body')
 path(f'arm-{side}',(24,20),[('L',(x(12),15))]);join(f'arm-{side}','body')
 path(f'claw-{side}',(x(18),6),[('A',(x(12),15),6,9,side==1),('A',(x(6),6),6,9,side==1)])
 join(f'arm-{side}',f'claw-{side}')
join('arm--1','arm-1');join('lower-leg--1','lower-leg-1')
path('tail',(24,34),[('A',(6,34),9,8,True)])
join('tail','body');join('tail','lower-leg--1');join('tail','lower-leg-1')
''')
revise(157,'Use a round baby face with curved ears and a small hair curl; remove the large angular bow.',body='''
path('face',(10,24),[('A',(24,6),14,18,True),('A',(38,24),14,18,True),('A',(42,28),4,4,True),('A',(38,32),4,4,True),('A',(24,42),14,10,True),('A',(10,32),14,10,True),('A',(6,28),4,4,True),('A',(10,24),4,4,True)],True)
dot('eye-left',(18,24));dot('eye-right',(30,24))
''',ref='Lucide baby and shared human reference: round cheeks, curved ears, paired eyes')
revise(159,'Round the rabbit head and muzzle while retaining the leaping body and long ear.',patch=lambda s:s.replace("self.add_polyline('head',(32, 18),(42, 18),(42, 30),(34, 30),(30, 34),closed=False)","self.add_line('head-1',(32,18),(36,18))\n    self.add_arc('head-2',(36,18),(42,24),radius_x=6)\n    self.add_arc('head-3',(42,24),(36,30),radius_x=6)\n    self.add_line('head-4',(36,30),(30,34))"))
revise(168,'Replace the diaper curve and tapered body with one rounded rectangular torso.',body='''
oval('head',24,10,6,6)
path('torso',(24,24),[('L',(28,24)),('A',(32,28),4,4,True),('L',(32,36)),('A',(28,40),4,4,True),('L',(20,40)),('A',(16,36),4,4,True),('L',(16,28)),('A',(20,24),4,4,True),('L',(24,24))],True)
line('arm-left',(16,28),(8,34));line('arm-right',(32,28),(40,34));join('arm-left','torso');join('arm-right','torso')
line('leg-left',(20,40),(16,44));line('leg-right',(28,40),(32,44));join('leg-left','torso');join('leg-right','torso')
''',keyshape='VRECT_L',ref='Shared full_body_ref.png: circular head; head bottom16 to torso top24 gives exactly 4 ink units')
for n in [203,204]:
 revise(n,'Reduce five lines to three, with a shared left edge and even vertical spacing.',body="\n".join(f"line('row-{i}',(6,{y}),({end},{y}))" for i,(y,end) in enumerate([(6,42),(24,42 if n==203 else 30),(42,42 if n==203 else 22)])))
for n in [205,206]:
 revise(n,'Widen the hexagon to the square envelope while retaining the original mark.',patch=lambda s:s.replace('(40, 33)','(42, 33)').replace('(40, 13)','(42, 15)').replace('(27, 4)','(27, 6)').replace('(24, 44)','(24, 42)').replace('(8, 33)','(6, 33)').replace('(8, 13)','(6, 15)').replace('(21, 4)','(21, 6)') if n==205 else s.replace('axis-16, axis+16','axis-18, axis+18').replace('(axis,4)','(axis,6)').replace('(axis,44)','(axis,42)'),keyshape='SQUARE')
revise(188,'Rebuild the robe with two short horizontal rectangular sleeves and a centered collar.',body='''
poly('robe',(16,6),(6,6),(6,18),(16,18),(16,30),(12,42),(36,42),(32,30),(32,18),(42,18),(42,6),(32,6),(16,6),closed=True)
poly('collar',(16,6),(24,18),(32,6));join('collar','robe')
poly('belt',(16,30),(24,30),(32,30));join('belt','robe')
line('front',(24,18),(24,30));join('front','collar');join('front','belt')
''',ref='Lucide shirt: mirrored sleeve and shoulder construction')
revise(217,'Replace both tapered sleeves with mirrored horizontal rectangles.',body='''
path('suit',(16,6),[('L',(6,6)),('L',(6,18)),('L',(14,18)),('L',(14,30)),('A',(20,36),6,6,True),('L',(20,42)),('L',(28,42)),('L',(28,36)),('A',(34,30),6,6,True),('L',(34,18)),('L',(42,18)),('L',(42,6)),('L',(32,6)),('A',(16,6),8,8,True)],True)
''',ref='Lucide shirt: mirrored rectangular sleeves')
revise(216,'Align the final pull-cord segment vertically through the pull-ring center.',patch=lambda s:s.replace('(42, 42)','(39, 42)').replace('(42, 24)','(39, 24)'))
revise(229,'Enlarge both bicycle wheels equally and rebalance the frame above them.',body='''
for n,x in [('rear',11),('front',37)]:oval(n,x,33,7,7)
poly('rear-frame',(11,26),(18,17),(29,29),(34,17),(18,17))
poly('fork',(37,26),(34,17),(30,8),(37,8))
poly('seat',(12,8),(18,8),(22,8));line('post',(18,8),(18,17))
for a,b in [('rear-frame','rear'),('fork','front'),('fork','rear-frame'),('post','rear-frame'),('post','seat')]:join(a,b)
''',ref='Lucide bike: shared wheel radii and simple frame')
revise(230,'Enlarge the matching wheels to radius eight and keep their baseline level.',body='''
for n,x in [('rear',12),('front',36)]:oval(n,x,32,8,8)
poly('frame',(12,24),(20,16),(30,16),(36,24))
poly('seat',(8,8),(16,8),(20,16));join('seat','frame')
poly('bar',(30,16),(30,11),(36,8));join('bar','frame')
join('rear','frame');join('front','frame')
''',ref='Lucide bike: matched circular wheels')
revise(231,'Center the arrowhead on the rising graph direction and use a coherent shared tip.',body='''
poly('graph',(4,38),(16,17),(28,40),(44,8))
poly('arrow',(36,10),(44,8),(46,16));join('arrow','graph')
''',keyshape='HRECT_L')
revise(228,'Replace tall pointed ears with smaller rounded Bengal-style ear tips.',body='''
path('head',(6,24),[('L',(6,10)),('A',(12,6),5,5,True),('L',(18,14)),('L',(30,14)),('L',(36,6)),('A',(42,10),5,5,True),('L',(42,24)),('A',(24,42),18,18,True),('A',(6,24),18,18,True)],True)
poly('nose',(21,29),(24,32),(27,29))
''',ref='Lucide cat: mirrored ears and rounded jaw')
