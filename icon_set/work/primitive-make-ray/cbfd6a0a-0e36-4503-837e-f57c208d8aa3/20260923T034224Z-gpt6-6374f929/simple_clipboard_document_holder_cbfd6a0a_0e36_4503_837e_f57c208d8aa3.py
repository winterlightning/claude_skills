"""An upright board with a shallow, central, round-shouldered clip.

Symbol plan: the board and clip share the two top attachment nodes; the clip's
shoulders mirror about x=24. VRECT_L extrema are x=8/40 and y=4/44.
Lucide clipboard supplied the open board and paired top attachments.
"""
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
    aliases = ("clipboard", "document holder")
    keywords = ("board", "clip", "paper", "office")

    def build(self) -> None:
        axis = 24
        clip_left, clip_right = 16, 2 * axis - 16
        self.add_line("clip-left", (clip_left, 12), (clip_left, 8))
        self.add_arc("clip-nw", (16, 8), (20, 4), radius_x=4, radius_y=4, sweep=True)
        self.add_line("clip-crown", (20, 4), (28, 4))
        self.add_arc("clip-ne", (28, 4), (clip_right, 8), radius_x=4, radius_y=4, sweep=True)
        self.add_line("clip-right", (clip_right, 8), (clip_right, 12))
        self.add_line("clip-base", (clip_right, 12), (clip_left, 12))
        self.add_contour("clip", "clip-left", "clip-nw", "clip-crown", "clip-ne", "clip-right", "clip-base", closed=True)

        self.add_line("board-top-right", (32, 12), (36, 12))
        self.add_arc("board-ne", (36, 12), (40, 16), radius_x=4, radius_y=4, sweep=True)
        self.add_line("board-right", (40, 16), (40, 40))
        self.add_arc("board-se", (40, 40), (36, 44), radius_x=4, radius_y=4, sweep=True)
        self.add_line("board-bottom", (36, 44), (12, 44))
        self.add_arc("board-sw", (12, 44), (8, 40), radius_x=4, radius_y=4, sweep=True)
        self.add_line("board-left", (8, 40), (8, 16))
        self.add_arc("board-nw", (8, 16), (12, 12), radius_x=4, radius_y=4, sweep=True)
        self.add_line("board-top-left", (12, 12), (16, 12))
        self.add_contour("board", "board-top-right", "board-ne", "board-right", "board-se", "board-bottom", "board-sw", "board-left", "board-nw", "board-top-left")
        self.relate("connect", "clip", "board")
