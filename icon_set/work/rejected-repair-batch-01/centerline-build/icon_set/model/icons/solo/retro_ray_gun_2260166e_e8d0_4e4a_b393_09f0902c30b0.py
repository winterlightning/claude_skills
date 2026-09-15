"""A ray gun points left from a curved upper housing above a slanted grip and small trigger guard. Its narrow barrel carries two crossbars and ends in a circular muzzle; a rectangular inset marks the body.

HRECT_XL visible bounds (2,6)-(46,42); left-facing barrel, circular muzzle, curved housing and slanted grip. Trigger guard and inset omitted; two close barrel rings reduced to one. No useful Lucide ray-gun match; directional asymmetry retained.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '2260166e-e8d0-4e4a-b393-09f0902c30b0'
SOURCE_PATH = 'pictographic-primitives/science/fiction weapon_2260166e-e8d0-4e4a-b393-09f0902c30b0.svg'
AUTHOR = 'gpt-6'

class RetroRayGun(Solo48):
    icon_id = 'retro-ray-gun'
    keyshape = Keyshape.HRECT_XL
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/science'
    aliases = ()
    keywords = ('ray gun', 'blaster', 'weapon', 'retro', 'fiction', 'space')

    def segments(self, name, *points):
        for i, (a, b) in enumerate(zip(points, points[1:]), 1):
            self.add_line(f'{name}-{i}', a, b)

    def circle(self, name, x, y, r):
        points = [(x - r, y), (x, y - r), (x + r, y), (x, y + r)]
        for i, start in enumerate(points):
            self.add_arc(f'{name}-{i}', start, points[(i + 1) % 4], radius_x=r)
        self.add_contour(name, *(f'{name}-{i}' for i in range(4)), closed=True)

    def build(self):
        """Open the circular muzzle while preserving its left envelope and the attached barrel."""
        self.add_arc('housing-top', (22, 18), (44, 8), radius_x=22, radius_y=10)
        self.add_arc('housing-back', (44, 8), (36, 24), radius_x=8, radius_y=16)
        self.segments('grip', (36, 24), (44, 40), (28, 40), (30, 28), (22, 28), (22, 20), (22, 18))
        self.add_contour('body', 'housing-top', 'housing-back', *(f'grip-{i}' for i in range(1, 7)), closed=True)
        self.add_line('barrel', (10, 20), (14, 20))
        self.add_line('barrel-body', (14, 20), (22, 20))
        self.add_line('barrel-ring-top', (14, 14), (14, 20))
        self.add_line('barrel-ring-bottom', (14, 20), (14, 26))
        self.circle('muzzle', 7, 20, 3)
        self.relate('connect', 'muzzle', 'barrel')
        self.relate('connect', 'barrel', 'barrel-body')
        for ring in ('barrel-ring-top', 'barrel-ring-bottom'):
            self.relate('connect', ring, 'barrel')
            self.relate('connect', ring, 'barrel-body')
        self.relate('connect', 'barrel-ring-top', 'barrel-ring-bottom')
        self.relate('connect', 'barrel-body', 'body')
