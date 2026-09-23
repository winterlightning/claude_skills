"""An empty clipboard with a raised, rounded spring clip."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "cbfd6a0a-0e36-4503-837e-f57c208d8aa3"
SOURCE_PATH = "pictographic-primitives/_uncategorized_11/clipboard_cbfd6a0a-0e36-4503-837e-f57c208d8aa3.svg"
AUTHOR = "gpt-6"


class SimpleClipboardDocumentHolder(Solo48):
    icon_id = "simple-clipboard-document-holder"
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/office"
    aliases = ("empty clipboard", "document holder")
    keywords = ("paper", "clip", "stationery", "board")

    def build(self) -> None:
        # Symmetric board: 32 wide with four-unit rounded corners. The top
        # stroke leaves a 16-unit slot owned by the central clip.
        self.add_line("body-top-left", (16, 9), (12, 9))
        self.add_arc("body-nw", (12, 9), (8, 13), radius_x=4)
        self.add_line("body-left", (8, 13), (8, 40))
        self.add_arc("body-sw", (8, 40), (12, 44), radius_x=4)
        self.add_line("body-bottom", (12, 44), (36, 44))
        self.add_arc("body-se", (36, 44), (40, 40), radius_x=4)
        self.add_line("body-right", (40, 40), (40, 13))
        self.add_arc("body-ne", (40, 13), (36, 9), radius_x=4)
        self.add_line("body-top-right", (36, 9), (32, 9))
        self.add_contour("board", "body-top-left", "body-nw", "body-left",
                         "body-sw", "body-bottom", "body-se", "body-right",
                         "body-ne", "body-top-right")

        # A raised four-unit radius hump flows into the lower grip. The
        # lower grip's three-unit corner arcs and horizontal base are paired.
        self.add_line("clip-left-ledge", (16, 9), (18, 9))
        self.add_line("clip-left-rise", (18, 9), (18, 8))
        self.add_arc("clip-nw", (18, 8), (22, 4), radius_x=4)
        self.add_line("clip-top", (22, 4), (26, 4))
        self.add_arc("clip-ne", (26, 4), (30, 8), radius_x=4)
        self.add_line("clip-right-fall", (30, 8), (30, 9))
        self.add_line("clip-right-ledge", (30, 9), (32, 9))
        self.add_line("clip-right-side", (32, 9), (32, 14))
        self.add_arc("clip-se", (32, 14), (29, 17), radius_x=3)
        self.add_line("clip-bottom", (29, 17), (19, 17))
        self.add_arc("clip-sw", (19, 17), (16, 14), radius_x=3)
        self.add_line("clip-left-side", (16, 14), (16, 9))
        self.add_contour("grip", "clip-left-ledge", "clip-left-rise",
                         "clip-nw", "clip-top", "clip-ne", "clip-right-fall",
                         "clip-right-ledge", "clip-right-side", "clip-se",
                         "clip-bottom", "clip-sw", "clip-left-side", closed=True)
        self.relate("connect", "body-top-left", "clip-left-ledge")
        self.relate("connect", "body-top-right", "clip-right-ledge")
