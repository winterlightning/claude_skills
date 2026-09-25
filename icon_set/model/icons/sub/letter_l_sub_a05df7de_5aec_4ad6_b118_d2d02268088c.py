"""Letter L: An uppercase L consists of a long vertical stem joined to a shorter horizontal foot extending to the right. Generate this component alone; exclude Circle Frame.

Construction: An upright and foot form one simple L contour.
Keyshape: VRECT_L; the four extrema follow the SUB32 contract.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = 'a05df7de-5aec-4ad6-b118-d2d02268088c'
SOURCE_PATH = 'pictographic-primitives/state/circle L_a05df7de-5aec-4ad6-b118-d2d02268088c.svg'
AUTHOR = 'gpt-6'


class LetterLSub(Sub32):
    icon_id = 'letter-l-sub'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'state'
    aliases = ()
    keywords = ('letter', 'l', 'uppercase', 'consists', 'long', 'vertical', 'stem', 'joined')

    def build(self):
        self.add_polyline('letter',(6,2),(6,30),(26,30))
