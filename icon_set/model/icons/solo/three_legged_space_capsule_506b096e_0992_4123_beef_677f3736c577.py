"""A tapered capsule has a domed top, a central rounded rectangular window, and a small side port. Three landing legs extend below its broad lower rim, each ending in a short flat foot.

HRECT_XL visible bounds (2,6)-(46,42); domed capsule and three landing legs with flat feet. Central window reduced to a dot; small side port omitted. No useful exact Lucide lander match; three supports retained.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '506b096e-0992-4123-beef-677f3736c577'
SOURCE_PATH = 'pictographic-primitives/science/space capsule_506b096e-0992-4123-beef-677f3736c577.svg'
AUTHOR = 'gpt-6'

class ThreeLeggedSpaceCapsule(Solo48):
    icon_id = 'three-legged-space-capsule'
    keyshape = Keyshape.HRECT_XL
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/science"
    aliases = ()
    keywords = ('capsule', 'lander', 'space', 'leg', 'window', 'landing')

    def segments(self, name, *points):
        for i,(a,b) in enumerate(zip(points,points[1:]),1):
            self.add_line(f'{name}-{i}',a,b)

    def circle(self, name, x, y, r):
        points = [(x-r,y), (x,y-r), (x+r,y), (x,y+r)]
        for i, start in enumerate(points):
            self.add_arc(f'{name}-{i}', start, points[(i+1)%4], radius_x=r)
        self.add_contour(name, *(f'{name}-{i}' for i in range(4)), closed=True)

    def build(self):
        self.add_arc('dome-right',(24,8),(32,14),radius_x=8,radius_y=6)
        self.segments('right-side',(32,14),(38,32),(36,32),(24,32),(12,32),(10,32),(16,14))
        self.add_arc('dome-left',(16,14),(24,8),radius_x=8,radius_y=6)
        self.add_contour('capsule','dome-right',*(f'right-side-{i}' for i in range(1,7)),'dome-left',closed=True)
        self.add_dot('window',(24,21))
        for n,a,b,x in [('left',(12,32),(8,40),8),('center',(24,32),(24,40),24),('right',(36,32),(40,40),40)]:
            self.add_line(n+'-leg',a,b);self.add_polyline(n+'-foot',(x-4,40),(x,40),(x+4,40))
            self.relate('connect',n+'-leg','capsule');self.relate('connect',n+'-foot',n+'-leg')
