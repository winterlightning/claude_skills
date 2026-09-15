from edit_batch import revise,remove_named
SOURCE_ICON_ID=None
SOURCE_PATH='/Users/jakesdev/Downloads/feedback-briefs 2/solo'
AUTHOR='gpt-6'
# All edits create independent variants in the isolated snapshot.
revise(11,'Remove the bow knot completely and raise both lower bow edges to open the forehead; preserve paired eyes and the round cheeks.',patch=lambda s:remove_named(s,{'knot'}).replace('(24, 13)','(24, 12)').replace('(10, 20)','(10, 18)').replace('(38, 20)','(38, 18)'),ref='Lucide baby: paired dot eyes and one broad cheek contour; shared human reference')
revise(13,'Widen the gate from 8 to 12 centerline units and raise its lintel by one unit; remove the inner tower divider so the larger opening stays clear.',patch=lambda s:remove_named(s,{'tower'}).replace('(14, 34), (22, 34), (22, 42)','(14, 33), (26, 33), (26, 42)'),ref='Lucide castle: one clear gate opening within the castle silhouette')
revise(14,'Square the drive housing on a shared horizontal baseline and retain one solid dot at the circular disc center.',patch=lambda s:s.replace('(8, 6), (40, 6)','(6, 6), (42, 6)'),ref='Lucide disc: a circular disc and exactly centered dot hub')
revise(17,'Double the single-stroke doorway height and center the tower crossbar, making the entrance legible at 48 pixels.',patch=lambda s:s.replace('(28, 38)','(28, 34)').replace('(13, 6)','(12, 6)'),ref='Lucide church: sparse doorway and centered architectural strokes')
revise(18,'Rebalance the monument vertically: enlarge the cross-to-attic gap and use matching ten-unit openings below it.',keyshape='VRECT_L',body="""
poly('gateway',(8,26),(16,26),(32,26),(40,26),(40,44),(32,44),(32,34),(16,34),(16,44),(8,44),closed=True)
poly('attic',(16,26),(16,16),(24,16),(32,16),(32,26))
join('attic','gateway')
poly('mast',(24,4),(24,6),(24,16))
poly('cross',(20,6),(24,6),(28,6))
join('mast','cross');join('mast','attic')
""",ref='Lucide landmark: shared architectural axis and even bays')
revise(21,'Open the crack entry further around the rim and spread the zigzag so it has a clear gap to the disc edge.',patch=lambda s:s.replace('(12, 8)','(8, 12)').replace('(16, 18), (29, 18), (18, 34)','(14, 20), (28, 20), (22, 32)'),ref='Lucide disc: one circular rim; deliberate asymmetric open crack')
revise(25,'Increase the mouth separation from 8 to 10 centerline units and align both dot apertures on one height.',patch=lambda s:s.replace('(6, 26)','(6, 24)').replace('(36, 26)','(36, 24)').replace('(15, 17)','(15, 16)'))
revise(28,'Use four matching 4-unit corner radii and center the solid hub dot on the disk; keep the shutter and label cleanly separated.',patch=lambda s:s.replace('p_8_6 = (8, 6)','p_8_6 = (10, 6)').replace('p_40_6 = (40, 6)','p_40_6 = (38, 6)').replace('p_42_8 = (42, 8)','p_42_8 = (42, 10)').replace('p_42_40 = (42, 40)','p_42_40 = (42, 38)').replace('p_40_42 = (40, 42)','p_40_42 = (38, 42)').replace('p_8_42 = (8, 42)','p_8_42 = (10, 42)').replace('p_6_40 = (6, 40)','p_6_40 = (6, 38)').replace('p_6_8 = (6, 8)','p_6_8 = (6, 10)').replace('radius_x=2, radius_y=2','radius_x=4, radius_y=4').replace('p_24_25 = (24, 25)','p_24_25 = (24, 24)').replace("self.add_line('hub', p_24_25, p_24_25)","self.add_dot('hub', p_24_25)"))
revise(31,'Redraw the torii with a smooth upturned roof, two evenly placed posts, and a wider vertical opening between its two horizontal beams.',keyshape='HRECT_L',body="""
path('roof',(4,8),[('C',(12,12),(4,11),(8,12)),('L',(36,12)),('C',(44,8),(40,12),(44,11))])
poly('beam',(4,24),(12,24),(36,24),(44,24))
for side,x in [('left',12),('right',36)]:
 poly(side,(x,12),(x,24),(x,40));join(side,'roof');join(side,'beam')
""",ref='Lucide landmark: paired posts; deliberate upturned torii roof')
revise(53,'Widen the space between the windmill supports and rebuild the entrance with an 8-unit arch radius; align all four sail endpoints around one hub.',keyshape='VRECT_L',body="""
poly('sail-a',(8,4),(24,16),(40,28));poly('sail-b',(8,28),(24,16),(40,4));join('sail-a','sail-b')
path('entrance',(8,44),[('L',(16,44)),('L',(16,42)),('A',(32,42),8,8,True),('L',(32,44)),('L',(40,44))])
""",ref='Lucide landmark: clean separated supports; no exact windmill reference')
revise(57,'Enlarge the bottle neck opening vertically and horizontally, shorten the shoulders, and center the simple star within the lower body.',patch=lambda s:s.replace('(8, 15, 40, 44, 4)','(8, 18, 40, 44, 4)').replace('(16, 15), (16, 4), (32, 4), (32, 15)','(14, 18), (14, 4), (34, 4), (34, 18)').replace('((24, 24), (30, 28), (28, 35), (20, 35), (18, 28))','((24, 27), (30, 30), (28, 35), (20, 35), (18, 30))').replace('(24, 30), tip','(24, 32), tip'))
revise(59,'Redraw the roof as two clean slopes and widen the hut body with matching lower corners; make the doorway one longer centered vertical stroke.',keyshape='SQUARE',body="""
poly('roof',(6,20),(10,17),(24,6),(38,17),(42,20))
path('walls',(10,17),[('L',(10,38)),('A',(14,42),4,4,False),('L',(24,42)),('L',(34,42)),('A',(38,38),4,4,False),('L',(38,17))])
line('door',(24,42),(24,28));join('walls','roof');join('door','walls')
""",ref='Lucide house: straight roof slopes and a centered entrance')
revise(71,'Rebuild the lower tower with equal stepped side walls and a rectangular central gate; simplify the pennant to a clean rectangle.',keyshape='VRECT_L',body="""
poly('wall',(8,44),(8,20),(16,20),(16,28),(24,28),(32,28),(32,20),(40,20),(40,44),(30,44),(30,36),(18,36),(18,44),closed=True)
poly('pole',(24,28),(24,12),(24,4))
poly('flag',(24,4),(40,4),(40,12),(24,12));join('pole','wall');join('flag','pole')
""",ref='Lucide castle: shared battlement widths and a clear gate')
revise(83,'Reduce the flock from five birds to three larger paired curves; use one repeated wing definition and generous air between the birds.',keyshape='SQUARE',body="""
for n,cx,y in [('left',14,6),('right',34,6),('low',24,34)]:
 path(n,(cx-8,y),[('C',(cx,y+8),(cx-4,y),(cx,y+3)),('C',(cx+8,y),(cx,y+3),(cx+4,y))])
""",ref='Lucide bird: minimal coherent wing silhouettes')
revise(108,'Rebalance the feather into a broader, smoother eye-shaped vane, move the solid dot along its diagonal axis, and join the quill tangentially.',keyshape='VRECT_L',body="""
path('vane',(40,4),[('C',(12,38),(18,4),(12,17)),('C',(40,4),(34,38),(40,23))],True)
line('quill',(12,38),(8,44));join('quill','vane');dot('eye',(25,22))
""",ref='Lucide feather: one dominant vane and aligned quill')
revise(144,'Redraw the crescent as two tangent circular arcs with generous middle width and clear rounded tips.',keyshape='CIRCLE',body="""
self.add_arc('outer',(24,4),(44,24),radius_x=20,sweep=False,large_arc=True)
self.add_arc('inner',(44,24),(24,4),radius_x=20,sweep=True)
self.add_contour('crescent','outer','inner',closed=True)
""",ref='Lucide moon: two clean opposing arcs and a legible crescent opening')
revise(171,'Rebuild the sword around one exact 45-degree centerline; straighten and lengthen the grip, use a perpendicular guard, and broaden the symmetrical blade.',keyshape='SQUARE',body="""
poly('blade',(16,24),(34,6),(42,6),(42,14),(24,32))
poly('guard',(12,20),(16,24),(20,28),(24,32),(28,36));join('guard','blade')
line('grip',(20,28),(9,39));join('grip','guard')
poly('pommel',(6,36),(9,39),(12,42));join('pommel','grip')
""",ref='Lucide sword: shared blade/handle axis and perpendicular guard')
for n,start,cmd in [(172,(6,42),[('L',(36,42)),('A',(42,36),6,6,False),('L',(42,6))]),(173,(6,6),[('L',(6,36)),('A',(12,42),6,6,False),('L',(42,42))]),(174,(42,42),[('L',(42,12)),('A',(36,6),6,6,False),('L',(6,6))])]:
 revise(n,'Keep the exact square envelope while replacing the abrupt elbow with a 6-unit tangent quarter-circle; both arms remain equal.',keyshape='SQUARE',body=f"path('corner',{start!r},{cmd!r})")
revise(187,'Make the handle a broader shallow half-ellipse, center it within a taller body opening, and give the two lower bag corners matching radii.',keyshape='VRECT_L',body="""
path('body',(8,14),[('L',(16,4)),('L',(32,4)),('L',(40,14)),('L',(40,40)),('A',(36,44),4,4,True),('L',(12,44)),('A',(8,40),4,4,True),('L',(8,14))],True)
line('fold',(8,14),(40,14));join('fold','body')
path('handle',(17,25),[('A',(31,25),7,5,False)])
""",ref='Lucide shopping-bag: centered curved handle and coherent bag corners')
revise(207,'Spread the amphitheater into a broad horseshoe, with flatter concentric elliptical rows and longer vertical ends.',keyshape='HRECT_L',body="""
path('seats',(4,40),[('L',(4,24)),('A',(44,24),20,16,True),('L',(44,40)),('L',(35,40)),('L',(35,24)),('A',(13,24),11,7,False),('L',(13,40)),('L',(4,40))],True)
""",ref='Lucide landmark: centered architectural geometry; deliberate horizontal ellipse')
revise(223,'Replace the nearly straight side seams with visibly curved, mirrored arcs; retain equal clear spaces around the central cross.',patch=lambda s:s.replace("(x(10), 12), (x(10), 18)","(x(8), 12), (x(10), 18)").replace("(x(10), 30), (x(10), 36)","(x(10), 30), (x(8), 36)"))
