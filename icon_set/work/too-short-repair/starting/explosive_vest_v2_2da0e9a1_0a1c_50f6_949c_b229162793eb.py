# Variant of explosive-vest; parent file remains unchanged.
"""Explosive Vest. Garment and attached bomb retained; single belt and short fuse reduce crowding.
Keyshape VRECT_XL: chosen for the subject's overall proportions; authored directly on SOLO48.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '2da0e9a1-0a1c-50f6-949c-b229162793eb'
SOURCE_PATH = 'pictographic-primitives/war/bomb explosive belt_2da0e9a1-0a1c-50f6-949c-b229162793eb.svg'
AUTHOR = 'gpt-6'

class ExplosiveVestVariant2(Solo48):
    icon_id = 'explosive-vest-v2'
    variant_of = 'explosive-vest'
    variant_label = 'Height envelope and full spacing repair'
    keyshape = Keyshape.VRECT_XL
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/war'
    aliases = ()
    keywords = ('vest', 'explosive', 'bomb', 'belt', 'military', 'garment')

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
        P('vest', (8, 42), (8, 20), (12, 16), (12, 6), (20, 6), (20, 14), (28, 14), (28, 6), (36, 6), (36, 16), (40, 20), (40, 42), (8, 42))
        C('bomb', 24, 32, 6)
        L('fuse', (24, 26), (24, 22))
        J('fuse', 'bomb')
        L('belt-left', (8, 32), (18, 32))
        L('belt-right', (30, 32), (40, 32))
        J('belt-left', 'vest')
        J('belt-left', 'bomb')
        J('belt-right', 'vest')
        J('belt-right', 'bomb')
