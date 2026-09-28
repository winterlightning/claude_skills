"""Two opposing arrows tracing complementary arcs of a circle."""

from ...keyshapes import Keyshape
from ._base import Solo48


SOURCE_ICON_ID = "e63cb3c3-10bb-4fb1-a675-1e6b119047a5"
SOURCE_PATH = "pictographic-primitives/_uncategorized_04/arrows spin_e63cb3c3-10bb-4fb1-a675-1e6b119047a5.svg"
AUTHOR = "gpt-5"


class CircularRotatingArrows(Solo48):
    icon_id = "circular-rotating-arrows"
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "actions/navigation"
    aliases = ("two-circular-rotation-arrows", "spin-arrows")
    keywords = ("rotation", "arrows", "circular", "cycle", "refresh", "spin")

    def build(self) -> None:
        # Plan: two radius-20 arcs are 180-degree rotational counterparts.
        # Their open arrowheads reuse mirrored coordinates and touch only the
        # corresponding arc endpoint.
        self.add_arc("arrow-upper-arc", (4, 24), (40, 12), radius_x=20)
        self.add_line("arrow-upper-head-outer", (34, 10), (40, 12))
        self.add_line("arrow-upper-head-inner", (40, 12), (38, 18))
        self.add_contour(
            "arrow-upper-head", "arrow-upper-head-outer", "arrow-upper-head-inner"
        )
        self.relate("connect", "arrow-upper-arc", "arrow-upper-head")

        self.add_arc("arrow-lower-arc", (44, 24), (8, 36), radius_x=20)
        self.add_line("arrow-lower-head-outer", (14, 38), (8, 36))
        self.add_line("arrow-lower-head-inner", (8, 36), (10, 30))
        self.add_contour(
            "arrow-lower-head", "arrow-lower-head-outer", "arrow-lower-head-inner"
        )
        self.relate("connect", "arrow-lower-arc", "arrow-lower-head")
