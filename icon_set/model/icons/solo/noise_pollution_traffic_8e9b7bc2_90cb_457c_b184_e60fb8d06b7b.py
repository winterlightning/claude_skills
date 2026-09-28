"""Two cars in traffic seen from the front, under a jagged line of noise.

SOLO48 HRECT_L: visible (2, 6)-(46, 42), centerline (4, 8)-(44, 40).

Symbol plan: a noise zigzag runs across the top (45-degree strokes 6 high,
12 apart, peaks at y 8 and 14). Below it two identical front-view cars, 16
wide and 8 apart (x=4 and x=28): a flat roof 8 wide at y=22, windshield
pillars slanting out to the belt line at y=30, a body 8 deep to y=38 and
two wheel stubs under its corners reaching y=40.
Revision: the rejected drawing's cars peaked into letter A shapes and the
noise marks read as a heart and a bolt; the cars now have flat roofs,
windshields and wheels, and the noise is one continuous jagged wave.
Construction reference: Lucide `car-front` (roof, windshield, body,
wheels).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '8e9b7bc2-90cb-457c-b184-e60fb8d06b7b'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__noise-pollution-traffic/20260926T160211Z-thuan-mac-1/reference/noise pollution traffic_8e9b7bc2-90cb-457c-b184-e60fb8d06b7b.svg'
AUTHOR = 'claude-opus-5-5'

ZIG_LOW, ZIG_HIGH, ZIG_STEP = 14, 8, 6
CAR_XS, CAR_W = (4, 28), 16
ROOF_Y, BELT_Y, FLOOR_Y, WHEEL_Y = 22, 30, 38, 40
ROOF_INSET, WHEEL_INSET = 4, 2


class Drawing(Solo48):
    icon_id = 'noise-pollution-traffic'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ('noise pollution traffic', 'traffic noise')
    keywords = ('noise', 'pollution', 'traffic', 'cars', 'loud', 'city', 'sound', 'jam')

    def build(self):
        pts, x, up = [], 4, False
        while x <= 44:
            pts.append((x, ZIG_HIGH if up else ZIG_LOW))
            x += ZIG_STEP
            up = not up
        self.add_polyline('noise', *pts)
        for k, x in enumerate(CAR_XS):
            r = x + CAR_W
            self.add_line(f'car-{k}-roof', (x + ROOF_INSET, ROOF_Y), (r - ROOF_INSET, ROOF_Y))
            self.add_line(f'car-{k}-pillar-r', (r - ROOF_INSET, ROOF_Y), (r, BELT_Y))
            self.add_line(f'car-{k}-side-r', (r, BELT_Y), (r, FLOOR_Y))
            wl, wr = x + WHEEL_INSET, r - WHEEL_INSET
            self.add_line(f'car-{k}-floor-r', (r, FLOOR_Y), (wr, FLOOR_Y))
            self.add_line(f'car-{k}-floor', (wr, FLOOR_Y), (wl, FLOOR_Y))
            self.add_line(f'car-{k}-floor-l', (wl, FLOOR_Y), (x, FLOOR_Y))
            self.add_line(f'car-{k}-side-l', (x, FLOOR_Y), (x, BELT_Y))
            self.add_line(f'car-{k}-pillar-l', (x, BELT_Y), (x + ROOF_INSET, ROOF_Y))
            self.add_contour(f'car-{k}', f'car-{k}-roof', f'car-{k}-pillar-r', f'car-{k}-side-r', f'car-{k}-floor-r', f'car-{k}-floor', f'car-{k}-floor-l',
                             f'car-{k}-side-l', f'car-{k}-pillar-l', closed=True)
            self.add_line(f'car-{k}-belt', (x, BELT_Y), (r, BELT_Y))
            self.relate('connect', f'car-{k}-belt', f'car-{k}')
            for side, wx in (('l', wl), ('r', wr)):
                self.add_line(f'car-{k}-wheel-{side}', (wx, FLOOR_Y), (wx, WHEEL_Y))
                self.relate('connect', f'car-{k}-wheel-{side}', f'car-{k}')
