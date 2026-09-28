"""Single-finger right-swipe gesture.
Plan: HRECT_L gives room to the contact halo and right arrow. Rounded fingertip and widened thumb/base band remain clear in both themes.
Reduction: Palm creases omitted; index, thumb, halo and right arrow retained.
Construction references: Lucide hand original and atomic-debug: semicircular fingertip; human-reference.md reviewed.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = "3b0fa0d0-112f-4a7d-9586-70fd5b30cbaa"
SOURCE_PATH = 'pictographic-primitives/_uncategorized_20/gesture tap swipe right 1_3b0fa0d0-112f-4a7d-9586-70fd5b30cbaa.svg'
AUTHOR = "gpt-6"

class HandSwipeRightGesture(Solo48):
    icon_id = "hand-swipe-right-gesture"
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "gestures/touch"
    aliases = ("tap swipe right",)
    keywords = ("hand", "contact arc", "right arrow")

    def build(self) -> None:
        # Small left-thumb hand under an open contact halo, with a right arrow.
        self.add_polyline('hand-left',(4,36),(4,30),(8,28),(14,30),(14,22))
        self.add_arc('fingertip',(14,22),(22,22),radius_x=4)
        self.add_polyline('hand-right',(22,22),(22,28),(28,28),(28,40),(12,40),(4,36))
        self.relate('connect','hand-left','fingertip')
        self.relate('connect','fingertip','hand-right')
        self.relate('connect','hand-left','hand-right')
        self.add_arc("contact-arc", (6, 20), (30, 20), radius_x=12, sweep=True)
        self.add_polyline("arrowhead", (38, 14), (44, 20), (38, 26))
        self.add_line("shaft", (38, 20), (44, 20))
        self.relate("connect", "arrowhead", "shaft")
