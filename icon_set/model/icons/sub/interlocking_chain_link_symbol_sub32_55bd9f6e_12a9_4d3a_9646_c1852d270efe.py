"""Interlocking Chain Link Symbol: user-requested grid-fitted 32px version of interlocking-chain-link-symbol-solo.
Plan: retain source primitive/contour topology and fit SQUARE ink (0, 0, 32, 32).
All geometry nodes, controls and radii are whole integers; final stroke stays 4.
Source construction and visual references are retained from the solo model.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID='55bd9f6e-12a9-4d3a-9646-c1852d270efe'
SOURCE_PATH='pictographic-primitives/other/attached file_55bd9f6e-12a9-4d3a-9646-c1852d270efe.svg'
SOLO_SOURCE_ICON_ID='interlocking-chain-link-symbol-solo'
AUTHOR='gpt-6'
class Drawing(Sub32):
    icon_id='interlocking-chain-link-symbol-sub32'
    keyshape=Keyshape.SQUARE
    semantic_role='SUB'
    semantic_kind='modifier'
    category = 'primitives-generate'
    tags=('sub icon',)
    keywords=('sub icon', 'grid fitted', 'interlocking chain link symbol')
    def build(self):
        self.add_bezier('lower-ring-0', (10, 10), ((16, 8), (24, 16), (22, 22)))
        self.add_line('lower-ring-1', (22, 22), (16, 28))
        self.add_bezier('lower-ring-2', (16, 28), ((14, 30), (13, 30), (11, 30)))
        self.add_bezier('lower-ring-3', (11, 30), ((7, 30), (2, 27), (2, 22)))
        self.add_bezier('lower-ring-4', (2, 22), ((2, 19), (5, 14), (10, 10)))
        self.add_line('upper-ring-0', (10, 10), (16, 4))
        self.add_bezier('upper-ring-1', (16, 4), ((18, 2), (19, 2), (21, 2)))
        self.add_bezier('upper-ring-2', (21, 2), ((25, 2), (30, 5), (30, 10)))
        self.add_bezier('upper-ring-3', (30, 10), ((30, 13), (27, 18), (22, 22)))
        self.add_bezier('upper-ring-4', (22, 22), ((16, 24), (8, 16), (10, 10)))
        self.add_contour('lower-ring', 'lower-ring-0', 'lower-ring-1', 'lower-ring-2', 'lower-ring-3', 'lower-ring-4', closed=True)
        self.add_contour('upper-ring', 'upper-ring-0', 'upper-ring-1', 'upper-ring-2', 'upper-ring-3', 'upper-ring-4', closed=True)
        self.relate('connect', 'lower-ring', 'upper-ring')
        self.add_anchor('center',(16, 16))
