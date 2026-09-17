"""Latin Cross: A long vertical stroke is crossed above its midpoint by a shorter horizontal bar. Generate this component alone; exclude Tombstone Frame.

Construction: One tall upright crosses a shorter bar above its midpoint.
Keyshape: VRECT_L; authored to the SUB32 envelope.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = 'd639010e-7131-46d6-b3fa-028d7353a5b9'
SOURCE_PATH = 'pictographic-primitives/state/tombstone_d639010e-7131-46d6-b3fa-028d7353a5b9.svg'
AUTHOR = 'gpt-6'


class LatinCross(Sub32):
    icon_id = 'latin-cross'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    aliases = ()
    keywords = ('latin', 'cross', 'long', 'vertical', 'stroke', 'crossed', 'midpoint', 'shorter')

    def build(self):
        self.add_line('stem',(16,2),(16,30))
        self.add_line('bar',(6,11),(26,11))
        self.relate('connect','stem','bar')
