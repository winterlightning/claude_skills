"""Independent 32px profile of canoe-and-paddle.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = '7b8e9bf7-9bed-5b92-918e-e02031e1e3e3'
SOURCE_PATH = 'pictographic-primitives/outdoors/canoe single_7b8e9bf7-9bed-5b92-918e-e02031e1e3e3.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('7b8e9bf7-9bed-5b92-918e-e02031e1e3e3', 'pictographic-primitives/outdoors/canoe single_7b8e9bf7-9bed-5b92-918e-e02031e1e3e3.svg'), ('18ef3c0c-f96b-4a36-b74d-e15aada31f40', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/canoe paddle_18ef3c0c-f96b-4a36-b74d-e15aada31f40.svg'))
PROFILE_SOURCE_KEYS = ('solo/canoe-and-paddle',)
SOLO_SOURCE_ICON_IDS = ('canoe-and-paddle',)
REFERENCE_EXPORT_SHA256 = 'c2006b5886003bd202267871505c8f18afff49910a68eb6479e0650f5ad3b651'

class Drawing(Sub32):
    icon_id = 'canoe-and-paddle-sub32'
    keyshape = Keyshape.HRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'outdoors'
    categories = ('outdoors', 'primitives')
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_arc('p1-r1-1', (22, 5), (30, 17), radius_x=8, radius_y=13, large_arc=False, sweep=True)
        self.add_line('p1-r1-2', (30, 17), (30, 22))
        self.add_arc('p1-r1-3', (30, 22), (13, 22), radius_x=8.5, radius_y=6.375, large_arc=False, sweep=True)
        self.add_line('p1-r1-4', (13, 22), (13, 17))
        self.add_arc('p1-r1-5', (13, 17), (22, 5), radius_x=8, radius_y=13, large_arc=False, sweep=True)
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', closed=False)
        self.add_arc('p2-r1-1', (20, 17), (24, 17), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_arc('p2-r1-2', (24, 17), (20, 17), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', closed=False)
        self.add_line('p3-r1-1', (2, 5), (8, 5))
        self.add_line('p3-r1-2', (8, 5), (8, 10))
        self.add_line('p3-r1-3', (8, 10), (5, 13))
        self.add_line('p3-r1-4', (5, 13), (2, 10))
        self.add_line('p3-r1-5', (2, 10), (2, 5))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', 'p3-r1-3', 'p3-r1-4', 'p3-r1-5', closed=False)
        self.add_line('p4-r1-1', (2, 27), (8, 27))
        self.add_line('p4-r1-2', (8, 27), (8, 22))
        self.add_line('p4-r1-3', (8, 22), (5, 19))
        self.add_line('p4-r1-4', (5, 19), (2, 22))
        self.add_line('p4-r1-5', (2, 22), (2, 27))
        self.add_contour('path-4-1', 'p4-r1-1', 'p4-r1-2', 'p4-r1-3', 'p4-r1-4', 'p4-r1-5', closed=False)
        self.add_line('p5-r1-1', (5, 13), (5, 19))
        self.add_contour('path-5-1', 'p5-r1-1', closed=False)
        self.relate('connect', 'p3-r1-3', 'p5-r1-1')
        self.relate('connect', 'p3-r1-4', 'p5-r1-1')
        self.relate('connect', 'p4-r1-3', 'p5-r1-1')
        self.relate('connect', 'p4-r1-4', 'p5-r1-1')
