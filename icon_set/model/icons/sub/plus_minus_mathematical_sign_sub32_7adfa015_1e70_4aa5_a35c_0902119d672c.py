"""Plus Minus Mathematical Sign: user-requested grid-fitted 32px version of plus-minus-mathematical-sign-solo.
Plan: retain source primitive/contour topology and fit CIRCLE ink (0, 0, 32, 32).
All geometry nodes, controls and radii are whole integers; final stroke stays 4.
Source construction and visual references are retained from the solo model.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = '7adfa015-1e70-4aa5-a35c-0902119d672c'
SOURCE_PATH = 'pictographic-primitives/other/circle plus minus_7adfa015-1e70-4aa5-a35c-0902119d672c.svg'
SOLO_SOURCE_ICON_ID = 'plus-minus-mathematical-sign-solo'
AUTHOR = 'gpt-6'

class Drawing(Sub32):
    icon_id = 'plus-minus-mathematical-sign-sub32'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'objects/interface-essential'
    tags = ('sub icon',)
    keywords = ('sub icon', 'grid fitted', 'plus minus mathematical sign')

    def build(self):
        self.add_arc('outline-top', (2, 16), (30, 16), radius_x=14, radius_y=14, large_arc=False, sweep=True)
        self.add_arc('outline-bottom', (30, 16), (2, 16), radius_x=14, radius_y=14, large_arc=False, sweep=True)
        self.add_line('plus-h-1', (11, 12), (12, 12))
        self.add_line('plus-h-2', (12, 12), (14, 12))
        self.add_line('plus-v-1', (12, 11), (12, 12))
        self.add_line('plus-v-2', (12, 12), (12, 14))
        self.add_line('slash', (11, 21), (21, 11))
        self.add_line('minus', (18, 20), (21, 20))
        self.add_contour('outline', 'outline-top', 'outline-bottom', closed=True)
        self.add_contour('plus-h', 'plus-h-1', 'plus-h-2', closed=False)
        self.add_contour('plus-v', 'plus-v-1', 'plus-v-2', closed=False)
        self.relate('connect', 'plus-h', 'plus-v')
        self.add_anchor('center', (16, 16))
