from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = "a954eb9f-9852-4a8c-917c-d8e5f407cf7e"
SOURCE_PATH = "pictographic-primitives/_uncategorized_20/gesture scroll_a954eb9f-9852-4a8c-917c-d8e5f407cf7e.svg"
AUTHOR = "gpt-6"

class VerticalTwoFingerScrollGesture(Solo48):
    icon_id = "vertical-two-finger-scroll-gesture"
    keyshape = Keyshape.VRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    categories = ("primitives", "primitives-generate")
    aliases = ("two-finger scroll", "vertical scroll gesture")
    keywords = ("fingers", "up", "down", "arrows")

    def build(self) -> None:
        # Two radius-7 fingertip arches meet at one central valley.
        self.add_line("left-wall", (10, 30), (10, 27))
        self.add_arc("left-tip", (10, 27), (24, 27), radius_x=7, sweep=True)
        self.add_arc("right-tip", (24, 27), (38, 27), radius_x=7, sweep=True)
        self.add_line("right-wall", (38, 27), (38, 30))
        self.add_contour("finger-pair", "left-wall", "left-tip", "right-tip", "right-wall")
        self.add_line("valley-wall", (24, 27), (24, 30))
        self.relate("connect", "finger-pair", "valley-wall")
        self.add_polyline("up-head", (20, 8), (24, 4), (28, 8))
        self.add_line("up-shaft", (24, 4), (24, 12))
        self.relate("connect", "up-head", "up-shaft")
        self.add_polyline("down-head", (20, 40), (24, 44), (28, 40))
        self.add_line("down-shaft", (24, 38), (24, 44))
        self.relate("connect", "down-head", "down-shaft")
