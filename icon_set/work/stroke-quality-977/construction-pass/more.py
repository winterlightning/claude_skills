from repair import *
patch('periodic-table','''
self.add_polyline('table',(4,8),(14,8),(14,20),(34,20),(34,8),(44,8),(44,20),(44,30),(44,40),(34,40),(14,40),(4,40),(4,30),(4,20),closed=True)
self.add_polyline('row',(4,30),(14,30),(34,30),(44,30))
for side,x in [('left',14),('right',34)]:
 self.add_polyline(side+'-column',(x,20),(x,30),(x,40));self.relate('connect',side+'-column','row');self.relate('connect',side+'-column','table')
self.add_line('left-cell',(4,20),(14,20));self.add_line('right-cell',(34,20),(44,20))
for part in ['row','left-cell','right-cell']:self.relate('connect',part,'table')
''','HRECT_L; a shared cell grid owns both towers, rows and exact column junctions; irregular top cap and rounded detours removed.')
patch('shopping-basket-e572b2c4','''
self.add_polyline('rim',(4,18),(8,18),(40,18),(44,18))
path('basket',(8,18),[('L',(10,35)),('C',(10+4/17,37),(12,40),(16,40)),('L',(32,40)),('C',(36,40),(38-4/17,37),(38,35)),('L',(40,18))])
path('handle',(8,18),[('C',(11,12),(12,8),(18,8)),('L',(30,8)),('C',(36,8),(37,12),(40,18))])
self.relate('connect','basket','rim');self.relate('connect','handle','rim');self.relate('connect','basket','handle')
''','HRECT_L; mirrored basket sides, tangent bottom corners and a smooth shared handle; no mismatched fitted corner pieces.')
patch('lab-tube-experiment','''
path('tube',(10,14),[('L',(10,30)),('A',(24,44),14,14,False),('A',(38,30),14,14,False),('L',(38,14))])
self.add_polyline('rim',(10,14),(10,8),(8,4),(40,4),(38,8),(38,14))
self.add_line('liquid',(10,14),(38,14))
self.relate('connect','tube','rim');self.relate('connect','tube','liquid');self.relate('connect','rim','liquid')
''','VRECT_L; true semicircular tube bottom, parallel walls and matching lip bevels.')
patch('supermarket','''
self.add_polyline('body',(8,24),(8,42),(20,42),(28,42),(40,42),(40,24))
self.add_polyline('left-step',(6,24),(8,24),(16,24),(16,15))
self.add_polyline('right-step',(42,24),(40,24),(32,24),(32,15))
self.add_polyline('roof',(14,15),(16,15),(24,15),(32,15),(34,15))
self.add_polyline('flag',(24,15),(24,6),(32,6))
path('door',(20,42),[('L',(20,34)),('A',(24,30),4,4,True),('A',(28,34),4,4,True),('L',(28,42))])
for side in ['left-step','right-step']:self.relate('connect',side,'body');self.relate('connect',side,'roof')
self.relate('connect','roof','flag');self.relate('connect','door','body')
''','SQUARE; symmetric building tiers and door, with a straight flag and exact roof junctions.')
patch('virtual-coin-crypto-waves','''
self.add_polyline('diamond',(24,6),(42,24),(24,42),(6,24),closed=True)
''','SQUARE; four equal straight diamond sides replace mismatched tiny corner arcs.')
patch('pen','''
self.add_polyline('barrel',(6,42),(11,31),(35,6),(42,13),(17,38),closed=True)
# The seam ends on the exact diagonal barrel edges.
self.add_line('seam',(26,15),(33,22));self.relate('connect','seam','barrel')
''','SQUARE; straight barrel sides and exact cap seam; the tip has two clean deliberate edges.','Lucide pencil: coherent barrel and shared seam endpoints.')
for id in ['shapes','shapes-design']:
 patch(id,'''
self.add_polyline('square',(19,19),(32,19),(42,19),(42,42),(19,42),(19,32),closed=True)
path('circle',(32,19),[('A',(19,6),13,13,False),('A',(6,19),13,13,False),('A',(19,32),13,13,False)])
self.relate('connect','circle','square')
''','SQUARE; true circle ends exactly on the foreground square; one-unit connector stubs removed.','Lucide shapes: a shared overlap boundary between the circle and square.')
for id in ['glass','glass-drinks']:
 patch(id,'''
path('bowl',(8,12),[('L',(8,4)),('L',(40,4)),('L',(40,12)),('A',(24,28),16,16,True),('A',(8,12),16,16,True)],True)
self.add_line('stem',(24,28),(24,44));self.add_polyline('base',(14,44),(24,44),(34,44))
self.relate('connect','stem','bowl');self.relate('connect','stem','base')
''','VRECT_L; symmetric circular bowl with its stem attached at the exact bottom extreme.')
patch('playstation-vr','''
path('headband',(6,26),[('A',(24,8),18,18,True),('A',(42,26),18,18,True)])
path('visor',(4,32),[('C',(4,29),(4,28),(6,26)),('C',(10,22),(17,21),(24,21)),
 ('C',(31,21),(38,22),(42,26)),('C',(44,28),(44,29),(44,32)),
 ('C',(44,36),(43,40),(39,40)),('C',(34,40),(30,38),(24,38)),
 ('C',(18,38),(14,40),(9,40)),('C',(5,40),(4,36),(4,32))],True)
self.relate('connect','headband','visor')
''','HRECT_L; true circular headband meets explicit visor nodes; both visor halves share matching tangent curves.')
patch('icon-3-d-box-corner','''
self.add_polyline('top',(24,14),(36,21),(24,28),(12,21),closed=True)
self.add_polyline('bottom',(12,21),(12,35),(24,42),(36,35),(36,21))
self.add_line('front',(24,28),(24,42))
self.add_line('upper-axis',(24,14),(24,6))
self.add_line('left-axis',(12,35),(6,39));self.add_line('right-axis',(36,35),(42,39))
self.relate('connect','top','bottom');self.relate('connect','front','top');self.relate('connect','front','bottom');self.relate('connect','upper-axis','top')
self.relate('connect','left-axis','bottom');self.relate('connect','right-axis','bottom')
''','SQUARE; all cube edges meet shared integer vertices; shortened side walls repaired.')
plant='''
path('leaves',(24,36),[('C',(14,36),(6,29),(6,20)),('C',(12,21),(16,23),(18,26)),
 ('C',(16,18),(20,10),(24,6)),('C',(28,10),(32,18),(30,26)),
 ('C',(32,23),(36,21),(42,20)),('C',(42,29),(34,36),(24,36))],True)
self.add_line('stem',(24,36),(24,42));self.relate('connect','stem','leaves')
'''
for id in ['plant','plant-f082c27d','plant-nature']:
 patch(id,plant,'SQUARE; mirrored three-lobe leaves and an exact stem attachment; fitted fragments at the top tip removed.')
for id in ['plant-61cad875','plant-93a59e45','plant-a3a09538']:
 patch(id,plant+'''
path('veins',(18,26),[('C',(19,30),(22,34),(24,36)),('C',(26,34),(29,30),(30,26))])
self.relate('connect','veins','leaves');self.relate('connect','veins','stem')
''','SQUARE; mirrored leaf curves with shared vein/stem nodes; no duplicate tip or one-unit attachment fragments.')
save()
