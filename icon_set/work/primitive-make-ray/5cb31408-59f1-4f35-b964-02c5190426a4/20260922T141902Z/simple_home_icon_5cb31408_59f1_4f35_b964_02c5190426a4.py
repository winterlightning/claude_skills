"""A minimal open-bottom home outline with a softly rounded roof peak."""

from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48


SOURCE_ICON_ID = "5cb31408-59f1-4f35-b964-02c5190426a4"
SOURCE_PATH = "pictographic-primitives/_uncategorized_04/arrow up 3_5cb31408-59f1-4f35-b964-02c5190426a4.svg"
AUTHOR = "gpt-5"


class SimpleHomeIcon(Solo48):
    icon_id = "simple-home-icon"
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "places/buildings"
    aliases = ("home-outline", "house-outline")
    keywords = ("home", "house", "building", "roof", "outline")

    def build(self) -> None:
        # Plan: one vertically symmetric open contour owns both walls, matched
        # roof slopes, and a circular two-unit apex arc.
        self.add_line("wall-left", (8, 44), (8, 20))
        self.add_line("roof-left", (8, 20), (22, 6))
        self.add_arc("roof-apex", (22, 6), (26, 6), radius_x=2)
        self.add_line("roof-right", (26, 6), (40, 20))
        self.add_line("wall-right", (40, 20), (40, 44))
        self.add_contour(
            "home-outline",
            "wall-left",
            "roof-left",
            "roof-apex",
            "roof-right",
            "wall-right",
        )
