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
            (40, 16),
            (40, 38),
            (30, 44),
            (18, 44),
            (8, 38),
            (8, 16),
            closed=True,
        )

        # A capsule abdomen and six separate limbs retain an insect silhouette.
        self.add_arc('body-top',(20,22),(28,22),radius_x=4)
        self.add_line('body-right-top',(28,22),(28,26))
        self.add_line('body-right-bottom',(28,26),(28,30))
        self.add_arc('body-bottom',(28,30),(20,30),radius_x=4)
        self.add_line('body-left-bottom',(20,30),(20,26))
        self.add_line('body-left-top',(20,26),(20,22))
        self.add_contour('body','body-top','body-right-top','body-right-bottom','body-bottom','body-left-bottom','body-left-top',closed=True)
        for side,root,tip in [('left',20,16),('right',28,32)]:
            for j,(y,ty) in enumerate(((22,18),(26,26),(30,34))):
                self.add_line(f'{side}-leg-{j}',(root,y),(tip,ty))
                self.relate('connect','body',f'{side}-leg-{j}')
