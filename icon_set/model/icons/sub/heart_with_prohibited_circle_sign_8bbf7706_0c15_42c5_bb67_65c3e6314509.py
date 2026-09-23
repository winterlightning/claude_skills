"""Heart inside a prohibition circle with the source's two exposed slash ends."""
from ...keyshapes import Keyshape
from ._base import Sub32
from ._compact_reference_helpers import circle

SOURCE_ICON_ID = "8bbf7706-0c15-42c5-bb67-65c3e6314509"
SOURCE_PATH = "pictographic-primitives/other/slash heart_8bbf7706-0c15-42c5-bb67-65c3e6314509.svg"
AUTHOR = "gpt-5"


class Drawing(Sub32):
    icon_id = "heart-with-prohibited-circle-sign"
    keyshape = Keyshape.CIRCLE
    semantic_role = "SUB"
    semantic_kind = "state"
    category = "primitives/state"
    aliases = ("no-heart", "heart-prohibited")
    keywords = ("heart", "prohibited", "ban", "slash", "no")

    def build(self):
        circle(self, "frame", 16, 16, 14)
        self.add_line("slash-upper", (4, 9), (8, 11))
        self.add_line("slash-lower", (24, 21), (28, 23))
        self.add_bezier("heart", (16, 24), ((9, 18), (8, 15), (8, 12)), ((8, 8), (13, 7), (16, 11)), ((19, 7), (24, 8), (24, 12)), ((24, 16), (21, 19), (16, 24)))
        self.add_contour("heart-shape", "heart", closed=True)
