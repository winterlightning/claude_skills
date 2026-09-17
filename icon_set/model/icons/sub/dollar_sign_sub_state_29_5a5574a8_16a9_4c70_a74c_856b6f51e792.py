"""Dollar Sign: An S-shaped dollar sign has short vertical strokes projecting above and below its curved body. Generate this component alone; exclude Board Frame.

Construction: An S with short terminal bars above and below; no invented full-height currency stem.
Keyshape: VRECT_L; final SUB32 envelope.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '5a5574a8-16a9-4c70-a74c-856b6f51e792'
SOURCE_PATH = 'pictographic-primitives/state/board dollar_5a5574a8-16a9-4c70-a74c-856b6f51e792.svg'
AUTHOR = 'gpt-6'


class DollarSignSubState29(Sub32):
    icon_id = 'dollar-sign-sub-state-29'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    aliases = ()
    keywords = ('dollar', 'sign', 's', 'shaped', 'short', 'vertical', 'strokes', 'projecting')

    def build(self):
        self.add_line('top-end',(22,6),(16,6))
        self.add_arc('upper',(16,6),(16,16),radius_x=10,radius_y=5,sweep=False)
        self.add_arc('lower',(16,16),(16,26),radius_x=10,radius_y=5)
        self.add_line('bottom-end',(16,26),(10,26))
        self.add_contour('s','top-end','upper','lower','bottom-end')
        self.add_line('top-tick',(16,2),(16,6))
        self.add_line('bottom-tick',(16,26),(16,30))
        self.relate('connect','s','top-tick')
        self.relate('connect','s','bottom-tick')
