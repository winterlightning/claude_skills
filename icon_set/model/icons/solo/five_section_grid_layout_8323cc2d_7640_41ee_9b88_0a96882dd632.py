"""Five section layout: two upper cells and three lower cells.

Plan: a rounded square owns one horizontal divider and two separate vertical
series. All junctions are constructed from shared integer coordinates.
Lucide layout-grid informed the even frame and consistent divider weight.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = "8323cc2d-7640-41ee-9b88-0a96882dd632"
SOURCE_PATH = "pictographic-primitives/_uncategorized_25/layout 13_8323cc2d-7640-41ee-9b88-0a96882dd632.svg"
AUTHOR = "gpt-6"


class FiveSectionGridLayout(Solo48):
    icon_id = "five-section-grid-layout"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/layout"
    aliases = ("five-panel-layout",)
    keywords = ("grid", "interface", "columns", "panels")

    def build(self) -> None:
        self.add_line("frame-top-left", (10, 6), (24, 6))
        self.add_line("frame-top-right", (24, 6), (38, 6))
        self.add_arc("frame-upper-right", (38, 6), (42, 10), radius_x=4, sweep=True)
        self.add_line("frame-right-upper", (42, 10), (42, 24))
        self.add_line("frame-right-lower", (42, 24), (42, 38))
        self.add_arc("frame-lower-right", (42, 38), (38, 42), radius_x=4, sweep=True)
        self.add_line("frame-bottom-right", (38, 42), (30, 42))
        self.add_line("frame-bottom-middle", (30, 42), (18, 42))
        self.add_line("frame-bottom-left", (18, 42), (10, 42))
        self.add_arc("frame-lower-left", (10, 42), (6, 38), radius_x=4, sweep=True)
        self.add_line("frame-left-lower", (6, 38), (6, 24))
        self.add_line("frame-left-upper", (6, 24), (6, 10))
        self.add_arc("frame-upper-left", (6, 10), (10, 6), radius_x=4, sweep=True)
        self.add_contour("frame", "frame-top-left", "frame-top-right", "frame-upper-right", "frame-right-upper", "frame-right-lower", "frame-lower-right", "frame-bottom-right", "frame-bottom-middle", "frame-bottom-left", "frame-lower-left", "frame-left-lower", "frame-left-upper", "frame-upper-left", closed=True)

        x_lower = (18, 30)
        self.add_polyline("row", (6, 24), (x_lower[0], 24), (24, 24), (x_lower[1], 24), (42, 24))
        self.add_line("top-division", (24, 6), (24, 24))
        for index, x in enumerate(x_lower):
            self.add_line(f"lower-division-{index}", (x, 24), (x, 42))
            self.relate("connect", f"lower-division-{index}", "row")
            self.relate("connect", f"lower-division-{index}", "frame")
        self.relate("connect", "row", "frame")
        self.relate("connect", "top-division", "frame")
        self.relate("connect", "top-division", "row")
