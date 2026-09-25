"""An empty portrait document with its upper right corner folded.

Symbol plan: one closed page silhouette plus an L-shaped crease sharing both
endpoints with the outer contour. VRECT_M bounds x=10..38, y=4..44.
"""

from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = "5dd06ce3-348a-41d2-9e63-b33ccde8c90b"
SOURCE_PATH = "pictographic-primitives/_uncategorized_23/item_5dd06ce3-348a-41d2-9e63-b33ccde8c90b.svg"
AUTHOR = "gpt-6"


class BlankDocumentFile(Solo48):
    icon_id = "blank-document-file"
    keyshape = Keyshape.VRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    aliases = ("blank file", "empty document")
    keywords = ("document", "file", "paper", "folded", "blank")

    def build(self) -> None:
        self.add_line("page-top", (14, 4), (30, 4))
        self.add_line("page-fold-edge", (30, 4), (38, 12))
        self.add_line("page-right", (38, 12), (38, 40))
        self.add_arc("page-bottom-right", (38, 40), (34, 44), radius_x=4)
        self.add_line("page-bottom", (34, 44), (14, 44))
        self.add_arc("page-bottom-left", (14, 44), (10, 40), radius_x=4)
        self.add_line("page-left", (10, 40), (10, 8))
        self.add_arc("page-top-left", (10, 8), (14, 4), radius_x=4)
        self.add_contour("page", "page-top", "page-fold-edge", "page-right", "page-bottom-right", "page-bottom", "page-bottom-left", "page-left", "page-top-left", closed=True)
        self.add_polyline("fold-crease", (30, 4), (30, 12), (38, 12))
        self.relate("connect", "fold-crease", "page")
