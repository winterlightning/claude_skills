"""A square-faced digital smart watch seen from the front, with its band running off top and bottom.

Symbol plan: one rounded-square case (equal corner radii) on axis x=24; two mirrored band stubs
leave the case at the ends of its straight top and bottom walls and taper inward to the canvas edge.
Reduction: the band ends are left open (a closed band loop would enclose a hole under 6 units).
Keyshape: VRECT_M -- the case is 28 wide, the band adds height only.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'c93fbbca-0204-4391-bdc8-00d23d10dc84'
SOURCE_PATH = 'pictographic-primitives/devices/smart watch square_c93fbbca-0204-4391-bdc8-00d23d10dc84.svg'
AUTHOR = 'claude-opus-5-5'

L, T, R, B, RAD = 10, 10, 38, 38, 6


class Drawing(Solo48):
    icon_id = 'square-digital-smartwatch'
    keyshape = Keyshape.VRECT_M
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'devices'
    categories = ('devices', 'primitives-generate')
    aliases = ('square smart watch', 'smartwatch')
    keywords = ('watch', 'smartwatch', 'wearable', 'square')

    def build(self):
        pts = [(L + RAD, T), (R - RAD, T), (R, T + RAD), (R, B - RAD), (R - RAD, B), (L + RAD, B), (L, B - RAD), (L, T + RAD)]
        for i in range(8):
            a, z = pts[i], pts[(i + 1) % 8]
            if i % 2:
                self.add_arc(f'case-{i}', a, z, radius_x=RAD)
            else:
                self.add_line(f'case-{i}', a, z)
        self.add_contour('case', *(f'case-{i}' for i in range(8)), closed=True)
        # Band stubs start where each straight wall meets its corner arc and taper by 2 per side.
        for name, y, edge, wall, left_arc, right_arc in (('band-top', T, 4, 'case-0', 'case-7', 'case-1'),
                                                         ('band-bottom', B, 44, 'case-4', 'case-5', 'case-3')):
            self.add_line(name + '-left', (L + RAD, y), (L + RAD + 2, edge))
            self.add_line(name + '-right', (R - RAD, y), (R - RAD - 2, edge))
            self.relate('connect', name + '-left', wall, left_arc)
            self.relate('connect', name + '-right', wall, right_arc)
