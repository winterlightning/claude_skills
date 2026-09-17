"""Letter C: A large uppercase C forms an almost circular curve with an open gap on its right side. Generate this component alone; exclude Circle Frame.

Construction: A left half ellipse joins short horizontal terminals tangentially; top and bottom mirror.
Keyshape: VRECT_L; the four extrema follow the SUB32 contract.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '7c2869d8-7c0f-4e63-8d8d-61a81b4c34c2'
SOURCE_PATH = 'pictographic-primitives/state/circle c_7c2869d8-7c0f-4e63-8d8d-61a81b4c34c2.svg'
AUTHOR = 'gpt-6'


class LetterCSub(Sub32):
    icon_id = 'letter-c-sub'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    aliases = ()
    keywords = ('letter', 'c', 'large', 'uppercase', 'forms', 'almost', 'circular', 'curve')

    def build(self):
        self.add_line('top',(26,2),(20,2))
        self.add_arc('curve',(20,2),(20,30),radius_x=14,radius_y=14,sweep=False)
        self.add_line('bottom',(20,30),(26,30))
        self.add_contour('c','top','curve','bottom')
