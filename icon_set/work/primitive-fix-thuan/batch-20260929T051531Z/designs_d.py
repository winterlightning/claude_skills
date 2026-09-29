author(8,'''
# Robot dog faces left: rounded mechanical head, capsule torso, two bent legs and an upturned tail.
self.path('head',(4,7),('L',(15,7)),('A',(21,13),6,6,True),('L',(21,23)),('A',(15,18),6,6,True),('L',(15,7)))
self.add_arc('muzzle',(4,7),(15,16),radius_x=11,radius_y=9,sweep=False)
self.path('body',(19,23),('L',(34,23)),('A',(41,30),7,7,True),('L',(40,34)),('L',(36,34)),('L',(31,34)),('L',(23,34)),('L',(18,34)),('A',(12,29),6,6,True),('A',(19,23),7,6,True),closed=True)
self.path('tail',(35,23),('A',(44,18),10,10,False),('C',(40,29),(44,24),(44,27)))
self.path('front-leg',(20,31),('L',(23,37)),('L',(19,44)),('L',(8,44)),('A',(12,40),4,4,True),('L',(16,40)),('L',(18,34)))
self.path('rear-leg',(32,31),('L',(36,38)),('L',(32,44)),('L',(25,44)),('A',(29,40),4,4,True),('L',(30,40)),('L',(31,34)))
self.relate('connect','body','head');self.relate('connect','body','tail');self.relate('connect','body','front-leg');self.relate('connect','body','rear-leg');self.relate('connect','head','muzzle')
''','SQUARE','The rejected robot dog had angular stick legs, a triangular face and a diagonal tail. The source has a rounded mechanical head, capsule body, articulated feet and a curved tail.',
 'Restore rounded muzzle and head casing, horizontal capsule torso, two bent outlined legs with feet, and an upturned curved tail.',
 'Lucide dog provides rounded animal contour principles; supplied robot-dog reference defines mechanical side silhouette.',
 'Small body seams omitted.',
 exception_reason='Mechanical body joins and articulated feet require compact interior openings. Retain the complete robotic dog under user-authorized visual exception with uniform4px strokes.')
author(9,'''
# No original was available; use rejected horse as meaning reference, then restore missing equine anatomy.
self.path('horse',(12,23),('L',(5,25)),('A',(4,19),4,4,True),('L',(14,11)),('L',(15,5)),('L',(20,10)),('L',(23,18)),('L',(33,18)),('A',(39,24),6,6,True),('A',(34,29),5,5,True),('L',(19,29)),('L',(16,22)),('L',(12,23)),closed=True)
self.add_line('mane',(18,11),(23,18));self.relate('connect','horse','mane')
self.path('tail',(39,23),('C',(44,30),(43,22),(44,26)))
self.path('front-support',(21,29),('L',(16,39)))
self.path('rear-support',(32,29),('L',(35,39)))
self.path('rocker',(4,36),('C',(24,44),(7,46),(16,44)),('C',(44,36),(32,44),(41,46)))
self.relate('connect','horse','tail');self.relate('connect','horse','front-support');self.relate('connect','horse','rear-support')
''','SQUARE','No original was available; the supplied reference is the rejected drawing. Its triangular head and flat rail obscure the rocking-horse shape.',
 'Add a distinct ear and muzzle, a curved chest and hindquarters, hanging tail, angled supports and a pronounced bowed rocker; preserve the left-facing toy.',
 'No useful Lucide rocking-horse match; supplied current drawing establishes the horse-on-rocker concept.',
 'Tiny eye omitted to avoid a solid head; the muzzle and ear supply recognition.',
 exception_reason='Horse anatomy and support-to-rocker relationships need compact spacing. User authorized visual exception for the complete toy silhouette at48px.')
author(10,'''
# Curved diagonal blade, true crossguard and hilt; separate poison drop and victim head silhouette.
self.path('blade',(12,29),('L',(32,5)),('C',(23,25),(33,14),(28,21)),('L',(17,32)))
self.add_line('guard',(7,25),(23,37))
self.path('handle',(11,28),('L',(5,36)),('A',(11,42),4,4,False),('L',(18,33)))
self.path('poison-drop',(40,14),('C',(35,24),(39,18),(35,20)),('A',(45,24),5,5,False),('C',(40,14),(45,20),(41,18)),closed=True)
self.path('victim',(30,44),('L',(30,39)),('A',(27,34),8,8,True),('A',(43,34),8,8,True),('A',(40,39),8,8,True),('L',(40,44)))
self.relate('connect','blade','guard');self.relate('connect','handle','guard')
''','SQUARE','The rejected poisonous dagger was a triangular spike and the victim cue became a small arch. The source has a curved blade, handle and guard, a poison droplet and a head silhouette.',
 'Restore a long curved dagger with a separate hilt and crossguard, an upright poison drop and rounded head silhouette at lower right.',
 'Lucide sword: distinct blade, crossguard and hilt; original controls curved blade and two right-side modifiers.',
 'Facial detail omitted as in source.',
 exception_reason='Three meaning-bearing elements require compact spacing and narrow blade/handle openings. User authorized the complete poisonous-dagger composition as a visual exception.')
author(11,'''
# The two rides share a ground plane; thin structural members preserve open supports.
self.path('coaster-track',(4,29),('C',(17,22),(4,13),(12,15)),('C',(42,39),(26,31),(26,45)))
self.add_line('ground',(4,44),(44,44))
for name,a,b in [('support-left',(4,29),(4,44)),('support-peak',(11,19),(11,44)),('support-middle',(20,27),(20,44)),('support-low',(29,37),(29,44)),('support-right',(42,39),(42,44))]:self.add_line(name,a,b)
self.circle('wheel',33,15,11)
self.circle('hub',33,15,2)
# Four paired spokes, interrupted at the hub.
for name,a,b in [('north',(33,4),(33,13)),('south',(33,17),(33,26)),('west',(22,15),(31,15)),('east',(35,15),(44,15)),('nw',(25,7),(31,13)),('ne',(35,13),(41,7)),('sw',(25,23),(31,17)),('se',(35,17),(41,23))]:self.add_line('spoke-'+name,a,b)
self.add_polyline('wheel-stand',(27,36),(33,22),(39,36))
''','SQUARE','The rejected amusement-park scene had a heavy four-spoke wheel and one thick arch, losing the flowing coaster track and its repeated supports.',
 'Restore the roller-coaster rise and dip on multiple supports beside an eight-spoke Ferris wheel and tapered stand; ground plane unifies the two rides.',
 'Lucide roller-coaster and ferris-wheel: flowing track, repeated supports, radial wheel geometry; original controls two-ride composition.',
 'Tiny passenger cabins omitted, matching the source spoke-wheel abstraction.',
 exception_reason='Complete amusement-park scene requires close structural overlaps, compact spoke openings and repeated supports. User authorized visual exception after48px review.')
author(14,'''
# Central T handle, straight spindle and broad valve base; arrows curl around both sides.
self.path('handle',(20,12),('L',(30,12)),('A',(30,18),3,3,True),('L',(20,18)),('A',(20,12),3,3,True),closed=True)
self.add_line('spindle',(25,18),(25,36))
self.path('mount',(18,40),('L',(18,37)),('A',(21,34),3,3,True),('L',(29,34)),('A',(32,37),3,3,True),('L',(32,40)))
self.path('base',(9,44),('L',(9,40)),('L',(41,40)),('L',(41,44)))
self.path('left-turn',(12,5),('C',(9,31),(0,11),(2,24)))
self.add_polyline('left-arrow',(4,31),(9,31),(8,26))
self.path('right-turn',(38,32),('C',(39,6),(49,26),(48,13)))
self.add_polyline('right-arrow',(44,6),(39,6),(40,11))
self.relate('connect','handle','spindle');self.relate('connect','mount','spindle');self.relate('connect','base','mount');self.relate('connect','left-turn','left-arrow');self.relate('connect','right-turn','right-arrow')
''','SQUARE','The rejected valve replaced the T handle with an oval and omitted its raised mount, while the rotation arrows were disconnected hooks.',
 'Restore horizontal T handle, straight spindle, stepped base and two opposing curved arrows with clear arrowheads.',
 'No useful Lucide valve match; supplied reference controls the T handle and opposing rotation directions.',
 exception_reason='Compact arrowheads, handle opening and stepped mount need local spacing below MIC. User authorized the full mechanical symbol at48px with4px strokes.')
