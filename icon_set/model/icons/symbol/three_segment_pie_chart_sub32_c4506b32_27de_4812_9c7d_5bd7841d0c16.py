"""Independent 32px profile of three-segment-pie-chart.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = 'c4506b32-27de-4812-9c7d-5bd7841d0c16'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/pie chart_c4506b32-27de-4812-9c7d-5bd7841d0c16.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('c4506b32-27de-4812-9c7d-5bd7841d0c16', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/pie chart_c4506b32-27de-4812-9c7d-5bd7841d0c16.svg'),)
PROFILE_SOURCE_KEYS = ('solo/three-segment-pie-chart',)
SOLO_SOURCE_ICON_IDS = ('three-segment-pie-chart',)
REFERENCE_EXPORT_SHA256 = '38df3b214758fa8c432181d64d34a754c7f15955998d5e4af585569a8f82d72d'

class Drawing(Sub32):
    icon_id = 'three-segment-pie-chart-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives-generate'
    categories = ('symbol', 'other', 'primitives-generate')
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_arc('p1-r1-1', (16, 2), (30, 16), radius_x=14, radius_y=14, large_arc=False, sweep=True)
        self.add_arc('p1-r1-2', (30, 16), (16, 30), radius_x=14, radius_y=14, large_arc=False, sweep=True)
        self.add_arc('p1-r1-3', (16, 30), (8, 27), radius_x=14, radius_y=14, large_arc=False, sweep=True)
        self.add_arc('p1-r1-4', (8, 27), (2, 16), radius_x=14, radius_y=14, large_arc=False, sweep=True)
        self.add_arc('p1-r1-5', (2, 16), (16, 2), radius_x=14, radius_y=14, large_arc=False, sweep=True)
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', closed=False)
        self.add_line('p2-r1-1', (16, 2), (16, 16))
        self.add_line('p2-r1-2', (16, 16), (30, 16))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', closed=False)
        self.add_line('p3-r1-1', (16, 16), (8, 27))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.relate('connect', 'p1-r1-1', 'p2-r1-1')
        self.relate('connect', 'p1-r1-1', 'p2-r1-2')
        self.relate('connect', 'p1-r1-2', 'p2-r1-2')
        self.relate('connect', 'p1-r1-3', 'p3-r1-1')
        self.relate('connect', 'p1-r1-4', 'p3-r1-1')
        self.relate('connect', 'p1-r1-5', 'p2-r1-1')
        self.relate('connect', 'p2-r1-1', 'p3-r1-1')
        self.relate('connect', 'p2-r1-2', 'p3-r1-1')
