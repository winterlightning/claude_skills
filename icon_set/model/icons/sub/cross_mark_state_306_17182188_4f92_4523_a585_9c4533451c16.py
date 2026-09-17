"""Cross Mark: Two diagonal strokes intersect centrally to form an evenly balanced X. Generate this component alone; exclude Map Pin Frame.

Construction: The source X is isolated from its location-pin frame.
Keyshape: SQUARE; the four extrema follow the SUB32 contract.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '17182188-4f92-4523-a585-9c4533451c16'
SOURCE_PATH = 'pictographic-primitives/state/x pin_17182188-4f92-4523-a585-9c4533451c16.svg'
AUTHOR = 'gpt-6'


class CrossMarkState306(Sub32):
    icon_id = 'cross-mark-state-306'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    aliases = ()
    keywords = ('cross', 'mark', 'diagonal', 'strokes', 'intersect', 'centrally', 'form', 'evenly')

    def build(self):
        self.add_line('down',(2,2),(30,30))
        self.add_line('up',(2,30),(30,2))
        self.relate('connect','down','up')
