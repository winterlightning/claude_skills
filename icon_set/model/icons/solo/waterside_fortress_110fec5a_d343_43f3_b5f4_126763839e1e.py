"""Waterside Fortress. Sloping fortress, flag and doorway; waves reduced, narrow firing slit omitted.
Keyshape VRECT_XL: chosen for the subject's overall proportions; authored directly on SOLO48.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '110fec5a-d343-43f3-b5f4-126763839e1e'
SOURCE_PATH = 'pictographic-primitives/war/water fortress_110fec5a-d343-43f3-b5f4-126763839e1e.svg'
AUTHOR = 'gpt-6'

class WatersideFortress(Solo48):
    icon_id = 'waterside-fortress'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'war'
    categories = ('war', 'primitives')
    aliases = ()
    keywords = ('fortress', 'water', 'flag', 'bunker', 'fortification', 'building')

    def build(self):
        # Height repair: exact SOLO48 keyshape extremes; original subject and stroke retained.

        def L(n, a, b):
            self.add_line(n, a, b)

        def P(n, *p, closed=False):
            self.add_polyline(n, *p, closed=closed)

        def A(n, a, b, r, ry=None, s=True):
            self.add_arc(n, a, b, radius_x=r, radius_y=ry or r, sweep=s)

        def C(n, x, y, r):
            A(n + 'a', (x - r, y), (x + r, y), r)
            A(n + 'b', (x + r, y), (x - r, y), r)
            self.add_contour(n, n + 'a', n + 'b', closed=True)

        def J(a, b):
            self.relate('connect', a, b)

        def R(n, x, y, w, h, r=4):
            L(n + 't', (x + r, y), (x + w - r, y))
            A(n + 'tr', (x + w - r, y), (x + w, y + r), r)
            L(n + 'r', (x + w, y + r), (x + w, y + h - r))
            A(n + 'br', (x + w, y + h - r), (x + w - r, y + h), r)
            L(n + 'b', (x + w - r, y + h), (x + r, y + h))
            A(n + 'bl', (x + r, y + h), (x, y + h - r), r)
            L(n + 'l', (x, y + h - r), (x, y + r))
            A(n + 'tl', (x, y + r), (x + r, y), r)
            self.add_contour(n, *[n + s for s in ('t', 'tr', 'r', 'br', 'b', 'bl', 'l', 'tl')], closed=True)
        P('fort', (8, 44), (8, 31), (20, 21), (32, 21), (40, 27), (40, 44))
        P('flag', (26, 21), (26, 4), (38, 4), (34, 12), (26, 12))
        J('flag', 'fort')
        P('door', (22, 44), (22, 34), (32, 34), (32, 44))
        P('water', (8, 44), (11, 41), (14, 44))
        J('water', 'fort')
