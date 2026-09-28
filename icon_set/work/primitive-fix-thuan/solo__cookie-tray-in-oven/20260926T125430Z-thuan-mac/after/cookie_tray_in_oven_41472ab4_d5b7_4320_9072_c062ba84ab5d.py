"""Cookie tray in an oven: an oven front with a control strip of knobs over
the baking chamber, where a tray of cookies sits on the shelf.
Review (meaning): the earlier floating trapezoid with two dots and corner
brackets did not read as an oven. This revision makes the oven itself the
frame (box, control strip, three knobs) and shows the tray inside as a shelf
line carrying two domed cookies.
Keyshape SQUARE (6,6)-(42,42).
Symbol plan: box with square centerline corners (exact 8-unit gaps certify
straight-to-straight); divider at y=22 splits the walls; knobs are dots on the
strip's midline; the tray is one line whose two cookie domes (rx3, ry2)
replace segments of it; tray at y=33 keeps 9 below, 9 from each wall
and dome tops 9 above (no closed half-disc holes); mirrored about x=24.
Lucide construction: microwave/refrigerator box-and-divider construction.
Omissions: steam lines and the tray's perspective; the chamber keeps only
what fits with 8-unit clearances.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.profiles import Profile
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '41472ab4-d5b7-4320-9072-c062ba84ab5d'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__cookie-tray-in-oven/20260926T125430Z-thuan-mac/reference/cooking baking tray oven_41472ab4-d5b7-4320-9072-c062ba84ab5d.svg'
AUTHOR = 'claude-opus-5-5'


class _Shapes:
    def circle(self, n, x, y, r):
        pts = [(x - r, y), (x, y - r), (x + r, y), (x, y + r), (x - r, y)]
        for i, (a, b) in enumerate(zip(pts, pts[1:])):
            self.add_arc(f"{n}-{i}", a, b, radius_x=r)
        self.add_contour(n, *(f"{n}-{i}" for i in range(4)), closed=True)

    def lines(self, n, *pts, closed=False):
        """Plain add_line segments grouped in one contour (members joinable by relate)."""
        seq = list(pts) + ([pts[0]] if closed else [])
        ids = []
        for i, (a, b) in enumerate(zip(seq, seq[1:])):
            self.add_line(f"{n}-{i}", a, b)
            ids.append(f"{n}-{i}")
        self.add_contour(n, *ids, closed=closed)
        return ids

class CookieTrayInOven(_Shapes, Solo48):
    icon_id = 'cookie-tray-in-oven'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/kitchen'
    categories = ('food', 'objects')
    aliases = ('cooking baking tray oven', 'baking tray', 'oven')
    keywords = ('cookie', 'tray', 'oven', 'baking', 'bake', 'kitchen', 'cooking')

    def build(self):
        L, T, R, B, div = 6, 6, 42, 42, 22
        self.lines('oven', (L, div), (L, T), (R, T), (R, div), (R, B), (L, B), closed=True)
        self.add_line('divider', (L, div), (R, div))
        self.relate('connect', 'oven', 'divider')
        for i, x in enumerate((16, 24, 32)):
            self.add_dot(f'knob-{i}', (x, 14))
        tray = 33
        self.add_arc('cookie-l', (15, tray), (21, tray), radius_x=3, radius_y=2)
        self.add_line('tray-m', (21, tray), (27, tray))
        self.add_arc('cookie-r', (27, tray), (33, tray), radius_x=3, radius_y=2)
        self.add_contour('tray-shelf', 'cookie-l', 'tray-m', 'cookie-r')
