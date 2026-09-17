"""Rupee Sign: The rupee sign has two upper horizontal bars, a curved bowl, and a long diagonal leg descending right. Generate this component alone; exclude Circle Frame.

Construction: Two top bars cross a circular bowl with an angled top attachment; its bottom turns into a diagonal leg.
Keyshape: VRECT_L; the four extrema follow the SUB32 contract.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = 'a3032c5e-934e-49f8-8e81-03865ad8ed37'
SOURCE_PATH = 'pictographic-primitives/state/circle rupee_a3032c5e-934e-49f8-8e81-03865ad8ed37.svg'
AUTHOR = 'gpt-6'


class RupeeSign(Sub32):
    icon_id = 'rupee-sign'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    aliases = ()
    keywords = ('rupee', 'sign', 'upper', 'horizontal', 'bars', 'curved', 'bowl', 'long')

    def build(self):
        self.add_line('top',(6,2),(26,2))
        self.add_line('bar',(6,10),(26,10))
        self.add_arc('bowl',(14,2),(8,20),radius_x=10,radius_y=10)
        self.add_line('bowl-base',(8,20),(6,20))
        self.add_line('leg',(6,20),(24,30))
        self.add_contour('body','bowl','bowl-base','leg')
        self.relate('connect','body','top')
        self.relate('connect','body','bar')
