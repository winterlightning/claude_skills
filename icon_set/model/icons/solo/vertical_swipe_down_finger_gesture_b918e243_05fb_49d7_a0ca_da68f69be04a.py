from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = "b918e243-05fb-49d7-a0ca-da68f69be04a"
SOURCE_PATH = "pictographic-primitives/_uncategorized_20/gesture swipe vertical down_b918e243-05fb-49d7-a0ca-da68f69be04a.svg"
AUTHOR = "gpt-6"

class VerticalSwipeDownFingerGesture(Solo48):
    icon_id = "vertical-swipe-down-finger-gesture"
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "gestures/touch"
    aliases = ("finger scroll down",)
    keywords = ("fingernail", "arrow", "down")

    def build(self) -> None:
        # Horizontal finger and D-shaped nail stay left of a bowed down arrow.
        self.add_line("finger-top", (4, 10), (20, 10))
        self.add_arc("fingertip", (20, 10), (20, 38), radius_x=14, sweep=True)
        self.add_line("finger-bottom", (20, 38), (4, 38))
        self.add_contour("finger", "finger-top", "fingertip", "finger-bottom")
        self.add_polyline("nail", (12, 19), (20, 19), (24, 22), (24, 26), (20, 29), (12, 29), (12, 19), closed=True)
        self.add_polyline("swipe", (44, 8), (44, 30), (36, 40))
        self.add_polyline("arrowhead", (40, 34), (36, 40), (44, 38))
        self.relate("connect", "swipe", "arrowhead")
