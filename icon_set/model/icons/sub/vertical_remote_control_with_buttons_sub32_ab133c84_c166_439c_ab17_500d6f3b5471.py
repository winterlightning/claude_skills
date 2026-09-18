"""Vertical Remote Control with Buttons: user-requested grid-fitted 32px version of vertical-remote-control-with-buttons-solo.
Plan: retain source primitive/contour topology and fit VRECT_L ink (4, 0, 28, 32).
All geometry nodes, controls and radii are whole integers; final stroke stays 4.
Source construction and visual references are retained from the solo model.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID='ab133c84-c166-439c-ab17-500d6f3b5471'
SOURCE_PATH='pictographic-primitives/other/remote control_ab133c84-c166-439c-ab17-500d6f3b5471.svg'
SOLO_SOURCE_ICON_ID='vertical-remote-control-with-buttons-solo'
AUTHOR='gpt-6'
class Drawing(Sub32):
    icon_id='vertical-remote-control-with-buttons-sub32'
    keyshape=Keyshape.VRECT_L
    semantic_role='SUB'
    semantic_kind='modifier'
    category='objects/interface-essential'
    tags=('sub icon',)
    keywords=('sub icon', 'grid fitted', 'vertical remote control with buttons')
    def build(self):
        self.add_line('case-0', (10, 2), (22, 2))
        self.add_arc('case-1', (22, 2), (26, 5), radius_x=4, radius_y=3, large_arc=False, sweep=True)
        self.add_line('case-2', (26, 5), (26, 27))
        self.add_arc('case-3', (26, 27), (22, 30), radius_x=4, radius_y=3, large_arc=False, sweep=True)
        self.add_line('case-4', (22, 30), (10, 30))
        self.add_arc('case-5', (10, 30), (6, 27), radius_x=4, radius_y=3, large_arc=False, sweep=True)
        self.add_line('case-6', (6, 27), (6, 5))
        self.add_arc('case-7', (6, 5), (10, 2), radius_x=4, radius_y=3, large_arc=False, sweep=True)
        self.add_arc('button-top', (13, 12), (19, 12), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_arc('button-bottom', (19, 12), (13, 12), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('control-v-1', (16, 21), (16, 22))
        self.add_line('control-v-2', (16, 22), (16, 23))
        self.add_line('control-h-1', (13, 22), (16, 22))
        self.add_line('control-h-2', (16, 22), (19, 22))
        self.add_contour('case', 'case-0', 'case-1', 'case-2', 'case-3', 'case-4', 'case-5', 'case-6', 'case-7', closed=True)
        self.add_contour('button', 'button-top', 'button-bottom', closed=True)
        self.add_contour('control-v', 'control-v-1', 'control-v-2', closed=False)
        self.add_contour('control-h', 'control-h-1', 'control-h-2', closed=False)
        self.relate('connect', 'control-v', 'control-h')
        self.add_anchor('center',(16, 16))
