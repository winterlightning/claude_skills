"""Smart Car Wi-Fi Connection: user-requested grid-fitted 32px version of smart-car-wi-fi-connection-solo.
Plan: retain source primitive/contour topology and fit VRECT_XL ink (2, 0, 30, 32).
All geometry nodes, controls and radii are whole integers; final stroke stays 4.
Source construction and visual references are retained from the solo model.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID='f59286ba-b86a-4e53-9fe0-93f931efec10'
SOURCE_PATH='pictographic-primitives/other/car wifi_f59286ba-b86a-4e53-9fe0-93f931efec10.svg'
SOLO_SOURCE_ICON_ID='smart-car-wi-fi-connection-solo'
AUTHOR='gpt-6'
class Drawing(Sub32):
    icon_id='smart-car-wi-fi-connection-sub32'
    keyshape=Keyshape.VRECT_XL
    semantic_role='SUB'
    semantic_kind='modifier'
    category='objects/interface-essential'
    tags=('sub icon',)
    keywords=('sub icon', 'grid fitted', 'smart car wi-fi connection')
    def build(self):
        self.add_bezier('outer-wave', (4, 6), ((8, 4), (12, 2), (16, 2)), ((20, 2), (24, 4), (28, 6)))
        self.add_bezier('inner-wave', (11, 12), ((13, 9), (19, 9), (21, 12)))
        self.add_line('roof-1', (8, 23), (12, 17))
        self.add_line('roof-2', (12, 17), (20, 17))
        self.add_line('roof-3', (20, 17), (24, 23))
        self.add_line('car-0', (7, 23), (25, 23))
        self.add_arc('car-1', (25, 23), (28, 26), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('car-2', (28, 26), (28, 27))
        self.add_arc('car-3', (28, 27), (25, 30), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('car-4', (25, 30), (7, 30))
        self.add_arc('car-5', (7, 30), (4, 27), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('car-6', (4, 27), (4, 26))
        self.add_arc('car-7', (4, 26), (7, 23), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_contour('roof', 'roof-1', 'roof-2', 'roof-3', closed=False)
        self.add_contour('car', 'car-0', 'car-1', 'car-2', 'car-3', 'car-4', 'car-5', 'car-6', 'car-7', closed=True)
        self.relate('connect', 'roof', 'car')
        self.add_anchor('center',(16, 16))
