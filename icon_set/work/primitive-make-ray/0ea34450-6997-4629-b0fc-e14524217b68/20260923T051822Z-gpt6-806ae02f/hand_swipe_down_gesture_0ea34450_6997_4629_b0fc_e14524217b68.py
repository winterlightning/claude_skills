from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = "0ea34450-6997-4629-b0fc-e14524217b68"
SOURCE_PATH = "pictographic-primitives/_uncategorized_20/gesture tap swipe down 1_0ea34450-6997-4629-b0fc-e14524217b68.svg"
AUTHOR = "gpt-6"

class HandSwipeDownGesture(Solo48):
    icon_id = "hand-swipe-down-gesture"
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "gestures/touch"
    aliases = ("tap swipe down",)
    keywords = ("pointing hand", "contact arc", "down arrow")

    def build(self) -> None:
        # Compact right-pointing hand sits within a right-side contact arc.
        self.add_polyline("hand", (4, 28), (4, 20), (16, 14), (20, 12), (24, 18), (30, 18), (32, 22), (30, 26), (20, 26), (16, 28), (4, 28), closed=True)
        self.add_polyline("contact-arc", (28, 8), (36, 10), (42, 16), (44, 22), (44, 28), (40, 32))
        self.add_polyline("down-head", (20, 36), (24, 40), (28, 36))
        self.add_line("down-shaft", (24, 38), (24, 40))
        self.relate("connect", "down-head", "down-shaft")
