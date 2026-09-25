"""Circled Curved Share Arrow: user-requested grid-fitted 32px version of circled-curved-share-arrow-solo.
Plan: retain source primitive/contour topology and fit CIRCLE ink (0, 0, 32, 32).
All geometry nodes, controls and radii are whole integers; final stroke stays 4.
Source construction and visual references are retained from the solo model.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = '54c4c96e-2201-4fc6-9905-c97205f79810'
SOURCE_PATH = 'pictographic-primitives/other/circle arrow next_54c4c96e-2201-4fc6-9905-c97205f79810.svg'
SOLO_SOURCE_ICON_ID = 'circled-curved-share-arrow-solo'
AUTHOR = 'gpt-6'

class Drawing(Sub32):
    icon_id = 'circled-curved-share-arrow-sub32'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives-generate'
    tags = ('sub icon',)
    keywords = ('sub icon', 'grid fitted', 'circled curved share arrow')

    def build(self):
        self.add_arc('outline-top', (2, 16), (30, 16), radius_x=14, radius_y=14, large_arc=False, sweep=True)
        self.add_arc('outline-bottom', (30, 16), (2, 16), radius_x=14, radius_y=14, large_arc=False, sweep=True)
        self.add_bezier('turn', (11, 21), ((11, 16), (16, 14), (21, 14)))
        self.add_line('head-1', (17, 10), (21, 14))
        self.add_line('head-2', (21, 14), (17, 16))
        self.add_contour('outline', 'outline-top', 'outline-bottom', closed=True)
        self.add_contour('head', 'head-1', 'head-2', closed=False)
        self.relate('connect', 'turn', 'head')
        self.add_anchor('center', (16, 16))
