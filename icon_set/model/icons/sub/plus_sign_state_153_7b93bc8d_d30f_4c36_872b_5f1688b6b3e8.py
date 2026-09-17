"""Plus Sign: Two equal perpendicular strokes cross at their centres to form a balanced plus sign with four straight arms. Generate this component alone; exclude Magnifying Glass Frame.

Construction: The isolated plus preserves equal arms and its central crossing.
Keyshape: SQUARE; final SUB32 envelope.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '7b93bc8d-d30f-4c36-872b-5f1688b6b3e8'
SOURCE_PATH = 'pictographic-primitives/state/magnifying glass add_7b93bc8d-d30f-4c36-872b-5f1688b6b3e8.svg'
AUTHOR = 'gpt-6'


class PlusSignState153(Sub32):
    icon_id = 'plus-sign-state-153'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    aliases = ()
    keywords = ('plus', 'sign', 'equal', 'perpendicular', 'strokes', 'cross', 'centres', 'form')

    def build(self):
        self.add_line('horizontal',(2,16),(30,16))
        self.add_line('vertical',(16,2),(16,30))
        self.relate('connect','horizontal','vertical')
