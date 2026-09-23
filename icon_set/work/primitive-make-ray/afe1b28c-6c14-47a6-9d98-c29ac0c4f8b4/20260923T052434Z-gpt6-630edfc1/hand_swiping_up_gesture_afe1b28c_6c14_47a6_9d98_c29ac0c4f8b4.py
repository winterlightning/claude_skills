from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = "afe1b28c-6c14-47a6-9d98-c29ac0c4f8b4"
SOURCE_PATH = "pictographic-primitives/_uncategorized_20/gesture tap swipe up 1_afe1b28c-6c14-47a6-9d98-c29ac0c4f8b4.svg"
AUTHOR = "gpt-6"

class HandSwipingUpGesture(Solo48):
    icon_id = "hand-swiping-up-gesture"
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "gestures/touch"
    aliases = ("tap swipe up",)
    keywords = ("pointing hand", "contact arc", "up arrow")

    def build(self) -> None:
        # Rightward index sits within an open contact arc; upward arrow above.
        self.add_polyline("hand", (4, 36), (4, 30), (16, 24), (20, 22), (24, 26), (30, 26), (32, 30), (30, 34), (22, 34), (20, 40), (4, 36), closed=True)
        self.add_polyline("contact-arc", (38, 20), (42, 24), (44, 30), (42, 36), (38, 40))
        self.add_polyline("arrowhead", (20, 12), (24, 8), (28, 12))
        self.add_line("shaft", (24, 8), (24, 14))
        self.relate("connect", "arrowhead", "shaft")
