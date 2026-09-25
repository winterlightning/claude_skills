from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = "fdd66e1b-0160-4f60-bbe1-7da952783381"
SOURCE_PATH = "pictographic-primitives/_uncategorized_20/gesture tap all direction_fdd66e1b-0160-4f60-bbe1-7da952783381.svg"
AUTHOR = "gpt-6"

class DragGestureInAllDirections(Solo48):
    icon_id = "drag-gesture-in-all-directions"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    aliases = ("four-way drag",)
    keywords = ("finger", "nail", "arrows")

    def build(self) -> None:
        # Centered fingertip and nail point are surrounded by four outward arrows.
        self.add_line("finger-left", (16, 32), (16, 24))
        self.add_arc("fingertip", (16, 24), (32, 24), radius_x=8, sweep=True)
        self.add_line("finger-right", (32, 24), (32, 32))
        self.add_contour("finger", "finger-left", "fingertip", "finger-right")
        self.add_polyline("up-head", (20, 8), (24, 6), (28, 8))
        self.add_line("up-shaft", (24, 6), (24, 8))
        self.relate("connect", "up-head", "up-shaft")
        self.add_polyline("down-head", (20, 40), (24, 42), (28, 40))
        self.add_line("down-shaft", (24, 40), (24, 42))
        self.relate("connect", "down-head", "down-shaft")
        self.add_polyline("left-head", (8, 20), (6, 24), (8, 28))
        self.add_polyline("right-head", (40, 20), (42, 24), (40, 28))
