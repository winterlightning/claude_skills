"""Location Pin With Check Mark: user-requested grid-fitted 32px version of location-pin-with-check-mark-solo.
Plan: retain source primitive/contour topology and fit VRECT_XL ink (2, 0, 30, 32).
All geometry nodes, controls and radii are whole integers; final stroke stays 4.
Source construction and visual references are retained from the solo model.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID='4435680b-318b-4218-8cd9-57af301bba08'
SOURCE_PATH='pictographic-primitives/symbol/pin check mark_4435680b-318b-4218-8cd9-57af301bba08.svg'
SOLO_SOURCE_ICON_ID='location-pin-with-check-mark-solo'
AUTHOR='gpt-6'
class Drawing(Sub32):
    icon_id='location-pin-with-check-mark-sub32'
    keyshape=Keyshape.VRECT_XL
    semantic_role='SUB'
    semantic_kind='modifier'
    category='objects/interface-essential'
    tags=('sub icon',)
    keywords=('sub icon', 'grid fitted', 'location pin with check mark')
    def build(self):
        self.add_arc('pin-top', (4, 13), (28, 13), radius_x=12, radius_y=11, large_arc=False, sweep=True)
        self.add_bezier('pin-bottom', (28, 13), ((28, 20), (20, 27), (16, 30)), ((12, 27), (4, 20), (4, 13)))
        self.add_line('check-1', (11, 13), (14, 17))
        self.add_line('check-2', (14, 17), (20, 12))
        self.add_contour('outline', 'pin-top', 'pin-bottom', closed=True)
        self.add_contour('check', 'check-1', 'check-2', closed=False)
        self.add_anchor('center',(16, 16))
