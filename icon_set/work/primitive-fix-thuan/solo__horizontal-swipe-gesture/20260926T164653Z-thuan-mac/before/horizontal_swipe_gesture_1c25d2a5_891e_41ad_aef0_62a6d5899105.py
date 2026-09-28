from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = "1c25d2a5-891e-41ad-aef0-62a6d5899105"
SOURCE_PATH = "pictographic-primitives/_uncategorized_20/gesture tap swipe horizontal_1c25d2a5-891e-41ad-aef0-62a6d5899105.svg"
AUTHOR = "gpt-6"

class HorizontalSwipeGesture(Solo48):
    icon_id = "horizontal-swipe-gesture"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    categories = ("primitives", "primitives-generate")
    aliases = ("horizontal drag",)
    keywords = ("touch", "capsule", "left", "right")

    def build(self) -> None:
        # Central capsule and two opposed arrows share horizontal and vertical axes.
        self.add_arc("capsule-top", (18, 12), (30, 12), radius_x=6, sweep=True)
        self.add_line("capsule-right", (30, 12), (30, 36))
        self.add_arc("capsule-bottom", (30, 36), (18, 36), radius_x=6, sweep=True)
        self.add_line("capsule-left", (18, 36), (18, 12))
        self.add_contour("capsule", "capsule-top", "capsule-right", "capsule-bottom", "capsule-left", closed=True)
        self.add_polyline("left-head", (10, 20), (6, 24), (10, 28))
        self.add_line("left-shaft", (6, 24), (10, 24))
        self.relate("connect", "left-head", "left-shaft")
        self.add_polyline("right-head", (38, 20), (42, 24), (38, 28))
        self.add_line("right-shaft", (38, 24), (42, 24))
        self.relate("connect", "right-head", "right-shaft")
