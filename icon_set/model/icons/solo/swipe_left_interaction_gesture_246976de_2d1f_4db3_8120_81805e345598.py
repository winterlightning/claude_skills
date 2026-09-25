from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = "246976de-2d1f-4db3-8120-81805e345598"
SOURCE_PATH = "pictographic-primitives/_uncategorized_20/gesture tap swipe left_246976de-2d1f-4db3-8120-81805e345598.svg"
AUTHOR = "gpt-6"

class SwipeLeftInteractionGesture(Solo48):
    icon_id = "swipe-left-interaction-gesture"
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    aliases = ("touch swipe left",)
    keywords = ("capsule", "arrow", "left")

    def build(self) -> None:
        # Tall capsule occupies the right side, leaving a clear left arrow lane.
        self.add_arc("capsule-top", (20, 14), (40, 14), radius_x=10, sweep=True)
        self.add_line("capsule-right", (40, 14), (40, 34))
        self.add_arc("capsule-bottom", (40, 34), (20, 34), radius_x=10, sweep=True)
        self.add_line("capsule-left", (20, 34), (20, 14))
        self.add_contour("capsule", "capsule-top", "capsule-right", "capsule-bottom", "capsule-left", closed=True)
        self.add_polyline("arrowhead", (12, 18), (8, 24), (12, 30))
        self.add_line("shaft", (8, 24), (12, 24))
        self.relate("connect", "arrowhead", "shaft")
