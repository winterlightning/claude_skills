from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = "29be15de-fd49-4163-972a-6f0743088f4e"
SOURCE_PATH = "pictographic-primitives/_uncategorized_20/gesture swipe vertical 1_29be15de-fd49-4163-972a-6f0743088f4e.svg"
AUTHOR = "gpt-6"

class VerticalSwipeGesture(Solo48):
    icon_id = "vertical-swipe-gesture"
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    categories = ("primitives", "primitives-generate")
    aliases = ("finger vertical swipe",)
    keywords = ("finger", "up", "down", "arrows")

    def build(self) -> None:
        # Open horizontal finger has one rounded tip and arrows above and below.
        self.add_line("finger-top", (4, 20), (40, 20))
        self.add_arc("fingertip", (40, 20), (40, 28), radius_x=4, sweep=True)
        self.add_line("finger-bottom", (40, 28), (4, 28))
        self.add_contour("finger", "finger-top", "fingertip", "finger-bottom")
        self.add_polyline("up-head", (20, 12), (24, 8), (28, 12))
        self.add_line("up-shaft", (24, 8), (24, 12))
        self.relate("connect", "up-head", "up-shaft")
        self.add_polyline("down-head", (20, 36), (24, 40), (28, 36))
        self.add_line("down-shaft", (24, 36), (24, 40))
        self.relate("connect", "down-head", "down-shaft")
