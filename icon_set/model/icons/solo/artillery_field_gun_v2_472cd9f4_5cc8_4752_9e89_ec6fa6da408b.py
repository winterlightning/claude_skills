"""Artillery Field Gun. Single plain wheel and long angled barrel; narrow carriage reduced to open trail.
Keyshape HRECT_XL: chosen for the subject's overall proportions; authored directly on SOLO48.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '472cd9f4-5cc8-4752-9e89-ec6fa6da408b'
SOURCE_PATH = 'pictographic-primitives/war/symbol artillery_472cd9f4-5cc8-4752-9e89-ec6fa6da408b.svg'
AUTHOR = 'gpt-6'

class ArtilleryFieldGunVariant2(Solo48):
    icon_id = 'artillery-field-gun-v2'
    variant_of = 'artillery-field-gun'
    variant_label = 'Hole and centerline reconstruction'
    keyshape = Keyshape.HRECT_XL
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/war'
    aliases = ()
    keywords = ('artillery', 'cannon', 'field gun', 'wheel', 'barrel', 'carriage')

    def build(self):
        """Widen the rear breech corner above the wheel."""

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
        C('wheel', 22, 30, 10)
        P('barrel', (14, 24), (6, 19), (44, 8), (44, 14), (30, 24))
        J('barrel', 'wheel')
        L('trail', (14, 36), (4, 40))
        J('trail', 'wheel')
