"""User Bust: A circular head floats above an open semicircular shoulder arc, with a short vertical mark in the torso centre. Generate this component alone; exclude Circle Frame.

Construction: The source detached bust keeps its short central torso mark and open shoulders; exact 4-unit head/body ink gap.
Keyshape: VRECT_L; the four extrema follow the SUB32 contract.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = 'd057817d-368d-4824-8b6d-a0ac8b9d532d'
SOURCE_PATH = 'pictographic-primitives/state/person_d057817d-368d-4824-8b6d-a0ac8b9d532d.svg'
AUTHOR = 'gpt-6'


class UserBustSubState203(Sub32):
    icon_id = 'user-bust-sub-state-203'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'state'
    aliases = ()
    keywords = ('user', 'bust', 'circular', 'head', 'floats', 'open', 'semicircular', 'shoulder')

    def build(self):
        def circle(name,cx,cy,radius):
            self.add_arc(name+"-top",(cx-radius,cy),(cx+radius,cy),radius_x=radius)
            self.add_arc(name+"-bottom",(cx+radius,cy),(cx-radius,cy),radius_x=radius)
            self.add_contour(name,name+"-top",name+"-bottom",closed=True)
        circle('head',16,7,5)
        self.add_arc('shoulders',(6,30),(26,30),radius_x=10)
        self.add_line('torso-mark',(16,28),(16,30))
