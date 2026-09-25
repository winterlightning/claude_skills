from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = "244a7f4d-148d-4ae8-9b10-c840685823e9"
SOURCE_PATH = "pictographic-primitives/_uncategorized_20/gesture swipe vertical up 3_244a7f4d-148d-4ae8-9b10-c840685823e9.svg"
AUTHOR = "gpt-6"

class HandSwipeUpGesture(Solo48):
    icon_id = "hand-swipe-up-gesture-solo"
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "gestures/touch"
    aliases = ("cursor hand swipe up",)
    keywords = ("finger", "thumb", "up arrow")

    def build(self) -> None:
        # Raised diagonal thumb leads into a rightward rounded index finger.
        self.add_polyline("hand", (4, 38), (4, 30), (18, 24), (22, 22), (26, 24), (28, 28), (24, 30), (40, 30), (44, 34), (40, 38), (28, 38), (24, 40), (4, 38), closed=True)
        self.add_polyline("arrowhead", (20, 12), (24, 8), (28, 12))
        self.add_line("shaft", (24, 8), (24, 14))
        self.relate("connect", "arrowhead", "shaft")
