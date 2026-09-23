"""A sheltering hand above a baby tucked into a diagonal swaddle.

Symbol plan: one open hand contour floats above a baby whose head and wrap
share a continuous outer contour. The wrap fold is a single inner line.
The SQUARE keyshape uses centerline extremes x=6..42 and y=6..42.
"""

from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "a8c124ba-bd78-456b-87fd-6763a1095d57"
SOURCE_PATH = "pictographic-primitives/_uncategorized_23/infancy care_a8c124ba-bd78-456b-87fd-6763a1095d57.svg"
AUTHOR = "gpt-6"


class HandProtectingSwaddledBaby(Solo48):
    icon_id = "hand-protecting-swaddled-baby"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "people/family"
    aliases = ("infant care", "protect baby")
    keywords = ("hand", "baby", "swaddle", "protect", "care")

    def build(self) -> None:
        # The finger reaches left; the two wrist ends deliberately stay open.
        self.add_line("hand-top", (42, 6), (30, 6))
        self.add_line("hand-slope", (30, 6), (18, 12))
        self.add_arc("hand-tip", (18, 12), (18, 16), radius_x=2, sweep=False)
        self.add_line("hand-under", (18, 16), (24, 16))
        self.add_line("hand-thumb", (24, 16), (30, 14))
        self.add_line("hand-palm", (30, 14), (42, 14))
        self.add_contour("hand", "hand-top", "hand-slope", "hand-tip", "hand-under", "hand-thumb", "hand-palm")

        # The baby's circular head joins the wrap at its right shoulder.
        self.add_arc("head-left-lower", (13, 38), (6, 31), radius_x=7)
        self.add_arc("head-left-upper", (6, 31), (13, 24), radius_x=7)
        self.add_arc("head-right-upper", (13, 24), (20, 31), radius_x=7)
        self.add_line("wrap-shoulder", (20, 31), (32, 26))
        self.add_arc("wrap-right", (32, 26), (42, 36), radius_x=10)
        self.add_arc("wrap-bottom", (42, 36), (36, 42), radius_x=6)
        self.add_line("wrap-base", (36, 42), (22, 42))
        self.add_line("wrap-lower-left", (22, 42), (13, 38))
        self.add_contour("baby-and-swaddle", "head-left-lower", "head-left-upper", "head-right-upper", "wrap-shoulder", "wrap-right", "wrap-bottom", "wrap-base", "wrap-lower-left", closed=True)
        self.add_line("swaddle-fold", (20, 31), (22, 40))
        self.relate("connect", "swaddle-fold", "head-right-upper")
