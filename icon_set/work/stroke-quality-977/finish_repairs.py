"""Last corrections from native-size and enlarged visual review."""
from polish_repairs import *
SOURCE_ICON_ID=None
SOURCE_PATH='icon_set/work/intersection-review-977/cohort.json'
AUTHOR='gpt-6'
for id,mirror in [('blind',True),('hidden',False)]:
 patch(id,f'mirror = {mirror}\n'+'''
axis = 24
def p(x,y):return (48-x,y) if mirror else (x,y)
self.add_bezier('upper-left',p(4,24),(p(7,19),p(10,14),p(14,12)),(p(18,10),p(20,8),p(24,8)))
self.add_bezier('upper-right',p(24,8),(p(28,8),p(30,10),p(34,12)),(p(38,14),p(41,19),p(44,24)))
self.add_bezier('lower-right',p(44,24),(p(41,29),p(38,34),p(34,36)),(p(30,38),p(28,40),p(24,40)))
self.add_bezier('lower-left',p(24,40),(p(20,40),p(18,38),p(14,36)),(p(10,34),p(7,29),p(4,24)))
self.add_contour('outline','upper-left','upper-right','lower-right','lower-left',closed=True)
self.add_line('slash',p(14,12),p(34,36))
self.relate('connect','slash','outline')
''','HRECT_L; mirror all lens quadrants; diagonal terminates on exact curve knots.','Geometric paired curves and shared nodes.')
p=Path(byid['hamburger']['python_source']['path']);s=p.read_text().replace('(11,24),(13,24)','(11,22),(13,22)').replace('(19,16),(21,16)','(19,18),(21,18)').replace('(27,24),(29,24)','(27,22),(29,22)').replace('(35,16),(37,16)','(35,18),(37,18)');p.write_text(s)
p=Path(byid['pot']['python_source']['path']);s=p.read_text().replace("self.add_polyline('spout',(10,42),(6,42),(6,38))","self.add_arc('base-left',(10,42),(6,38),radius_x=4)").replace("'spout-1','spout-2'","'base-left'").replace('self.contours=self.contours[2:]','self.contours=self.contours[1:]');p.write_text(s)
patch('information','''
self.add_line('dot-bar',(19,4),(29,4))
self.add_polyline('stem',(8,18),(24,18),(24,44))
self.add_line('foot',(8,44),(40,44))
self.relate('connect','stem','foot')
''','VRECT_L; level cap stroke, centered dot-bar and exact upright stem.','Geometric typographic construction.')
patch('shape-triangle',"self.add_polyline('outline',(24,6),(42,42),(6,42),closed=True)",'SQUARE; three straight sides, level baseline and shared axis.','Geometric triangle; remove the extra sagging base vertex.')
save()
