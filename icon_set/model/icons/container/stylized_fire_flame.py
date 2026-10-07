"""An asymmetric flame enclosure with two pointed tongues and a rounded base.

VRECT_L: (8, 0, 56, 64); chosen for the source silhouette.
Lucide flame: curved bowl and uneven flame tongues; asymmetry preserves upward movement; original and atomic-debug inspected for construction.
Source details retained; export irregularities simplified.
Hosting measured with compose.py: plus blocked, heart blocked, check blocked.

v2 (2026-09-30): resized onto the v2 CONTAINER64 keyshapes by container_v2_fit (stylized-fire-flame VRECT_L -> VRECT_M). Lattice snap: shared columns and rows move together, gaps of 8 or less keep their size, stroke stays 4.

v3 (2026-10-07): redrawn for symbol room on v2 (container-combination64): the shape caps it below 24, now it takes a 20 symbol with a 4 px gap.
"""

from ...keyshapes import Keyshape
from ._base import Container64

AUTHOR = 'claude-opus-5-5'


class StylizedFireFlame(Container64):
    icon_id = 'stylized-fire-flame'
    keyshape = Keyshape.VRECT_L
    aliases = ()
    keywords = ('stylized', 'fire', 'flame')

    def build(self) -> None:
        # VRECT_L (was VRECT_M): a full round base (10..54, bottom 60) rising to the tip (30,4), with the second
        # tongue tucked high on the left (19,18)-(25,24) so the body holds a symbol of 20 with a 4 px gap (was 18.5).
        self.add_bezier('flame-outer', (30, 4), ((42, 14), (54, 27), (54, 40)), ((54, 51), (44, 60), (32, 60)),
                        ((20, 60), (10, 51), (10, 40)), ((10, 31), (14, 24), (19, 18)))
        self.add_bezier('flame-tongue', (19, 18), ((20, 22), (22, 24), (25, 24)))
        self.add_bezier('flame-inner', (25, 24), ((25, 16), (27, 10), (30, 4)))
        self.add_contour('flame', 'flame-outer', 'flame-tongue', 'flame-inner', closed=True)
