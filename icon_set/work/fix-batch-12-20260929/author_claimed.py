from author import *
D.clear()
add('arrow-horizontal-with-two-open-heads','HRECT_M','Steep narrow arrowheads distort the 45-degree open heads in the source. Rebalance as matched 45-degree heads.','move-horizontal: mirrored chevrons and shaft', '''
line('shaft',(4,24),(44,24))
for n,sgn in [('left',1),('right',-1)]:
 x=4 if sgn==1 else 44
 poly(n,(x+14*sgn,10),(x,24),(x+14*sgn,38));join(n,'shaft')
''')
add('bow-tie-suit','VRECT_L','Short lapels and tiny bow openings weaken the tuxedo; lengthen the V and broaden bow.','shirt: continuous jacket outline', '''
poly('bow',(12,4),(24,11),(36,4),(36,18),(24,11),(12,18),closed=True)
poly('lapels',(12,18),(24,40),(36,18));join('lapels','bow')
for s in [-1,1]:
 x=lambda v:24+s*v
 path(f'jacket{s}',(x(12),18),[('L',(x(16),22)),('C',(x(10),44),(x(16),27),(x(12),38))]);join(f'jacket{s}','bow')
line('seam',(24,40),(24,44));join('lapels','seam')
''')
add('cat-head-affection-component','SQUARE','Rejected drawing omits the heart and thought mark entirely. Restore heart above a compact cat head.','cat and heart: ear silhouette and rounded lobes', '''
path('cat',(6,26),[('L',(12,30)),('L',(18,30)),('L',(24,26)),('L',(24,33)),('A',(15,42),9,9,True),('A',(6,33),9,9,True),('L',(6,26))],True)
path('heart',(32,9),[('C',(22,11),(25,1),(22,7)),('C',(32,22),(22,15),(28,19)),('C',(42,11),(36,19),(42,15)),('C',(32,9),(42,7),(39,1))],True)
''','Thought dot and tiny nose omitted to prioritize the cat/heart composition.')
add('circular-emblem-with-banner','SQUARE','Circular emblem reduced to a narrow arch with banner across its middle. Restore circular medallion above a low banner.','award: round medallion hierarchy', '''
path('seal',(10,28),[('C',(8,20),(8,26),(8,23)),('A',(24,6),16,14,True),('A',(40,20),16,14,True),('C',(38,28),(40,23),(40,26))])
oval('inner',24,20,7,6)
poly('banner',(6,34),(42,34),(36,38),(42,42),(6,42),(12,38),closed=True)
''','Tiny folded banner tabs omitted.')
add('curved-showerhead-water-jets','SQUARE','Head is bulky and jets shrink unevenly. Use a clean diagonal dome and equal parallel jets.','shower-head: diagonal face and separate jets', '''
path('pipe',(42,42),[('L',(42,18)),('A',(30,6),12,12,False),('C',(22,10),(26,6),(24,8))])
path('head',(12,14),[('C',(22,10),(15,11),(18,10)),('C',(30,14),(25,10),(28,11)),('C',(30,30),(35,19),(35,26)),('L',(12,14))],True);join('head','pipe')
for j,(x,y) in enumerate([(12,28),(20,36)]):line(f'jet-{j}',(x,y),(x-6,y+6))
''','Three jets reduced to two equal jets to keep clear spacing.')
add('diagonal-harpoon-spear','SQUARE','Hook is too short and closes against shaft; restore long downward hook and more distinct barb.','No useful exact local Lucide match.', '''
poly('shaft',(6,42),(26,22),(34,14))
poly('tip',(34,14),(29,10),(42,6),(38,19),(34,14),closed=True);join('shaft','tip')
path('hook',(26,22),[('L',(26,36)),('A',(14,36),6,6,True)]);join('hook','shaft')
''')
add('space-station-with-paired-solar-wings','SQUARE','Dense three-cell wings and low links obscure the airy horizontal panel arrangement. Restore two-cell wings and central alignment.','satellite: balanced linked modules', '''
for x in (6,34):
 box(f'wing{x}',x,16,x+8,42)
 line(f'row{x}',(x,29),(x+8,29));join(f'row{x}',f'wing{x}')
box('upper',20,6,28,14)
box('core',20,24,28,36)
line('spine',(24,14),(24,24));join('spine','upper');join('spine','core')
line('link-left',(14,29),(20,29));line('link-right',(28,29),(34,29))
for n,a,b in [('link-left','wing6','core'),('link-right','wing34','core')]:join(n,a);join(n,b)
''','Each wing reduced from four source cells to two.')
add('square-wristwatch-solo-ac5e07e4','VRECT_L','Blank watch removes the euro symbol; restore its C-shaped curve and crossbar on a larger square face.','watch: face with centered straps', '''
box('face',8,10,40,38,4)
line('strap-upper',(24,4),(24,10));join('strap-upper','face')
line('strap-lower',(24,38),(24,44));join('strap-lower','face')
path('euro',(30,18),[('L',(25,18)),('A',(19,24),6,6,False),('A',(25,30),6,6,False),('L',(30,30))])
line('euro-bar',(16,24),(25,24));join('euro-bar','euro')
''','Straps reduced to central strokes; single-bar euro follows source.')
add('stacked-application-windows','SQUARE','Rear window disconnected at bottom left and reads as a bracket. Restore a visibly overlapping rounded rear window.','panels-top-left: rounded frame and header line', '''
box('front',6,6,32,32,3)
line('header',(6,14),(32,14));join('header','front')
path('rear',(32,14),[('L',(38,14)),('A',(42,18),4,4,True),('L',(42,38)),('A',(38,42),4,4,True),('L',(18,42)),('A',(14,38),4,4,True),('L',(14,32))]);join('rear','front')
line('rear-header',(32,24),(42,24));join('rear-header','rear');join('rear-header','front')
''')
add('tilted-square-paint-bucket','SQUARE','Tiny diamond body and squat drop lose the large pouring bucket. Enlarge and soften bucket silhouette.','paint-bucket: diagonal vessel and separate droplet', '''
path('bucket',(6,25),[('L',(23,8)),('L',(36,21)),('L',(19,38)),('L',(6,25))],True)
path('handle',(11,20),[('L',(11,12)),('A',(23,12),6,6,True),('L',(23,20))]);join('handle','bucket')
path('drop',(38,30),[('C',(42,38),(40,34),(42,36)),('A',(34,38),4,4,True),('C',(38,30),(34,36),(36,34))],True)
''')
add('traveler-beside-suitcase','SQUARE','Stick figure replaces source profile bust; restore head/neck/shoulder profile beside suitcase.','Shared human user.svg: smooth head and shoulders; luggage: rounded case', '''
path('person',(6,42),[('L',(6,29)),('C',(12,22),(6,25),(9,23)),('L',(12,19)),('C',(10,12),(10,18),(10,15)),('A',(22,12),6,6,True),('L',(25,17)),('L',(21,17)),('L',(21,22)),('C',(24,31),(23,25),(24,27)),('L',(24,42))])
box('suitcase',32,26,42,42,2)
poly('handle',(34,26),(34,18),(42,18),(42,26));join('handle','suitcase')
''','Bust profile retained; sleeve seam omitted. Continuous anatomical neck, no detached head gap.')
add('tree-with-hanging-swing-solo-b016-r02','SQUARE','Open hooked canopy no longer reads as a tree. Restore a full leafy canopy and suspended seat.','tree-deciduous: lobed canopy; source swing geometry', '''
path('canopy',(14,27),[('C',(6,20),(8,27),(6,24)),('C',(12,12),(6,15),(8,12)),('C',(23,6),(12,7),(18,6)),('C',(34,12),(29,6),(34,8)),('C',(40,20),(38,12),(40,15)),('C',(33,27),(40,25),(37,27))])
poly('trunk',(18,18),(18,30),(18,42))
line('branch',(18,30),(33,27));join('branch','trunk');join('branch','canopy')
poly('swing',(30,28),(30,42),(42,42),(42,28));join('swing','branch')
''','Minor trunk twigs omitted; swing ropes retained.')
add('treehouse-with-ladder-solo-b016-r02','SQUARE','Tree reduced to a pole with one hook; restore a leafy canopy around the left trunk.','tree-deciduous and house: canopy, roof and ladder', '''
path('canopy',(12,28),[('C',(6,20),(7,28),(6,25)),('C',(12,12),(6,15),(8,12)),('C',(24,6),(12,8),(17,6))])
line('trunk',(15,21),(15,42))
poly('house',(26,18),(34,10),(42,18),(42,26),(26,26),closed=True)
for x in (28,40):line(f'rail{x}',(x,26),(x,42));join(f'rail{x}','house')
line('rung',(28,34),(40,34));join('rung','rail28');join('rung','rail40')
''','House doorway omitted; two ladder rails and one rung retained.')
add('two-connected-sensors-before-a-tablet','SQUARE','Sensors stacked vertically instead of side by side in front of tablet; restore source arrangement.','panels-top-left: device rectangle; source sensor placement', '''
path('tablet',(22,14),[('L',(22,6)),('L',(42,6)),('L',(42,34)),('L',(38,34))])
for x in (6,22):
 box(f'sensor{x}',x,22,x+8,34,2)
 line(f'stem{x}',(x+4,34),(x+4,42));join(f'stem{x}',f'sensor{x}')
line('bus',(6,42),(42,42))
for x in (6,22):join('bus',f'stem{x}')
''','Tiny circular sensor buttons omitted; shared bus retained.')
add('two-hands-cupping-a-house','SQUARE','Single strokes read like twigs rather than hands; restore rounded finger-and-palm contours around house.','hand: rounded fingers; house: roof silhouette', '''
poly('house',(15,16),(24,6),(33,16),(33,23),(15,23),closed=True)
for s in (-1,1):
 x=lambda a:24+s*a
 path(f'hand{s}',(x(8),42),[('C',(x(10),35),(x(8),39),(x(8),38)),('L',(x(14),31)),('C',(x(18),31),(x(17),28),(x(18),29)),('L',(x(18),24)),('L',(x(18),34)),('C',(x(15),42),(x(18),37),(x(16),40))])
''','Door omitted to allow clear hand silhouettes.')
add('two-linked-wifi-routers','SQUARE','Wireless arcs omitted; boxes read as wired devices. Restore a radio arc above each diagonal router.','router: antenna and wireless arc', '''
box('router-a',6,18,22,26,2)
box('router-b',26,34,42,42,2)
line('antenna-a',(14,14),(14,18));join('antenna-a','router-a')
line('antenna-b',(34,30),(34,34));join('antenna-b','router-b')
path('wifi-a',(6,10),[('C',(22,10),(10,5),(18,5))])
path('wifi-b',(26,22),[('C',(42,22),(30,17),(38,17))])
line('link',(12,35),(18,39))
''','One radio arc per router; link remains detached as in source.')
add('two-opposing-gamepads','SQUARE','Extreme inward notches make controllers look like handles; flatten notches and deepen bodies.','gamepad-2: rounded grip silhouette', '''
for j,s in enumerate((1,-1)):
 p=lambda x,y:(x,24+s*(y-24))
 path(f'pad{j}',p(6,12),[('A',p(18,12),6,6,s==1),('L',p(30,12)),('A',p(42,12),6,6,s==1),('L',p(42,15)),('A',p(37,20),5,5,s==1),('L',p(11,20)),('A',p(6,15),5,5,s==1),('L',p(6,12))],True)
''','Tiny control dots omitted.')
add('two-piece-bikini-set','VRECT_L','Sharp low-rise bottom and angular cups differ from rounded fabric shapes; soften curves and deepen bottom.','No useful exact Lucide match; source garment contour.', '''
path('cups',(14,12),[('C',(24,22),(19,15),(22,18)),('C',(34,12),(26,18),(29,15)),('C',(40,22),(37,15),(40,19)),('C',(24,22),(40,28),(30,28)),('C',(8,22),(18,28),(8,28)),('C',(14,12),(8,19),(11,15))],True)
for x in (14,34):line(f'strap{x}',(x,4),(x,12));join(f'strap{x}','cups')
path('bottom',(8,35),[('C',(40,35),(18,37),(30,37)),('C',(28,44),(34,37),(31,41)),('L',(20,44)),('C',(8,35),(17,41),(14,37))],True)
''')
add('two-wheel-cart-with-a-marked-suitcase','SQUARE','Suitcase lost its marking and tiny solid wheels; restore one clear case mark and hollow wheels.','luggage: rounded case and paired wheels', '''
path('cart',(6,6),[('A',(14,14),8,8,True),('L',(14,27)),('A',(18,31),4,4,False),('L',(42,31))])
path('case',(22,31),[('L',(22,18)),('A',(26,14),4,4,True),('L',(38,14)),('A',(42,18),4,4,True),('L',(42,31))]);join('case','cart')
poly('handle',(26,14),(26,6),(38,6),(38,14));join('handle','case')
line('mark',(30,23),(34,23))
for x in (18,38):oval(f'wheel{x}',x,40,2,2)
''','Two source case marks reduced to one; wheel circles use approved small-circle size.')
add('upright-skeleton-key','VRECT_M','Long teeth and solid stem read as an F; restore outlined shaft integrated with bow and shorter teeth.','key-round: continuous bow-to-shaft silhouette', '''
path('key',(20,28),[('C',(10,16),(14,26),(10,22)),('A',(24,4),14,12,True),('A',(38,16),14,12,True),('C',(28,28),(38,22),(34,26)),('L',(28,40)),('A',(20,40),4,4,True),('L',(20,28))],True)
oval('hole',24,15,3,3)
for y in (30,38):line(f'tooth{y}',(28,y),(35,y));join(f'tooth{y}','key')
''')
if __name__=='__main__':
 import author
 author.D=D
 generate(sys.argv[1:])
