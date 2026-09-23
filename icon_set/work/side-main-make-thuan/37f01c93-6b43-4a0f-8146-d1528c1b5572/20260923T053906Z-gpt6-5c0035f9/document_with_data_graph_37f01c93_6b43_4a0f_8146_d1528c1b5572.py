"""A clipped-corner document with axes and a rising line graph."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "37f01c93-6b43-4a0f-8146-d1528c1b5572"
SOURCE_PATH = "pictographic-primitives/other/data file graph line_37f01c93-6b43-4a0f-8146-d1528c1b5572.svg"
AUTHOR = "gpt-6"


class DocumentWithDataGraph(Solo48):
    icon_id = "document-with-data-graph"
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/document"
    aliases = ("data file", "graph document")
    keywords = ("chart", "analytics", "data", "trend")

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

        # The three-point series rises overall, echoing the reference.
        self.add_line("axis-upper", (17, 16), (17, 27))
        self.add_line("axis-lower", (17, 27), (17, 34))
        self.add_line("axis-bottom", (17, 34), (31, 34))
        self.add_polyline("trend", (17, 27), (22, 22), (27, 24), (31, 19))
        self.relate("connect", "trend", "axis-upper")
