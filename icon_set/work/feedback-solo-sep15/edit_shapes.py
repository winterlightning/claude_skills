from edit_batch import *
revise([5,225],'Round the bill with a semicircular tip while retaining the duck silhouette.',patch=lambda s:s.replace("self.add_line('bill-1', (13, 26), (4, 26))","self.add_line('bill-1', (13,26), (8,26))").replace("self.add_line('bill-2', (4, 26), (4, 18))","self.add_arc('bill-2',(8,26),(8,18),radius_x=4)").replace("self.add_line('bill-3', (4, 18), (10, 18))","self.add_line('bill-3',(8,18),(10,18))"),ref='Lucide bird: coherent outline with a rounded bill')
revise([7,226],'Simplify the necklace to three dot beads, paired curved chain sections, and one hexagonal pendant.',body='''
for x in (6,24,42):dot(f'bead-{x}',(x,6))
path('chain-left',(6,16),[('A',(16,30),10,14,False)])
path('chain-right',(42,16),[('A',(32,30),10,14,True)])
poly('stone',(24,26),(32,30),(32,38),(24,42),(16,38),(16,30),closed=True)
join('chain-left','stone');join('chain-right','stone')
''',ref='Lucide gem: minimal faceted perimeter')
revise(22,'Use continuous smooth screen curves and a single centered stand.',body='''
path('screen',(4,8),[('C',(44,8),(16,12),(32,12)),('L',(44,32)),('C',(24,30),(38,30),(30,30)),('C',(4,32),(18,30),(10,30)),('L',(4,8))],True)
line('stand',(24,30),(24,40));join('stand','screen')
poly('base',(14,40),(24,40),(34,40));join('stand','base')
''')
revise(23,'Reduce the spillway to two falling streams above a single smooth water stroke.',body='''
for i,x in enumerate((10,32)):
 path(f'stream-{i}',(x,8),[('L',(x,23)),('A',(x+6,29),6,6,False)])
path('water',(4,38),[('C',(24,38),(10,40),(18,40)),('C',(44,38),(30,36),(38,36))])
''')
revise(43,'Simplify the locket portrait to a dot head and one shoulder curve; retain both hinged halves.',patch=lambda s:remove_named(s,{'portrait-head-top','portrait-head-bottom','portrait-head'})+"\n    self.add_dot('portrait-head',(28,18))\n")
revise(68,'Replace the angular tail tip with a smooth rounded return.',patch=lambda s:s.replace("self.add_line('tail-1', (36, 28), (42, 34))","self.add_arc('tail-1',(36,28),(42,34),radius_x=6)").replace("self.add_line('tail-2', (42, 34), (38, 38))","self.add_arc('tail-2',(42,34),(38,38),radius_x=4)"))
revise(85,'Raise and lengthen both cactus branches equally.',patch=lambda s:s.replace('(8,12)','(8,8)').replace('(40,12)','(40,8)'))
revise(111,'Rebuild the fan blade as an exact circle with a diagonal handle at a shared circle point.',body='''
path('blade',(17,33),[('A',(14,24),15,15,True),('A',(29,9),15,15,True),('A',(44,24),15,15,True),('A',(29,39),15,15,True),('A',(17,33),15,15,True)],True)
line('handle',(4,40),(17,33));join('handle','blade')
''',keyshape='HRECT_L')
revise(114,'Remove the triangular crest and enlarge the smooth crown to retain the full icon height.',body='''
path('front',(8,24),[('A',(24,4),16,20,True),('A',(34,20),10,16,True),('L',(40,16)),('L',(32,28)),('L',(40,32)),('L',(29,40)),('L',(30,44))])
path('back',(8,24),[('C',(10,39),(8,31),(9,36)),('L',(8,44))]);join('front','back')
dot('eye',(23,19))
''',ref='Lucide bird: rounded head with a simple open beak')
revise(145,'Straight-bottom dam alternative: replace the curved lower edge with a flat base.',patch=lambda s:s.replace('(4, 32)','(4, 40)').replace('(44, 32)','(44, 40)').replace("self.add_arc('water', (44, 40), (4, 40), radius_x=20, radius_y=8, sweep=True)","self.add_line('water',(44,40),(4,40))"))
revise(165,'Wave-bottom dam alternative: add three equal wave sections along the base.',body='''
poly('wall',(4,34),(4,8),(14,8),(14,16),(34,16),(34,8),(44,8),(44,34))
path('water',(44,34),[('A',(30,34),7,6,True),('A',(18,34),6,6,True),('A',(4,34),7,6,True)])
join('wall','water')
line('flow-left',(18,25),(16,30));line('flow-right',(32,25),(30,30))
''')
revise(148,'Folded-corner mural alternative: a rectangular inner sheet with one folded corner.',body='''
poly('panel',(4,8),(44,8),(44,40),(4,40),closed=True)
poly('mural',(14,17),(34,17),(34,31),(25,31),(14,31),closed=True)
poly('fold',(34,22),(25,22),(25,31));join('mural','fold')
''',keyshape='HRECT_L')
revise(149,'Plain mural alternative: widen the panel and use a centered rectangular inner motif.',body='''
poly('panel',(4,8),(44,8),(44,40),(4,40),closed=True)
poly('mural',(14,17),(34,17),(34,31),(14,31),closed=True)
''',keyshape='HRECT_L')
revise(177,'Round all four envelope corners with equal-radius arcs; retain the folded flap.',body='''
path('envelope',(8,8),[('L',(40,8)),('A',(44,12),4,4,True),('L',(44,36)),('A',(40,40),4,4,True),('L',(8,40)),('A',(4,36),4,4,True),('L',(4,12)),('A',(8,8),4,4,True)],True)
path('flap',(4,12),[('L',(21,26)),('A',(27,26),5,5,False),('L',(44,12))]);join('envelope','flap')
''')
revise(180,'Use a smaller rounded rectangle behind a larger bottom-right rounded rectangle.',body='''
path('back',(24,16),[('L',(24,10)),('A',(20,6),4,4,False),('L',(10,6)),('A',(6,10),4,4,False),('L',(6,26)),('A',(10,30),4,4,False),('L',(16,30))])
path('front',(20,16),[('L',(24,16)),('L',(38,16)),('A',(42,20),4,4,True),('L',(42,38)),('A',(38,42),4,4,True),('L',(20,42)),('A',(16,38),4,4,True),('L',(16,30)),('L',(16,20)),('A',(20,16),4,4,True)],True)
join('back','front')
''')
revise(184,'Replace the upper oval with a circular semicircle and center the cross beneath it.',body='''
path('crescent',(40,4),[('A',(24,20),16,16,True),('A',(8,4),16,16,True)])
poly('stem',(24,20),(24,34),(24,44));join('stem','crescent')
poly('cross',(14,34),(24,34),(34,34));join('stem','cross')
''')
revise(192,'Align the cursor tail to the center axis of the pointer, keeping exact square proportions.',body='''
poly('pointer',(6,6),(42,22),(24,24),(22,42),closed=True)
line('tail',(24,24),(38,38));join('pointer','tail')
''',keyshape='SQUARE')
revise(194,'Round the document perimeter and folded corner with coherent equal-radius turns.',body='''
path('paper',(10,6),[('L',(38,6)),('A',(42,10),4,4,True),('L',(42,28)),('A',(40,32),5,5,True),('L',(32,40)),('A',(28,42),5,5,True),('L',(10,42)),('A',(6,38),4,4,True),('L',(6,10)),('A',(10,6),4,4,True)],True)
path('fold',(42,28),[('L',(32,28)),('A',(28,32),4,4,False),('L',(28,42))]);join('paper','fold')
''')
revise(209,'Recompose the antenna phone horizontally with a landscape body and clear screen division.',body='''
path('body',(8,18),[('L',(18,18)),('L',(40,18)),('A',(44,22),4,4,True),('L',(44,36)),('A',(40,40),4,4,True),('L',(18,40)),('L',(8,40)),('A',(4,36),4,4,True),('L',(4,22)),('A',(8,18),4,4,True)],True)
line('antenna',(8,8),(8,18));join('antenna','body')
line('screen-edge',(18,18),(18,40));join('screen-edge','body')
''',keyshape='HRECT_L')
revise(210,'Replace the outlined axe handle with one diagonal stick aligned to the blade socket.',patch=lambda s:s[:s.index("        path('handle'")] if False else s.replace("path('handle',(24,18),[('L',(8,34)),('C',(6,38),(6,36),(6,36)),('A',(10,42),4,4,False),('C',(14,40),(12,42),(13,41)),('L',(30,24))])","line('handle',(27,21),(6,42))"))
revise(218,'Shorten the carry handle and raise the bag top to create a taller body.',patch=lambda s:s.replace('(18,24)','(18,16)').replace('(30,24)','(30,16)').replace('(12,24)','(12,16)').replace('(36,24)','(36,16)'))
revise(219,'Use a rounded carry handle above the existing rounded rectangular camera bag.',patch=lambda s:s.replace("poly('handle',(16,16),(16,8),(32,8),(32,16))","path('handle',(16,16),[('A',(32,16),8,8,True)])"))
revise(221,'Align all four barcode bars to the same top baseline.',patch=lambda s:s.replace('(44, 9)','(44, 8)'))
revise(222,'Replace the tapered handle with one smooth half-ellipse.',patch=lambda s:remove_named(s,{'handle-left','handle-cap','handle-right','handle'})+"\n    self.add_arc('handle',(16,22),(32,22),radius_x=8,radius_y=16)\n    self.relate('connect','rim','handle')\n")
revise(232,'Recompose the bendable phone as a broad horizontal rectangle with smoothly bowed long edges.',body='''
path('body',(8,8),[('C',(40,8),(17,16),(31,16)),('A',(44,12),4,4,True),('L',(44,36)),('A',(40,40),4,4,True),('C',(8,40),(31,32),(17,32)),('A',(4,36),4,4,True),('L',(4,12)),('A',(8,8),4,4,True)],True)
line('slot',(33,22),(33,27))
''',keyshape='HRECT_L')
revise(233,'Align both blocks in one left column with a centered connector and downward arrow on the right.',body='''
poly('first',(6,6),(20,6),(20,13),(20,20),(6,20),closed=True)
poly('second',(6,28),(20,28),(20,35),(20,42),(6,42),closed=True)
poly('link',(20,13),(36,13),(36,24),(36,35),(20,35))
poly('arrow',(30,18),(36,24),(42,18))
join('link','first');join('link','second');join('arrow','link')
''')
