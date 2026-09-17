"""Crescent Moon: A crescent moon has a rounded outer right edge and a deep inward curve opening to the left, ending in two pointed tips. Generate this component alone; exclude Badge Frame.

Construction: A left-opening crescent is bounded by a broad outer and shallow inner right-bowed arc.
Keyshape: VRECT_L; authored to the SUB32 envelope.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '8940d02c-5859-47ed-aa06-278c4cad9a31'
SOURCE_PATH = 'pictographic-primitives/state/dark mode_8940d02c-5859-47ed-aa06-278c4cad9a31.svg'
AUTHOR = 'gpt-6'


class CrescentMoonSub(Sub32):
    icon_id = 'crescent-moon-sub'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives/shape'
    aliases = ()
    keywords = ('crescent', 'moon', 'rounded', 'outer', 'right', 'edge', 'deep', 'inward')

    def build(self):
        self.add_arc('outer',(6,2),(6,30),radius_x=20,radius_y=14)
        self.add_arc('inner',(6,30),(6,2),radius_x=10,radius_y=14,sweep=False)
        self.add_contour('moon','outer','inner',closed=True)
