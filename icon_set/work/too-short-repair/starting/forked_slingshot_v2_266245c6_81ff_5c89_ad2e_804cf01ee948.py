# Variant of forked-slingshot; parent file remains unchanged.
"""Forked Slingshot. Y fork and drawn-back sling band; simplified open pouch.
Keyshape VRECT_XL: chosen for the subject's overall proportions; authored directly on SOLO48.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '266245c6-81ff-5c89-ad2e-804cf01ee948'
SOURCE_PATH = 'pictographic-primitives/war/antique sling_266245c6-81ff-5c89-ad2e-804cf01ee948.svg'
AUTHOR = 'gpt-6'

class ForkedSlingshotVariant2(Solo48):
    icon_id = 'forked-slingshot-v2'
    variant_of = 'forked-slingshot'
    variant_label = 'Height envelope and full spacing repair'
    keyshape = Keyshape.VRECT_XL
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/war'
    aliases = ()
    keywords = ('slingshot', 'sling', 'fork', 'band', 'pouch', 'weapon')

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
        P('fork-left', (23, 42), (23, 28), (16, 20), (16, 6))
        P('fork-right', (33, 42), (33, 28), (40, 20), (40, 6))
        A('fork-bowl', (16, 6), (40, 6), 12, 16, s=False)
        J('fork-bowl', 'fork-left')
        J('fork-bowl', 'fork-right')
        L('base', (23, 42), (33, 42))
        J('base', 'fork-left')
        J('base', 'fork-right')
        P('band', (16, 12), (8, 27), (15, 35), (23, 28))
        J('band', 'fork-left')
