"""A compact fossil beetle enclosed by a faceted amber-resin outline."""

from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48


SOURCE_ICON_ID = "3ccf997d-67a6-4970-9541-a4835906cdba"
SOURCE_PATH = 'pictographic-primitives/_uncategorized_03/amber_3ccf997d-67a6-4970-9541-a4835906cdba.svg'
AUTHOR = 'gpt-6'


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

        # Simplify the fossil to a spine and three mirrored leg pairs, keeping six legs.
        self.add_polyline('beetle-spine',(24,16),(24,18),(24,26),(24,34))
        for j,y in enumerate((18,26,34)):
            self.add_polyline(f'legs-{j}',(17,y),(24,y),(31,y))
            self.relate('connect','beetle-spine',f'legs-{j}')
