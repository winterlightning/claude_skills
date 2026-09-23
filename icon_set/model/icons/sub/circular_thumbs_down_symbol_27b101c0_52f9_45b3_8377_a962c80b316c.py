"""Downward thumb gesture enclosed by the source's circular frame."""
from ...keyshapes import Keyshape
from ._base import Sub32
from ._compact_reference_helpers import circle

SOURCE_ICON_ID = "27b101c0-52f9-45b3-8377-a962c80b316c"
SOURCE_PATH = "pictographic-primitives/state/circle thumbs down_27b101c0-52f9-45b3-8377-a962c80b316c.svg"
AUTHOR = "gpt-5"


class Drawing(Sub32):
    icon_id = "circular-thumbs-down-symbol"
    keyshape = Keyshape.CIRCLE
    semantic_role = "SUB"
    semantic_kind = "state"
    category = "primitives/state"
    aliases = ("dislike-circle", "thumbs-down-circle")
    keywords = ("thumb", "down", "dislike", "negative")

    def build(self):
        circle(self, "frame", 16, 16, 14)
        self.add_line("cuff", (9, 11), (9, 20))
        self.add_bezier("hand", (9, 12), ((13, 12), (13, 10), (17, 10)), ((20, 10), (21, 11), (22, 14)), ((23, 17), (25, 20), (22, 20)), ((19, 20), (18, 20), (18, 20)), ((19, 23), (18, 26), (16, 26)), ((14, 26), (13, 21), (10, 20)), ((9, 20), (9, 18), (9, 12)))
        self.add_contour("thumb", "hand", closed=True)
