from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = "ff6baaa4-fe03-46f9-959c-fb6764074f58"
SOURCE_PATH = "pictographic-primitives/_uncategorized_20/gesture tap swipe right_ff6baaa4-fe03-46f9-959c-fb6764074f58.svg"
AUTHOR = "gpt-6"

class TapAndSwipeRightGesture(Solo48):
    icon_id = "tap-and-swipe-right-gesture"
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    aliases = ("finger tap swipe right",)
    keywords = ("finger", "contact arc", "right arrow")

    def build(self) -> None:
        # Contact semicircle encloses a narrow upright fingertip; arrow runs right.
        self.add_arc("contact-arc", (4, 20), (28, 20), radius_x=12, sweep=True)
        self.add_line("finger-left", (12, 40), (12, 24))
        self.add_arc("fingertip", (12, 24), (20, 24), radius_x=4, sweep=True)
        self.add_line("finger-right", (20, 24), (20, 40))
        self.add_contour("finger", "finger-left", "fingertip", "finger-right")
        self.add_polyline("arrowhead", (36, 14), (44, 20), (36, 26))
        self.add_line("shaft", (36, 20), (44, 20))
        self.relate("connect", "arrowhead", "shaft")
