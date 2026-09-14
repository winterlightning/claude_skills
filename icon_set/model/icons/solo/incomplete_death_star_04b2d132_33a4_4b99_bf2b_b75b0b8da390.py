"""A partially built spherical station has a rounded left half and a stepped open right edge. A broad equatorial section projects rightward, a small dish sits above-left, and cross-shaped framework appears in the missing sections.

CIRCLE radius 22 envelope; rounded left shell, stepped incomplete right side and exposed framework. Dish reduced to a dot; one framework cross retained. No useful exact Lucide match; construction gaps intentionally asymmetric.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '04b2d132-33a4-4b99-bf2b-b75b0b8da390'
SOURCE_PATH = 'pictographic-primitives/science/fiction death star_04b2d132-33a4-4b99-bf2b-b75b0b8da390.svg'
AUTHOR = 'gpt-6'

class IncompleteDeathStar(Solo48):
    icon_id = 'incomplete-death-star'
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/science"
    aliases = ()
    keywords = ('death star', 'space station', 'framework', 'sphere', 'construction', 'fiction')

    def segments(self, name, *points):
        for i,(a,b) in enumerate(zip(points,points[1:]),1):
            self.add_line(f'{name}-{i}',a,b)

    def circle(self, name, x, y, r):
        points = [(x-r,y), (x,y-r), (x+r,y), (x,y+r)]
        for i, start in enumerate(points):
            self.add_arc(f'{name}-{i}', start, points[(i+1)%4], radius_x=r)
        self.add_contour(name, *(f'{name}-{i}' for i in range(4)), closed=True)

    def build(self):
        self.add_arc('shell-upper',(24,4),(4,24),radius_x=20,sweep=False)
        self.add_arc('shell-lower',(4,24),(24,44),radius_x=20,sweep=False)
        self.segments('unfinished-edge',(24,44),(24,36),(36,36),(36,28),(43,28),(43,20),(26,20),(26,12),(26,8),(24,8),(24,4))
        self.add_contour('shell','shell-upper','shell-lower',*(f'unfinished-edge-{i}' for i in range(1,11)),closed=True)
        self.add_line('equator',(4,24),(24,24))
        self.relate('connect','equator','shell')
        self.add_dot('dish',(16,16))
        self.add_polyline('upper-frame',(26,12),(34,12),(40,12))
        self.add_line('frame-upright',(34,8),(34,18))
        self.relate('connect','upper-frame','shell')
        self.relate('connect','upper-frame','frame-upright')
