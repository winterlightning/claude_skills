"""Diagonal Hyperlink Chain Link: user-requested grid-fitted 32px version of overlapping-chain-rings.
Plan: retain source primitive/contour topology and fit SQUARE ink (0, 0, 32, 32).
All geometry nodes, controls and radii are whole integers; final stroke stays 4.
Source construction and visual references are retained from the solo model.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID='f3554d59-4ee9-5ba8-bc14-5b1324691503'
SOURCE_PATH='pictographic-primitives/interface-essential/attachment_f3554d59-4ee9-5ba8-bc14-5b1324691503.svg'
SOLO_SOURCE_ICON_ID='overlapping-chain-rings'
AUTHOR='gpt-6'
class Drawing(Sub32):
    icon_id='overlapping-chain-rings-sub32'
    keyshape=Keyshape.SQUARE
    semantic_role='SUB'
    semantic_kind='modifier'
    category='objects/interface-essential'
    tags=('sub icon',)
    keywords=('sub icon', 'grid fitted', 'diagonal hyperlink chain link')
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
