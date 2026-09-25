"""An empty rounded square frame."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = "eca7a06d-f576-4b8b-97db-6b3531c97a9b"
SOURCE_PATH = "pictographic-primitives/other/square_eca7a06d-f576-4b8b-97db-6b3531c97a9b.svg"
AUTHOR = "gpt-6"


class RoundedCornerSquareFrame(Solo48):
    icon_id = "rounded-corner-square-frame"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    categories = ("container", "other", "primitives-generate")
    aliases = ("rounded square", "empty frame")
    keywords = ("square", "border", "frame", "shape")

    def build(self) -> None:
        # Shared radius-four corners preserve four-fold symmetry.
        self.add_line("top", (10, 6), (38, 6))
        self.add_arc("ne", (38, 6), (42, 10), radius_x=4)
        self.add_line("right", (42, 10), (42, 38))
        self.add_arc("se", (42, 38), (38, 42), radius_x=4)
        self.add_line("bottom", (38, 42), (10, 42))
        self.add_arc("sw", (10, 42), (6, 38), radius_x=4)
        self.add_line("left", (6, 38), (6, 10))
        self.add_arc("nw", (6, 10), (10, 6), radius_x=4)
        self.add_contour("square-frame", "top", "ne", "right", "se",
                         "bottom", "sw", "left", "nw", closed=True)
