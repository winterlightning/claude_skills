"""RIP Gravestone. RIP letters arranged as R above IP to preserve legibility and spacing inside the arch; plinth removed.
Keyshape VRECT_XL: chosen for the subject's overall proportions; authored directly on SOLO48.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'c37f6508-e0df-51bf-9da4-8fafc43e3b54'
SOURCE_PATH = 'pictographic-primitives/war/death rip_c37f6508-e0df-51bf-9da4-8fafc43e3b54.svg'
AUTHOR = 'gpt-6'

class RipGravestone(Solo48):
    icon_id = 'rip-gravestone'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/war'
    aliases = ()
    keywords = ('gravestone', 'rip', 'grave', 'tombstone', 'cemetery', 'memorial')

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
        A('arch', (8, 20), (40, 20), 16)
        P('walls', (40, 20), (40, 44), (8, 44), (8, 20))
        J('walls', 'arch')
        L('r-stem', (22, 14), (22, 21))
        C('r-loop', 24, 16, 2)
        J('r-stem', 'r-loop')
        L('r-leg', (24, 18), (26, 21))
        J('r-leg', 'r-loop')
        L('i', (18, 29), (18, 36))
        L('p-stem', (27, 29), (27, 35))
        C('p-loop', 29, 31, 2)
        J('p-stem', 'p-loop')
