from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = "2a7dc515-f6b9-47c6-b582-d41dbe15acd5"
SOURCE_PATH = "pictographic-primitives/_uncategorized_19/fold_2a7dc515-f6b9-47c6-b582-d41dbe15acd5.svg"
AUTHOR = "gpt-6"

class DocumentWithFoldedCorner(Solo48):
    icon_id = "document-with-folded-corner-solo"
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    categories = ("primitives", "primitives-generate")
    aliases = ("folded document", "file")
    keywords = ("page", "paper", "corner", "fold")

    def build(self) -> None:
        # Upright page with a triangular turn at its upper-right corner.
        self.add_polyline("page-outline", (12, 4), (28, 4), (40, 16), (40, 40), (36, 44), (12, 44), (8, 40), (8, 8), (12, 4), closed=True)
        self.add_polyline("fold", (28, 4), (28, 16), (40, 16))
        self.relate("connect", "page-outline", "fold")
