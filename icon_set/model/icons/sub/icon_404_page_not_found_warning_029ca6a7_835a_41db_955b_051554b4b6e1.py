"""Warning triangle with exclamation above the complete 404 code."""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = "029ca6a7-835a-41db-955b-051554b4b6e1"
SOURCE_PATH = "pictographic-primitives/state/warning with 400 error_029ca6a7-835a-41db-955b-051554b4b6e1.svg"
AUTHOR = "gpt-5"
TYPEFACE_GLYPH_IDS = ("digit-4", "digit-0", "digit-4")


class Drawing(Sub32):
    icon_id = "icon-404-page-not-found-warning"
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "state"
    category = "primitives/state"
    aliases = ("404-warning", "page-not-found")
    keywords = ("404", "warning", "error", "not found")

    def build(self):
        # Plan: one complete warning symbol over three repeated compact glyph slots.
        self.add_polyline("warning-frame", (16, 2), (27, 16), (5, 16), closed=True)
        self.add_line("exclamation-stem", (16, 6), (16, 10))
        self.add_dot("exclamation-dot", (16, 14))
        self.add_polyline("four-left", (2, 27), (6, 22), (6, 30))
        self.add_line("four-left-bar", (2, 27), (7, 27))
        self.add_arc("zero-top", (12, 26), (18, 26), radius_x=3, radius_y=4)
        self.add_arc("zero-bottom", (18, 26), (12, 26), radius_x=3, radius_y=4)
        self.add_contour("zero", "zero-top", "zero-bottom", closed=True)
        self.add_polyline("four-right", (23, 27), (28, 22), (28, 30))
        self.add_line("four-right-bar", (23, 27), (30, 27))
