"""Plus Sign: Two equal straight strokes intersect at their centres to form a balanced plus. Generate this component alone; exclude Magnifying Glass Frame.

Construction: The source centred plus retains equal orthogonal arms.
Keyshape: SQUARE; the four extrema follow the SUB32 contract.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '1def2ef1-f927-4218-84fc-c0b5791fb075'
SOURCE_PATH = 'pictographic-primitives/state/search medical cross_1def2ef1-f927-4218-84fc-c0b5791fb075.svg'
AUTHOR = 'gpt-6'


class PlusSignState249(Sub32):
    icon_id = 'plus-sign-state-249'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'state'
    aliases = ()
    keywords = ('plus', 'sign', 'equal', 'straight', 'strokes', 'intersect', 'centres', 'form')

    def build(self):
        self.add_line('horizontal',(2,16),(30,16))
        self.add_line('vertical',(16,2),(16,30))
        self.relate('connect','horizontal','vertical')
