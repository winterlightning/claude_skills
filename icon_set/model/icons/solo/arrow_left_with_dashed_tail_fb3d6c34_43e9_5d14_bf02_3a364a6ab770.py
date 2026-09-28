"""Arrow Left with Dashed Tail.

Plan: HRECT centerlines (4,8)-(44,40); broad left arrow with mirrored shaft edges and one paired dash.
Construction references: Lucide arrow-big-up: coherent outline construction, newly authored horizontally.
Reduction: Rejoined the open head to its lower shaft and reduced the tail to one paired dash for a clear broad dashed arrow.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'fb3d6c34-43e9-5d14-bf02-3a364a6ab770'
SOURCE_PATH = 'pictographic-primitives/arrows/arrow dash left_fb3d6c34-43e9-5d14-bf02-3a364a6ab770.svg'
SOURCE_ICON_IDS = ('fb3d6c34-43e9-5d14-bf02-3a364a6ab770',)
SOURCE_PATHS = ('pictographic-primitives/arrows/arrow dash left_fb3d6c34-43e9-5d14-bf02-3a364a6ab770.svg',)
AUTHOR = 'gpt-6'


class ArrowLeftWithDashedTail(Solo48):
    icon_id = 'arrow-left-with-dashed-tail'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'arrows'
    categories = ('arrows', 'primitives')
    aliases = ()
    keywords = ('arrow', 'left', 'with', 'dashed', 'tail')

    def build(self) -> None:
        axis, shaft_half = 24, 6
        upper, lower = axis-shaft_half, axis+shaft_half
        self.add_polyline("head-and-shaft",(32,lower),(20,lower),(20,40),(4,axis),(20,8),(20,upper),(32,upper))
        for side,y in [("upper",upper),("lower",lower)]:
            self.add_line(f"dash-{side}",(40,y),(44,y))
