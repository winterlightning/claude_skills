"""Zoom Out Magnifying Glass: user-requested grid-fitted 32px version of zoom-out-magnifying-glass-solo.
Plan: retain source primitive/contour topology and fit SQUARE ink (0, 0, 32, 32).
All geometry nodes, controls and radii are whole integers; final stroke stays 4.
Source construction and visual references are retained from the solo model.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID='175a065e-b228-4fa8-9503-eb4f350508b7'
SOURCE_PATH='pictographic-primitives/state/magnifying glass minus_175a065e-b228-4fa8-9503-eb4f350508b7.svg'
SOLO_SOURCE_ICON_ID='zoom-out-magnifying-glass-solo'
AUTHOR='gpt-6'
class Drawing(Sub32):
    icon_id='zoom-out-magnifying-glass-sub32'
    keyshape=Keyshape.SQUARE
    semantic_role='SUB'
    semantic_kind='modifier'
    category='objects/interface-essential'
    tags=('sub icon',)
    keywords=('sub icon', 'grid fitted', 'zoom out magnifying glass')
    def build(self):
        self.add_arc('ring-a', (2, 14), (14, 2), radius_x=12, radius_y=12, large_arc=False, sweep=True)
        self.add_arc('ring-b', (14, 2), (25, 14), radius_x=11, radius_y=12, large_arc=False, sweep=True)
        self.add_arc('ring-c', (25, 14), (21, 23), radius_x=12, radius_y=12, large_arc=False, sweep=True)
        self.add_arc('ring-d', (21, 23), (2, 14), radius_x=12, radius_y=12, large_arc=False, sweep=True)
        self.add_line('handle', (21, 23), (30, 30))
        self.add_line('minus', (9, 14), (18, 14))
        self.add_contour('lens', 'ring-a', 'ring-b', 'ring-c', 'ring-d', closed=True)
        self.relate('connect', 'lens', 'handle')
        self.add_anchor('center',(16, 16))
