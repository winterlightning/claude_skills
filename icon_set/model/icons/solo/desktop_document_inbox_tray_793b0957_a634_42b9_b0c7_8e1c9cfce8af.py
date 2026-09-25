from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = "793b0957-a634-42b9-b0c7-8e1c9cfce8af"
SOURCE_PATH = "pictographic-primitives/_uncategorized_23/inbox_793b0957-a634-42b9-b0c7-8e1c9cfce8af.svg"
AUTHOR = "gpt-6"

class DesktopDocumentInboxTray(Solo48):
    icon_id = "desktop-document-inbox-tray"
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    aliases = ("inbox tray", "desk in-tray")
    keywords = ("documents", "paper", "notch")

    def build(self) -> None:
        # Broad trapezoid rises behind a low front wall with a central handhold notch.
        self.add_polyline("tray-outline", (4, 26), (12, 8), (36, 8), (44, 26), (44, 36), (40, 40), (8, 40), (4, 36), (4, 26), closed=True)
        self.add_polyline("front-notch", (4, 26), (14, 26), (18, 32), (30, 32), (34, 26), (44, 26))
        self.relate("connect", "tray-outline", "front-notch")
