"""A clipped-corner document containing a play symbol."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = "689771b0-30f8-4120-80b3-7887e1a46a1e"
SOURCE_PATH = "pictographic-primitives/other/video file_689771b0-30f8-4120-80b3-7887e1a46a1e.svg"
AUTHOR = "gpt-6"


class DocumentWithPlayButton(Solo48):
    icon_id = "document-with-play-button"
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/media"
    aliases = ("video file", "play document")
    keywords = ("video", "file", "media", "play")

    def build(self) -> None:
        self.add_line("top", (12, 4), (31, 4))
        self.add_line("fold-angle", (31, 4), (40, 13))
        self.add_line("right", (40, 13), (40, 40))
        self.add_arc("corner-se", (40, 40), (36, 44), radius_x=4)
        self.add_line("bottom", (36, 44), (12, 44))
        self.add_arc("corner-sw", (12, 44), (8, 40), radius_x=4)
        self.add_line("left", (8, 40), (8, 8))
        self.add_arc("corner-nw", (8, 8), (12, 4), radius_x=4)
        self.add_contour("page-outline", "top", "fold-angle", "right",
                         "corner-se", "bottom", "corner-sw", "left",
                         "corner-nw", closed=True)
        self.add_polyline("play-symbol", (17, 17), (31, 24),
                          (17, 31), (17, 17), closed=True)
