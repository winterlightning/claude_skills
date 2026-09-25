"""An empty clipboard with a raised, rounded spring clip."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = "cbfd6a0a-0e36-4503-837e-f57c208d8aa3"
SOURCE_PATH = "pictographic-primitives/_uncategorized_11/clipboard_cbfd6a0a-0e36-4503-837e-f57c208d8aa3.svg"
AUTHOR = "claude-fable-5-1"


class SimpleClipboardDocumentHolder(Solo48):
    icon_id = "simple-clipboard-document-holder"
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    aliases = ("empty clipboard", "document holder")
    keywords = ("paper", "clip", "stationery", "board")

    def build(self) -> None:
        # Board: 32-wide, 3-unit corners, top edge open between the clip sides.
        self.add_line("body-top-left", (19, 9), (11, 9))
        self.add_arc("body-nw", (11, 9), (8, 12), radius_x=3, sweep=False)
        self.add_line("body-left", (8, 12), (8, 41))
        self.add_arc("body-sw", (8, 41), (11, 44), radius_x=3, sweep=False)
        self.add_line("body-bottom", (11, 44), (37, 44))
        self.add_arc("body-se", (37, 44), (40, 41), radius_x=3, sweep=False)
        self.add_line("body-right", (40, 41), (40, 12))
        self.add_arc("body-ne", (40, 12), (37, 9), radius_x=3, sweep=False)
        self.add_line("body-top-right", (37, 9), (29, 9))
        self.add_contour("board", "body-top-left", "body-nw", "body-left",
                         "body-sw", "body-bottom", "body-se", "body-right",
                         "body-ne", "body-top-right")
        # Clip: Lucide clipboard's rounded clip, 10 wide, a 5-unit semicircle
        # hump above the board and 3-unit lower corners; inner hole 6 wide.
        self.add_line("clip-left-side", (19, 14), (19, 9))
        self.add_arc("clip-nw", (19, 9), (24, 4), radius_x=5)
        self.add_arc("clip-ne", (24, 4), (29, 9), radius_x=5)
        self.add_line("clip-right-side", (29, 9), (29, 14))
        self.add_arc("clip-se", (29, 14), (26, 17), radius_x=3)
        self.add_line("clip-bottom", (26, 17), (22, 17))
        self.add_arc("clip-sw", (22, 17), (19, 14), radius_x=3)
        self.add_contour("clip", "clip-left-side", "clip-nw", "clip-ne",
                         "clip-right-side", "clip-se", "clip-bottom",
                         "clip-sw", closed=True)
        self.relate("connect", "body-top-left", "clip-left-side")
        self.relate("connect", "body-top-right", "clip-right-side")
