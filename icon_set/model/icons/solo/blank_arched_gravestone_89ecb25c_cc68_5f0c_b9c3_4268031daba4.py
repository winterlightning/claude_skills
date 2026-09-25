"""Blank Arched Gravestone. Arched stone and wider plinth; plain face preserved.
Keyshape VRECT_XL: chosen for the subject's overall proportions; authored directly on SOLO48.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '89ecb25c-cc68-5f0c-b9c3-4268031daba4'
SOURCE_PATH = 'pictographic-primitives/war/death grave_89ecb25c-cc68-5f0c-b9c3-4268031daba4.svg'
AUTHOR = 'gpt-6'

class BlankArchedGravestone(Solo48):
    icon_id = 'blank-arched-gravestone'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'war'
    aliases = ()
    keywords = ('gravestone', 'grave', 'tombstone', 'memorial', 'cemetery', 'stone')

    def build(self):
        """Centerline review: preserve the silhouette; remove duplicated ink and split real attachments into shared nodes."""

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
        A('arch', (12, 16), (36, 16), 12)
        L('wall-right', (36, 16), (36, 36))
        L('walls', (12, 36), (12, 16))
        J('wall-right', 'arch')
        J('wall-right', 'base')
        J('walls', 'arch')
        P('base', (8, 36), (12, 36), (36, 36), (40, 36), (40, 44), (8, 44), closed=True)
        J('base', 'walls')
