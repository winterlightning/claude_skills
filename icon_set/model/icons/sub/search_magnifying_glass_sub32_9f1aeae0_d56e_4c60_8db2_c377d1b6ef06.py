"""Search Magnifying Glass: user-requested grid-fitted 32px version of search-magnifying-glass-solo.
Plan: retain source primitive/contour topology and fit SQUARE ink (0, 0, 32, 32).
All geometry nodes, controls and radii are whole integers; final stroke stays 4.
Source construction and visual references are retained from the solo model.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID='9f1aeae0-d56e-4c60-8db2-c377d1b6ef06'
SOURCE_PATH='pictographic-primitives/other/magnifying glass_9f1aeae0-d56e-4c60-8db2-c377d1b6ef06.svg'
SOLO_SOURCE_ICON_ID='search-magnifying-glass-solo'
AUTHOR='gpt-6'
class Drawing(Sub32):
    icon_id='search-magnifying-glass-sub32'
    keyshape=Keyshape.SQUARE
    semantic_role='SUB'
    semantic_kind='modifier'
    category = 'primitives-generate'
    tags=('sub icon',)
    keywords=('sub icon', 'grid fitted', 'search magnifying glass')
    def build(self):
        self.add_arc('ring-a', (2, 14), (14, 2), radius_x=12, radius_y=12, large_arc=False, sweep=True)
        self.add_arc('ring-b', (14, 2), (25, 14), radius_x=11, radius_y=12, large_arc=False, sweep=True)
        self.add_arc('ring-c', (25, 14), (21, 23), radius_x=12, radius_y=12, large_arc=False, sweep=True)
        self.add_arc('ring-d', (21, 23), (2, 14), radius_x=12, radius_y=12, large_arc=False, sweep=True)
        self.add_line('handle', (21, 23), (30, 30))
        self.add_contour('lens', 'ring-a', 'ring-b', 'ring-c', 'ring-d', closed=True)
        self.relate('connect', 'lens', 'handle')
        self.add_anchor('center',(16, 16))
