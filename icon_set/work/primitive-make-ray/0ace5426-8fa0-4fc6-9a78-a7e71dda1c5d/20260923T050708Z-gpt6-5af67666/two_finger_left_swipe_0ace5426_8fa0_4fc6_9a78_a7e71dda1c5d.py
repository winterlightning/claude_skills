from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = "0ace5426-8fa0-4fc6-9a78-a7e71dda1c5d"
SOURCE_PATH = "pictographic-primitives/_uncategorized_20/gesture swipe horizontal left two fingers_0ace5426-8fa0-4fc6-9a78-a7e71dda1c5d.svg"
AUTHOR = "gpt-6"

class TwoFingerLeftSwipe(Solo48):
    icon_id = "two-finger-left-swipe"
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "gestures/touch"
    aliases = ("two-finger swipe left",)
    keywords = ("fingers", "left", "curved arrow")

    def build(self) -> None:
        # Mirrored upright fingertips sit below a leftward arched motion line.
        for side, left in (("left", 10), ("right", 28)):
            self.add_line(f"{side}-wall-left", (left, 40), (left, 29))
            self.add_arc(f"{side}-tip", (left, 29), (left + 10, 29), radius_x=5, sweep=True)
            self.add_line(f"{side}-wall-right", (left + 10, 29), (left + 10, 40))
            self.add_contour(f"{side}-finger", f"{side}-wall-left", f"{side}-tip", f"{side}-wall-right")
        self.add_arc("swipe", (44, 16), (4, 16), radius_x=20, radius_y=8, sweep=False)
        self.add_polyline("arrowhead", (10, 8), (4, 16), (10, 16))
        self.relate("connect", "swipe", "arrowhead")
