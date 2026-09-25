"""A rounded page layout with one full-width header and three lower columns.

Symbol plan: shared outer frame, one row divider, two equal column dividers.
The SQUARE centerline extremes are x/y 6..42; columns have 12-unit pitch.
"""

from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = "769b8cf9-3c8c-4674-a5c6-7da2d0a5f9d0"
SOURCE_PATH = "pictographic-primitives/_uncategorized_25/layout 11_769b8cf9-3c8c-4674-a5c6-7da2d0a5f9d0.svg"
AUTHOR = "gpt-6"


class HeaderAndThreeColumnLayout(Solo48):
    icon_id = "header-and-three-column-layout"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    aliases = ("three column page", "header grid")
    keywords = ("layout", "header", "columns", "grid", "page")

    def build(self) -> None:
        self.add_line("top", (12, 6), (36, 6))
        self.add_arc("top-right", (36, 6), (42, 12), radius_x=6)
        self.add_line("right", (42, 12), (42, 36))
        self.add_arc("bottom-right", (42, 36), (36, 42), radius_x=6)
        self.add_line("bottom", (36, 42), (12, 42))
        self.add_arc("bottom-left", (12, 42), (6, 36), radius_x=6)
        self.add_line("left", (6, 36), (6, 12))
        self.add_arc("top-left", (6, 12), (12, 6), radius_x=6)
        self.add_contour("frame", "top", "top-right", "right", "bottom-right", "bottom", "bottom-left", "left", "top-left", closed=True)
        self.add_line("header-divider", (6, 22), (42, 22))
        self.relate("connect", "header-divider", "frame")
        for index, x in enumerate((18, 30), 1):
            part = f"column-divider-{index}"
            self.add_line(part, (x, 22), (x, 42))
            self.relate("connect", part, "header-divider")
            self.relate("connect", part, "frame")
