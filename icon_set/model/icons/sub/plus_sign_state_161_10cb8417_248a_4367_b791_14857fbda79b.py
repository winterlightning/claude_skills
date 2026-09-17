"""Plus Sign: A vertical stroke intersects a horizontal stroke at its midpoint, forming a simple balanced cross. Generate this component alone; exclude Clipboard Frame.

Construction: One centred plus remains after removing the source clipboard enclosure.
Keyshape: SQUARE; final SUB32 envelope.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '10cb8417-248a-4367-b791-14857fbda79b'
SOURCE_PATH = 'pictographic-primitives/state/medical note 1_10cb8417-248a-4367-b791-14857fbda79b.svg'
AUTHOR = 'gpt-6'


class PlusSignState161(Sub32):
    icon_id = 'plus-sign-state-161'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    aliases = ()
    keywords = ('plus', 'sign', 'vertical', 'stroke', 'intersects', 'horizontal', 'midpoint', 'forming')

    def build(self):
        self.add_line('horizontal',(2,16),(30,16))
        self.add_line('vertical',(16,2),(16,30))
        self.relate('connect','horizontal','vertical')
