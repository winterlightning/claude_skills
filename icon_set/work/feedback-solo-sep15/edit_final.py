from edit_batch import *
revise(183,'Widen and straighten the ATV upper body while keeping both wheels and handlebar.',body='''
path('body',(4,33),[('L',(4,20)),('L',(28,20)),('L',(38,20)),('A',(44,26),6,6,True),('L',(44,33))])
line('handlebar',(28,20),(24,8));join('handlebar','body')
for n,x in [('rear',11),('front',37)]:oval(n,x,33,7,7);join(n,'body')
line('chassis',(18,33),(30,33));join('chassis','rear');join('chassis','front')
''')
revise(185,'Widen the central shield symmetrically while retaining its side wings.',body='''
path('shield',(24,8),[('L',(36,14)),('L',(36,20)),('L',(36,26)),('A',(24,40),12,14,True),('A',(12,26),12,14,True),('L',(12,20)),('L',(12,14)),('L',(24,8))],True)
path('wing-left',(12,20),[('L',(4,20)),('A',(12,28),8,8,False)])
path('wing-right',(36,20),[('L',(44,20)),('A',(36,28),8,8,True)])
join('shield','wing-left');join('shield','wing-right')
''')
revise(191,'Rebuild the glue stick as a narrow upright tube with a wider cap and a simple base seam.',body='''
poly('cap',(8,4),(40,4),(40,14),(32,14),(16,14),(8,14),closed=True)
path('tube',(16,14),[('L',(16,36)),('L',(16,40)),('A',(20,44),4,4,False),('L',(28,44)),('A',(32,40),4,4,False),('L',(32,36)),('L',(32,14))]);join('tube','cap')
line('base',(16,36),(32,36));join('base','tube')
''',keyshape='VRECT_L')
revise(189,'Round the roof, windscreen slope and lower body corners consistently.',body='''
path('body',(9,35),[('L',(8,35)),('A',(4,31),4,4,True),('L',(4,12)),('A',(8,8),4,4,True),('L',(28,8)),('C',(34,11),(31,8),(33,9)),('L',(42,21)),('C',(44,27),(43,23),(44,25)),('L',(44,31)),('A',(40,35),4,4,True),('L',(39,35))])
for n,x in [('rear',14),('front',34)]:oval(n,x,35,5,5);join('body',n)
line('sill',(19,35),(29,35));join('sill','rear');join('sill','front')
line('window',(13,20),(23,20))
''')
revise(208,'Enlarge both ant eyes from radius three to four and rebalance the head between them.',body='''
path('head',(16,27),[('A',(20,18),4,9,True),('L',(28,18)),('A',(32,27),4,9,True),('L',(32,34)),('A',(28,38),4,4,True),('L',(28,44)),('L',(20,44)),('L',(20,38)),('A',(16,34),4,4,True),('L',(16,27))],True)
for n,x in [('left',12),('right',36)]:oval(n,x,27,4,4);join(n,'head')
poly('antenna-left',(20,18),(20,8),(14,4));poly('antenna-right',(28,18),(28,8),(34,4))
join('antenna-left','head');join('antenna-right','head')
''')
revise(211,'Replace the short stem mark with a pointed curved leaf and rebalance the fruit below it.',body='''
path('leaf',(22,12),[('C',(34,4),(22,6),(28,4)),('C',(22,12),(34,10),(28,12))],True)
path('fruit',(40,24),[('C',(24,22),(34,18),(29,24)),('C',(8,28),(16,18),(8,21)),('C',(18,44),(8,36),(13,44)),('C',(24,42),(21,44),(22,42)),('C',(30,44),(26,42),(28,44)),('C',(40,34),(36,44),(39,38)),('C',(40,24),(30,32),(31,26))],True)
''')
revise(224,'Curve the outer wing shoulders and keep the paired lower scallops symmetric.',patch=lambda s:s.replace("poly('crown', (4, 26), (9, 8), (14, 18), (19, 18), (20, 10), (24, 14), (28, 10), (29, 18), (34, 18), (39, 8), (44, 26))","self.add_bezier('crown-1',(4,26),((4,20),(7,13),(9,8)))\n    self.add_bezier('crown-2',(9,8),((9,14),(11,18),(14,18)))\n    poly('middle',(14,18),(19,18),(20,10),(24,14),(28,10),(29,18),(34,18))\n    self.add_bezier('crown-9',(34,18),((37,18),(39,14),(39,8)))\n    self.add_bezier('crown-10',(39,8),((41,13),(44,20),(44,26)))").replace("*[f'crown-{i}' for i in range(1, 11)]","'crown-1','crown-2',*[f'middle-{i}' for i in range(1,7)],'crown-9','crown-10'"))
revise(227,'Widen the kidney bean and use four coherent rounded arcs.',body='''
path('bean',(24,16),[('A',(44,16),10,8,True),('A',(12,40),32,24,True),('A',(12,24),8,8,True),('A',(24,16),12,8,False)],True)
path('seam',(16,32),[('A',(34,18),18,18,False)])
''',keyshape='HRECT_L',ref='Lucide bean: one notched outline and a curved inner seam')
revise(235,'Replace segmented eye curves with coherent mirrored elliptical arcs and exact slash attachment points.',body='''
path('eye',(4,24),[('A',(9,16),25,40,True),('A',(44,24),25,40,True),('A',(39,32),25,40,True),('A',(4,24),25,40,True)],True)
line('slash',(9,16),(39,32));join('slash','eye')
''',ref='Lucide eye: simple mirrored eyelid curves')
revise(178,'Rounded-tail takeoff alternative: soften the tail and wing corners while keeping the rising airplane.',body='''
path('plane',(12,26),[('C',(6,16),(9,25),(7,20)),('A',(10,12),4,4,True),('L',(17,17)),('L',(30,11)),('L',(34,8)),('A',(40,16),5,5,True),('L',(18,25)),('C',(12,26),(16,26),(14,26))],True)
line('wing',(30,11),(22,6));join('wing','plane')
poly('runway',(10,34),(38,34),(42,42),(6,42),closed=True)
''')
revise(179,'Line-tail takeoff alternative: a simple tail stroke, rounded fuselage and clear runway.',body='''
path('body',(12,18),[('L',(26,18)),('L',(38,18)),('A',(42,22),4,4,True),('A',(38,26),4,4,True),('L',(26,26)),('L',(12,26)),('A',(8,22),4,4,True),('A',(12,18),4,4,True)],True)
line('tail',(8,22),(6,12));join('tail','body')
line('upper-wing',(26,18),(20,6));line('lower-wing',(26,26),(20,32));join('upper-wing','body');join('lower-wing','body')
line('runway',(6,42),(42,42))
''')
revise(198,'Side-view takeoff alternative: a larger tail, clear upper and lower wings, and one runway line.',body='''
path('plane',(6,12),[('L',(14,12)),('L',(18,18)),('L',(26,18)),('L',(38,18)),('A',(42,22),4,4,True),('A',(38,26),4,4,True),('L',(26,26)),('L',(12,26)),('L',(6,12))],True)
line('upper-wing',(26,18),(20,6));line('lower-wing',(26,26),(20,32));join('upper-wing','plane');join('lower-wing','plane')
line('runway',(6,42),(42,42))
''')
revise(200,'Give the aircraft a closed top-side silhouette with a rounded nose, swept wing and separate falling bomb.',body='''
path('plane',(6,12),[('L',(14,16)),('L',(18,16)),('L',(24,6)),('L',(32,6)),('L',(28,18)),('L',(38,18)),('A',(42,22),4,4,True),('A',(38,26),4,4,True),('L',(12,26)),('L',(6,12))],True)
path('bomb',(14,34),[('L',(24,34)),('L',(24,38)),('L',(24,42)),('L',(14,42)),('A',(14,34),4,4,True)],True)
poly('tail',(32,34),(24,38),(32,42));join('tail','bomb')
''',keyshape='SQUARE')
revise(214,'Clarify the tail connection with a broad straight rear fuselage and one centered tail fin.',body='''
path('airframe',(4,16),[('L',(12,18)),('L',(18,18)),('L',(14,8)),('L',(22,8)),('L',(32,18)),('L',(38,18)),('A',(38,30),6,6,True),('L',(32,30)),('L',(22,40)),('L',(14,40)),('L',(18,30)),('L',(12,30)),('L',(4,32)),('L',(8,24)),('L',(4,16))],True)
line('tail-center',(8,24),(16,24));join('tail-center','airframe')
''')
revise(215,'Shorten and widen both wings around a horizontal fuselage; retain the landing wheel.',body='''
path('plane',(4,12),[('L',(12,16)),('L',(16,20)),('L',(20,20)),('L',(16,8)),('L',(24,8)),('L',(32,20)),('L',(40,20)),('A',(40,28),4,4,True),('L',(32,28)),('L',(24,36)),('L',(16,36)),('L',(20,28)),('L',(12,28)),('L',(4,12))],True)
line('strut',(40,28),(40,34));join('strut','plane')
oval('wheel',40,37,3,3);join('strut','wheel')
''',keyshape='HRECT_L')
