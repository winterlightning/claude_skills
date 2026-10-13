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
    keyshape = Keyshape.HRECT_L
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives-generate'
    categories = ('symbol', 'other', 'primitives-generate')
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        # Pie chart: a true circle with one slice, and two legend marks beside it.
        self.add_arc('pie-1', (2, 16), (22, 16), radius_x=10, radius_y=10, large_arc=False, sweep=True)
        self.add_arc('pie-2', (22, 16), (2, 16), radius_x=10, radius_y=10, large_arc=False, sweep=True)
        self.add_contour('pie', 'pie-1', 'pie-2', closed=True)
        self.add_polyline('slice', (12, 6), (12, 16), (22, 16))
        self.relate('connect', 'pie', 'slice')
        self.add_line('sum-1', (30, 12), (30, 12))
        self.add_line('sum-2', (30, 20), (30, 20))
