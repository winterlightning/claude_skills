"""Letter R: An uppercase R combines a straight upright stem, rounded upper bowl, and diagonal leg descending to the right. Generate this component alone; exclude Circle Frame.

Construction: An upright, upper elliptical bowl and diagonal leg share attachment nodes.
Keyshape: VRECT_L; the four extrema follow the SUB32 contract.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = 'bacc3012-d61e-47f0-8068-aba74c1f83c7'
SOURCE_PATH = 'pictographic-primitives/state/circle R_bacc3012-d61e-47f0-8068-aba74c1f83c7.svg'
AUTHOR = 'gpt-6'


class LetterRSub(Sub32):
    icon_id = 'letter-r-sub'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'state'
    aliases = ()
    keywords = ('letter', 'r', 'uppercase', 'combines', 'straight', 'upright', 'stem', 'rounded')

    def build(self):
        self.add_line('stem',(6,2),(6,30))
        self.add_line('top',(6,2),(16,2))
        self.add_arc('round',(16,2),(16,16),radius_x=10,radius_y=7)
        self.add_line('middle',(16,16),(6,16))
        self.add_contour('bowl','top','round','middle')
        self.add_line('leg',(16,16),(26,30))
        self.relate('connect','stem','bowl')
        self.relate('connect','bowl','leg')
