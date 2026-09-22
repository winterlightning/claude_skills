"""Stylized five with an enclosed circular cross.
Plan: VRECT_L extremes (8,4)-(40,44); bowl centered at (24,28),
outer radius 16, inner ring radius 8, central cross arms 2 each axis.
Keep the numeral stem and bar plus both nested symbols from the reference.
Lucide circle-x informs the closed ring and two crossing straight strokes.
The nested cross/ring spacing may require review; do not erase either feature.
"""
from icon_set.model.icons.solo._base import Solo48
from icon_set.model.keyshapes import Keyshape
SOURCE_ICON_ID = "437f3f7e-d2b1-4eb1-8f9e-65a9b2b55503"
SOURCE_PATH = "pictographic-primitives/_uncategorized_01/500px logo_437f3f7e-d2b1-4eb1-8f9e-65a9b2b55503.svg"
AUTHOR = "gpt-6"

class StylizedNumberFiveWithCross(Solo48):
    icon_id = "stylized-number-five-with-cross"
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "symbols/numerals"
    aliases = ("500px logo", "five with cross")
    keywords = ("5", "five", "cross", "circle", "logo")

    def build(self):
        cx, cy, outer, inner, arm = 24, 28, 16, 8, 2
        self.add_line("top-bar", (34,4), (12,4))
        self.add_line("stem", (12,4), (12,20))
        self.add_arc("shoulder", (12,20), (cx,cy-outer), radius_x=12, radius_y=8)
        self.add_arc("bowl-upper", (cx,cy-outer), (cx+outer,cy), radius_x=outer)
        self.add_arc("bowl-lower-right", (cx+outer,cy), (cx,cy+outer), radius_x=outer)
        self.add_arc("bowl-lower-left", (cx,cy+outer), (cx-outer,cy), radius_x=outer)
        self.add_contour("five", "top-bar", "stem", "shoulder", "bowl-upper", "bowl-lower-right", "bowl-lower-left")
        self.add_arc("ring-top", (cx-inner,cy), (cx+inner,cy), radius_x=inner)
        self.add_arc("ring-bottom", (cx+inner,cy), (cx-inner,cy), radius_x=inner)
        self.add_contour("ring", "ring-top", "ring-bottom", closed=True)
        self.add_line("cross-descending", (cx-arm,cy-arm), (cx+arm,cy+arm))
        self.add_line("cross-ascending", (cx-arm,cy+arm), (cx+arm,cy-arm))
