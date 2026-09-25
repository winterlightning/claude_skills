from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = "a3e6d289-ee88-4de3-ba1a-d29da5c5d1e9"
SOURCE_PATH = "pictographic-primitives/_uncategorized_20/gesture swipe vertical down two fingers_a3e6d289-ee88-4de3-ba1a-d29da5c5d1e9.svg"
AUTHOR = "gpt-6"

class TwoFingerSwipeDownGesture(Solo48):
    icon_id = "two-finger-swipe-down-gesture"
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "gestures/touch"
    aliases = ("two-finger scroll down",)
    keywords = ("fingers", "curved", "down arrow")

    def build(self) -> None:
        # Upper finger curls right; lower finger is a second open horizontal stroke.
        self.add_line("upper-finger-top", (4, 14), (28, 14))
        self.add_arc("upper-tip", (28, 14), (28, 22), radius_x=4, sweep=True)
        self.add_line("upper-finger-bottom", (28, 22), (4, 22))
        self.add_contour("upper-finger", "upper-finger-top", "upper-tip", "upper-finger-bottom")
        self.add_line("lower-finger", (4, 32), (20, 32))
        self.add_polyline("swipe", (38, 8), (44, 18), (44, 24), (42, 32), (34, 40))
        self.add_polyline("arrowhead", (30, 32), (34, 40), (42, 36))
        self.relate("connect", "swipe", "arrowhead")
