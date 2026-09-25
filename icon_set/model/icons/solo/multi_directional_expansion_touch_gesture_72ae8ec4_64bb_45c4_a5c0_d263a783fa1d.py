from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = "72ae8ec4-64bb-45c4-a5c0-d263a783fa1d"
SOURCE_PATH = "pictographic-primitives/_uncategorized_20/gesture expand_72ae8ec4-64bb-45c4-a5c0-d263a783fa1d.svg"
AUTHOR = "gpt-6"

class MultiDirectionalExpansionTouchGesture(Solo48):
    icon_id = "multi-directional-expansion-touch-gesture"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    aliases = ("four-way expand", "spread gesture")
    keywords = ("finger", "arrows", "directions")

    def build(self) -> None:
        # One rounded fingertip is centered among four equally spaced arrowheads.
        self.add_line("finger-left", (20, 28), (20, 22))
        self.add_arc("fingertip", (20, 22), (28, 22), radius_x=4, sweep=True)
        self.add_line("finger-right", (28, 22), (28, 28))
        self.add_contour("finger", "finger-left", "fingertip", "finger-right")
        self.add_polyline("up-head", (20, 10), (24, 6), (28, 10))
        self.add_line("up-shaft", (24, 6), (24, 10))
        self.relate("connect", "up-head", "up-shaft")
        self.add_polyline("down-head", (20, 38), (24, 42), (28, 38))
        self.add_line("down-shaft", (24, 36), (24, 42))
        self.relate("connect", "down-head", "down-shaft")
        self.add_polyline("left-head", (12, 20), (6, 24), (12, 28))
        self.add_polyline("right-head", (36, 20), (42, 24), (36, 28))
