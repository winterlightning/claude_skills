"""Independent 32px profile of pie-chart.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = '27b9bc66-43e0-4dee-990c-b6f75f57c869'
SOURCE_PATH = 'pictographic-primitives/symbol/pie chart_27b9bc66-43e0-4dee-990c-b6f75f57c869.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('27b9bc66-43e0-4dee-990c-b6f75f57c869', 'pictographic-primitives/symbol/pie chart_27b9bc66-43e0-4dee-990c-b6f75f57c869.svg'),)
PROFILE_SOURCE_KEYS = ('solo/pie-chart',)
SOLO_SOURCE_ICON_IDS = ('pie-chart',)
REFERENCE_EXPORT_SHA256 = 'a0c09bf05742b71400843abb583206d049ca056fc746145d89210265019c0594'

class DrawingContainerSymbol(Sub32):
    icon_id = 'pie-chart-sub32-symbol'
    related_origin_icon_id = 'pie-chart-sub32'
    variant_label = 'Independent container symbol'
    usage_category = 'symbol'
    related_group = 'sub-origin/pie-chart-sub32'
    counterpart_icon_id = 'pie-chart-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'symbol'
    categories = ('symbol', 'state')
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (24, 27), (16, 15))
        self.add_line('p1-r1-2', (16, 15), (8, 27))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', closed=False)
        self.add_line('p2-r1-1', (16, 2), (16, 15))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_arc('p3-r1-1', (2, 16), (30, 16), radius_x=14, radius_y=14, large_arc=False, sweep=True)
        self.add_arc('p3-r1-2', (30, 16), (24, 27), radius_x=14, radius_y=14, large_arc=False, sweep=True)
        self.add_arc('p3-r1-3', (24, 27), (8, 27), radius_x=14, radius_y=14, large_arc=False, sweep=True)
        self.add_arc('p3-r1-4', (8, 27), (2, 16), radius_x=14, radius_y=14, large_arc=False, sweep=True)
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', 'p3-r1-3', 'p3-r1-4', closed=False)
        self.relate('connect', 'p1-r1-1', 'p2-r1-1')
        self.relate('connect', 'p1-r1-1', 'p3-r1-2')
        self.relate('connect', 'p1-r1-1', 'p3-r1-3')
        self.relate('connect', 'p1-r1-2', 'p2-r1-1')
        self.relate('connect', 'p1-r1-2', 'p3-r1-3')
        self.relate('connect', 'p1-r1-2', 'p3-r1-4')
