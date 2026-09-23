"""A clipped-corner document with three descending data bars."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "d48f86f5-12a6-47ce-a5d0-968db65faf5e"
SOURCE_PATH = "pictographic-primitives/other/file data bars_d48f86f5-12a6-47ce-a5d0-968db65faf5e.svg"
AUTHOR = "gpt-6"


class DocumentWithBarChart(Solo48):
    icon_id = "document-with-bar-chart"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/document"
    aliases = ("bar graph file", "data bars document")
    keywords = ("chart", "analytics", "data", "bars")

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
        # Three equally stepped columns, left tallest as in the source.
        self.add_line("baseline-left", (16, 33), (24, 33))
        self.add_line("baseline-right", (24, 33), (32, 33))
        for name, x, y, base in (
            ("bar-left", 16, 16, "baseline-left"),
            ("bar-middle", 24, 21, "baseline-left"),
            ("bar-right", 32, 26, "baseline-right"),
        ):
            self.add_line(name, (x, y), (x, 33))
            self.relate("connect", name, base)
