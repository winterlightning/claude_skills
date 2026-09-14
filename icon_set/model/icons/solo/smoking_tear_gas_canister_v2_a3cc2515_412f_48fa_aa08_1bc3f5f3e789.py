"""Smoking Tear Gas Canister. Canister and rising smoke curl; second trail removed.
Keyshape VRECT_XL: chosen for the subject's overall proportions; authored directly on SOLO48.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'a3cc2515-412f-48fa-aa08-1bc3f5f3e789'
SOURCE_PATH = 'pictographic-primitives/war/protest tear gas_a3cc2515-412f-48fa-aa08-1bc3f5f3e789.svg'
AUTHOR = 'gpt-6'

class SmokingTearGasCanisterVariant2(Solo48):
    icon_id = 'smoking-tear-gas-canister-v2'
    variant_of = 'smoking-tear-gas-canister'
    variant_label = 'Height envelope and full spacing repair'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/war'
    aliases = ()
    keywords = ('canister', 'tear gas', 'smoke', 'gas', 'protest', 'container')

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
        R('canister', 8, 32, 20, 12, 3)
        L('outlet', (28, 38), (33, 38))
        J('outlet', 'canister')
        A('smoke-lower', (33, 38), (40, 27), 7, 11, s=False)
        A('smoke-upper', (40, 27), (30, 16), 10, 11, s=False)
        A('smoke-tip', (30, 16), (20, 4), 10, 12)
        self.add_contour('smoke', 'smoke-lower', 'smoke-upper', 'smoke-tip')
        J('smoke', 'outlet')
