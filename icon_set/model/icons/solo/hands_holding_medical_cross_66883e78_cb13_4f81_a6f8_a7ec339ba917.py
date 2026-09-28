"""Two cupped hands shelter a medical cross.

Symbol plan: the cross is a 12-segment orthogonal contour. One hand's contour
is mirrored around x=24 for the other. HRECT_L extremes x=4..44, y=8..40.
"""

from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = "66883e78-cb13-4f81-a6f8-a7ec339ba917"
SOURCE_PATH = "pictographic-primitives/_uncategorized_23/insurance hands_66883e78-cb13-4f81-a6f8-a7ec339ba917.svg"
AUTHOR = "gpt-6"


class HandsHoldingMedicalCross(Solo48):
    icon_id = "hands-holding-medical-cross"
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "health/care"
    aliases = ("health insurance hands", "medical protection")
    keywords = ("hands", "medical", "cross", "health", "care")

    def build(self) -> None:
        self.add_polyline(
            "medical-cross", (20, 8), (28, 8), (28, 14), (32, 14),
            (32, 22), (28, 22), (28, 26), (20, 26),
            (20, 22), (16, 22), (16, 14), (20, 14), closed=True,
        )
        left = ((10, 40), (4, 32), (4, 26), (6, 24),
                (8, 26), (13, 32), (17, 36), (17, 40))
        self.add_polyline("hand-left", *left)
        self.add_polyline("hand-right", *((48 - x, y) for x, y in left))
