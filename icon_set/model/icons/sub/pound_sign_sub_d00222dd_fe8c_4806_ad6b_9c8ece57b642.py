"""Pound Sign: A pound sign has a curved upper hook, upright stem, middle crossbar, and a flat lower foot extending right. Generate this component alone; exclude Circle Frame.

Construction: A rounded upper hook flows tangentially into a vertical stem above a broad foot and crossing bar.
Keyshape: VRECT_L; the four extrema follow the SUB32 contract.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = 'd00222dd-fe8c-4806-ad6b-9c8ece57b642'
SOURCE_PATH = 'pictographic-primitives/state/circle pound_d00222dd-fe8c-4806-ad6b-9c8ece57b642.svg'
AUTHOR = 'gpt-6'


class PoundSignSub(Sub32):
    icon_id = 'pound-sign-sub'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'state'
    categories = ('state',)
    aliases = ()
    keywords = ('pound', 'sign', 'curved', 'upper', 'hook', 'upright', 'stem', 'middle')

    def build(self):
        self.add_arc('hook',(26,8),(12,8),radius_x=7,radius_y=6,sweep=False)
        self.add_line('stem',(12,8),(12,30))
        self.add_contour('body','hook','stem')
        self.add_line('bar',(6,18),(22,18))
        self.add_line('foot',(6,30),(26,30))
        self.relate('connect','body','bar')
        self.relate('connect','body','foot')
