"""A clipped-corner data document with two rows of binary digits."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "470b12d0-fbc3-4ff0-a9a3-8290363fff35"
SOURCE_PATH = "pictographic-primitives/other/file binary_470b12d0-fbc3-4ff0-a9a3-8290363fff35.svg"
AUTHOR = "gpt-6"


class BinaryDataDocument(Solo48):
    icon_id = "binary-data-document"
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/document"
    aliases = ("binary file", "digital data file")
    keywords = ("binary", "data", "code", "file")

    def build(self) -> None:
        self.add_line("top", (12, 4), (31, 4))
        self.add_line("fold-angle", (31, 4), (40, 13))
        self.add_line("right", (40, 13), (40, 40))
        self.add_arc("corner-se", (40, 40), (36, 44), radius_x=4)
        self.add_line("bottom", (36, 44), (12, 44))
        self.add_arc("corner-sw", (12, 44), (8, 40), radius_x=4)
        self.add_line("left", (8, 40), (8, 8))
        self.add_arc("corner-nw", (8, 8), (12, 4), radius_x=4)
        self.add_contour("page-outline", "top", "fold-angle", "right",
                         "corner-se", "bottom", "corner-sw", "left",
                         "corner-nw", closed=True)
        # Two rows retain the binary reading order. The source's extra two
        # upper-row ones cannot retain SOLO48 clearance inside this file.
        self.add_line("top-one", (17, 14), (17, 20))
        self.add_arc("top-zero-upper", (30, 17), (26, 17),
                     radius_x=2, radius_y=3, sweep=False)
        self.add_arc("top-zero-lower", (26, 17), (30, 17),
                     radius_x=2, radius_y=3, sweep=False)
        self.add_contour("top-zero", "top-zero-upper", "top-zero-lower", closed=True)
        self.add_arc("bottom-zero-upper", (22, 31), (18, 31),
                     radius_x=2, radius_y=3, sweep=False)
        self.add_arc("bottom-zero-lower", (18, 31), (22, 31),
                     radius_x=2, radius_y=3, sweep=False)
        self.add_contour("bottom-zero", "bottom-zero-upper", "bottom-zero-lower", closed=True)
        self.add_line("bottom-one", (31, 28), (31, 34))
