# Variant of military-drone-overhead; parent file remains unchanged.
"""Military Drone from Above. Symmetric overhead fuselage and tapered wings; tiny propeller marks omitted.
Keyshape VRECT_XL: chosen for the subject's overall proportions; authored directly on SOLO48.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'e69b65dc-1f55-4022-b7dd-ae536b0ce78f'
SOURCE_PATH = 'pictographic-primitives/war/military drone_e69b65dc-1f55-4022-b7dd-ae536b0ce78f.svg'
AUTHOR = 'gpt-6'

class MilitaryDroneOverheadVariant2(Solo48):
    icon_id = 'military-drone-overhead-v2'
    variant_of = 'military-drone-overhead'
    variant_label = 'Height envelope and full spacing repair'
    keyshape = Keyshape.VRECT_XL
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/war'
    aliases = ()
    keywords = ('drone', 'aircraft', 'military', 'wing', 'propeller', 'overhead')

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
        P('airframe', (24, 6), (28, 10), (28, 18), (40, 22), (40, 28), (28, 27), (28, 36), (34, 40), (24, 42), (14, 40), (20, 36), (20, 27), (8, 28), (8, 22), (20, 18), (20, 10), closed=True)
