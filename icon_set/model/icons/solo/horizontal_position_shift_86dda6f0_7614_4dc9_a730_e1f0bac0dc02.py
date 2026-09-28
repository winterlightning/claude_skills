"""Two stacked horizontal bars between opposing movement arrows."""

from ...keyshapes import Keyshape
from ._base import Solo48


SOURCE_ICON_ID = "86dda6f0-7614-4dc9-a730-e1f0bac0dc02"
SOURCE_PATH = "pictographic-primitives/_uncategorized_01/align middle move horizontal_86dda6f0-7614-4dc9-a730-e1f0bac0dc02.svg"
AUTHOR = "gpt-5"


class HorizontalPositionShift(Solo48):
    icon_id = "horizontal-position-shift"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    categories = ("primitives", "primitives-generate")
    aliases = ("move-horizontal-bars", "opposing-horizontal-shift")
    keywords = ("move", "horizontal", "shift", "bars", "arrows")

    def build(self) -> None:
        # Plan: two identical centered bar strokes form a regular vertical
        # series. The upper arrow points left and the mirrored lower arrow
        # points right, preserving the source's opposing motion.
        self.add_line("bar-top", (6, 20), (42, 20))
        self.add_line("bar-bottom", (6, 30), (42, 30))

        self.add_line("arrow-top-shaft", (14, 8), (34, 8))
        self.add_line("arrow-top-upper-head", (18, 6), (14, 8))
        self.add_line("arrow-top-lower-head", (14, 8), (18, 10))
        self.add_contour(
            "arrow-top-head", "arrow-top-upper-head", "arrow-top-lower-head"
        )
        self.relate("connect", "arrow-top-shaft", "arrow-top-head")

        self.add_line("arrow-bottom-shaft", (14, 40), (34, 40))
        self.add_line("arrow-bottom-upper-head", (30, 38), (34, 40))
        self.add_line("arrow-bottom-lower-head", (34, 40), (30, 42))
        self.add_contour(
            "arrow-bottom-head",
            "arrow-bottom-upper-head",
            "arrow-bottom-lower-head",
        )
        self.relate("connect", "arrow-bottom-shaft", "arrow-bottom-head")
