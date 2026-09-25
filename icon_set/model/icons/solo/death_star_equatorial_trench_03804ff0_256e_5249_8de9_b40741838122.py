"""A spherical space station has a small circular dish in its upper-right quadrant and a horizontal trench across the middle. A shorter horizontal panel line runs inward from the lower-left edge.

CIRCLE visible extremes (2,2)-(46,46); sphere, equator, dish, and lower panel retained. Dish reduced to a dot; panel detached from rim to avoid a cramped wedge. Lucide orbit informed circular construction. Dish deliberately upper-right.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '03804ff0-256e-5249-8de9-b40741838122'
SOURCE_PATH = 'pictographic-primitives/science/death star_03804ff0-256e-5249-8de9-b40741838122.svg'
AUTHOR = 'gpt-6'

class DeathStarEquatorialTrench(Solo48):
    icon_id = 'death-star-equatorial-trench'
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "science"
    aliases = ()
    keywords = ('death star', 'space station', 'sphere', 'trench', 'dish', 'fiction')

    def circle(self, name, x, y, r):
        points = [(x-r,y), (x,y-r), (x+r,y), (x,y+r)]
        for i, start in enumerate(points):
            self.add_arc(f'{name}-{i}', start, points[(i+1)%4], radius_x=r)
        self.add_contour(name, *(f'{name}-{i}' for i in range(4)), closed=True)

    def build(self):
        self.add_arc('hemisphere-top',(4,24),(44,24),radius_x=20)
        self.add_arc('hemisphere-bottom',(44,24),(4,24),radius_x=20)
        self.add_contour('sphere','hemisphere-top','hemisphere-bottom',closed=True)
        self.add_line('trench',(4,24),(44,24))
        self.relate('connect','sphere','trench')
        self.add_dot('dish',(29,14))
        self.add_line('panel',(20,34),(26,34))
