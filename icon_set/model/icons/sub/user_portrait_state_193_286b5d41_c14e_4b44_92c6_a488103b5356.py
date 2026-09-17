"""User Portrait: A continuous head-and-shoulders outline includes rounded hair, small ears, a narrow neck, and outward-sloping shoulders without facial features. Generate this component alone; exclude Book Frame.

Construction: The continuous head, neck and shoulders are isolated from the source book cover; shared human reference informs smooth shoulders.
Keyshape: SQUARE; the four extrema follow the SUB32 contract.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '286b5d41-c14e-4b44-92c6-a488103b5356'
SOURCE_PATH = 'pictographic-primitives/state/passbook person_286b5d41-c14e-4b44-92c6-a488103b5356.svg'
AUTHOR = 'gpt-6'


class UserPortraitState193(Sub32):
    icon_id = 'user-portrait-state-193'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives/shape'
    aliases = ()
    keywords = ('user', 'portrait', 'continuous', 'head', 'shoulders', 'outline', 'includes', 'rounded')

    def build(self):
        self.add_arc('head-top',(8,10),(24,10),radius_x=8)
        self.add_arc('head-right',(24,10),(20,18),radius_x=10,radius_y=10)
        self.add_arc('neck-right',(20,18),(22,22),radius_x=4,radius_y=4,sweep=False)
        self.add_arc('shoulder-right',(22,22),(30,30),radius_x=8,radius_y=8)
        self.add_arc('shoulder-left',(2,30),(10,22),radius_x=8,radius_y=8)
        self.add_arc('neck-left',(10,22),(12,18),radius_x=4,radius_y=4,sweep=False)
        self.add_arc('head-left',(12,18),(8,10),radius_x=10,radius_y=10)
        self.add_contour('portrait','shoulder-left','neck-left','head-left','head-top','head-right','neck-right','shoulder-right')
