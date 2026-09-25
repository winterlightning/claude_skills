"""A circular center sits inside a wide, horizontally stretched outline with rounded tapered ends. The upper and lower contours swell around the center, forming a balanced lens-shaped disk.

HRECT_XL visible extremes (2,6)-(46,42); symmetric wide disk. Pointed ends softened into a continuous ellipse. Lucide orbit informed concentric circle and orbit spacing.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e0a48783-ebfe-55e1-8d0d-dc95394f8e4a'
SOURCE_PATH = 'pictographic-primitives/science/astronomy blackhole_e0a48783-ebfe-55e1-8d0d-dc95394f8e4a.svg'
AUTHOR = 'gpt-6'

class BlackHoleAccretionDisk(Solo48):
    icon_id = 'black-hole-accretion-disk'
    keyshape = Keyshape.HRECT_XL
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "science"
    aliases = ()
    keywords = ('black hole', 'accretion', 'disk', 'astronomy', 'space', 'orbit')

    def circle(self, name, x, y, r):
        points = [(x-r,y), (x,y-r), (x+r,y), (x,y+r)]
        for i, start in enumerate(points):
            self.add_arc(f'{name}-{i}', start, points[(i+1)%4], radius_x=r)
        self.add_contour(name, *(f'{name}-{i}' for i in range(4)), closed=True)

    def build(self):
        self.add_arc('disk-top',(4,24),(44,24),radius_x=20,radius_y=16)
        self.add_arc('disk-bottom',(44,24),(4,24),radius_x=20,radius_y=16)
        self.add_contour('disk','disk-top','disk-bottom',closed=True)
        self.circle('event-horizon',24,24,6)
