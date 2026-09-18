"""Circular Downward Pointing Arrow: user-requested grid-fitted 32px version of circular-downward-pointing-arrow-solo.
Plan: retain source primitive/contour topology and fit CIRCLE ink (0, 0, 32, 32).
All geometry nodes, controls and radii are whole integers; final stroke stays 4.
Source construction and visual references are retained from the solo model.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID='9703959b-8d72-4272-aa87-6963634386ca'
SOURCE_PATH='pictographic-primitives/other/circle arrow down_9703959b-8d72-4272-aa87-6963634386ca.svg'
SOLO_SOURCE_ICON_ID='circular-downward-pointing-arrow-solo'
AUTHOR='gpt-6'
class Drawing(Sub32):
    icon_id='circular-downward-pointing-arrow-sub32'
    keyshape=Keyshape.CIRCLE
    semantic_role='SUB'
    semantic_kind='modifier'
    category='objects/interface-essential'
    tags=('sub icon',)
    keywords=('sub icon', 'grid fitted', 'circular downward pointing arrow')
    def build(self):
        self.add_arc('outline-top', (2, 16), (30, 16), radius_x=14, radius_y=14, large_arc=False, sweep=True)
        self.add_arc('outline-bottom', (30, 16), (2, 16), radius_x=14, radius_y=14, large_arc=False, sweep=True)
        self.add_line('shaft', (16, 9), (16, 22))
        self.add_line('head-1', (11, 17), (16, 22))
        self.add_line('head-2', (16, 22), (21, 17))
        self.add_contour('outline', 'outline-top', 'outline-bottom', closed=True)
        self.add_contour('head', 'head-1', 'head-2', closed=False)
        self.relate('connect', 'shaft', 'head')
        self.add_anchor('center',(16, 16))
