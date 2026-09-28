"""Independent 32px profile of bar-chart-lines.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = '3bb45fbb-182b-4dcd-92bf-ebd5c20fa96c'
SOURCE_PATH = 'pictographic-primitives/symbol/bar chart_3bb45fbb-182b-4dcd-92bf-ebd5c20fa96c.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('3bb45fbb-182b-4dcd-92bf-ebd5c20fa96c', 'pictographic-primitives/symbol/bar chart_3bb45fbb-182b-4dcd-92bf-ebd5c20fa96c.svg'),)
PROFILE_SOURCE_KEYS = ('solo/bar-chart-lines',)
SOLO_SOURCE_ICON_IDS = ('bar-chart-lines',)
REFERENCE_EXPORT_SHA256 = 'ec48eb8a370bfd5f46c868bd6db046c7b737f64d6a8fa51ffed579af4687549f'

class DrawingContainerSymbol(Sub32):
    icon_id = 'bar-chart-lines-sub32-symbol'
    related_origin_icon_id = 'bar-chart-lines-sub32'
    variant_label = 'Independent container symbol'
    usage_category = 'symbol'
    related_group = 'sub-origin/bar-chart-lines-sub32'
    counterpart_icon_id = 'bar-chart-lines-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'symbol'
    categories = ('symbol', 'state')
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (2, 30), (30, 30))
        self.add_contour('path-1-1', 'p1-r1-1', closed=False)
        self.add_line('p2-r1-1', (7, 11), (7, 24))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p3-r1-1', (16, 2), (16, 24))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_line('p4-r1-1', (25, 18), (25, 24))
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
