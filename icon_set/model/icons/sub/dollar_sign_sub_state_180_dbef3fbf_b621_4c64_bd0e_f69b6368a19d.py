"""Dollar Sign: An S-shaped curve has a short upright stem projecting above and below, forming an open dollar sign. Generate this component alone; exclude Rectangle Frame.

Construction: A rounded S has short upper and lower stems only, matching the source absence of a crossing centre stroke.
Keyshape: VRECT_L; final SUB32 envelope.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = 'dbef3fbf-b621-4c64-bd0e-f69b6368a19d'
SOURCE_PATH = 'pictographic-primitives/state/money bill dollar_dbef3fbf-b621-4c64-bd0e-f69b6368a19d.svg'
AUTHOR = 'gpt-6'


class DollarSignSubState180(Sub32):
    icon_id = 'dollar-sign-sub-state-180'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'state'
    categories = ('state',)
    aliases = ()
    keywords = ('dollar', 'sign', 's', 'shaped', 'curve', 'short', 'upright', 'stem')

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
