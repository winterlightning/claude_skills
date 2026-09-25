"""Upward Arrow Inside Circle: user-requested grid-fitted 32px version of upward-arrow-inside-circle-solo.
Plan: retain source primitive/contour topology and fit CIRCLE ink (0, 0, 32, 32).
All geometry nodes, controls and radii are whole integers; final stroke stays 4.
Source construction and visual references are retained from the solo model.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID='7bd3a2bd-439f-4018-b851-acf302ef01a5'
SOURCE_PATH='pictographic-primitives/other/circle arrow up_7bd3a2bd-439f-4018-b851-acf302ef01a5.svg'
SOLO_SOURCE_ICON_ID='upward-arrow-inside-circle-solo'
AUTHOR='gpt-6'
class Drawing(Sub32):
    icon_id='upward-arrow-inside-circle-sub32'
    keyshape=Keyshape.CIRCLE
    semantic_role='SUB'
    semantic_kind='modifier'
    category = 'primitives-generate'
    categories = ('state', 'other', 'primitives-generate')
    tags=('sub icon',)
    keywords=('sub icon', 'grid fitted', 'upward arrow inside circle')
    def build(self):
        self.add_arc('outline-top', (2, 16), (30, 16), radius_x=14, radius_y=14, large_arc=False, sweep=True)
        self.add_arc('outline-bottom', (30, 16), (2, 16), radius_x=14, radius_y=14, large_arc=False, sweep=True)
        self.add_line('shaft', (16, 23), (16, 10))
        self.add_line('head-1', (11, 15), (16, 10))
        self.add_line('head-2', (16, 10), (21, 15))
        self.add_contour('outline', 'outline-top', 'outline-bottom', closed=True)
        self.add_contour('head', 'head-1', 'head-2', closed=False)
        self.relate('connect', 'shaft', 'head')
        self.add_anchor('center',(16, 16))
