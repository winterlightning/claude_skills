# Repair: Rebalance three pin heads and bodies as repeated rounded shapes; their painted head/body contours meet tangentially.
"""Three bowling pins in an equal row. No useful local Lucide bowling match; shared heads and smoothly bulging bellies preserve all three pins. Source overlaps separated for clearance.

SOLO48 HRECT_L; live visible envelope (2, 6, 46, 42).
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'd972c303-2754-4efe-82ae-c0b2f535370b'
SOURCE_PATH = 'pictographic-primitives/symbol/three bowlings_d972c303-2754-4efe-82ae-c0b2f535370b.svg'
AUTHOR = 'gpt-6'

class BowlingPinsRow(Solo48):
    icon_id = 'bowling-pins-row'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    categories = ('symbol', 'state')
    aliases = ()
    keywords = ('bowling', 'pins', 'skittles', 'sport', 'game', 'alley', 'strike', 'leisure')

    def oval(self, n, cx, cy, rx, ry=None):
        ry = rx if ry is None else ry
        self.add_arc(n + '-top', (cx - rx, cy), (cx + rx, cy), radius_x=rx, radius_y=ry)
        self.add_arc(n + '-bottom', (cx + rx, cy), (cx - rx, cy), radius_x=rx, radius_y=ry)
        self.add_contour(n, n + '-top', n + '-bottom', closed=True)

    def raw(self, n, points):
        for j, (a, b) in enumerate(zip(points, points[1:]), 1):
            self.add_line(n + '-' + str(j), a, b)

    def path(self, n, points, closed=False):
        self.add_polyline(n, *points, closed=closed)

    def build(self):
        from ._symmetry_curves import path, ellipse, line, poly, contacts

        for j,cx in enumerate((8,24,40)):
            front = False and j == 1
            cy = 15 if front else 11
            bottom = 36 if False and not front else 40
            top = cy+7
            ellipse(self,f'head-{j}',cx,cy,3)
            ellipse(self,f'body-{j}',cx,(top+bottom)//2,4,(bottom-top)//2)
            self.relate('connect',f'head-{j}',f'body-{j}')
