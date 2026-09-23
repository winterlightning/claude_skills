"""A clipped-corner document containing an analog clock."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "0ef08051-f8cf-452c-9504-27f2eb99eb1b"
SOURCE_PATH = "pictographic-primitives/other/file clock_0ef08051-f8cf-452c-9504-27f2eb99eb1b.svg"
AUTHOR = "gpt-6"


class DocumentWithClockSymbol(Solo48):
    icon_id = "document-with-clock-symbol"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/document"
    aliases = ("time file", "clock document")
    keywords = ("time", "clock", "schedule", "file")

    def build(self) -> None:
        self.add_line("top", (10, 6), (32, 6))
        self.add_line("fold-angle", (32, 6), (42, 16))
        self.add_line("right", (42, 16), (42, 38))
        self.add_arc("corner-se", (42, 38), (38, 42), radius_x=4)
        self.add_line("bottom", (38, 42), (10, 42))
        self.add_arc("corner-sw", (10, 42), (6, 38), radius_x=4)
        self.add_line("left", (6, 38), (6, 10))
        self.add_arc("corner-nw", (6, 10), (10, 6), radius_x=4)
        self.add_contour("page-outline", "top", "fold-angle", "right",
                         "corner-se", "bottom", "corner-sw", "left",
                         "corner-nw", closed=True)
        # Clock outline has one common center and four equal radius-nine arcs.
        points = ((24, 15), (33, 24), (24, 33), (15, 24))
        for index, start in enumerate(points):
            self.add_arc(f"clock-{index}", start, points[(index+1) % 4], radius_x=9)
        self.add_contour("clock-ring", *(f"clock-{i}" for i in range(4)), closed=True)
        self.add_line("hour-hand", (24, 15), (24, 24))
        self.add_line("minute-hand", (24, 24), (33, 24))
        self.relate("connect", "hour-hand", "clock-0")
        self.relate("connect", "minute-hand", "clock-0")
