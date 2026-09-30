from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = "2122378f-042e-4e39-bc17-d9bd07419cbd"
SOURCE_PATH = "pictographic-primitives/_uncategorized_20/gesture swipe vertical up 2_2122378f-042e-4e39-bc17-d9bd07419cbd.svg"
AUTHOR = "gpt-6"

class HandSwipeUpGesture(Solo48):
    icon_id = "hand-swipe-up-gesture"
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    categories = ("primitives", "primitives-generate")
    aliases = ("pointing hand swipe up",)
    keywords = ("index finger", "hooked thumb", "arrow")

    def build(self) -> None:
        # Horizontal pointing finger sits over a small inward hooked thumb.
        self.add_polyline("hand", (4, 38), (4, 28), (18, 22), (40, 22), (44, 26), (40, 30), (26, 30), (26, 38), (20, 40), (4, 38), closed=True)
        self.add_polyline("arrowhead", (20, 12), (24, 8), (28, 12))
        self.add_line("shaft", (24, 8), (24, 14))
        self.relate("connect", "arrowhead", "shaft")
