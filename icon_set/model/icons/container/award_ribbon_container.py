"""A round award badge with two folded ribbon tails.

VRECT_L: centerline extremes (10,2)-(54,62), visible (8,0)-(56,64).
A circular face carries the identity; mirrored angular tails retain the
folded ribbon. Lucide award informs the circle and attached ribbon, while
the supplied references supply the two-tail silhouette. The curved crossed
folds of the first reference are reduced to the clearer symmetric second.
Batch 01 hosting measured with compose.py: plus, heart pass. check do not pass (including uncertified review).
"""

from ...keyshapes import Keyshape
from ._base import Container64


class AwardRibbonContainer(Container64):
    icon_id = 'award-ribbon-container'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "containers"
    aliases = ('circular-award-medal-ribbon', 'circular-award-ribbon-badge')
    keywords = ('award', 'ribbon', 'container')

    def build(self) -> None:
        self.add_arc("medal-top", (12, 22), (52, 22), radius_x=20)
        self.add_arc("medal-bottom", (52, 22), (12, 22), radius_x=20)
        self.add_contour("medal", "medal-top", "medal-bottom", closed=True)
        self.add_polyline("ribbon-left", (20, 38), (10, 54), (20, 54), (24, 62), (32, 42))
        self.add_polyline("ribbon-right", (44, 38), (54, 54), (44, 54), (40, 62), (32, 42))
        self.relate("connect", "medal", "ribbon-left")
        self.relate("connect", "medal", "ribbon-right")
        self.relate("connect", "ribbon-left", "ribbon-right")
