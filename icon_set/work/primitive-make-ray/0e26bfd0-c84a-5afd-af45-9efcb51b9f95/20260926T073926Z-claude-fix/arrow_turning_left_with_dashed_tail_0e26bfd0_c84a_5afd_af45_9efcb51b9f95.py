"""Arrow Turning Left with Dashed Tail.

Plan: SQUARE centerlines (6,6)-(42,42); open head leads a bent double-edged shaft, with paired dashes. The turn intentionally has directional asymmetry.
Construction references: Lucide repeat-2: coherent bent paths and explicit arrowhead junctions.
Reduction: Reduced trailing marks to one dash per edge.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '0e26bfd0-c84a-5afd-af45-9efcb51b9f95'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__arrow-turning-left-with-dashed-tail/20260926T073831Z-thuan-mac/reference/arrow dash corner point left_0e26bfd0-c84a-5afd-af45-9efcb51b9f95.svg'
SOURCE_ICON_IDS = ('0e26bfd0-c84a-5afd-af45-9efcb51b9f95',)
SOURCE_PATHS = ('pictographic-primitives/arrows/arrow dash corner point left_0e26bfd0-c84a-5afd-af45-9efcb51b9f95.svg',)
AUTHOR = "claude-opus-5-5"


class ArrowTurningLeftWithDashedTail(Solo48):
    icon_id = 'arrow-turning-left-with-dashed-tail'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'arrows'
    categories = ('arrows', 'primitives')
    aliases = ()
    keywords = ('arrow', 'turning', 'left', 'with', 'dashed', 'tail')

    def build(self) -> None:
        # Revision per review: the left arrowhead is smaller and narrower (arms 8 long, 4 either
        # side of the shaft, were 16 and 12); the outer path is straight - the shaft runs level
        # from the tip (4, 12) to (44, 12) and turns down to (44, 30); the shorter inner path is a
        # separate L, (19, 20)-(36, 20)-(36, 30), 8 inside the outer path and 8.9 from the
        # arrowhead. A dash continues each vertical below its gap: (44, 38)-(44, 40) and
        # (36, 38)-(36, 40).
        self.add_polyline("outer", (4, 12), (44, 12), (44, 30))
        self.add_polyline("head", (11, 8), (4, 12), (11, 16))
        self.relate("connect", "outer", "head")
        self.add_polyline("inner", (19, 20), (36, 20), (36, 30))
        for x in (36, 44):
            self.add_line(f"dash-{x}", (x, 38), (x, 40))
