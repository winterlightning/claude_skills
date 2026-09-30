from author import make
make(1,'CIRCLE','The rejected two wind strokes were separated almost the full canvas height. Bring the two unequal horizontal lines back together to match the simple reference.', '''
line('long',(5,18),(43,18))
line('short',(5,30),(32,30))
''','Original two-line wind mark; radial envelope preserves its naturally shallow proportions.')
make(2,'HRECT_L','The rejected water drops were triangular wedges. Restore two rounded teardrops and the upper-right curled wind stroke.', '''
path('drop-a',(12,8),[('C',(4,20),(8,14),(4,16)),('A',(20,20),8,6,False),('C',(12,8),(20,16),(16,12))],True)
path('drop-b',(32,24),[('C',(24,34),(28,28),(24,31)),('A',(40,34),8,6,False),('C',(32,24),(40,31),(36,28))],True)
path('wind',(28,16),[('L',(38,16)),('A',(44,10),6,6,False),('C',(40,8),(44,8),(42,8))])
''','Lucide wind original and atoms inform the curling run; original rounded droplets retained.')
make(3,'HRECT_L','The rejected bottle was square at the base and the glass was tiny and rectangular. Restore a wider stemmed bowl beside a rounded wine bottle.', '''
path('bottle',(8,8),[('L',(16,8)),('L',(16,20)),('C',(20,27),(16,24),(20,23)),('L',(20,36)),('A',(16,40),4,4,True),('L',(8,40)),('A',(4,36),4,4,True),('L',(4,27)),('C',(8,20),(4,23),(8,24)),('L',(8,8))],True)
path('bowl',(28,20),[('L',(44,20)),('L',(44,24)),('A',(36,32),8,8,True),('A',(28,24),8,8,True),('L',(28,20))],True)
line('stem',(36,32),(36,40));join('stem','bowl')
poly('base',(30,40),(36,40),(42,40));join('base','stem')
''','Lucide wine circular bowl and stem; source bottle-and-glass arrangement.')
make(4,'SQUARE','The rejected winged lion resembled a rabbit with angular ears. Restore curved outspread wings above a rounded mane and central muzzle.', '''
path('mane',(12,30),[('A',(36,30),12,8,True),('A',(12,30),12,12,True)],True)
poly('nose',(22,32),(24,33),(26,32))
path('wing-left',(20,14),[('C',(6,6),(20,10),(12,8)),('C',(14,14),(6,11),(9,14))])
path('wing-right',(28,14),[('C',(42,6),(28,10),(36,8)),('C',(34,14),(42,11),(39,14))])
''','Original winged lion; mirrored swept wings and rounded mane, no useful exact Lucide match.')
make(5,'SQUARE','The rejected totem became a wide head with small slanted arms. Restore a tall narrow pole with a rounded crown and broad horizontal wings.', '''
path('pole',(18,12),[('A',(30,12),6,6,True),('L',(30,42)),('L',(18,42)),('L',(18,12))],True)
path('wing-left',(18,18),[('L',(6,18)),('A',(14,26),8,8,False),('L',(18,26))]);join('wing-left','pole')
path('wing-right',(30,18),[('L',(42,18)),('A',(34,26),8,8,True),('L',(30,26))]);join('wing-right','pole')
''','Original totem; narrow crown and paired quarter-circle wings. Tiny face marks omitted.')
make(6,'HRECT_L','The rejected winged lion had a blocky single wing, a plain rounded head and squared limbs. Restore a swept wing, a scalloped mane and a rounded muzzle with stepping feet.', '''
path('lion',(10,28),[('L',(6,36)),('L',(10,40)),('L',(18,40)),('L',(16,32)),('L',(28,32)),('L',(34,40)),('L',(44,40)),('L',(38,32)),('C',(44,24),(42,32),(44,29)),('C',(38,16),(44,19),(43,16)),('C',(30,24),(30,16),(30,18)),('L',(22,24)),('L',(22,16)),('C',(4,8),(22,11),(13,11)),('C',(10,28),(5,18),(8,23))],True)
path('tail',(10,28),[('C',(4,31),(5,26),(4,28))]);join('tail','lion')
''','Original winged lion; swept wing and rounded head; fine mane scallops and distant legs reduced.')
make(7,'VRECT_M','The rejected comb looked like an E with squared spine corners. Restore a rounded vertical spine and evenly spaced teeth with consistent lengths.', '''
path('spine',(38,4),[('L',(14,4)),('A',(10,8),4,4,False),('L',(10,40)),('A',(14,44),4,4,False),('L',(38,44))])
for i,y in enumerate((14,24,34)):
 line(f'tooth-{i}',(10,y),(38,y));join(f'tooth-{i}','spine')
''','Original styling comb; one rounded spine and an evenly spaced tooth series.')
make(8,'HRECT_L','The rejected pirate had a straight brim and no smile. Restore a curved straw-hat brim, rounded crown, a wink and a small smiling mouth.', '''
path('crown',(10,18),[('A',(24,8),14,10,True),('A',(38,18),14,10,True)])
path('brim',(4,18),[('C',(24,22),(8,22),(16,22)),('C',(44,18),(32,22),(40,22))]);join('crown','brim')
path('jaw',(8,21),[('C',(24,40),(8,32),(14,40)),('C',(40,21),(34,40),(40,32))]);join('jaw','brim')
self.add_dot('eye',(18,30));line('wink',(29,30),(32,29))
''','Original straw hat and wink; curved brim and balanced circular-looking jaw. Smile added in a later spacing pass if room permits.')
make(9,'SQUARE','The rejected USB mouse had a short inverted-U cable and a blocklike plug. Restore a large looping cable around the rounded mouse and an angled USB connector.', '''
box('mouse',21,18,39,42,9)
line('wheel',(30,26),(30,30))
path('cable',(30,18),[('L',(30,14)),('C',(18,6),(30,6),(24,6)),('C',(6,22),(8,6),(6,12)),('C',(14,42),(6,32),(8,40))])
poly('plug',(14,42),(22,38),(18,30),(10,34),closed=True);join('plug','cable')
''','Lucide mouse rounded capsule and scroll mark; original looping USB cable.')
earbuds='''
path('case',(6,28),[('L',(42,28)),('L',(42,34)),('A',(34,42),8,8,True),('L',(14,42)),('A',(6,34),8,8,True),('L',(6,28))],True)
path('left-bud',(18,28),[('L',(18,12)),('A',(6,12),6,6,False),('A',(18,12),6,6,False)])
path('right-bud',(30,28),[('L',(30,12)),('A',(42,12),6,6,True),('A',(30,12),6,6,True)])
join('left-bud','case');join('right-bud','case')
poly('charge',(26,32),(22,35),(26,35),(22,38))
'''
make(10,'SQUARE','The rejected earbuds were plain circles on stems and lacked the charging indicator. Restore opposed rounded earbud heads and a charging zigzag in the case.',earbuds,'Original earbud case; paired mirrored heads and rounded charging box.')
make(11,'SQUARE','The rejected earbuds were split semicircles with a plain status dot. Restore fuller opposed earbud heads and a charging zigzag inside the rounded case.',earbuds,'Original earbud case; mirrored earbuds and central charging mark.')
