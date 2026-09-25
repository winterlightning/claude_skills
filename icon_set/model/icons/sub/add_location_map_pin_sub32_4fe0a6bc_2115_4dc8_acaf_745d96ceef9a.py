"""Add Location Map Pin: user-requested grid-fitted 32px version of add-location-map-pin-solo.
Plan: retain source primitive/contour topology and fit VRECT_XL ink (2, 0, 30, 32).
All geometry nodes, controls and radii are whole integers; final stroke stays 4.
Source construction and visual references are retained from the solo model.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID='4fe0a6bc-2115-4dc8-acaf-745d96ceef9a'
SOURCE_PATH='pictographic-primitives/other/drop cross_4fe0a6bc-2115-4dc8-acaf-745d96ceef9a.svg'
SOLO_SOURCE_ICON_ID='add-location-map-pin-solo'
AUTHOR='gpt-6'
class Drawing(Sub32):
    icon_id='add-location-map-pin-sub32'
    keyshape=Keyshape.VRECT_XL
    semantic_role='SUB'
    semantic_kind='modifier'
    category = 'primitives-generate'
    tags=('sub icon',)
    keywords=('sub icon', 'grid fitted', 'add location map pin')
    def build(self):
        self.add_arc('pin-top', (4, 13), (28, 13), radius_x=12, radius_y=11, large_arc=False, sweep=True)
        self.add_bezier('pin-bottom', (28, 13), ((28, 19), (20, 27), (16, 30)), ((12, 27), (4, 19), (4, 13)))
        self.add_line('h-1', (11, 13), (16, 13))
        self.add_line('h-2', (16, 13), (21, 13))
        self.add_line('v-1', (16, 9), (16, 13))
        self.add_line('v-2', (16, 13), (16, 18))
        self.add_contour('outline', 'pin-top', 'pin-bottom', closed=True)
        self.add_contour('h', 'h-1', 'h-2', closed=False)
        self.add_contour('v', 'v-1', 'v-2', closed=False)
        self.relate('connect', 'h', 'v')
        self.add_anchor('center',(16, 16))
