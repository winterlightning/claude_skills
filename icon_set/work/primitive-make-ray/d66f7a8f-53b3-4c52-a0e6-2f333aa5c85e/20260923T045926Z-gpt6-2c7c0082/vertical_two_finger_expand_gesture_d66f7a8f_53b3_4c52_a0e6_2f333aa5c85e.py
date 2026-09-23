from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = "d66f7a8f-53b3-4c52-a0e6-2f333aa5c85e"
SOURCE_PATH = "pictographic-primitives/_uncategorized_20/gesture expand two fingers_d66f7a8f-53b3-4c52-a0e6-2f333aa5c85e.svg"
AUTHOR = "gpt-6"

class VerticalTwoFingerExpandGesture(Solo48):
    icon_id = "vertical-two-finger-expand-gesture"
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "gestures/touch"
    aliases = ("two finger expand", "spread up")
    keywords = ("fingers", "arrows", "vertical")

    def build(self) -> None:
        # Mirrored fingertips occupy the middle band; arrows repeat above and below.
        for side, left in (("left", 8), ("right", 30)):
            self.add_line(f"{side}-edge-left", (left, 28), (left, 23))
            self.add_arc(f"{side}-tip", (left, 23), (left + 10, 23), radius_x=5, sweep=True)
            self.add_line(f"{side}-edge-right", (left + 10, 23), (left + 10, 28))
            self.add_contour(f"{side}-finger", f"{side}-edge-left", f"{side}-tip", f"{side}-edge-right")
        self.add_polyline("upper-arrowhead", (20, 8), (24, 4), (28, 8))
        self.add_line("upper-shaft", (24, 4), (24, 10))
        self.relate("connect", "upper-arrowhead", "upper-shaft")
        self.add_polyline("lower-arrowhead", (20, 40), (24, 36), (28, 40))
        self.add_line("lower-shaft", (24, 36), (24, 44))
        self.relate("connect", "lower-arrowhead", "lower-shaft")
