"""Two Text Lines: Two left-aligned horizontal lines sit one above the other, with the lower line slightly longer. Generate this component alone; exclude Folded Document Frame.

Construction: The lower of two left-aligned source text lines remains slightly longer.
Keyshape: HRECT_S; the four extrema follow the SUB32 contract.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '79cdd0a6-8dc1-4fc9-b435-3c790f3688ef'
SOURCE_PATH = 'pictographic-primitives/state/rectangle with lines_79cdd0a6-8dc1-4fc9-b435-3c790f3688ef.svg'
AUTHOR = 'gpt-6'


class TwoTextLinesState235(Sub32):
    icon_id = 'two-text-lines-state-235'
    keyshape = Keyshape.HRECT_S
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    aliases = ()
    keywords = ('text', 'lines', 'left', 'aligned', 'horizontal', 'sit', 'other', 'lower')

    def build(self):
        self.add_line('upper',(2,10),(26,10))
        self.add_line('lower',(2,22),(30,22))
