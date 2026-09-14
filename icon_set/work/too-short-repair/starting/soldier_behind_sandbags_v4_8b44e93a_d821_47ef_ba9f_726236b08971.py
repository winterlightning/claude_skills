# Variant of soldier-behind-sandbags-v2; parent file remains unchanged.
"""Soldier Behind Sandbags. Helmeted head above two sandbags with a leftward rifle; supporting arm removed.
Keyshape HRECT_XL: chosen for the subject's overall proportions; authored directly on SOLO48.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '8b44e93a-d821-47ef-ba9f-726236b08971'
SOURCE_PATH = 'pictographic-primitives/war/sand bag soldier_8b44e93a-d821-47ef-ba9f-726236b08971.svg'
AUTHOR = 'gpt-6'

class SoldierBehindSandbagsVariant4(Solo48):
    icon_id = 'soldier-behind-sandbags-v4'
    variant_of = 'soldier-behind-sandbags-v2'
    variant_label = 'Height envelope and full spacing repair'
    keyshape = Keyshape.HRECT_XL
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/war'
    aliases = ()
    keywords = ('soldier', 'sandbag', 'rifle', 'helmet', 'barricade', 'military')

    def build(self):
        """Opening repair: Removed the thin central brim divider and made the helmeted head rounder; kept the rifle and both bags."""

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
        A('helmet', (30, 15), (42, 15), 6)
        A('face', (30, 15), (42, 15), 6, s=False)
        J('face', 'helmet')
        L('rifle', (6, 15), (30, 15))
        J('rifle', 'helmet')
        J('rifle', 'face')
        R('bag-left', 4, 31, 15, 9, 4)
        R('bag-right', 29, 31, 15, 9, 4)
