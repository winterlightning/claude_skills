from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = "3808dced-acba-4c34-8f9f-05ba44dfe152"
SOURCE_PATH = "pictographic-primitives/_uncategorized_20/gesture two finger flip right_3808dced-acba-4c34-8f9f-05ba44dfe152.svg"
AUTHOR = "gpt-6"

class TwoFingerSwipeRight(Solo48):
    icon_id = "two-finger-swipe-right"
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "gestures/touch"
    aliases = ("two-finger flip right",)
    keywords = ("hand", "spread fingers", "right arrow")

    def build(self) -> None:
        # Two raised finger peaks and a bent left thumb rise from one palm.
        self.add_polyline("hand", (8, 34), (8, 30), (12, 28), (18, 34), (14, 22), (16, 20), (20, 20), (22, 22), (24, 30), (28, 24), (30, 22), (32, 22), (34, 24), (32, 32), (38, 32), (40, 36), (38, 40), (16, 40), (8, 34), closed=True)
        self.add_line("shaft", (4, 12), (44, 12))
        self.add_polyline("arrowhead", (38, 8), (44, 12), (38, 16))
        self.relate("connect", "shaft", "arrowhead")
