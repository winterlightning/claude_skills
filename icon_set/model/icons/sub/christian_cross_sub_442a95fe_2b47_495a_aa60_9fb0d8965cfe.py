"""Christian Cross: An upright cross has a long vertical stem and a shorter horizontal crossbar positioned above its centre. Generate this component alone; exclude Circle Frame.

Construction: A long vertical stem has one shorter crossbar above its midpoint.
Keyshape: VRECT_L; the four extrema follow the SUB32 contract.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '442a95fe-2b47-495a-aa60-9fb0d8965cfe'
SOURCE_PATH = 'pictographic-primitives/state/circle christian cross_442a95fe-2b47-495a-aa60-9fb0d8965cfe.svg'
AUTHOR = 'gpt-6'


class ChristianCrossSub(Sub32):
    icon_id = 'christian-cross-sub'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    aliases = ()
    keywords = ('christian', 'cross', 'upright', 'long', 'vertical', 'stem', 'shorter', 'horizontal')

    def build(self):
        self.add_line('upright',(16,2),(16,30))
        self.add_line('bar',(6,12),(26,12))
        self.relate('connect','upright','bar')
