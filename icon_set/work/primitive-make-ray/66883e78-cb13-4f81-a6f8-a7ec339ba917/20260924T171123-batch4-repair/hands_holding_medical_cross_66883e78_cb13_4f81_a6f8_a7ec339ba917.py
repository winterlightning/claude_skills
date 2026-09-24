"""Two cupped hands protecting a medical cross.
Plan: HRECT_L provides width for mirrored hands around the cross. Mirrored palms and outlined cross retain clear separation; reviewed at native size in both themes.
Reduction: Narrow hand return edges simplified into open curved palms.
Construction references: human-reference.md and Lucide hand construction vocabulary; source supplies mirrored cupped gesture.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "66883e78-cb13-4f81-a6f8-a7ec339ba917"
SOURCE_PATH = 'pictographic-primitives/_uncategorized_23/insurance hands_66883e78-cb13-4f81-a6f8-a7ec339ba917.svg'
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
        # Mirrored open palms retain wrists and rising fingers; omit narrow return edge.
        for side in (-1,1):
            p=lambda x,y:(24+side*x,y)
            self.add_bezier(f'hand-{side}',p(20,24),(p(20,34),p(18,40),p(8,40)),(p(8,36),p(11,33),p(14,31)))