"""Arrow Turning Left with Dashed Tail.

Plan: SQUARE centerlines (6,6)-(42,42); open head leads a bent double-edged shaft, with paired dashes. The turn intentionally has directional asymmetry.
Construction references: Lucide repeat-2: coherent bent paths and explicit arrowhead junctions.
Reduction: Reduced trailing marks to one dash per edge.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '0e26bfd0-c84a-5afd-af45-9efcb51b9f95'
SOURCE_PATH = 'pictographic-primitives/arrows/arrow dash corner point left_0e26bfd0-c84a-5afd-af45-9efcb51b9f95.svg'
SOURCE_ICON_IDS = ('0e26bfd0-c84a-5afd-af45-9efcb51b9f95',)
SOURCE_PATHS = ('pictographic-primitives/arrows/arrow dash corner point left_0e26bfd0-c84a-5afd-af45-9efcb51b9f95.svg',)
AUTHOR = 'gpt-6'


class ArrowTurningLeftWithDashedTail(Solo48):
    icon_id = 'arrow-turning-left-with-dashed-tail'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'arrows'
    aliases = ()
    keywords = ('arrow', 'turning', 'left', 'with', 'dashed', 'tail')

    def build(self) -> None:
        self.add_polyline("outer",(22,6),(6,18),(42,18),(42,32))
        self.add_line("head-lower",(6,18),(22,30))
        self.relate("connect","outer","head-lower")
        self.add_polyline("inner",(22,30),(30,30),(30,32))
        self.relate("connect","head-lower","inner")
        for x in (30,42): self.add_line(f"dash-{x}",(x,40),(x,42))
