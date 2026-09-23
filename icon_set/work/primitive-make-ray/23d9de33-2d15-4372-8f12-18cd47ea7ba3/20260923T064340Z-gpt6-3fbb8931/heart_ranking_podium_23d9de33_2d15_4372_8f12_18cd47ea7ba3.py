"""A heart above a three-place ranking podium.

Plan: a symmetric heart is suspended over the tallest center block;
one baseline aligns the three blocks. Lucide heart informed the lobes,
and Lucide podium informed the staggered block tops.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "23d9de33-2d15-4372-8f12-18cd47ea7ba3"
SOURCE_PATH = "pictographic-primitives/_uncategorized_26/love heart ranking_23d9de33-2d15-4372-8f12-18cd47ea7ba3.svg"
AUTHOR = "gpt-6"


class HeartRankingPodium(Solo48):
    icon_id = "heart-ranking-podium"
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/award"
    aliases = ("love-ranking",)
    keywords = ("heart", "podium", "ranking", "winner")

    def build(self) -> None:
        axis = 24
        self.add_polyline("heart", (axis, 21), (14, 14), (14, 11),
                          (17, 8), (axis, 12), (31, 8),
                          (34, 11), (34, 14), closed=True)
        # A single connected stair profile retains three different heights.
        self.add_polyline("podium", (4, 40), (4, 34), (17, 34),
                          (17, 29), (31, 29), (31, 34),
                          (44, 34), (44, 40))
        self.add_line("left-center-seam", (17, 34), (17, 40))
        self.add_line("right-center-seam", (31, 34), (31, 40))
        self.relate("connect", "left-center-seam", "podium")
        self.relate("connect", "right-center-seam", "podium")
