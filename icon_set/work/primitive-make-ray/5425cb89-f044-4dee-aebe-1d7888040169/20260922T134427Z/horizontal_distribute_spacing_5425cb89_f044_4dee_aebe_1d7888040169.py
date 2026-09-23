"""Parallel rails with outward-facing chevrons for horizontal distribution."""

from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48


SOURCE_ICON_ID = "5425cb89-f044-4dee-aebe-1d7888040169"
SOURCE_PATH = "pictographic-primitives/_uncategorized_01/align left right_5425cb89-f044-4dee-aebe-1d7888040169.svg"
AUTHOR = "gpt-5"


class HorizontalDistributeSpacing(Solo48):
    icon_id = "horizontal-distribute-spacing"
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "actions/alignment"
    aliases = ("distribute-horizontal", "space-left-right")
    keywords = ("align", "distribute", "spacing", "rails", "chevrons")

    def build(self) -> None:
        # Plan: mirrored rails own the outer envelope. Two independently
        # mirrored chevrons point away from the center, with eight-unit gaps
        # between one another and between each tip and its rail.
        self.add_line("rail-left", (4, 8), (4, 40))
        self.add_line("rail-right", (44, 8), (44, 40))

        self.add_polyline("chevron-left", (20, 16), (12, 24), (20, 32))
        self.add_polyline("chevron-right", (28, 16), (36, 24), (28, 32))
