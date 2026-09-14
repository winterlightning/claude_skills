# Variant of automatic-rifle; parent file remains unchanged.
"""Automatic Rifle. Stock, raised receiver and magazine retained; trigger and second grip omitted.
Keyshape HRECT_XL: chosen for the subject's overall proportions; authored directly on SOLO48.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '835277d4-590e-5008-a9cb-07213ea668e9'
SOURCE_PATH = 'pictographic-primitives/war/modern weapon machine gun_835277d4-590e-5008-a9cb-07213ea668e9.svg'
AUTHOR = 'gpt-6'

class AutomaticRifleVariant3(Solo48):
    icon_id = 'automatic-rifle-v3'
    variant_of = 'automatic-rifle'
    variant_label = 'Roomier spacing — review 01'
    keyshape = Keyshape.HRECT_XL
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/war'
    aliases = ()
    keywords = ('rifle', 'automatic', 'magazine', 'stock', 'barrel', 'weapon')

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
        P('body', (6, 19), (15, 19), (19, 13), (32, 13), (32, 21), (40, 21), (40, 29), (14, 29), (6, 35), closed=True)
        L('barrel', (40, 25), (42, 25))
        J('barrel', 'body')
        P('magazine', (31, 29), (33, 40), (23, 40), (21, 29))
        J('magazine', 'body')
        L('sight', (40, 21), (40, 8))
        J('sight', 'body')
