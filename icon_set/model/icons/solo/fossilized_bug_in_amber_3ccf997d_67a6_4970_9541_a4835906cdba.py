'A six-legged fossil insect enclosed in faceted amber.\nPlan: VRECT_L follows the tall resin outline.\nReduction: Simplified head/abdomen to one capsule; omitted antennae and the wing divider. Retained all six legs.\nConstruction: Lucide bug: a bilateral abdomen and three mirrored leg pairs.'

from ...keyshapes import Keyshape
from ._base import Solo48


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
        # A centered faceted resin loop encloses a capsule insect with six mirrored limbs.
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
        for side,root,tip in [('left',20,17),('right',28,31)]:
            for j,(y,ty) in enumerate(((22,18),(26,26),(30,34))):
                self.add_line(f'{side}-leg-{j}',(root,y),(tip,ty))
                self.relate('connect','body',f'{side}-leg-{j}')
