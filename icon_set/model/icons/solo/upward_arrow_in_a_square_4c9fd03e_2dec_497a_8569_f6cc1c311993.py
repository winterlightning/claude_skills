"""A vertical upward arrow centered in a rounded square.

Plan: one symmetric rounded frame encloses a joined chevron head and shaft.
Lucide square-arrow-up informed the one-piece arrow placement and frame radii.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = "4c9fd03e-2dec-497a-8569-f6cc1c311993"
SOURCE_PATH = "pictographic-primitives/_uncategorized_27/maximize_4c9fd03e-2dec-497a-8569-f6cc1c311993.svg"
AUTHOR = "gpt-6"


class UpwardArrowInASquare(Solo48):
    icon_id = "upward-arrow-in-a-square"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    categories = ("primitives", "primitives-generate")
    aliases = ("maximize-up",)
    keywords = ("arrow", "up", "square", "maximize")

    def build(self) -> None:
        self.add_line("top", (10, 6), (38, 6))
        self.add_arc("ne", (38, 6), (42, 10), radius_x=4, sweep=True)
        self.add_line("right", (42, 10), (42, 38))
        self.add_arc("se", (42, 38), (38, 42), radius_x=4, sweep=True)
        self.add_line("bottom", (38, 42), (10, 42))
        self.add_arc("sw", (10, 42), (6, 38), radius_x=4, sweep=True)
        self.add_line("left", (6, 38), (6, 10))
        self.add_arc("nw", (6, 10), (10, 6), radius_x=4, sweep=True)
        self.add_contour("frame", "top", "ne", "right", "se", "bottom", "sw", "left", "nw", closed=True)
        self.add_polyline("arrow-head", (16, 23), (24, 15), (32, 23))
        self.add_line("arrow-shaft", (24, 15), (24, 33))
        self.relate("connect", "arrow-head", "arrow-shaft")
