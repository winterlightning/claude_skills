"""Letter A: An uppercase A has straight sloping sides meeting at a pointed apex and a horizontal crossbar across its lower half. Generate this component alone; exclude Circle Frame.

Construction: A pointed A with a crossbar retains the source open upright letter.
Keyshape: SQUARE; final SUB32 envelope.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '9acf2ddc-e641-4e61-bf85-234e98a67475'
SOURCE_PATH = 'pictographic-primitives/state/circle a_9acf2ddc-e641-4e61-bf85-234e98a67475.svg'
AUTHOR = 'gpt-6'


class LetterASubState46(Sub32):
    icon_id = 'letter-a-sub-state-46'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    aliases = ()
    keywords = ('letter', 'uppercase', 'straight', 'sloping', 'sides', 'meeting', 'pointed', 'apex')

    def build(self):
        self.add_polyline('a',(2,30),(16,2),(30,30))
        self.add_line('bar',(8,18),(24,18))
        self.relate('connect','a','bar')
