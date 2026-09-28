"""Offset Plus Minus: A plus sign sits at upper left and a separate minus sign at lower right, forming a diagonal arrangement. Generate this component alone; exclude Circle Frame.

Construction: An upper-left plus and separate lower-right minus preserve diagonal placement.
Keyshape: SQUARE; the four extrema follow the SUB32 contract.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '5fc5fb01-1b7e-47da-9482-695e21297677'
SOURCE_PATH = 'pictographic-primitives/state/circle plus minus 1_5fc5fb01-1b7e-47da-9482-695e21297677.svg'
AUTHOR = 'gpt-6'


class OffsetPlusMinus(Sub32):
    icon_id = 'offset-plus-minus'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'state'
    categories = ('state',)
    aliases = ()
    keywords = ('offset', 'plus', 'minus', 'sign', 'sits', 'upper', 'left', 'separate')

    def build(self):
        self.add_line('vertical',(10,2),(10,18))
        self.add_line('horizontal',(2,10),(18,10))
        self.relate('connect','vertical','horizontal')
        self.add_line('minus',(18,30),(30,30))
