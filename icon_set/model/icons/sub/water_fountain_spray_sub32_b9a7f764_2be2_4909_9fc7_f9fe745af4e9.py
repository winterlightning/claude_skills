"""Water Fountain Spray: user-requested grid-fitted 32px version of water-fountain-spray-solo.
Plan: retain source primitive/contour topology and fit HRECT_XL ink (0, 2, 32, 30).
All geometry nodes, controls and radii are whole integers; final stroke stays 4.
Source construction and visual references are retained from the solo model.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID='b9a7f764-2be2-4909-9fc7-f9fe745af4e9'
SOURCE_PATH='pictographic-primitives/other/fountain_b9a7f764-2be2-4909-9fc7-f9fe745af4e9.svg'
SOLO_SOURCE_ICON_ID='water-fountain-spray-solo'
AUTHOR='gpt-6'
class Drawing(Sub32):
    icon_id='water-fountain-spray-sub32'
    keyshape=Keyshape.HRECT_XL
    semantic_role='SUB'
    semantic_kind='modifier'
    category='objects/interface-essential'
    tags=('sub icon',)
    keywords=('sub icon', 'grid fitted', 'water fountain spray')
    def build(self):
        self.add_bezier('left', (2, 13), ((6, 1), (11, 1), (16, 13)))
        self.add_bezier('right', (16, 13), ((21, 1), (26, 1), (30, 13)))
        self.add_line('stem', (16, 13), (16, 28))
        self.relate('connect', 'left', 'right', 'stem')
        self.add_anchor('center',(16, 16))
