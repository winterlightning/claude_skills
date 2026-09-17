"""Cross Mark: Two equal diagonal strokes cross at their midpoints to form an X. Generate this component alone; exclude Circle Frame.

Construction: The source circular frame is excluded, retaining its plain diagonal X.
Keyshape: SQUARE; the four extrema follow the SUB32 contract.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '1db6929b-7342-43b7-a628-129ea6599ef1'
SOURCE_PATH = 'pictographic-primitives/state/state remove_1db6929b-7342-43b7-a628-129ea6599ef1.svg'
AUTHOR = 'gpt-6'


class CrossMarkState269(Sub32):
    icon_id = 'cross-mark-state-269'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    aliases = ()
    keywords = ('cross', 'mark', 'equal', 'diagonal', 'strokes', 'midpoints', 'form', 'x')

    def build(self):
        self.add_line('down',(2,2),(30,30))
        self.add_line('up',(2,30),(30,2))
        self.relate('connect','down','up')
