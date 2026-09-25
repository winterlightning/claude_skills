from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = "e62395aa-eb63-4166-835d-6e931dc59a5e"
SOURCE_PATH = "pictographic-primitives/_uncategorized_23/inboxes_e62395aa-eb63-4166-835d-6e931dc59a5e.svg"
AUTHOR = "gpt-6"

class EmptyInboxTray(Solo48):
    icon_id = "empty-inbox-tray"
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    categories = ("primitives", "primitives-generate")
    aliases = ("inboxes", "empty in-tray")
    keywords = ("desktop", "paper", "notch")

    def build(self) -> None:
        # One broad empty tray has a semicircular opening in its front wall.
        self.add_polyline("tray", (4, 22), (12, 8), (36, 8), (44, 22), (44, 36), (40, 40), (8, 40), (4, 36), (4, 22), closed=True)
        self.add_line("front-left", (4, 22), (15, 22))
        self.add_arc("notch", (15, 22), (33, 22), radius_x=9, sweep=False)
        self.add_line("front-right", (33, 22), (44, 22))
        self.add_contour("front", "front-left", "notch", "front-right")
        self.relate("connect", "tray", "front")
