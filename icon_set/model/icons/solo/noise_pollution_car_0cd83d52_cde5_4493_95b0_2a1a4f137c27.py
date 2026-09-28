"""A car making noise: a side-view car with sound bursting from it.

SOLO48 SQUARE: visible (4, 4)-(44, 44), centerline (6, 6)-(42, 42).

Symbol plan: the car is one closed side-view outline: rear at x=6, trunk
at y=26, a rear window slanting up to a roof at y=16, a windshield down to
the hood at y=26, the nose at x=42 and a floor at y=34 split where the
wheels hang. The wheels are r4 rings whose top nodes sit on the floor.
Noise: an outward chevron at each upper corner (< on the left, > on the
right), 8+ clear of the windows.
Revision: the rejected drawing's flat body with bump wheels read as a bone
and the noise marks floated; the car now has a cabin with windows, round
wheels and sound chevrons radiating from it.
Construction reference: Lucide `car` (cabin and round wheels) and
`volume-2` (sound marks).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '0cd83d52-cde5-4493-95b0-2a1a4f137c27'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__noise-pollution-car/20260926T160211Z-thuan-mac-1/reference/noise pollution car_0cd83d52-cde5-4493-95b0-2a1a4f137c27.svg'
AUTHOR = 'claude-opus-5-5'

FLOOR, WAIST, ROOF = 34, 26, 16
BODY = [(6, FLOOR), (6, WAIST), (12, WAIST), (17, ROOF), (29, ROOF), (35, WAIST), (42, WAIST), (42, FLOOR)]
WHEEL_XS, WHEEL_R = (34, 14), 4
CHEVRON_L = ((9, 6), (6, 10), (9, 14))


def mx(p):
    return (48 - p[0], p[1])


class Drawing(Solo48):
    icon_id = 'noise-pollution-car'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ('noise pollution car', 'loud car')
    keywords = ('noise', 'pollution', 'car', 'loud', 'traffic', 'sound', 'honk', 'vehicle')

    def build(self):
        pts = BODY + [(x, FLOOR) for x in WHEEL_XS]
        members = []
        for i in range(len(pts)):
            a, b = pts[i], pts[(i + 1) % len(pts)]
            self.add_line(f'body-{i}', a, b)
            members.append(f'body-{i}')
        self.add_contour('body', *members, closed=True)
        for k, x in enumerate(WHEEL_XS):
            top, right, bottom, left = (x, FLOOR), (x + WHEEL_R, FLOOR + WHEEL_R), (x, FLOOR + 2 * WHEEL_R), (x - WHEEL_R, FLOOR + WHEEL_R)
            ring = [top, right, bottom, left]
            for i in range(4):
                self.add_arc(f'wheel-{k}-{i}', ring[i], ring[(i + 1) % 4], radius_x=WHEEL_R, sweep=True)
            self.add_contour(f'wheel-{k}', *[f'wheel-{k}-{i}' for i in range(4)], closed=True)
            self.relate('connect', f'wheel-{k}', 'body')
        self.add_polyline('noise-left', *CHEVRON_L)
        self.add_polyline('noise-right', *[mx(p) for p in CHEVRON_L])
