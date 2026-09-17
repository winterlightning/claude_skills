"""Cross Mark: Two diagonal strokes cross at their centres, forming an evenly balanced X. Generate this component alone; exclude Rounded Rectangle Frame.

Construction: A centred diagonal X is isolated from its enclosing rectangular frame.
Keyshape: SQUARE; the four extrema follow the SUB32 contract.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '104467b1-f804-420a-a178-c7d9d6634b03'
SOURCE_PATH = 'pictographic-primitives/state/rectangle remove_104467b1-f804-420a-a178-c7d9d6634b03.svg'
AUTHOR = 'gpt-6'


class CrossMarkState230(Sub32):
    icon_id = 'cross-mark-state-230'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    aliases = ()
    keywords = ('cross', 'mark', 'diagonal', 'strokes', 'centres', 'forming', 'evenly', 'balanced')

    def build(self):
        self.add_line('down',(2,2),(30,30))
        self.add_line('up',(2,30),(30,2))
        self.relate('connect','down','up')
