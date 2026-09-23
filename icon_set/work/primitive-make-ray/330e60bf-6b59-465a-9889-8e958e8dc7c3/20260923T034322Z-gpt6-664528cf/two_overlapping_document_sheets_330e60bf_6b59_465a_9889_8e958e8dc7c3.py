"""Two offset document sheets with a clipped upper-right corner on the front.

SQUARE extrema are (6,6)-(42,42). The rear outline is interrupted where the
front sheet occludes it. Lucide copy suggests the offset and interrupted edge.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "330e60bf-6b59-465a-9889-8e958e8dc7c3"
SOURCE_PATH = "pictographic-primitives/_uncategorized_11/clone_330e60bf-6b59-465a-9889-8e958e8dc7c3.svg"
AUTHOR = "gpt-6"


class TwoOverlappingDocumentSheets(Solo48):
    icon_id = "two-overlapping-document-sheets"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "files"
    aliases = ("copy", "duplicate documents")
    keywords = ("clone", "duplicate", "sheets", "paper")

    def build(self) -> None:
        self.add_polyline("rear", (14, 14), (14, 10), (18, 6), (38, 6), (42, 10), (42, 30), (38, 34), (34, 34))
        self.add_polyline("front", (14, 14), (28, 14), (34, 20), (34, 38), (30, 42), (10, 42), (6, 38), (6, 18), (10, 14), (14, 14), closed=True)
        self.relate("connect", "rear", "front")
