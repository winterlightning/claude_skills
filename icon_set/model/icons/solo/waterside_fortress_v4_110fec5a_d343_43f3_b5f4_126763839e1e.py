"""Restored arched doorway, notched flag and a full waterline. Door-to-wall and door-to-roof clearances are enlarged; waves meet the structural base. Narrow firing slit omitted."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '110fec5a-d343-43f3-b5f4-126763839e1e'
SOURCE_PATH = 'pictographic-primitives/war/water fortress_110fec5a-d343-43f3-b5f4-126763839e1e.svg'
AUTHOR = 'gpt-6'

class WatersideFortressVariant4(Solo48):
    icon_id = 'waterside-fortress-v4'
    variant_of = 'waterside-fortress-v2'
    variant_label = 'Height envelope and full spacing repair'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/war'
    aliases = ()
    keywords = ('waterside', 'fortress')

    def build(self):

        def L(n, a, b):
            self.add_line(n, a, b)

        def P(n, *p, closed=False):
            self.add_polyline(n, *p, closed=closed)

        def A(n, a, b, r, ry=None, s=True):
            self.add_arc(n, a, b, radius_x=r, radius_y=ry or r, sweep=s)

        def J(a, b):
            self.relate('connect', a, b)

        def C(n, x, y, r):
            A(n + '-upper', (x - r, y), (x + r, y), r)
            A(n + '-lower', (x + r, y), (x - r, y), r)
            self.add_contour(n, n + '-upper', n + '-lower', closed=True)
        P('fort', (8, 40), (8, 34), (18, 22), (24, 22), (30, 22), (40, 32), (40, 40))
        P('flag', (24, 4), (38, 4), (34, 8), (38, 12), (24, 12), closed=True)
        L('pole', (24, 12), (24, 22))
        J('pole', 'flag')
        J('pole', 'fort')
        L('door-left', (22, 40), (22, 35))
        A('door-arch', (22, 35), (30, 35), 4)
        L('door-right', (30, 35), (30, 40))
        self.add_contour('door', 'door-left', 'door-arch', 'door-right')
        A('wave-a', (8, 40), (14, 40), 3, 4, s=False)
        A('wave-b', (14, 40), (22, 40), 4, 4, s=False)
        A('wave-c', (22, 40), (30, 40), 4, 4, s=False)
        A('wave-d', (30, 40), (40, 40), 5, 4, s=False)
        self.add_contour('water', 'wave-a', 'wave-b', 'wave-c', 'wave-d')
        J('water', 'fort')
        J('water', 'door')
