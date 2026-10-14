"""A full rounded sack with a flared mouth and a tied neck.

Keyshape VRECT_XL: (4, 0, 60, 64); chosen for the reference silhouette.
Construction reference: Lucide circle: coherent arc construction; no useful local sack match. Original and atomic-debug inspected.
Mirrored body uses circular shoulders tangent to the elliptical base. Two leftward tie ends preserve the source asymmetry.
Hosting measured with compose.py: plus passes, heart does not pass, check does not pass.

v2 (2026-09-30): resized onto the v2 CONTAINER64 keyshapes by container_v2_fit (tied-money-sack VRECT_XL -> VRECT_L). Lattice snap: shared columns and rows move together, gaps of 8 or less keep their size, stroke stays 4.

v3 (2026-10-07): redrawn for symbol room on v2 (container-combination64): a symbol of at least 24 fits with a 4 px gap.
"""

from ...keyshapes import Keyshape
from ._base import Container64

AUTHOR = 'claude-opus-5-5'


class TiedMoneySack(Container64):
    icon_id = 'tied-money-sack'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'container'
    categories = ('container',)
    aliases = ()
    keywords = ('tied', 'money', 'sack')

    def build(self) -> None:
        # SQUARE (was VRECT_L): the body swells from a neck at y 16 to the full keyshape width at y 41, so the
        # sack holds a symbol of 24 with a 4 px gap (was 21). Mirrored about x = 32 apart from the tie.
        self.add_bezier('body-left', (24, 16), ((11, 21), (6, 31), (6, 41)), ((6, 53), (17, 58), (32, 58)))
        self.add_bezier('body-right', (32, 58), ((47, 58), (58, 53), (58, 41)), ((58, 31), (53, 21), (40, 16)))
        self.add_line('neck', (40, 16), (24, 16))
        self.add_line('mouth-left', (24, 16), (20, 8))
        self.add_arc('mouth-top', (20, 8), (44, 8), radius_x=12, radius_y=2)
        self.add_line('mouth-right', (44, 8), (40, 16))
        self.add_line('tie-top', (24, 16), (16, 12))
        self.add_line('tie-bottom', (24, 16), (16, 20))
        self.add_contour('body', 'body-left', 'body-right', 'neck', closed=True)
        self.add_contour('mouth', 'mouth-left', 'mouth-top', 'mouth-right')
        self.relate('connect', 'body', 'mouth')
        self.relate('connect', 'tie-top', 'body')
        self.relate('connect', 'tie-top', 'mouth')
        self.relate('connect', 'tie-bottom', 'body')
        self.relate('connect', 'tie-bottom', 'mouth')
        self.relate('connect', 'tie-top', 'tie-bottom')
