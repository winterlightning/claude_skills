"""Two overlapping documents with a plus sign on the front page.

Symbol plan: an open rear sheet is occluded by a clipped front sheet;
the plus sign uses two orthogonal arms centered in its free interior.
Lucide files informed the offset pages and clipped page corner.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = "9de2a8a2-983a-425a-99ec-00774bb6aef2"
SOURCE_PATH = "pictographic-primitives/_uncategorized_27/merge pdf_9de2a8a2-983a-425a-99ec-00774bb6aef2.svg"
AUTHOR = "gpt-6"


class StackedDocumentsPlus(Solo48):
    icon_id = "stacked-documents-plus"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    categories = ("primitives", "primitives-generate")
    aliases = ("merge pdf", "add documents")
    keywords = ("files", "pages", "plus", "merge")

    def build(self) -> None:
        self.add_line("rear-bottom", (16, 34), (9, 34))
        self.add_arc("rear-sw", (9, 34), (6, 31), radius_x=3, sweep=True)
        self.add_line("rear-left", (6, 31), (6, 9))
        self.add_arc("rear-nw", (6, 9), (9, 6), radius_x=3, sweep=True)
        self.add_line("rear-top", (9, 6), (27, 6))
        self.add_arc("rear-ne", (27, 6), (30, 9), radius_x=3, sweep=True)
        self.add_line("rear-right", (30, 9), (30, 16))
        self.add_contour("rear-document", "rear-bottom", "rear-sw", "rear-left", "rear-nw", "rear-top", "rear-ne", "rear-right")

        self.add_polyline("front-document", (16, 39), (16, 16), (34, 16), (42, 24), (42, 39), (39, 42), (19, 42), closed=True)
        self.relate("connect", "rear-bottom", "front-document-1")
        self.relate("connect", "rear-right", "front-document-2")
        self.add_line("plus-vertical", (29, 24), (29, 34))
        self.add_line("plus-horizontal", (24, 29), (34, 29))
        self.relate("connect", "plus-vertical", "plus-horizontal")
