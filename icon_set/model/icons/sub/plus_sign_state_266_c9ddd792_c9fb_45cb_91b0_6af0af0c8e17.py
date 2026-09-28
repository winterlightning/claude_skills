"""Plus Sign: A vertical and horizontal stroke cross at their centres, forming four equal arms. Generate this component alone; exclude Rounded Square Frame.

Construction: The source plus remains a centred crossing of two equal strokes.
Keyshape: SQUARE; the four extrema follow the SUB32 contract.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = 'c9ddd792-c9fb-45cb-91b0-6af0af0c8e17'
SOURCE_PATH = 'pictographic-primitives/state/square medical cross_c9ddd792-c9fb-45cb-91b0-6af0af0c8e17.svg'
AUTHOR = 'gpt-6'


class PlusSignState266(Sub32):
    icon_id = 'plus-sign-state-266'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'state'
    categories = ('state',)
    aliases = ()
    keywords = ('plus', 'sign', 'vertical', 'horizontal', 'stroke', 'cross', 'centres', 'forming')

    def build(self):
        self.add_line('horizontal',(2,16),(30,16))
        self.add_line('vertical',(16,2),(16,30))
        self.relate('connect','horizontal','vertical')
