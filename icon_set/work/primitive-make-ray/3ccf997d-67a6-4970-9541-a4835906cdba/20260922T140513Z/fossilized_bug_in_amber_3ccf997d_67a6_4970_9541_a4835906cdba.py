"""A compact fossil beetle enclosed by a faceted amber-resin outline."""

from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48


SOURCE_ICON_ID = "3ccf997d-67a6-4970-9541-a4835906cdba"
SOURCE_PATH = "pictographic-primitives/_uncategorized_03/amber_3ccf997d-67a6-4970-9541-a4835906cdba.svg"
AUTHOR = "gpt-5"


class FossilizedBugInAmber(Solo48):
    icon_id = "fossilized-bug-in-amber"
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "nature/fossils"
    aliases = ("beetle-embedded-in-amber", "amber-fossil")
    keywords = ("amber", "beetle", "insect", "fossil", "resin", "legs")

    def build(self) -> None:
        # Plan: one centered faceted resin loop encloses a bilaterally symmetric
        # beetle. Each side's three projecting legs form one coherent zigzag so
        # all six legs remain visible without sub-minimum gaps at their roots.
        self.add_polyline(
            "amber-outline",
            (18, 4),
            (30, 4),
            (40, 18),
            (40, 36),
            (30, 44),
            (18, 44),
            (8, 36),
            (8, 18),
            closed=True,
        )

        self.add_polyline(
            "beetle-outline",
            (21, 18),
            (20, 15),
            (22, 17),
            (24, 14),
            (26, 17),
            (28, 15),
            (27, 18),
            (26, 22),
            (28, 26),
            (28, 31),
            (24, 35),
            (20, 31),
            (20, 26),
            (22, 22),
            closed=True,
        )

        self.add_polyline(
            "legs-left",
            (22, 22),
            (18, 20),
            (20, 26),
            (16, 26),
            (20, 31),
            (19, 34),
        )
        self.add_polyline(
            "legs-right",
            (26, 22),
            (30, 20),
            (28, 26),
            (32, 26),
            (28, 31),
            (29, 34),
        )
        self.relate("connect", "beetle-outline", "legs-left")
        self.relate("connect", "beetle-outline", "legs-right")
