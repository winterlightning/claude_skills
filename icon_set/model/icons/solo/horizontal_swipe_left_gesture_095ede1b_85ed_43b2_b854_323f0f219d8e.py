from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = "095ede1b-85ed-43b2-b854-323f0f219d8e"
SOURCE_PATH = "pictographic-primitives/_uncategorized_20/gesture swipe horizontal left_095ede1b-85ed-43b2-b854-323f0f219d8e.svg"
AUTHOR = "gpt-6"

class HorizontalSwipeLeftGesture(Solo48):
    icon_id = "horizontal-swipe-left-gesture"
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    aliases = ("finger swipe left",)
    keywords = ("finger", "arrow", "left")

    def build(self) -> None:
        # Tall rounded finger remains right of a gently rising left arrow.
        self.add_line("finger-left", (24, 40), (24, 18))
        self.add_arc("fingertip", (24, 18), (44, 18), radius_x=10, sweep=True)
        self.add_line("finger-right", (44, 18), (44, 40))
        self.add_contour("finger", "finger-left", "fingertip", "finger-right")
        self.add_line("swipe-shaft", (16, 22), (4, 24))
        self.add_polyline("arrowhead", (10, 16), (4, 24), (12, 30))
        self.relate("connect", "swipe-shaft", "arrowhead")
