"""Plus Minus: A plus sign stands above a separate horizontal minus stroke. The plus has equal crossing arms, and the lower line is centred beneath it with a broad vertical gap.

Construction: Plus centred above minus; true crossing split into shared centre endpoints.
Keyshape: VRECT_L; extremes follow the SUB32 contract.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '8fa308a1-3be9-4ab9-baba-2f507d871486'
SOURCE_PATH = 'pictographic-primitives/state/plus minus_8fa308a1-3be9-4ab9-baba-2f507d871486.svg'
AUTHOR = 'gpt-6'


class PlusMinusSub(Sub32):
    icon_id = 'plus-minus-sub'
    keyshape = Keyshape.VRECT_L
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = "primitives/mark"
    aliases = ()
    keywords = ('plus', 'minus', 'sign', 'stands', 'separate', 'horizontal', 'stroke', 'equal')

    def build(self):
        self.add_polyline("vertical",(16,2),(16,12),(16,22))
        self.add_polyline("horizontal",(6,12),(16,12),(26,12))
        self.relate("connect","vertical","horizontal")
        self.add_line("minus",(6,30),(26,30))
