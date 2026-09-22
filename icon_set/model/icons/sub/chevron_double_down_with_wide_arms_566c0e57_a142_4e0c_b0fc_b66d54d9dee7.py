"""Two equal downward chevrons with wide arms, preserving the complete source.

SQUARE reaches centerline extrema (2,2)-(30,30). One repeated V definition
owns arm length 14 and vertical step 14; both mirror about x=16.
Lucide chevrons-down contributes continuous two-segment contours and an equal
repeat. The supplied reference contributes the wider square proportions.
All four arms and both downward points are retained; no parts are omitted.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = "566c0e57-a142-4e0c-b0fc-b66d54d9dee7"
SOURCE_PATH = "pictographic-primitives/_uncategorized_15/down 2_566c0e57-a142-4e0c-b0fc-b66d54d9dee7.svg"
AUTHOR = "gpt-6-astra"


class Drawing(Sub32):
    icon_id = "chevron-double-down-with-wide-arms"
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = "primitives/chevron"
    aliases = ("Double Downward Chevron",)
    keywords = ("chevron", "down", "double", "direction", "angle", "stack", "pointer")

    def build(self):
        axis, arm, step = 16, 14, 14
        for index in range(2):
            top = 2 + index * step
            self.add_polyline(f"chevron-{index + 1}",
                              (axis - arm, top), (axis, top + arm),
                              (axis + arm, top))
