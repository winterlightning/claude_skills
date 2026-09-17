"""Plus Sign: A simple plus sign consists of a vertical stroke crossed centrally by a horizontal stroke. Generate this component alone; exclude Paw Frame.

Construction: The standalone plus is isolated from the source paw frame.
Keyshape: SQUARE; final SUB32 envelope.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = 'de729c05-6cce-4720-a0be-a92e22cd665a'
SOURCE_PATH = 'pictographic-primitives/state/paw print with a cross_de729c05-6cce-4720-a0be-a92e22cd665a.svg'
AUTHOR = 'gpt-6'


class PlusSignState195(Sub32):
    icon_id = 'plus-sign-state-195'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    aliases = ()
    keywords = ('plus', 'sign', 'simple', 'consists', 'vertical', 'stroke', 'crossed', 'centrally')

    def build(self):
        self.add_line('horizontal',(2,16),(30,16))
        self.add_line('vertical',(16,2),(16,30))
        self.relate('connect','horizontal','vertical')
