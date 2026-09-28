"""User Bust: A continuous rounded head narrows into a neck and flares into two open shoulders. Generate this component alone; exclude Circle Frame, Plus Sign.

Construction: A continuous rounded head narrows into a neck then flares into open shoulders, as in the original.
Keyshape: SQUARE; final SUB32 envelope.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = 'd88f7704-0052-4b46-88c5-77e9f80cf86d'
SOURCE_PATH = 'pictographic-primitives/state/person with plus_d88f7704-0052-4b46-88c5-77e9f80cf86d.svg'
AUTHOR = 'gpt-6'


class UserBustSubState199(Sub32):
    icon_id = 'user-bust-sub-state-199'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'state'
    categories = ('state',)
    aliases = ()
    keywords = ('user', 'bust', 'continuous', 'rounded', 'head', 'narrows', 'neck', 'flares')

    def build(self):
        self.add_arc('head-top',(8,10),(24,10),radius_x=8)
        self.add_arc('head-right',(24,10),(20,18),radius_x=10,radius_y=10)
        self.add_arc('neck-right',(20,18),(22,22),radius_x=4,radius_y=4,sweep=False)
        self.add_arc('shoulder-right',(22,22),(30,30),radius_x=8,radius_y=8)
        self.add_arc('shoulder-left',(2,30),(10,22),radius_x=8,radius_y=8)
        self.add_arc('neck-left',(10,22),(12,18),radius_x=4,radius_y=4,sweep=False)
        self.add_arc('head-left',(12,18),(8,10),radius_x=10,radius_y=10)
        self.add_contour('portrait','shoulder-left','neck-left','head-left','head-top','head-right','neck-right','shoulder-right')
