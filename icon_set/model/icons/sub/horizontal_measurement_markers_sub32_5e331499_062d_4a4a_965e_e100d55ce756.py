"""Horizontal Measurement Markers: user-requested grid-fitted 32px version of horizontal-measurement-markers-solo.
Plan: retain source primitive/contour topology and fit HRECT_XL ink (0, 2, 32, 30).
All geometry nodes, controls and radii are whole integers; final stroke stays 4.
Source construction and visual references are retained from the solo model.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID='5e331499-062d-4a4a-965e-e100d55ce756'
SOURCE_PATH='pictographic-primitives/other/measurement markers_5e331499-062d-4a4a-965e-e100d55ce756.svg'
SOLO_SOURCE_ICON_ID='horizontal-measurement-markers-solo'
AUTHOR='gpt-6'
class Drawing(Sub32):
    icon_id='horizontal-measurement-markers-sub32'
    keyshape=Keyshape.HRECT_XL
    semantic_role='SUB'
    semantic_kind='modifier'
    category='objects/interface-essential'
    tags=('sub icon',)
    keywords=('sub icon', 'grid fitted', 'horizontal measurement markers')
    def build(self):
        self.add_line('top-1', (30, 4), (11, 4))
        self.add_line('top-2', (11, 4), (8, 10))
        self.add_line('top-3', (8, 10), (2, 10))
        self.add_line('top-4', (2, 10), (2, 4))
        self.add_line('top-5', (2, 4), (11, 4))
        self.add_line('bottom-1', (30, 28), (30, 22))
        self.add_line('bottom-2', (30, 22), (11, 22))
        self.add_line('bottom-3', (11, 22), (8, 16))
        self.add_line('bottom-4', (8, 16), (2, 16))
        self.add_line('bottom-5', (2, 16), (2, 22))
        self.add_line('bottom-6', (2, 22), (11, 22))
        self.add_line('measure', (21, 16), (30, 16))
        self.add_contour('top', 'top-1', 'top-2', 'top-3', 'top-4', 'top-5', closed=False)
        self.add_contour('bottom', 'bottom-1', 'bottom-2', 'bottom-3', 'bottom-4', 'bottom-5', 'bottom-6', closed=False)
        self.add_anchor('center',(16, 16))
