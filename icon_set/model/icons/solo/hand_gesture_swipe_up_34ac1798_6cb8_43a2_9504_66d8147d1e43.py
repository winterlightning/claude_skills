from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = "34ac1798-6cb8-43a2-9504-66d8147d1e43"
SOURCE_PATH = "pictographic-primitives/_uncategorized_20/gesture tap swipe up_34ac1798-6cb8-43a2-9504-66d8147d1e43.svg"
AUTHOR = "gpt-6"

class HandGestureSwipeUp(Solo48):
    icon_id = "hand-gesture-swipe-up"
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "gestures/touch"
    aliases = ("finger tap swipe up",)
    keywords = ("horizontal finger", "contact arc", "up arrow")

    def build(self) -> None:
        # Short horizontal fingertip faces a broad open right contact arc.
        self.add_line("finger-top", (4, 26), (28, 26))
        self.add_arc("fingertip", (28, 26), (28, 34), radius_x=4, sweep=True)
        self.add_line("finger-bottom", (28, 34), (4, 34))
        self.add_contour("finger", "finger-top", "fingertip", "finger-bottom")
        self.add_polyline("contact-arc", (34, 18), (40, 20), (44, 26), (44, 32), (40, 38), (38, 40))
        self.add_polyline("arrowhead", (20, 12), (24, 8), (28, 12))
        self.add_line("shaft", (24, 8), (24, 16))
        self.relate("connect", "arrowhead", "shaft")
