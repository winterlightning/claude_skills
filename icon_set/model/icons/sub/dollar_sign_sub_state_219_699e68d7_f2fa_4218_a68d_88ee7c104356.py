"""Dollar Sign: A broad S-shaped curve has short upright extensions above and below, forming a dollar symbol. Generate this component alone; exclude Prohibition Frame.

Construction: The source S has short upper and lower stems only; no crossing central stem is added.
Keyshape: VRECT_L; the four extrema follow the SUB32 contract.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '699e68d7-f2fa-4218-a68d-88ee7c104356'
SOURCE_PATH = 'pictographic-primitives/state/prohitbition dollar_699e68d7-f2fa-4218-a68d-88ee7c104356.svg'
AUTHOR = 'gpt-6'


class DollarSignSubState219(Sub32):
    icon_id = 'dollar-sign-sub-state-219'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    aliases = ()
    keywords = ('dollar', 'sign', 'broad', 's', 'shaped', 'curve', 'short', 'upright')

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
