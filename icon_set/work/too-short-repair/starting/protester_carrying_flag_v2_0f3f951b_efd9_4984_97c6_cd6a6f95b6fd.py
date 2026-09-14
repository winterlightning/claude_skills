# Variant of protester-carrying-flag; parent file remains unchanged.
"""Protester Carrying a Flag. Flag, diagonal pole and striding figure; closed limb contours reduced to strokes.
Keyshape VRECT_XL: chosen for the subject's overall proportions; authored directly on SOLO48.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '0f3f951b-efd9-4984-97c6-cd6a6f95b6fd'
SOURCE_PATH = 'pictographic-primitives/war/protester flag_0f3f951b-efd9-4984-97c6-cd6a6f95b6fd.svg'
AUTHOR = 'gpt-6'

class ProtesterCarryingFlagVariant2(Solo48):
    icon_id = 'protester-carrying-flag-v2'
    variant_of = 'protester-carrying-flag'
    variant_label = 'Height envelope and full spacing repair'
    keyshape = Keyshape.VRECT_XL
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/war'
    aliases = ()
    keywords = ('protester', 'flag', 'person', 'march', 'pole', 'demonstration')

    def build(self):

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
        P('flag', (8, 6), (40, 6), (30, 14))
        L('pole', (8, 6), (20, 31))
        J('pole', 'flag')
        C('head', 37, 25, 3)
        P('body', (36, 42), (30, 33), (37, 28), (30, 33), (24, 31), (16, 39), (14, 42))
        P('arms', (30, 33), (20, 30), (16, 26))
        J('arms', 'body')
        J('arms', 'pole')
        J('head', 'body')
