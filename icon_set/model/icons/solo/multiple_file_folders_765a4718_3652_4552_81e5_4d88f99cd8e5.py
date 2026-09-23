from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = "765a4718-3652-4552-81e5-4d88f99cd8e5"
SOURCE_PATH = "pictographic-primitives/_uncategorized_19/folders_765a4718-3652-4552-81e5-4d88f99cd8e5.svg"
AUTHOR = "gpt-6"

class MultipleFileFolders(Solo48):
    icon_id = "multiple-file-folders"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/office"
    aliases = ("folders", "stacked folders")
    keywords = ("files", "documents", "stack")

    def build(self) -> None:
        # Repeated tabbed folder shape, rear one partly hidden by front one.
        self.add_polyline("rear-folder-visible", (14, 32), (6, 32), (6, 10), (10, 6), (18, 6), (22, 10), (32, 10))
        self.add_polyline("front-folder", (14, 38), (14, 20), (18, 16), (22, 16), (26, 20), (38, 20), (42, 24), (42, 38), (38, 42), (18, 42), (14, 38), closed=True)
