from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = "03865b1d-fc66-475a-9459-24a0071714cf"
SOURCE_PATH = "pictographic-primitives/_uncategorized_20/gesture swipe vertical down 2_03865b1d-fc66-475a-9459-24a0071714cf.svg"
AUTHOR = "gpt-6"

class HandGestureVerticalSwipeDown(Solo48):
    icon_id = "hand-gesture-vertical-swipe-down"
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    aliases = ("down swipe hand",)
    keywords = ("pointing", "thumb", "curved arrow")

    def build(self) -> None:
        # Right-pointing hand stays left of a bowed downward arrow.
        self.add_polyline("hand", (4, 30), (4, 20), (16, 8), (24, 16), (28, 16), (30, 18), (30, 22), (28, 24), (22, 24), (18, 32), (4, 30), closed=True)
        self.add_polyline("swipe", (40, 8), (44, 20), (40, 32), (32, 40))
        self.add_polyline("arrowhead", (34, 32), (32, 40), (40, 38))
        self.relate("connect", "swipe", "arrowhead")
