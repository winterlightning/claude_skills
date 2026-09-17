"""Crescent Moon: A crescent has a bowed left edge and a deep concave right edge ending in two pointed horns. Generate this component alone; exclude Rounded Square Frame, Cross Mark.

Construction: Right-opening crescent isolates the moon from its frame and X; preserve source opening direction.
Keyshape: VRECT_L; the four extrema follow the SUB32 contract.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '6baf4ff9-771c-456d-8de8-57ca7ef5601a'
SOURCE_PATH = 'pictographic-primitives/state/moon and cancel_6baf4ff9-771c-456d-8de8-57ca7ef5601a.svg'
AUTHOR = 'gpt-6'


class CrescentMoonSubState182(Sub32):
    icon_id = 'crescent-moon-sub-state-182'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives/shape'
    aliases = ()
    keywords = ('crescent', 'moon', 'bowed', 'left', 'edge', 'deep', 'concave', 'right')

    def build(self):
        self.add_arc('outer',(26,2),(26,30),radius_x=20,radius_y=14,sweep=False)
        self.add_arc('inner',(26,30),(26,2),radius_x=10,radius_y=14)
        self.add_contour('moon','outer','inner',closed=True)
