"""Two Offset Crosses: Two upright strokes have short horizontal crossbars at different heights, lower on the left and higher on the right. Generate this component alone; exclude Rounded Rectangle Frame.

Construction: Two upright strokes have equal crossbars at different heights, lower left and upper right.
Keyshape: HRECT_XL; authored to the SUB32 envelope.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '9a4bbab3-550c-4407-82c3-7568b5d88688'
SOURCE_PATH = 'pictographic-primitives/state/service system_9a4bbab3-550c-4407-82c3-7568b5d88688.svg'
AUTHOR = 'gpt-6'


class TwoOffsetCrosses(Sub32):
    icon_id = 'two-offset-crosses'
    keyshape = Keyshape.HRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    aliases = ()
    keywords = ('offset', 'crosses', 'upright', 'strokes', 'have', 'short', 'horizontal', 'crossbars')

    def build(self):
        for name,x,y in (('left',8,20),('right',24,12)):
            self.add_line(name+'-stem',(x,4),(x,28))
            self.add_line(name+'-bar',(x-6,y),(x+6,y))
            self.relate('connect',name+'-stem',name+'-bar')
