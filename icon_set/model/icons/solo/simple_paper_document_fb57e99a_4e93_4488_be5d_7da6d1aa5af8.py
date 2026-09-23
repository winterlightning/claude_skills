"""A blank document with a clipped upper-right corner."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = "fb57e99a-4e93-4488-be5d-7da6d1aa5af8"
SOURCE_PATH = "pictographic-primitives/other/file 1_fb57e99a-4e93-4488-be5d-7da6d1aa5af8.svg"
AUTHOR = "gpt-6"


class SimplePaperDocument(Solo48):
    icon_id = "simple-paper-document"
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/document"
    aliases = ("blank file", "paper sheet")
    keywords = ("document", "file", "page")

    def build(self) -> None:
        # The folded-corner silhouette is the only identity-bearing detail.
        # Rounded lower and upper-left corners balance its angled top right.
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
