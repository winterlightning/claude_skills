from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = "3404178e-6c6c-4e81-923b-4c9570a627a0"
SOURCE_PATH = "pictographic-primitives/_uncategorized_20/gesture tap expand all direction_3404178e-6c6c-4e81-923b-4c9570a627a0.svg"
AUTHOR = "gpt-6"

class TapGestureExpandAllDirections(Solo48):
    icon_id = "tap-gesture-expand-all-directions"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "gestures/touch"
    aliases = ("four-way tap expand",)
    keywords = ("finger", "arrows", "spread")

    def build(self) -> None:
        # Central tapping fingertip is framed by four expansion arrows.
        self.add_line("finger-left", (20, 30), (20, 22))
        self.add_arc("fingertip", (20, 22), (28, 22), radius_x=4, sweep=True)
        self.add_line("finger-right", (28, 22), (28, 30))
        self.add_contour("finger", "finger-left", "fingertip", "finger-right")
        self.add_polyline("up-head", (20, 10), (24, 6), (28, 10))
        self.add_line("up-shaft", (24, 6), (24, 10))
        self.relate("connect", "up-head", "up-shaft")
        self.add_polyline("down-head", (20, 38), (24, 42), (28, 38))
        self.add_line("down-shaft", (24, 38), (24, 42))
        self.relate("connect", "down-head", "down-shaft")
        self.add_polyline("left-head", (12, 20), (6, 24), (12, 28))
        self.add_polyline("right-head", (36, 20), (42, 24), (36, 28))
