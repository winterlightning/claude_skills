"""Downward thumb gesture enclosed by the source's circular frame."""
from ...keyshapes import Keyshape
from ._base import Sub32
from ._compact_reference_helpers import circle

SOURCE_ICON_ID = "27b101c0-52f9-45b3-8377-a962c80b316c"
SOURCE_PATH = "pictographic-primitives/state/circle thumbs down_27b101c0-52f9-45b3-8377-a962c80b316c.svg"
AUTHOR = 'gpt-6'
SOURCE_PARTS = ('enclosing circle', 'cuff', 'downward thumb hand')
REPAIR_PLAN = {'concept': 'Circular Thumbs Down Symbol', 'core_parts': ('enclosing circle', 'cuff', 'downward thumb hand'), 'flexible_parts': 'separate overlapping cuff line', 'ladder': 'Inked cuff edge merged into the hand outline and thumb moved inward'}



class DrawingVariant2(Sub32):
    icon_id = "circular-thumbs-down-symbol-v2"
    variant_label = 'Inked cuff edge merged into the hand outline and thumb moved inward'
    keyshape = Keyshape.CIRCLE
    semantic_role = "SUB"
    semantic_kind = "state"
    category = "state"
    categories = ("state",)
    aliases = ("dislike-circle", "thumbs-down-circle")
    keywords = ("thumb", "down", "dislike", "negative")

    def build(self):
        circle(self, "frame", 16, 16, 14)
        self.add_bezier("hand", (10, 12), ((13, 12), (13, 10), (17, 10)), ((20, 10), (21, 11), (22, 14)), ((22, 17), (23, 19), (22, 20)), ((19, 20), (18, 20), (18, 20)), ((19, 22), (18, 23), (16, 23)), ((14, 23), (13, 20), (10, 20)), ((10, 20), (10, 18), (10, 12)))
        self.add_contour("thumb", "hand", closed=True)
