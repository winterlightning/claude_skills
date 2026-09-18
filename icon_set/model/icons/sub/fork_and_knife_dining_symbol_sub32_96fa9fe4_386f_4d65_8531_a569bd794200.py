"""Fork and Knife Dining Symbol: user-requested grid-fitted 32px version of fork-and-knife-dining-symbol-solo.
Plan: retain source primitive/contour topology and fit CIRCLE ink (0, 0, 32, 32).
All geometry nodes, controls and radii are whole integers; final stroke stays 4.
Source construction and visual references are retained from the solo model.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID='96fa9fe4-386f-4d65-8531-a569bd794200'
SOURCE_PATH='pictographic-primitives/state/circle fork knife_96fa9fe4-386f-4d65-8531-a569bd794200.svg'
SOLO_SOURCE_ICON_ID='fork-and-knife-dining-symbol-solo'
AUTHOR='gpt-6'
class Drawing(Sub32):
    icon_id='fork-and-knife-dining-symbol-sub32'
    keyshape=Keyshape.CIRCLE
    semantic_role='SUB'
    semantic_kind='modifier'
    category='objects/interface-essential'
    tags=('sub icon',)
    keywords=('sub icon', 'grid fitted', 'fork and knife dining symbol')
    def build(self):
        self.add_arc('outline-top', (2, 16), (30, 16), radius_x=14, radius_y=14, large_arc=False, sweep=True)
        self.add_arc('outline-bottom', (30, 16), (2, 16), radius_x=14, radius_y=14, large_arc=False, sweep=True)
        self.add_line('fork-1', (8, 10), (8, 15))
        self.add_line('fork-2', (8, 15), (13, 18))
        self.add_line('fork-3', (13, 18), (16, 15))
        self.add_line('fork-4', (16, 15), (16, 10))
        self.add_line('stem', (13, 18), (13, 23))
        self.add_line('knife', (24, 11), (24, 21))
        self.add_contour('outline', 'outline-top', 'outline-bottom', closed=True)
        self.add_contour('fork', 'fork-1', 'fork-2', 'fork-3', 'fork-4', closed=False)
        self.relate('connect', 'fork', 'stem')
        self.add_anchor('center',(16, 16))
