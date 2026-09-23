from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = "7527d1e3-c6a9-40f4-9897-718ae8aaa5f4"
SOURCE_PATH = "pictographic-primitives/_uncategorized_20/gesture tap all direction 1_7527d1e3-c6a9-40f4-9897-718ae8aaa5f4.svg"
AUTHOR = "gpt-6"

class VerticalSwipeGesture(Solo48):
    icon_id = "vertical-swipe-gesture-solo"
    keyshape = Keyshape.VRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "gestures/touch"
    aliases = ("fingernail vertical swipe",)
    keywords = ("finger", "nail", "up", "down")

    def build(self) -> None:
        # Broad fingertip encloses one compact nail, flanked vertically by arrows.
        self.add_line("finger-left", (10, 32), (10, 28))
        self.add_arc("fingertip", (10, 28), (38, 28), radius_x=14, sweep=True)
        self.add_line("finger-right", (38, 28), (38, 32))
        self.add_contour("finger", "finger-left", "fingertip", "finger-right")
        self.add_polyline("nail", (20, 31), (20, 27), (22, 23), (26, 23), (28, 27), (28, 31), (20, 31), closed=True)
        self.add_polyline("up-head", (20, 6), (24, 4), (28, 6))
        self.add_line("up-shaft", (24, 4), (24, 6))
        self.relate("connect", "up-head", "up-shaft")
        self.add_polyline("down-head", (20, 40), (24, 44), (28, 40))
        self.add_line("down-shaft", (24, 39), (24, 44))
        self.relate("connect", "down-head", "down-shaft")
