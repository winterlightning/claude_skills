"""A full rounded sack with a flared mouth and a tied neck.

Keyshape VRECT_XL: (4, 0, 60, 64); chosen for the reference silhouette.
Construction reference: Lucide circle: coherent arc construction; no useful local sack match. Original and atomic-debug inspected.
Mirrored body uses circular shoulders tangent to the elliptical base. Two leftward tie ends preserve the source asymmetry.
Hosting measured with compose.py: plus passes, heart does not pass, check does not pass.

v2 (2026-09-30): resized onto the v2 CONTAINER64 keyshapes by container_v2_fit (tied-money-sack VRECT_XL -> VRECT_L). Lattice snap: shared columns and rows move together, gaps of 8 or less keep their size, stroke stays 4.
"""

from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.container._base import Container64

AUTHOR = 'claude-opus-5-5'


class TiedMoneySack(Container64):
    icon_id = 'tied-money-sack'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'container'
    categories = ('container',)
    aliases = ()
    keywords = ('tied', 'money', 'sack')

    def build(self) -> None:
        self.add_arc('body-left', (24, 19), (10, 49), radius_x=40, sweep=False)
        self.add_arc('body-sw', (10, 49), (32, 60), radius_x=22, radius_y=11, sweep=False)
        self.add_arc('body-se', (32, 60), (54, 49), radius_x=22, radius_y=11, sweep=False)
        self.add_arc('body-right', (54, 49), (40, 19), radius_x=40, sweep=False)
        self.add_line('neck', (40, 19), (24, 19))
        self.add_line('mouth-left', (24, 19), (20, 6))
        self.add_arc('mouth-top', (20, 6), (44, 6), radius_x=12, radius_y=2)
        self.add_line('mouth-right', (44, 6), (40, 19))
        self.add_line('tie-top', (24, 19), (14, 15))
        self.add_line('tie-bottom', (24, 19), (12, 26))
        self.add_contour('body', 'body-left', 'body-sw', 'body-se', 'body-right', 'neck', closed=True)
        self.add_contour('mouth', 'mouth-left', 'mouth-top', 'mouth-right')
        self.relate('connect', 'body', 'mouth')
        self.relate('connect', 'tie-top', 'body')
        self.relate('connect', 'tie-top', 'mouth')
        self.relate('connect', 'tie-bottom', 'body')
        self.relate('connect', 'tie-bottom', 'mouth')
        self.relate('connect', 'tie-top', 'tie-bottom')
