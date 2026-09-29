author(10,'''
# Six rounded teeth; both axes mirror exactly around (24,24).
self.add_bezier('gear',(22,13),
    ((22,10),(26,10),(26,13)),
    ((26,16),(28,17),(31,15)),
    ((34,13),(37,18),(34,20)),
    ((31,22),(31,26),(34,28)),
    ((37,30),(34,35),(31,33)),
    ((28,31),(26,32),(26,35)),
    ((26,38),(22,38),(22,35)),
    ((22,32),(20,31),(17,33)),
    ((14,35),(11,30),(14,28)),
    ((17,26),(17,22),(14,20)),
    ((11,18),(14,13),(17,15)),
    ((20,17),(22,16),(22,13)))
self.add_contour('gear-outline','gear',closed=True)
for name,p,q in [('top',(24,3),(24,5)),('bottom',(24,43),(24,45)),('left',(3,24),(6,24)),('right',(42,24),(45,24)),('nw',(7,7),(10,10)),('ne',(38,10),(41,7)),('sw',(7,41),(10,38)),('se',(38,38),(41,41))]:
    self.add_line(name,p,q)
''','SQUARE','The rejected cog used four dots instead of radiating strokes and reduced its lobes to a coarse hexagon. Feedback asks to recover the radiating cog meaning.',
 'Restore six smooth, symmetric gear lobes and eight surrounding short rays. The cog has no central hub, matching the reference.',
 'Lucide settings original and atomic geometry: alternating smooth outer teeth and inner valleys; source controls absence of hub and eight rays.',
 'No defining features omitted.',
 exception_reason='Compact ray-to-cog spacing and radial bounds retain all six teeth and eight rays in48px with uniform4px strokes; user authorized visual exception after native-size review.')
