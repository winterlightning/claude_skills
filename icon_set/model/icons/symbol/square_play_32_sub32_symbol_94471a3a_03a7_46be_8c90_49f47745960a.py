"""Square Video Play Button: user-requested grid-fitted 32px version of square-play-32-solo.
Plan: retain source primitive/contour topology and fit SQUARE ink (0, 0, 32, 32).
All geometry nodes, controls and radii are whole integers; final stroke stays 4.
Source construction and visual references are retained from the solo model.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = '94471a3a-03a7-46be-8c90-49f47745960a'
SOURCE_PATH = 'pictographic-primitives/other/media_94471a3a-03a7-46be-8c90-49f47745960a.svg'
SOLO_SOURCE_ICON_ID = 'square-play-32-solo'
AUTHOR = 'gpt-6'

class DrawingContainerSymbol(Sub32):
    icon_id = 'square-play-32-sub32-symbol'
    related_origin_icon_id = 'square-play-32-sub32'
    variant_label = 'Independent container symbol'
    usage_category = 'symbol'
    related_group = 'sub-origin/square-play-32-sub32'
    counterpart_icon_id = 'square-play-32-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives-generate'
    tags = ('sub icon',)
    keywords = ('sub icon', 'grid fitted', 'square video play button')

    def build(self):
        self.add_line('outline-0', (6, 2), (26, 2))
        self.add_arc('outline-1', (26, 2), (30, 6), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_line('outline-2', (30, 6), (30, 26))
        self.add_arc('outline-3', (30, 26), (26, 30), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_line('outline-4', (26, 30), (6, 30))
        self.add_arc('outline-5', (6, 30), (2, 26), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_line('outline-6', (2, 26), (2, 6))
        self.add_arc('outline-7', (2, 6), (6, 2), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_line('play-1', (11, 9), (22, 16))
        self.add_line('play-2', (22, 16), (11, 23))
        self.add_line('play-3', (11, 23), (11, 9))
        self.add_contour('outline', 'outline-0', 'outline-1', 'outline-2', 'outline-3', 'outline-4', 'outline-5', 'outline-6', 'outline-7', closed=True)
        self.add_contour('play', 'play-1', 'play-2', 'play-3', closed=True)
        self.add_anchor('center', (16, 16))
