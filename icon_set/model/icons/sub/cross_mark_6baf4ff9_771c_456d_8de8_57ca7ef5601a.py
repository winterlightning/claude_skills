"""Cross Mark: Two diagonal strokes cross to form an X. Generate this component alone; exclude Rounded Square Frame, Crescent Moon.

Construction: Two equal diagonals cross centrally to form the source X.
Keyshape: SQUARE; authored to the SUB32 envelope.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '6baf4ff9-771c-456d-8de8-57ca7ef5601a'
SOURCE_PATH = 'pictographic-primitives/state/moon and cancel_6baf4ff9-771c-456d-8de8-57ca7ef5601a.svg'
AUTHOR = 'gpt-6'


class CrossMark(Sub32):
    icon_id = 'cross-mark'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    aliases = ()
    keywords = ('cross', 'mark', 'diagonal', 'strokes', 'form', 'x')

    def build(self):
        self.add_line('down',(2,2),(30,30))
        self.add_line('up',(2,30),(30,2))
        self.relate('connect','down','up')
