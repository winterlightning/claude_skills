"""A round award badge with two folded ribbon tails.

VRECT_L: centerline extremes (10,2)-(54,62), visible (8,0)-(56,64).
A circular face carries the identity; mirrored angular tails retain the
folded ribbon. Lucide award informs the circle and attached ribbon, while
the supplied references supply the two-tail silhouette. The curved crossed
folds of the first reference are reduced to the clearer symmetric second.
Batch 01 hosting measured with compose.py: plus, heart pass. check do not pass (including uncertified review).

v2 (2026-09-30): resized onto the v2 CONTAINER64 keyshapes by container_v2_fit (award-ribbon-container VRECT_L -> VRECT_M). Lattice snap: shared columns and rows move together, gaps of 8 or less keep their size, stroke stays 4.
"""

from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.container._base import Container64

AUTHOR = 'claude-opus-5-5'


class AwardRibbonContainer(Container64):
    icon_id = 'award-ribbon-container'
    keyshape = Keyshape.VRECT_M
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'container'
    categories = ('container',)
    aliases = ('circular-award-medal-ribbon', 'circular-award-ribbon-badge')
    keywords = ('award', 'ribbon', 'container')

    def build(self) -> None:
        self.add_arc('medal-top', (14, 22), (50, 22), radius_x=18)
        self.add_arc('medal-bottom', (50, 22), (14, 22), radius_x=18)
        self.add_line('ribbon-left-1', (21, 37), (12, 52))
        self.add_line('ribbon-left-2', (12, 52), (21, 52))
        self.add_line('ribbon-left-3', (21, 52), (25, 60))
        self.add_line('ribbon-left-4', (25, 60), (32, 41))
        self.add_line('ribbon-right-1', (43, 37), (52, 52))
        self.add_line('ribbon-right-2', (52, 52), (43, 52))
        self.add_line('ribbon-right-3', (43, 52), (39, 60))
        self.add_line('ribbon-right-4', (39, 60), (32, 41))
        self.add_contour('medal', 'medal-top', 'medal-bottom', closed=True)
        self.add_contour('ribbon-left', 'ribbon-left-1', 'ribbon-left-2', 'ribbon-left-3', 'ribbon-left-4')
        self.add_contour('ribbon-right', 'ribbon-right-1', 'ribbon-right-2', 'ribbon-right-3', 'ribbon-right-4')
        self.relate('connect', 'medal', 'ribbon-left')
        self.relate('connect', 'medal', 'ribbon-right')
        self.relate('connect', 'ribbon-left', 'ribbon-right')
