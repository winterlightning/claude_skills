"""Plus Sign: A small plus sign has two equal crossing strokes. Generate this component alone; exclude Circle Frame, User Bust.

Construction: Isolate the equal-arm plus from its portrait and circle.
Keyshape: SQUARE; the four extrema follow the SUB32 contract.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '3de9999e-7410-4c80-9d5a-2a8cd07b4298'
SOURCE_PATH = 'pictographic-primitives/state/circle user plus_3de9999e-7410-4c80-9d5a-2a8cd07b4298.svg'
AUTHOR = 'gpt-6'


class PlusSignState87(Sub32):
    icon_id = 'plus-sign-state-87'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives/shape'
    aliases = ()
    keywords = ('plus', 'sign', 'small', 'equal', 'crossing', 'strokes')

    def build(self):
        self.add_line('horizontal',(2,16),(30,16))
        self.add_line('vertical',(16,2),(16,30))
        self.relate('connect','horizontal','vertical')
