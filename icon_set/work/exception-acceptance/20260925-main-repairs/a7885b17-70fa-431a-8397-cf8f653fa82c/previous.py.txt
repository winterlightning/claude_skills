"""A clipped-corner source file with opposing code chevrons."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = "a7885b17-70fa-431a-8397-cf8f653fa82c"
SOURCE_PATH = "pictographic-primitives/other/file code left_a7885b17-70fa-431a-8397-cf8f653fa82c.svg"
AUTHOR = "gpt-6"


class SourceCodeFile(Solo48):
    icon_id = "source-code-file"
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/document"
    aliases = ("code file", "source document")
    keywords = ("programming", "code", "file", "markup")

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
        # Mirrored angle brackets are the complete code glyph in the source.
        self.add_polyline("left-bracket", (20, 17), (17, 24), (20, 31))
        self.add_polyline("right-bracket", (28, 17), (31, 24), (28, 31))
