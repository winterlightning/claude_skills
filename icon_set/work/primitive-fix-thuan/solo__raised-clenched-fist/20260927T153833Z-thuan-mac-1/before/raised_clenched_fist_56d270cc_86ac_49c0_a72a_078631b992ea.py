"""Raised Clenched Fist. Clenched fingers and folded thumb retained; three knuckle masses and one ray replace small repetitions.
Keyshape VRECT_XL: chosen for the subject's overall proportions; authored directly on SOLO48.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '56d270cc-86ac-49c0-a72a-078631b992ea'
SOURCE_PATH = 'pictographic-primitives/war/protest knuckle up_56d270cc-86ac-49c0-a72a-078631b992ea.svg'
AUTHOR = 'gpt-6'

class RaisedClenchedFist(Solo48):
    icon_id = 'raised-clenched-fist'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'war'
    categories = ('war', 'primitives')
    aliases = ()
    keywords = ('fist', 'hand', 'protest', 'knuckle', 'wrist', 'raised')

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
        P('outline', (12, 44), (12, 36), (8, 29), (8, 18))
        A('knuckle-left', (8, 18), (16, 18), 4)
        P('finger-left', (16, 18), (16, 13))
        A('knuckle-top', (16, 13), (24, 13), 4)
        P('finger-right', (24, 13), (24, 22), (34, 22))
        A('thumb', (34, 22), (40, 28), 6)
        P('palm', (40, 28), (36, 38), (32, 44))
        J('palm', 'thumb')
        J('outline', 'knuckle-left')
        J('knuckle-left', 'finger-left')
        J('finger-left', 'knuckle-top')
        J('knuckle-top', 'finger-right')
        J('finger-right', 'thumb')
        L('thumb-fold', (34, 22), (24, 32))
        J('thumb-fold', 'finger-right')
        J('thumb-fold', 'thumb')
        L('ray', (36, 4), (40, 8))
