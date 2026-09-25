"""Wireless Beacon Remote Signal: user-requested grid-fitted 32px version of wireless-beacon-remote-signal-solo.
Plan: retain source primitive/contour topology and fit VRECT_XL ink (2, 0, 30, 32).
All geometry nodes, controls and radii are whole integers; final stroke stays 4.
Source construction and visual references are retained from the solo model.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID='46d6bfb6-5e8d-4747-b6e1-870a15b50b92'
SOURCE_PATH='pictographic-primitives/other/beacon remote_46d6bfb6-5e8d-4747-b6e1-870a15b50b92.svg'
SOLO_SOURCE_ICON_ID='wireless-beacon-remote-signal-solo'
AUTHOR='gpt-6'
class Drawing(Sub32):
    icon_id='wireless-beacon-remote-signal-sub32'
    keyshape=Keyshape.VRECT_XL
    semantic_role='SUB'
    semantic_kind='modifier'
    category = 'primitives-generate'
    tags=('sub icon',)
    keywords=('sub icon', 'grid fitted', 'wireless beacon remote signal')
    def build(self):
        self.add_bezier('signal-outer', (4, 8), ((8, 4), (12, 2), (16, 2)), ((20, 2), (24, 4), (28, 8)))
        self.add_bezier('signal-inner', (10, 12), ((13, 10), (19, 10), (22, 12)))
        self.add_line('device-0', (14, 19), (18, 19))
        self.add_arc('device-1', (18, 19), (20, 21), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_line('device-2', (20, 21), (20, 28))
        self.add_arc('device-3', (20, 28), (18, 30), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_line('device-4', (18, 30), (14, 30))
        self.add_arc('device-5', (14, 30), (12, 28), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_line('device-6', (12, 28), (12, 21))
        self.add_arc('device-7', (12, 21), (14, 19), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_contour('device', 'device-0', 'device-1', 'device-2', 'device-3', 'device-4', 'device-5', 'device-6', 'device-7', closed=True)
        self.add_anchor('center',(16, 16))
