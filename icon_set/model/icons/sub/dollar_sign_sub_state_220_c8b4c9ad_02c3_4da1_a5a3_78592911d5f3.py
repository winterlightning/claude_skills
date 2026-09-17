"""Dollar Sign: A narrow S-shaped curve has a short vertical extension at its top and bottom. Generate this component alone; exclude Service Sign Frame.

Construction: The source S has short upper and lower stems only; no crossing central stem is added.
Keyshape: VRECT_L; the four extrema follow the SUB32 contract.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = 'c8b4c9ad-02c3-4da1-a5a3-78592911d5f3'
SOURCE_PATH = 'pictographic-primitives/state/public service dollar_c8b4c9ad-02c3-4da1-a5a3-78592911d5f3.svg'
AUTHOR = 'gpt-6'


class DollarSignSubState220(Sub32):
    icon_id = 'dollar-sign-sub-state-220'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    aliases = ()
    keywords = ('dollar', 'sign', 'narrow', 's', 'shaped', 'curve', 'short', 'vertical')

    def build(self):
        self.add_arc('top',(26,10),(6,10),radius_x=10,radius_y=4,sweep=False)
        self.add_arc('upper-return',(6,10),(16,16),radius_x=10,radius_y=6,sweep=False)
        self.add_arc('lower-start',(16,16),(26,22),radius_x=10,radius_y=6)
        self.add_arc('bottom',(26,22),(6,22),radius_x=10,radius_y=4)
        self.add_contour('s','top','upper-return','lower-start','bottom')
        self.add_line('top-tick',(16,2),(16,6))
        self.add_line('bottom-tick',(16,26),(16,30))
        self.relate('connect','s','top-tick')
        self.relate('connect','s','bottom-tick')
