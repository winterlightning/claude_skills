"""Plus Sign: Two equal straight strokes cross at their centres to form a balanced plus sign. Generate this component alone; exclude Heart Frame.

Construction: Two equal crossing strokes form the isolated source plus.
Keyshape: SQUARE; final SUB32 envelope.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '1a3dfb1a-5701-4324-a7a3-eec313f6a36e'
SOURCE_PATH = 'pictographic-primitives/state/heart medical cross_1a3dfb1a-5701-4324-a7a3-eec313f6a36e.svg'
AUTHOR = 'gpt-6'


class PlusSignState131(Sub32):
    icon_id = 'plus-sign-state-131'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'state'
    categories = ('state',)
    aliases = ()
    keywords = ('plus', 'sign', 'equal', 'straight', 'strokes', 'cross', 'centres', 'form')

    def build(self):
        self.add_line('horizontal',(2,16),(30,16))
        self.add_line('vertical',(16,2),(16,30))
        self.relate('connect','horizontal','vertical')
