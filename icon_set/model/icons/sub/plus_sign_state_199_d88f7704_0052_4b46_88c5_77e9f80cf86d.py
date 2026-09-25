"""Plus Sign: Two straight perpendicular strokes cross at their centres. Generate this component alone; exclude Circle Frame, User Bust.

Construction: Isolate the equal-arm plus from the continuous portrait and round frame.
Keyshape: SQUARE; the four extrema follow the SUB32 contract.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = 'd88f7704-0052-4b46-88c5-77e9f80cf86d'
SOURCE_PATH = 'pictographic-primitives/state/person with plus_d88f7704-0052-4b46-88c5-77e9f80cf86d.svg'
AUTHOR = 'gpt-6'


class PlusSignState199(Sub32):
    icon_id = 'plus-sign-state-199'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'state'
    aliases = ()
    keywords = ('plus', 'sign', 'straight', 'perpendicular', 'strokes', 'cross', 'centres')

    def build(self):
        self.add_line('horizontal',(2,16),(30,16))
        self.add_line('vertical',(16,2),(16,30))
        self.relate('connect','horizontal','vertical')
