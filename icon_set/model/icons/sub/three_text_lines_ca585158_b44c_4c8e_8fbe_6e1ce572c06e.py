"""Three Text Lines: Three horizontal lines share a left alignment; the upper two are equal and the bottom line is shorter. Generate this component alone; exclude Tall Rectangle Frame.

Construction: Three left-aligned text strokes; the lower is shorter, as in the source.
Keyshape: VRECT_L; authored to the SUB32 envelope.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = 'ca585158-b44c-4c8e-8fbe-6e1ce572c06e'
SOURCE_PATH = 'pictographic-primitives/state/rectangle with lines_ca585158-b44c-4c8e-8fbe-6e1ce572c06e.svg'
AUTHOR = 'gpt-6'


class ThreeTextLines(Sub32):
    icon_id = 'three-text-lines'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    aliases = ()
    keywords = ('text', 'lines', 'horizontal', 'share', 'left', 'alignment', 'upper', 'are')

    def build(self):
        self.add_line('upper',(6,2),(26,2))
        self.add_line('middle',(6,16),(26,16))
        self.add_line('lower',(6,30),(20,30))
