"""Zero: A tall oval zero forms a single closed loop with an empty centre. Generate this component alone; exclude Circle Frame.

Construction: One upright ellipse, symmetric around the canvas centre.
Keyshape: VRECT_L; the four extrema follow the SUB32 contract.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = 'e3714f65-499d-4ba7-9ecb-87ecc26acfff'
SOURCE_PATH = 'pictographic-primitives/state/0 text in circle_e3714f65-499d-4ba7-9ecb-87ecc26acfff.svg'
AUTHOR = 'gpt-6'


class Zero(Sub32):
    icon_id = 'zero'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'state'
    aliases = ()
    keywords = ('zero', 'tall', 'oval', 'forms', 'single', 'closed', 'loop', 'empty')

    def build(self):
        self.add_arc('left',(16,2),(16,30),radius_x=10,radius_y=14,sweep=False)
        self.add_arc('right',(16,30),(16,2),radius_x=10,radius_y=14,sweep=False)
        self.add_contour('zero','left','right',closed=True)
