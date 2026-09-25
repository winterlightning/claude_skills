"""love heart ranking: standalone repair of supplied reference.

Plan: Broad three-place podium. Keyshape HRECT_L.
Reduction: Rounded the heart lobes; preserved three podium sections.
Construction references: local Lucide originals and atomic-debug: heart.

All geometry is authored for SOLO48; earlier runs remain unchanged.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = "23d9de33-2d15-4372-8f12-18cd47ea7ba3"
SOURCE_PATH = "pictographic-primitives/_uncategorized_26/love heart ranking_23d9de33-2d15-4372-8f12-18cd47ea7ba3.svg"
AUTHOR = "gpt-6"


class HeartRankingPodium(Solo48):
    icon_id = 'heart-ranking-podium'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    aliases = ("love-ranking",)
    keywords = ("heart", "podium", "ranking", "winner")

    def build(self) -> None:
        axis = 24
        self.add_arc("heart-left", (14, 13), (24, 13), radius_x=5)
        self.add_arc("heart-right", (24, 13), (34, 13), radius_x=5)
        self.add_bezier("heart-bottom", (34, 13), ((34, 17), (28, 20), (24, 23)), ((20, 20), (14, 17), (14, 13)))
        self.add_contour("heart", "heart-left", "heart-right", "heart-bottom", closed=True)
        # A single connected stair profile retains three different heights.
        self.add_polyline("podium", (4, 40), (4, 34), (17, 34),
                          (17, 31), (31, 31), (31, 34),
                          (44, 34), (44, 40))
        self.add_line("left-center-seam", (17, 34), (17, 40))
        self.add_line("right-center-seam", (31, 34), (31, 40))
        self.relate("connect", "left-center-seam", "podium")
        self.relate("connect", "right-center-seam", "podium")
