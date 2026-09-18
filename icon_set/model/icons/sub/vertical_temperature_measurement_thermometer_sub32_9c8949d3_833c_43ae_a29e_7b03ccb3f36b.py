"""Vertical Temperature Measurement Thermometer: user-requested grid-fitted 32px version of vertical-temperature-measurement-thermometer-solo.
Plan: retain source primitive/contour topology and fit VRECT_XL ink (2, 0, 30, 32).
All geometry nodes, controls and radii are whole integers; final stroke stays 4.
Source construction and visual references are retained from the solo model.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID='9c8949d3-833c-43ae-a29e-7b03ccb3f36b'
SOURCE_PATH='pictographic-primitives/other/thermometer_9c8949d3-833c-43ae-a29e-7b03ccb3f36b.svg'
SOLO_SOURCE_ICON_ID='vertical-temperature-measurement-thermometer-solo'
AUTHOR='gpt-6'
class Drawing(Sub32):
    icon_id='vertical-temperature-measurement-thermometer-sub32'
    keyshape=Keyshape.VRECT_XL
    semantic_role='SUB'
    semantic_kind='modifier'
    category='objects/interface-essential'
    tags=('sub icon',)
    keywords=('sub icon', 'grid fitted', 'vertical temperature measurement thermometer')
    def build(self):
        self.add_line('tube-left', (6, 18), (6, 8))
        self.add_arc('top', (6, 8), (19, 8), radius_x=7, radius_y=6, large_arc=False, sweep=True)
        self.add_line('tube-right', (19, 8), (19, 18))
        self.add_bezier('bulb', (19, 18), ((25, 24), (22, 30), (13, 30)), ((4, 30), (4, 27), (4, 24)), ((4, 22), (5, 20), (6, 18)))
        self.add_line('mercury', (12, 16), (12, 24))
        self.add_line('scale', (26, 11), (28, 11))
        self.add_contour('outline', 'tube-left', 'top', 'tube-right', 'bulb', closed=True)
        self.add_anchor('center',(16, 16))
