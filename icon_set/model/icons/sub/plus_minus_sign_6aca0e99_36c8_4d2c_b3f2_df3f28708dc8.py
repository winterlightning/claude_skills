"""Plus Minus Sign: A plus sign sits above a separate horizontal minus sign, with both marks centred on the same vertical axis. Generate this component alone; exclude Drop Frame.

Construction: A centred plus and separate lower minus share equal horizontal lengths.
Keyshape: SQUARE; the four extrema follow the SUB32 contract.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '6aca0e99-36c8-4d2c-b3f2-df3f28708dc8'
SOURCE_PATH = 'pictographic-primitives/state/blood add minus_6aca0e99-36c8-4d2c-b3f2-df3f28708dc8.svg'
AUTHOR = 'gpt-6'


class PlusMinusSign(Sub32):
    icon_id = 'plus-minus-sign'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    aliases = ()
    keywords = ('plus', 'minus', 'sign', 'sits', 'separate', 'horizontal', 'both', 'marks')

    def build(self):
        self.add_line('upright',(16,2),(16,18))
        self.add_line('crossbar',(2,10),(30,10))
        self.relate('connect','upright','crossbar')
        self.add_line('minus',(2,30),(30,30))
