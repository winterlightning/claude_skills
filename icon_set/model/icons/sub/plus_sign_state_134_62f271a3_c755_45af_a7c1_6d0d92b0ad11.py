"""Plus Sign: A vertical stroke crosses a matching horizontal stroke at their centres, forming four equal arms. Generate this component alone; exclude House Frame.

Construction: The source plus remains a pair of centred orthogonal strokes.
Keyshape: SQUARE; final SUB32 envelope.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '62f271a3-c755-45af-a7c1-6d0d92b0ad11'
SOURCE_PATH = 'pictographic-primitives/state/home medical cross_62f271a3-c755-45af-a7c1-6d0d92b0ad11.svg'
AUTHOR = 'gpt-6'


class PlusSignState134(Sub32):
    icon_id = 'plus-sign-state-134'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    aliases = ()
    keywords = ('plus', 'sign', 'vertical', 'stroke', 'crosses', 'matching', 'horizontal', 'centres')

    def build(self):
        self.add_line('horizontal',(2,16),(30,16))
        self.add_line('vertical',(16,2),(16,30))
        self.relate('connect','horizontal','vertical')
