"""Monitor with Dollar Symbol: user-requested grid-fitted 32px version of monitor-with-dollar-symbol-solo.
Plan: retain source primitive/contour topology and fit VRECT_XL ink (2, 0, 30, 32).
All geometry nodes, controls and radii are whole integers; final stroke stays 4.
Source construction and visual references are retained from the solo model.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID='a113d58d-e6b9-465b-a63a-51b045031b0b'
SOURCE_PATH='pictographic-primitives/symbol/monitor dollar sign_a113d58d-e6b9-465b-a63a-51b045031b0b.svg'
SOLO_SOURCE_ICON_ID='monitor-with-dollar-symbol-solo'
AUTHOR='gpt-6'
class Drawing(Sub32):
    icon_id='monitor-with-dollar-symbol-sub32'
    keyshape=Keyshape.VRECT_XL
    semantic_role='SUB'
    semantic_kind='modifier'
    category='objects/finance'
    tags=('sub icon',)
    keywords=('sub icon', 'grid fitted', 'monitor with dollar symbol')
    def build(self):
        self.add_line('screen-0', (7, 2), (25, 2))
        self.add_arc('screen-1', (25, 2), (28, 5), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('screen-2', (28, 5), (28, 24))
        self.add_arc('screen-3', (28, 24), (25, 27), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('screen-4', (25, 27), (7, 27))
        self.add_arc('screen-5', (7, 27), (4, 24), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('screen-6', (4, 24), (4, 5))
        self.add_arc('screen-7', (4, 5), (7, 2), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('stand', (16, 27), (16, 30))
        self.add_line('currency-top', (20, 11), (16, 11))
        self.add_arc('currency-upper', (16, 11), (16, 15), radius_x=4, radius_y=2, large_arc=False, sweep=False)
        self.add_arc('currency-lower', (16, 15), (16, 19), radius_x=4, radius_y=2, large_arc=False, sweep=True)
        self.add_line('currency-foot', (16, 19), (12, 19))
        self.add_line('stem-top', (16, 9), (16, 11))
        self.add_line('stem-bottom', (16, 19), (16, 21))
        self.add_contour('screen', 'screen-0', 'screen-1', 'screen-2', 'screen-3', 'screen-4', 'screen-5', 'screen-6', 'screen-7', closed=True)
        self.add_contour('currency', 'currency-top', 'currency-upper', 'currency-lower', 'currency-foot', closed=False)
        self.relate('connect', 'screen', 'stand')
        self.relate('connect', 'currency', 'stem-top')
        self.relate('connect', 'currency', 'stem-bottom')
        self.add_anchor('center',(16, 16))
