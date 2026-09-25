from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = "d98ff112-975f-484e-8360-e821f5790178"
SOURCE_PATH = "pictographic-primitives/_uncategorized_20/gesture swipe vertical up 1_d98ff112-975f-484e-8360-e821f5790178.svg"
AUTHOR = "gpt-6"

class HandSwipeUpGesture(Solo48):
    icon_id = "hand-swipe-up-gesture-d98ff112"
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    aliases = ("one-finger swipe up",)
    keywords = ("hand", "index finger", "up arrow")

    def build(self) -> None:
        # A raised index finger rises above a broad rounded palm and left thumb.
        self.add_polyline("hand", (8, 32), (8, 28), (12, 26), (18, 30), (18, 20), (22, 16), (26, 16), (30, 20), (30, 28), (34, 26), (38, 28), (40, 32), (40, 38), (36, 44), (16, 44), (8, 32), closed=True)
        self.add_polyline("arrowhead", (20, 8), (24, 4), (28, 8))
        self.add_line("shaft", (24, 4), (24, 8))
        self.relate("connect", "arrowhead", "shaft")
