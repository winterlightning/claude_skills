"""Two stick people holding hands; bounds (2,2)-(46,46).

Construction reference: Lucide person-standing: spare straight limbs; source retains circular heads and joined hands.
Centerline extremes are the declared keyshape's exact bounds.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '6c0a315d-d919-5e6b-8ff3-48d670cea3b4'
SOURCE_PATH = 'pictographic-primitives/culture/batch-07/primitive symbols group_6c0a315d-d919-5e6b-8ff3-48d670cea3b4.svg'
AUTHOR = 'astra-chatgpt'


class TwoStickFigures(Solo48):
    icon_id = 'two-stick-figures'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/culture"
    aliases = ()
    keywords = ('stick figure', 'people', 'primitive', 'cave art', 'pair', 'symbols', 'human', 'ancient')

    def build(self) -> None:
        for side, x, outer, inner in (("left", 12, 2, 22), ("right", 36, 46, 26)):
            self.add_arc(side+"-head-a", (x, 2), (x, 10), radius_x=4)
            self.add_arc(side+"-head-b", (x, 10), (x, 2), radius_x=4)
            self.add_contour(side+"-head", side+"-head-a", side+"-head-b", closed=True)
            self.add_polyline(side+"-body", (x, 10), (x, 19), (x, 32))
            self.add_polyline(side+"-arms", (outer, 28), (x, 19), (24, 29))
            self.add_polyline(side+"-legs", (outer+ (2 if side=="left" else -2), 46), (x, 32), (inner, 46))
            self.relate("connect", side+"-head", side+"-body")
            self.relate("connect", side+"-body", side+"-arms")
            self.relate("connect", side+"-body", side+"-legs")
        self.relate("connect", "left-arms", "right-arms")
