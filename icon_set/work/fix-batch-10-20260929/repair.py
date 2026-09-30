from author import make
make(4,'HRECT_L','The rejected unicorn had a sideways spike, square back and fused rectangular legs. Restore a single upright horn, a curved back and rounded stepped hooves; distant legs omitted for clearance.', '''
path('horse',(4,18),[('L',(14,16)),('C',(24,23),(18,16),(20,23)),('L',(34,23)),('A',(40,29),6,6,True),('L',(40,36)),('A',(36,40),4,4,True),('L',(32,40)),('L',(32,32)),('L',(22,32)),('L',(20,40)),('L',(10,40)),('L',(14,29)),('L',(17,25)),('L',(4,27)),('L',(4,18))],True)
line('horn',(14,16),(12,8));join('horn','horse')
path('tail',(40,29),[('C',(44,37),(44,29),(44,33))]);join('tail','horse')
''','Original horse silhouette; smooth circular haunch and stepped hooves, no useful exact Lucide match.')
make(10,'SQUARE','The rejected headset used small circular strap loops and a sharp V nose. Restore a wide visor with a rounded nose arch and a broader head strap.', '''
path('visor',(12,16),[('L',(36,16)),('A',(42,22),6,6,True),('L',(42,28)),('A',(36,34),6,6,True),('L',(32,34)),('C',(24,25),(28,34),(28,25)),('C',(16,34),(20,25),(20,34)),('L',(12,34)),('A',(6,28),6,6,True),('L',(6,22)),('A',(12,16),6,6,True)],True)
path('strap',(10,16),[('C',(24,6),(10,9),(16,6)),('C',(38,16),(32,6),(38,9))]);join('strap','visor')
path('lower',(12,34),[('C',(24,42),(12,40),(18,42)),('C',(36,34),(30,42),(36,40))]);join('lower','visor')
''','Original headset; symmetric rounded visor and broad head outline.')
make(14,'SQUARE','The rejected doll had a huge horizontal head and tiny pointed feet, and lost the pin. Rebalance the round sewn head over a larger outstretched body and restore a left-side pin; retain cross eyes.', '''
path('doll',(14,26),[('C',(8,16),(8,25),(8,21)),('A',(24,6),16,10,True),('A',(40,16),16,10,True),('C',(34,26),(40,21),(40,25)),('L',(42,30)),('L',(34,34)),('L',(34,42)),('L',(24,36)),('L',(14,42)),('L',(14,34)),('L',(6,30)),('L',(14,26))],True)
for x in (18,30):
 poly(f'eye-{x}-a',(x-1,15),(x,16),(x+1,17))
 poly(f'eye-{x}-b',(x-1,17),(x,16),(x+1,15));join(f'eye-{x}-a',f'eye-{x}-b')
line('pin',(6,18),(14,26));join('pin','doll')
''','Original sewn doll; two small crossed eyes, larger round-ended limbs and a pin simplified to its shaft.')
make(17,'HRECT_L','The rejected vibrating controller lost its controls and placed vibration strokes above and below. Restore side vibration arcs and a central direction pad within rounded gamepad grips.', '''
path('body',(17,8),[('L',(31,8)),('C',(36,16),(35,8),(36,12)),('L',(36,34)),('A',(30,40),6,6,True),('C',(24,32),(27,40),(28,32)),('C',(18,40),(20,32),(21,40)),('A',(12,34),6,6,True),('L',(12,16)),('C',(17,8),(12,12),(13,8))],True)
poly('pad-h',(21,20),(24,20),(27,20));poly('pad-v',(24,17),(24,20),(24,23));join('pad-h','pad-v')
path('buzz-left',(4,10),[('L',(4,24)),('L',(4,38))])
path('buzz-right',(44,10),[('L',(44,24)),('L',(44,38))])
''','Lucide gamepad-2: rounded hanging grips and crossed pad; original side vibration marks. One control retained to give the side arcs room.')
make(18,'SQUARE','The rejected watermelon was an upright bowl. Restore a diagonal slice with a thick curved rind; omit seeds to preserve clear flesh and rind at 48px.', '''
path('wedge',(6,32),[('L',(32,6)),('C',(42,24),(39,10),(42,17)),('C',(24,42),(42,35),(35,42)),('C',(6,32),(17,42),(10,39))],True)
path('rind',(12,26),[('C',(26,12),(25,37),(37,25))]);join('rind','wedge')
''','Original diagonal watermelon; symmetric quarter-turn slice and bowed rind, seeds omitted for legal separation.')
make(19,'SQUARE','The rejected Iota mark used short inward hooks. Restore four broad open sweeps with a shared rotational construction and consistent central opening.', '''
for j in range(4):
 def p(x,y):
  for _ in range(j):x,y=48-y,x
  return x,y
 self.add_bezier(f'arm-{j}',p(18,6),(p(28,6),p(33,10),p(33,18)),(p(33,21),p(32,22),p(31,23)))
''','Original Iota rotational sweeps; one curve definition rotated four times.')
make(20,'SQUARE','The rejected profile-selection mark lost its hair division. Restore a broad swept hairline within the open round head and keep the pointer lower right.', '''
path('head',(18,30),[('A',(6,18),12,12,True),('A',(30,18),12,12,True)])
path('hair',(6,18),[('C',(18,14),(11,22),(16,17)),('C',(30,18),(23,17),(26,15))]);join('head','hair')
poly('cursor',(26,25),(42,33),(35,35),(32,42),closed=True)
''','Original profile hair and pointer; circular head and shared hair attachments.')
