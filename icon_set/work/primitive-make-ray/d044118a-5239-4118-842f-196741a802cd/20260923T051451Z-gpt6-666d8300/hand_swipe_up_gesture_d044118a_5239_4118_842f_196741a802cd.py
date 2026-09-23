from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = "d044118a-5239-4118-842f-196741a802cd"
SOURCE_PATH = "pictographic-primitives/_uncategorized_20/gesture swipe vertical up_d044118a-5239-4118-842f-196741a802cd.svg"
AUTHOR = "gpt-6"

class HandSwipeUpGesture(Solo48):
    icon_id = "hand-swipe-up-gesture"
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "gestures/touch"
    aliases = ("horizontal finger swipe up",)
    keywords = ("finger", "palm", "up arrow")

    def build(self) -> None:
        # Long open finger with a separate lower palm contour beneath its wrist.
        self.add_line("finger-top", (4, 24), (38, 24))
        self.add_arc("fingertip", (38, 24), (38, 36), radius_x=6, sweep=True)
        self.add_line("finger-bottom", (38, 36), (26, 36))
        self.add_contour("finger", "finger-top", "fingertip", "finger-bottom")
        self.add_polyline("palm-lower", (4, 38), (12, 38), (18, 40))
        self.add_polyline("arrowhead", (20, 12), (24, 8), (28, 12))
        self.add_line("shaft", (24, 8), (24, 16))
        self.relate("connect", "arrowhead", "shaft")
