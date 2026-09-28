"""Plus Sign: A straight upright stroke crosses an equal horizontal stroke at their centres, forming four balanced arms. Generate this component alone; exclude Circle Frame.

Construction: The source plus is slightly wider than tall, with a single central crossing.
Keyshape: HRECT_XL; final SUB32 envelope.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = 'c8cdc83b-0683-4b47-8454-a4e5b0461a29'
SOURCE_PATH = 'pictographic-primitives/state/circle medical cross_c8cdc83b-0683-4b47-8454-a4e5b0461a29.svg'
AUTHOR = 'gpt-6'


class PlusSignState66(Sub32):
    icon_id = 'plus-sign-state-66'
    keyshape = Keyshape.HRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'state'
    categories = ('state',)
    aliases = ()
    keywords = ('plus', 'sign', 'straight', 'upright', 'stroke', 'crosses', 'equal', 'horizontal')

    def build(self):
        self.add_line('horizontal',(2,16),(30,16))
        self.add_line('vertical',(16,4),(16,28))
        self.relate('connect','horizontal','vertical')
