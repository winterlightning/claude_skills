"""Independent 32px profile of pie-chart-with-summary-lines.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = 'ae146d04-dcf5-4d2f-b306-71d0613e6dce'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/text pie_ae146d04-dcf5-4d2f-b306-71d0613e6dce.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('ae146d04-dcf5-4d2f-b306-71d0613e6dce', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/text pie_ae146d04-dcf5-4d2f-b306-71d0613e6dce.svg'),)
PROFILE_SOURCE_KEYS = ('solo/pie-chart-with-summary-lines',)
SOLO_SOURCE_ICON_IDS = ('pie-chart-with-summary-lines',)
REFERENCE_EXPORT_SHA256 = '772dc5df9f11485f338a96a7c263a913ba5d8182b3ea0f7c009a9ed7b9a64c9b'

class Drawing(Sub32):
    icon_id = 'pie-chart-with-summary-lines-sub32'
    keyshape = Keyshape.HRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives-generate'
    categories = ('symbol', 'other', 'primitives-generate')
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_arc('p1-r1-1', (16, 16), (9, 28), radius_x=7, radius_y=12, large_arc=False, sweep=True)
        self.add_arc('p1-r1-2', (9, 28), (2, 16), radius_x=7, radius_y=12, large_arc=False, sweep=True)
        self.add_arc('p1-r1-3', (2, 16), (9, 4), radius_x=7, radius_y=12, large_arc=False, sweep=True)
        self.add_arc('p1-r1-4', (9, 4), (16, 16), radius_x=7, radius_y=12, large_arc=False, sweep=True)
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', closed=False)
        self.add_line('p2-r1-1', (9, 4), (9, 16))
        self.add_line('p2-r1-2', (9, 16), (16, 16))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', closed=False)
        self.add_line('p3-r1-1', (9, 16), (9, 28))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_line('p4-r1-1', (25, 11), (30, 11))
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
        self.add_line('p5-r1-1', (25, 21), (30, 21))
        self.add_contour('path-5-1', 'p5-r1-1', closed=False)
        self.relate('connect', 'p1-r1-1', 'p2-r1-2')
        self.relate('connect', 'p1-r1-3', 'p2-r1-1')
        self.relate('connect', 'p1-r1-4', 'p2-r1-1')
        self.relate('connect', 'p1-r1-4', 'p2-r1-2')
        self.relate('connect', 'p2-r1-1', 'p3-r1-1')
        self.relate('connect', 'p2-r1-2', 'p3-r1-1')
        self.relate('connect', 'p1-r1-1', 'p3-r1-1')
        self.relate('connect', 'p1-r1-2', 'p3-r1-1')
