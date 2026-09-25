"""Two Text Lines: Two horizontal lines share a left edge, with the upper line noticeably longer than the lower one. Generate this component alone; exclude Magnifying Glass Frame.

Construction: Two left-aligned strokes retain the long upper and shorter lower proportions.
Keyshape: HRECT_S; authored to the SUB32 envelope.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '95ce7206-163d-407b-992a-15a039d71489'
SOURCE_PATH = 'pictographic-primitives/state/magnify glass 1_95ce7206-163d-407b-992a-15a039d71489.svg'
AUTHOR = 'gpt-6'


class TwoTextLines(Sub32):
    icon_id = 'two-text-lines'
    keyshape = Keyshape.HRECT_S
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'state'
    aliases = ()
    keywords = ('text', 'lines', 'horizontal', 'share', 'left', 'edge', 'upper', 'line')

    def build(self):
        self.add_line('upper',(2,10),(30,10))
        self.add_line('lower',(2,22),(20,22))
