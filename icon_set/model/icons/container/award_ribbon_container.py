"""A round award badge with two folded ribbon tails.

VRECT_L: centerline extremes (10,2)-(54,62), visible (8,0)-(56,64).
A circular face carries the identity; mirrored angular tails retain the
folded ribbon. Lucide award informs the circle and attached ribbon, while
the supplied references supply the two-tail silhouette. The curved crossed
folds of the first reference are reduced to the clearer symmetric second.
Batch 01 hosting measured with compose.py: plus, heart pass. check do not pass (including uncertified review).

v2 (2026-09-30): resized onto the v2 CONTAINER64 keyshapes by container_v2_fit (award-ribbon-container VRECT_L -> VRECT_M). Lattice snap: shared columns and rows move together, gaps of 8 or less keep their size, stroke stays 4.

v3 (2026-10-07): redrawn for symbol room on v2 (container-combination64): the shape caps it below 24, now it takes a 20 symbol with a 4 px gap.
"""

from ...keyshapes import Keyshape
from ._base import Container64

AUTHOR = 'claude-opus-5-5'


class AwardRibbonContainer(Container64):
    icon_id = 'award-ribbon-container'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'container'
    categories = ('container',)
    aliases = ('circular-award-medal-ribbon', 'circular-award-ribbon-badge')
    keywords = ('award', 'ribbon', 'container')

    def build(self) -> None:
        # VRECT_L (was VRECT_M): medal r22 about (32,26) (was r18) with the two ribbon tails below it to 60, so the
        # medal holds a symbol of 20 with a 4 px gap (was 17). Mirrored about x = 32.
        self.add_arc('medal-top', (10, 26), (54, 26), radius_x=22)
        self.add_arc('medal-bottom', (54, 26), (10, 26), radius_x=22)
        self.add_line('ribbon-left-1', (22, 46), (15, 58))
        self.add_line('ribbon-left-2', (15, 58), (22, 57))
        self.add_line('ribbon-left-3', (22, 57), (26, 60))
        self.add_line('ribbon-left-4', (26, 60), (32, 48))
        self.add_line('ribbon-right-1', (42, 46), (49, 58))
        self.add_line('ribbon-right-2', (49, 58), (42, 57))
        self.add_line('ribbon-right-3', (42, 57), (38, 60))
        self.add_line('ribbon-right-4', (38, 60), (32, 48))
        self.add_contour('medal', 'medal-top', 'medal-bottom', closed=True)
        self.add_contour('ribbon-left', 'ribbon-left-1', 'ribbon-left-2', 'ribbon-left-3', 'ribbon-left-4')
        self.add_contour('ribbon-right', 'ribbon-right-1', 'ribbon-right-2', 'ribbon-right-3', 'ribbon-right-4')
        self.relate('connect', 'medal', 'ribbon-left')
        self.relate('connect', 'medal', 'ribbon-right')
        self.relate('connect', 'ribbon-left', 'ribbon-right')
