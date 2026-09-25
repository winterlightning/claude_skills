"""A broad shallow saucer supports a central semicircular dome. Two angled landing struts extend downward from its underside, with a short detached vertical mark centered between them.

HRECT_XL visible bounds (2,6)-(46,42); shallow saucer, central dome, two landing struts and detached center mark. No useful Lucide saucer match. Symmetric curves and landing gear retained.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b93c8314-312a-450a-b457-e0c4f530e56d'
SOURCE_PATH = 'pictographic-primitives/science/spaceship_b93c8314-312a-450a-b457-e0c4f530e56d.svg'
AUTHOR = 'gpt-6'

class DomedFlyingSaucer(Solo48):
    icon_id = 'domed-flying-saucer'
    keyshape = Keyshape.HRECT_XL
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "science"
    categories = ("science", "primitives")
    aliases = ()
    keywords = ('ufo', 'saucer', 'spacecraft', 'dome', 'alien', 'landing')

    def segments(self, name, *points):
        for i,(a,b) in enumerate(zip(points,points[1:]),1):
            self.add_line(f'{name}-{i}',a,b)

    def circle(self, name, x, y, r):
        points = [(x-r,y), (x,y-r), (x+r,y), (x,y+r)]
        for i, start in enumerate(points):
            self.add_arc(f'{name}-{i}', start, points[(i+1)%4], radius_x=r)
        self.add_contour(name, *(f'{name}-{i}' for i in range(4)), closed=True)

    def build(self):
        self.add_arc('dome',(14,20),(34,20),radius_x=10,radius_y=12)
        self.add_arc('saucer-right',(34,20),(44,28),radius_x=10,radius_y=8)
        self.segments('saucer-bottom',(44,28),(32,28),(16,28),(4,28))
        self.add_arc('saucer-left',(4,28),(14,20),radius_x=10,radius_y=8)
        self.add_line('saucer-top',(14,20),(34,20))
        self.add_contour('saucer','saucer-right','saucer-bottom-1','saucer-bottom-2','saucer-bottom-3','saucer-left','saucer-top',closed=True)
        self.relate('connect','dome','saucer')
        self.add_line('leg-left',(16,28),(10,40));self.add_line('leg-right',(32,28),(38,40))
        self.relate('connect','leg-left','saucer');self.relate('connect','leg-right','saucer')
        self.add_line('center-mark',(24,37),(24,40))
