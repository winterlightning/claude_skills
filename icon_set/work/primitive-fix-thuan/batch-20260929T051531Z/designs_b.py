author(18,'''
# Tomato body is broad and round, with a pointed calyx rather than two leaf-like wings.
self.path('fruit',(13,16),('C',(4,29),(6,19),(4,24)),('C',(24,44),(4,39),(13,44)),('C',(44,29),(35,44),(44,39)),('C',(35,16),(44,24),(42,19)))
self.path('calyx',(24,13),('C',(10,14),(19,9),(14,10)),('L',(16,16)),('L',(14,22)),('L',(22,19)),('L',(24,26)),('L',(28,19)),('L',(35,22)),('L',(33,16)),('L',(39,14)),('C',(24,13),(34,10),(29,10)),closed=True)
self.add_line('stem',(24,4),(24,13));self.relate('connect','calyx','stem')
self.add_arc('highlight',(31,37),(37,30),radius_x=11,radius_y=11,sweep=False)
''','SQUARE','The rejected tomato had a simple two-leaf top and no pointed star calyx or skin highlight, so it resembled a generic round fruit.',
 'Round tomato body with a pointed five-lobed calyx, upright stem and one curved skin highlight; maintain the source broad natural silhouette.',
 'No useful local Lucide tomato match; source establishes star-shaped calyx and round body.',
 exception_reason='The calyx has tightly connected pointed leaves and compact fruit junctions. Preserve these identifying details with4px strokes using the authorized visual exception.')
author(19,'''
# Seven rounded berries, with rear contours interrupted behind the central foreground berry.
self.circle('center-berry',24,22,7)
self.path('upper-left',(18,19),('C',(8,17),(12,24),(6,22)),('C',(21,16),(7,6),(20,6)))
self.path('upper-right',(27,16),('C',(41,17),(28,6),(41,6)),('C',(30,21),(43,23),(36,25)))
self.path('left-middle',(17,24),('C',(11,37),(6,25),(5,34)),('C',(23,29),(20,42),(24,35)))
self.path('right-middle',(29,27),('C',(36,38),(38,24),(43,32)),('C',(23,29),(31,42),(22,38)))
self.path('far-right',(41,21),('C',(42,34),(49,23),(47,32)),('L',(38,35)))
self.path('bottom',(17,38),('C',(30,38),(13,49),(34,49)))
self.path('stem',(24,15),('C',(28,4),(23,10),(25,6)))
self.relate('connect','center-berry','stem')
''','SQUARE','The rejected drawing was a scalloped flower with a dot. The reference is a cluster of seven round fruit segments with a curved stem.',
 'Restore seven individual round fruit forms in the source cluster, using occluded rear contours around the foreground central berry and a curved stem.',
 'Lucide grape original and atomic-debug: independently legible round berries; supplied source controls seven-fruit arrangement.',
 exception_reason='Adjacent fruit contours intentionally touch or overlap as a cluster. Separate rounded interiors remain readable; organic cluster bounds and local gaps use the authorized visual exception.')
author(15,'''
# Hen is a single round-bellied silhouette; upright tail, comb, beak and two feet carry identity.
self.path('hen',(6,15),('C',(23,21),(12,20),(17,23)),('C',(29,13),(27,21),(25,16)),('C',(39,12),(29,7),(35,8)),('L',(44,16)),('L',(39,19)),('L',(39,25)),('C',(24,38),(39,33),(33,38)),('C',(6,23),(12,38),(6,32)),('L',(6,15)),closed=True)
self.add_arc('comb',(29,10),(37,10),radius_x=4,radius_y=6,sweep=True)
self.add_arc('wattle',(39,19),(38,26),radius_x=3,radius_y=4,sweep=True)
self.path('left-foot',(20,38),('L',(20,44)),('L',(17,44)))
self.path('right-foot',(28,38),('L',(28,44)),('L',(31,44)))
self.relate('connect','hen','comb');self.relate('connect','hen','wattle');self.relate('connect','hen','left-foot');self.relate('connect','hen','right-foot')
''','SQUARE','The rejected hen lost its comb, wattle and articulated feet and resembled a generic bathtub bird.',
 'Restore a round-bellied hen with raised tail, curved neck, comb, pointed beak, wattle and two small feet.',
 'Lucide bird: continuous bird outline and short legs; supplied reference owns round body, comb and wattle.',
 'Eye omitted as in the source to keep head details open.',
 exception_reason='Comb and wattle have compact outline gaps at48px, while attached feet and beak retain natural contacts. User authorized the complete hen silhouette as a visual exception.')
author(16,'''
self.path('bomb',(24,18),('A',(32,27),14,14,True),('A',(18,44),15,15,True),('A',(4,29),14,15,True),('A',(18,15),14,14,True),('L',(21,11)),('L',(29,16)),('L',(26,20)))
self.path('fuse',(27,14),('A',(35,9),9,9,True))
# Five detached rays around the burning fuse endpoint.
for name,a,b in [('top',(39,2),(39,5)),('upper-right',(44,7),(46,5)),('right',(44,13),(46,14)),('bottom',(39,17),(39,20)),('upper-left',(32,3),(34,5))]: self.add_line(name,a,b)
''','SQUARE','The rejected bomb had a straight stalk and a plus sign, losing the angled neck, curved fuse and radiating spark.',
 'Round bomb with a short angled neck, curved fuse and five detached spark rays, retaining the upper-right ignition detail.',
 'Lucide bomb: round body and angled fuse housing; source defines curved fuse and radiating spark.',
 exception_reason='Compact ignition rays and neck joins require local spacing below MIC. The bomb remains a clear round silhouette with4px strokes, accepted under user authorization.')
author(17,'''
# Mirrored handset lobes sit on a wide desk-phone body.
self.path('handset',(4,18),('C',(24,6),(3,8),(11,6)),('C',(44,18),(37,6),(45,8)),('A',(40,21),3,3,True),('L',(36,21)),('A',(33,18),3,3,True),('L',(33,16)),('A',(30,13),3,3,False),('L',(18,13)),('A',(15,16),3,3,False),('L',(15,18)),('A',(12,21),3,3,True),('L',(8,21)),('A',(4,18),4,3,True),closed=True)
self.path('base',(17,21),('L',(31,21)),('C',(42,37),(35,24),(42,32)),('A',(37,42),5,5,True),('L',(11,42)),('A',(6,37),5,5,True),('C',(17,21),(6,32),(13,24)),closed=True)
self.circle('rotary-dial',24,31,6)
''','HRECT_L','The rejected phone reduced the handset to an open arc and the rotary dial to a small dot-like hole. The source shows a complete receiver with two earpieces and a broad circular dial.',
 'Restore a complete symmetric handset with rounded earpieces above a softly tapered desk base and an enlarged round dial.',
 'Lucide phone: rounded receiver ends and coherent handset contour; supplied rotary-phone reference owns desk base and dial.',
 exception_reason='Complete handset earpieces and large rotary dial need compact openings and close body spacing. Native-size legibility is prioritized under the user-authorized visual exception.')
