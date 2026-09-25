SOURCE_ICON_ID = None
SOURCE_PATH = None
AUTHOR = 'gpt-6'

def populate(design):
    design(0,'SQUARE','Outlined diagonal arrow with eight-unit arms and rounded terminals.',"""
path('arrow',(7,14),[('A',(15,8),5,5,True),('L',(34,30)),('L',(34,10)),('A',(42,10),4,4,True),('L',(42,38)),('A',(38,42),4,4,True),('L',(10,42)),('A',(10,34),4,4,True),('L',(22,34)),('L',(7,14))],True)
""",'move-down-right')
    design(1,'VRECT_M','Narrow descending zigzag with extended downward shaft and open head.',"""
poly('shaft',(16,4),(16,12),(38,12),(10,28),(24,28),(24,44))
poly('head',(14,34),(24,44),(34,34));join('shaft','head')
""",'move-up')
    design(2,'SQUARE','Regular data ticks and mirrored right U loops surround a horizontal arrow.',"""
for x in (6,14,22):
 line(f'top-{x}',(x,6),(x,10));line(f'bottom-{x}',(x,38),(x,42))
path('upper',(30,6),[('L',(30,8)),('A',(42,8),6,6,False),('L',(42,6))])
path('lower',(30,42),[('L',(30,40)),('A',(42,40),6,6,True),('L',(42,42))])
line('shaft',(6,24),(34,24));poly('head',(26,19),(34,24),(26,29));join('shaft','head')
""",'move-down-right')
    design(3,'SQUARE','Equal upward arrowheads with separated tips and tangent semicircular U return.',"""
path('u',(12,6),[('L',(12,30)),('A',(36,30),12,12,False),('L',(36,6))])
for x in (12,36):
 poly(f'head-{x}',(x-6,12),(x,6),(x+6,12));join('u',f'head-{x}')
""",'move-up')
    design(4,'VRECT_L','Crescent with circular outer bulge, concave inner face and intentional pointed cusps.',"""
path('crescent',(8,8),[('A',(20,4),20,20,True),('A',(40,24),20,20,True),('A',(20,44),20,20,True),('A',(8,40),20,20,True),('A',(8,8),18,16,False)],True)
""",'moon')
    design(5,'SQUARE','Steep mountain with curved summit and snow contour, falling snowballs and motion.',"""
path('slope',(6,18),[('C',(14,10),(8,4),(10,4)),('L',(20,26)),('L',(26,42))])
path('snow',(8,32),[('C',(14,28),(10,28),(12,27)),('C',(20,26),(17,30),(18,28))]);join('snow','slope')
circle('large-snow',36,26,6);circle('small-snow',39,9,3)
line('motion',(24,6),(26,10))
""",'mountain')
    design(6,'VRECT_L','Broad inverted ribbon meets the shoulders of an enlarged circular medal.',"""
circle('medal',24,32,12)
poly('ribbon',(16,23),(8,4),(40,4),(32,23));join('ribbon','medal')
""",'medal')
    design(7,'HRECT_L','Round baby face with side ears and smooth inward curl; no invented facial features.',"""
path('face',(8,20),[('C',(24,8),(9,12),(15,8)),('C',(40,20),(33,8),(39,12)),('A',(40,28),4,4,True),('C',(24,40),(39,36),(33,40)),('C',(8,28),(15,40),(9,36)),('A',(8,20),4,4,True)],True)
path('curl',(28,9),[('L',(28,16)),('A',(20,16),4,4,True)]);join('curl','face')
""",'baby; human_ref/user.svg')
    design(8,'SQUARE','Sloping sleeves, rounded neckline and mirrored curved leg openings.',"""
path('onesie',(18,6),[('A',(30,6),6,6,False),('L',(34,6)),('L',(42,12)),('L',(39,20)),('L',(34,18)),('L',(34,32)),('A',(28,42),10,10,False),('L',(20,42)),('A',(14,32),10,10,False),('L',(14,18)),('L',(9,20)),('L',(6,12)),('L',(14,6)),('L',(18,6))],True)
""",'shirt')
    design(9,'VRECT_M','Upright rounded battery and rounded terminal share shoulder nodes.',"""
path('body',(14,12),[('L',(18,12)),('L',(30,12)),('L',(34,12)),('A',(38,16),4,4,True),('L',(38,40)),('A',(34,44),4,4,True),('L',(14,44)),('A',(10,40),4,4,True),('L',(10,16)),('A',(14,12),4,4,True)],True)
path('terminal',(18,12),[('L',(18,8)),('A',(22,4),4,4,True),('L',(26,4)),('A',(30,8),4,4,True),('L',(30,12))]);join('terminal','body')
""",'battery')
    for i in (10,11):
        design(i,'HRECT_M','Wide battery body and centered rounded terminal retain the reference aspect.',"""
path('body',(8,10),[('L',(32,10)),('A',(36,14),4,4,True),('L',(36,18)),('L',(36,30)),('L',(36,34)),('A',(32,38),4,4,True),('L',(8,38)),('A',(4,34),4,4,True),('L',(4,14)),('A',(8,10),4,4,True)],True)
path('terminal',(36,18),[('L',(41,18)),('A',(44,21),3,3,True),('L',(44,27)),('A',(41,30),3,3,True),('L',(36,30))]);join('terminal','body')
""",'battery')
    design(12,'HRECT_L','Wide battery with rounded terminal and centered downward charging lead.',"""
path('body',(8,8),[('L',(32,8)),('A',(36,12),4,4,True),('L',(36,16)),('L',(36,28)),('A',(32,32),4,4,True),('L',(20,32)),('L',(8,32)),('A',(4,28),4,4,True),('L',(4,12)),('A',(8,8),4,4,True)],True)
path('terminal',(36,16),[('L',(41,16)),('A',(44,19),3,3,True),('L',(44,25)),('A',(41,28),3,3,True),('L',(36,28))]);join('terminal','body')
line('cable',(20,32),(20,40));join('cable','body')
""",'battery')
    design(13,'HRECT_M','Battery outline integrates a rounded terminal; interior rectangular charge block is centered vertically.',"""
path('outline',(8,10),[('L',(32,10)),('A',(36,14),4,4,True),('L',(36,18)),('L',(41,18)),('A',(44,21),3,3,True),('L',(44,27)),('A',(41,30),3,3,True),('L',(36,30)),('L',(36,34)),('A',(32,38),4,4,True),('L',(8,38)),('A',(4,34),4,4,True),('L',(4,14)),('A',(8,10),4,4,True)],True)
poly('charge',(13,19),(24,19),(24,29),(13,29),closed=True)
""",'battery')
    design(14,'HRECT_L','Round batting shell, projecting brim and smooth ear guard with visible circular vent.',"""
path('shell',(40,26),[('A',(4,26),18,18,False),('C',(18,40),(4,34),(8,40)),('C',(29,29),(32,40),(34,34)),('C',(28,26),(27,27),(27,26)),('L',(40,26))],True)
line('brim',(40,26),(44,26));join('brim','shell')
circle('ear-vent',18,28,3)
""",'moon')
    design(15,'VRECT_L','Three battlements, tapered tower, closed arched window and broad plinth retain fortress identity.',"""
poly('crown',(8,12),(8,4),(14,4),(14,10),(20,10),(20,4),(28,4),(28,10),(34,10),(34,4),(40,4),(40,12),(37,16),(11,16),(8,12))
poly('tower',(11,16),(10,36),(38,36),(37,16));join('tower','crown')
poly('plinth',(8,36),(10,36),(38,36),(40,36),(40,44),(8,44),closed=True);join('plinth','tower')
path('window',(20,30),[('L',(20,27)),('A',(28,27),4,4,True),('L',(28,30)),('L',(20,30))],True)
""",'castle')
    for i,tilt in ((16,False),(17,True)):
        design(i,'VRECT_L','Distinct bitcoin and dollar symbols sit above a '+('tilted' if tilt else 'level')+' beam and closed triangular fulcrum.',f"""
path('bitcoin',(8,6),[('L',(16,6)),('A',(16,14),4,4,True),('A',(16,22),4,4,True),('L',(8,22)),('L',(8,14)),('L',(8,6))],True)
line('bitcoin-bar',(8,14),(16,14));join('bitcoin-bar','bitcoin')
line('bitcoin-tick',(12,4),(12,6));join('bitcoin-tick','bitcoin')
line('bitcoin-foot',(12,22),(12,24));join('bitcoin-foot','bitcoin')
dy={4 if tilt else 0}
path('dollar',(40,6+dy),[('L',(34,6+dy)),('C',(34,14+dy),(26,6+dy),(26,13+dy)),('C',(34,22+dy),(42,15+dy),(42,22+dy)),('L',(28,22+dy))])
line('dollar-top',(34,4+dy),(34,6+dy));join('dollar-top','dollar')
line('dollar-bottom',(34,22+dy),(34,24+dy));join('dollar-bottom','dollar')
poly('beam',(8,{30 if tilt else 32}),(24,{34 if tilt else 32}),(40,{38 if tilt else 32}))
poly('fulcrum',(24,{34 if tilt else 32}),(16,44),(32,44),closed=True);join('beam','fulcrum')
""",'scale')
    design(18,'SQUARE','Open box uses coherent diamond opening, four outward flaps, vertical front seam and closed base.',"""
poly('opening',(10,18),(24,12),(38,18),(24,26),closed=True)
poly('back-left',(10,18),(6,10),(18,6),(24,12));join('back-left','opening')
poly('back-right',(24,12),(30,6),(42,10),(38,18));join('back-right','opening')
poly('front-left',(10,18),(6,26),(18,32),(24,26));join('front-left','opening')
poly('front-right',(24,26),(30,32),(42,26),(38,18));join('front-right','opening')
poly('body',(10,28),(10,36),(24,42),(38,36),(38,28));join('body','front-left');join('body','front-right')
line('seam',(24,26),(24,42));join('seam','opening');join('seam','body')
""",'package-open; box')
    design(19,'HRECT_L','Perspective cube retains three faces; three complete outward arrows replace detached chevrons.',"""
poly('cube',(16,28),(24,24),(32,28),(32,36),(24,40),(16,36),closed=True)
poly('cube-top',(16,28),(24,32),(32,28));join('cube-top','cube')
line('cube-seam',(24,32),(24,40));join('cube-seam','cube');join('cube-seam','cube-top')
line('up',(24,8),(24,16));poly('up-head',(20,12),(24,8),(28,12));join('up','up-head')
line('left',(4,20),(12,20));poly('left-head',(8,16),(4,20),(8,24));join('left','left-head')
line('right',(36,20),(44,20));poly('right-head',(40,16),(44,20),(40,24));join('right','right-head')
""",'box; move-up')
