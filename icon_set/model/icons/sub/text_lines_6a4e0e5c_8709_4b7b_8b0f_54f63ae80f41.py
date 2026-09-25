"""Text Lines: Two horizontal text lines are stacked with space between them, with the upper line longer than the lower one. Generate this component alone; exclude Speech Bubble.

Construction: Two left-aligned strokes with a shorter lower line.
Keyshape: HRECT_M; the four extrema follow the SUB32 contract.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '6a4e0e5c-8709-4b7b-8b0f-54f63ae80f41'
SOURCE_PATH = 'pictographic-primitives/state/chat bubble 1_6a4e0e5c-8709-4b7b-8b0f-54f63ae80f41.svg'
AUTHOR = 'gpt-6'


class TextLines(Sub32):
    icon_id = 'text-lines'
    keyshape = Keyshape.HRECT_M
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'state'
    categories = ('state',)
    aliases = ()
    keywords = ('text', 'lines', 'horizontal', 'are', 'stacked', 'space', 'between', 'them')

    def build(self):
        self.add_line('upper',(2,8),(30,8))
        self.add_line('lower',(2,24),(22,24))
