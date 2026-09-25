"""Plus Minus Sign: A plus sign stands directly above a detached horizontal minus sign, both centred on the same axis. Generate this component alone; exclude Circle Frame.

Construction: A centred plus remains above a separate minus of equal width.
Keyshape: SQUARE; final SUB32 envelope.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = '3f98c7ee-fee3-4e59-a8f0-396c97cdef92'
SOURCE_PATH = 'pictographic-primitives/state/circle math_3f98c7ee-fee3-4e59-a8f0-396c97cdef92.svg'
AUTHOR = 'gpt-6'

class PlusMinusSignState64ContainerSymbol(Sub32):
    icon_id = 'plus-minus-sign-state-64-symbol'
    related_origin_icon_id = 'plus-minus-sign-state-64'
    variant_label = 'Independent container symbol'
    usage_category = 'symbol'
    related_group = 'sub-origin/plus-minus-sign-state-64'
    counterpart_icon_id = 'plus-minus-sign-state-64'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'state'
    aliases = ()
    keywords = ('plus', 'minus', 'sign', 'stands', 'directly', 'detached', 'horizontal', 'both')

    def build(self):
        self.add_line('upright', (16, 2), (16, 18))
        self.add_line('crossbar', (2, 10), (30, 10))
        self.relate('connect', 'upright', 'crossbar')
        self.add_line('minus', (2, 30), (30, 30))
