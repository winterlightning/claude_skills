"""A wider hexagon, preserving the original as a separate review candidate."""

from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = None
SOURCE_PATH = None
AUTHOR = "gpt-6"


class HexagonVariant2(Sub32):
    icon_id = "hexagon-v2"
    variant_of = "hexagon"
    variant_label = "Wider proportions"
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives/shape"
    keywords = ("cell", "badge", "honeycomb")

    def build(self) -> None:
        # HRECT_L centerline extremes: (2, 6)-(30, 26).
        # Mirror across both axes, retaining flat top and bottom edges.
        axis_x, axis_y = 16, 16
        shoulder_x, top_y = 9, 6
        self.add_polyline(
            "outline",
            (shoulder_x, top_y), (2 * axis_x - shoulder_x, top_y),
            (30, axis_y),
            (2 * axis_x - shoulder_x, 2 * axis_y - top_y),
            (shoulder_x, 2 * axis_y - top_y), (2, axis_y),
            closed=True,
        )
