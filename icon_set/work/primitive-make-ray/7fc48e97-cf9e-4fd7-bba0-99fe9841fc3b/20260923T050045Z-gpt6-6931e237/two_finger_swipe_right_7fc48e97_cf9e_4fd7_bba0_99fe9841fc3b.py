from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = "7fc48e97-cf9e-4fd7-bba0-99fe9841fc3b"
SOURCE_PATH = "pictographic-primitives/_uncategorized_20/gesture flip right_7fc48e97-cf9e-4fd7-bba0-99fe9841fc3b.svg"
AUTHOR = "gpt-6"

class TwoFingerSwipeRight(Solo48):
    icon_id = "two-finger-swipe-right"
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "gestures/touch"
    aliases = ("flip right gesture", "two-finger right swipe")
    keywords = ("fingers", "arrow", "right")

    def build(self) -> None:
        # Matched fingertip arches below a rightward sloping motion arrow.
        for side, left in (("left", 4), ("right", 30)):
            self.add_line(f"{side}-wall-left", (left, 40), (left, 31))
            self.add_arc(f"{side}-tip", (left, 31), (left + 14, 31), radius_x=7, sweep=True)
            self.add_line(f"{side}-wall-right", (left + 14, 31), (left + 14, 40))
            self.add_contour(f"{side}-finger", f"{side}-wall-left", f"{side}-tip", f"{side}-wall-right")
        self.add_polyline("swipe-shaft", (20, 8), (28, 9), (36, 12), (42, 16))
        self.add_polyline("swipe-head", (36, 8), (42, 16), (34, 16))
        self.relate("connect", "swipe-shaft", "swipe-head")
