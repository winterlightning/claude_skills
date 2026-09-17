"""Cross Mark: Two equal diagonal strokes intersect to form an X. Generate this component alone; exclude Divided Capsule Frame, Check Mark.

Construction: Isolate the diagonal X from the capsule and neighbouring check.
Keyshape: SQUARE; the four extrema follow the SUB32 contract.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '67a3758e-aa06-455b-bb00-226525eeddc2'
SOURCE_PATH = 'pictographic-primitives/state/pill with checkmark and x_67a3758e-aa06-455b-bb00-226525eeddc2.svg'
AUTHOR = 'gpt-6'


class CrossMarkState208(Sub32):
    icon_id = 'cross-mark-state-208'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives/shape'
    aliases = ()
    keywords = ('cross', 'mark', 'equal', 'diagonal', 'strokes', 'intersect', 'form', 'x')

    def build(self):
        self.add_line('down',(2,2),(30,30))
        self.add_line('up',(2,30),(30,2))
        self.relate('connect','down','up')
