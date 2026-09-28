"""One-finger vertical swipe gesture.
Plan: VRECT_M allocates height to the up/down movement marks. Rounded index tip, open palm and two direction marks reviewed at 48px in both themes.
Reduction: Very short arrow shafts omitted; up/down chevrons retain direction. Palm simplified.
Construction references: Lucide hand original and atomic-debug: rounded finger tip and coherent broad palm; human-reference.md applies to the hand.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = "db37e620-1eb0-4c99-bce3-2c53b5c5fa76"
SOURCE_PATH = 'pictographic-primitives/_uncategorized_20/gesture swipe vertical 3_db37e620-1eb0-4c99-bce3-2c53b5c5fa76.svg'
AUTHOR = "gpt-6"

class OneFingerVerticalSwipeGesture(Solo48):
    icon_id = "one-finger-vertical-swipe-gesture"
    keyshape = Keyshape.VRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "gestures/touch"
    aliases = ("single-finger vertical swipe",)
    keywords = ("hand", "finger", "up", "down")

    def build(self) -> None:
        # Raised index finger and left thumb sit between repeated vertical arrows.
        self.add_polyline('hand-left',(10,28),(16,24),(18,26),(18,20))
        self.add_arc('fingertip',(18,20),(26,20),radius_x=4)
        self.add_polyline('hand-right',(26,20),(26,24),(38,24),(38,32),(18,32),(10,28))
        self.relate('connect','hand-left','fingertip')
        self.relate('connect','hand-right','fingertip')
        self.relate('connect','hand-right','hand-left')
        self.add_polyline("up-head", (20, 8), (24, 4), (28, 8))
        self.add_polyline("down-head", (20, 40), (24, 44), (28, 40))
