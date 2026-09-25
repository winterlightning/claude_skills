"""Open Hand Palm: user-requested grid-fitted 32px version of open-hand-palm-solo.
Plan: retain source primitive/contour topology and fit VRECT_XL ink (2, 0, 30, 32).
All geometry nodes, controls and radii are whole integers; final stroke stays 4.
Source construction and visual references are retained from the solo model.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID='92d8dd38-d4cf-4c21-a6ee-c09f59061b77'
SOURCE_PATH='pictographic-primitives/other/hand 1_92d8dd38-d4cf-4c21-a6ee-c09f59061b77.svg'
SOLO_SOURCE_ICON_ID='open-hand-palm-solo'
AUTHOR='gpt-6'
class Drawing(Sub32):
    icon_id='open-hand-palm-sub32'
    keyshape=Keyshape.VRECT_XL
    semantic_role='SUB'
    semantic_kind='modifier'
    category = 'primitives-generate'
    tags=('sub icon',)
    keywords=('sub icon', 'grid fitted', 'open hand palm')
    def build(self):
        self.add_bezier('hand', (12, 30), ((7, 27), (4, 23), (4, 20)), ((4, 17), (7, 17), (9, 20)))
        self.add_line('index', (9, 20), (9, 6))
        self.add_arc('finger-a', (9, 6), (15, 6), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('joint-a', (15, 6), (15, 5))
        self.add_arc('finger-b', (15, 5), (23, 5), radius_x=4, radius_y=3, large_arc=False, sweep=True)
        self.add_line('joint-b', (23, 5), (23, 8))
        self.add_arc('finger-c', (23, 8), (27, 8), radius_x=2, radius_y=3, large_arc=False, sweep=True)
        self.add_bezier('outer', (27, 8), ((28, 13), (28, 18), (28, 21)), ((28, 27), (23, 30), (19, 30)))
        self.add_line('wrist', (19, 30), (12, 30))
        self.add_contour('outline', 'hand', 'index', 'finger-a', 'joint-a', 'finger-b', 'joint-b', 'finger-c', 'outer', 'wrist', closed=True)
        self.add_anchor('center',(16, 16))
