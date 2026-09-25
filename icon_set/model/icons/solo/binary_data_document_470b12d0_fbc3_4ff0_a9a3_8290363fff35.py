"""A clipped-corner data document with a binary one and zero."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = "470b12d0-fbc3-4ff0-a9a3-8290363fff35"
SOURCE_PATH = "pictographic-primitives/other/file binary_470b12d0-fbc3-4ff0-a9a3-8290363fff35.svg"
AUTHOR = "claude-fable-5-1"


class BinaryDataDocument(Solo48):
    icon_id = "binary-data-document"
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    aliases = ("binary file", "digital data file")
    keywords = ("binary", "data", "code", "file")

    def build(self) -> None:
        # Page: Lucide file outline with a short 5-unit fold so the digits
        # keep 9 units from the fold edge.
        self.add_line("top", (12, 4), (35, 4))
        self.add_line("fold-angle", (35, 4), (40, 9))
        self.add_line("right", (40, 9), (40, 40))
        self.add_arc("corner-se", (40, 40), (36, 44), radius_x=4)
        self.add_line("bottom", (36, 44), (12, 44))
        self.add_arc("corner-sw", (12, 44), (8, 40), radius_x=4)
        self.add_line("left", (8, 40), (8, 8))
        self.add_arc("corner-nw", (8, 8), (12, 4), radius_x=4)
        self.add_contour("page-outline", "top", "fold-angle", "right",
                         "corner-se", "bottom", "corner-sw", "left",
                         "corner-nw", closed=True)
        # Binary "1" and "0" read top-left to bottom-right. The 14-unit band
        # inside the page cannot hold a side-by-side pair at 9 units of
        # clearance, so each row carries one digit; the zero is a complete
        # 8-unit circle with a 4-unit hole.
        self.add_line("one", (17, 13), (17, 21))
        self.add_arc("zero-upper", (31, 31), (23, 31), radius_x=4, sweep=False)
        self.add_arc("zero-lower", (23, 31), (31, 31), radius_x=4, sweep=False)
        self.add_contour("zero", "zero-upper", "zero-lower", closed=True)
