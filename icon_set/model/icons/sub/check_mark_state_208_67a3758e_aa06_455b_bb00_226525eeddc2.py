"""Check Mark: A short descending arm joins a longer ascending arm at a low angular corner. Generate this component alone; exclude Divided Capsule Frame, Cross Mark.

Construction: The source check is isolated from the divided capsule and adjacent X.
Keyshape: HRECT_M; the four extrema follow the SUB32 contract.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '67a3758e-aa06-455b-bb00-226525eeddc2'
SOURCE_PATH = 'pictographic-primitives/state/pill with checkmark and x_67a3758e-aa06-455b-bb00-226525eeddc2.svg'
AUTHOR = 'gpt-6'


class CheckMarkState208(Sub32):
    icon_id = 'check-mark-state-208'
    keyshape = Keyshape.HRECT_M
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    aliases = ()
    keywords = ('check', 'mark', 'short', 'descending', 'arm', 'joins', 'longer', 'ascending')

    def build(self):
        self.add_polyline('check',(2,14),(12,24),(30,8))
