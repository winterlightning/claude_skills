# Independent container symbol; edit separately from linked side sub-icon.
"""Independent 32px profile of trash-symbol.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = '65adbc02-2e53-460d-8ac2-44fa49dbce5f'
SOURCE_PATH = 'pictographic-primitives/symbol/trash_65adbc02-2e53-460d-8ac2-44fa49dbce5f.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('65adbc02-2e53-460d-8ac2-44fa49dbce5f', 'pictographic-primitives/symbol/trash_65adbc02-2e53-460d-8ac2-44fa49dbce5f.svg'),)
PROFILE_SOURCE_KEYS = ('solo/trash-symbol',)
SOLO_SOURCE_ICON_IDS = ('trash-symbol',)
REFERENCE_EXPORT_SHA256 = '30f99f07168d104c199b39cacd2d0d504c301df1dcc5f3ce655639c3cecd3879'

class DrawingContainerSymbol(Sub32):
    icon_id = 'trash-symbol-sub32-symbol'
    variant_of = 'trash-symbol-sub32'
    variant_label = 'Independent container symbol'
    usage_category = 'symbol'
    related_group = 'sub-origin/trash-symbol-sub32'
    counterpart_icon_id = 'trash-symbol-sub32'
    keyshape = Keyshape.VRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'symbol'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (8, 9), (10, 30))
        self.add_line('p1-r1-2', (10, 30), (22, 30))
        self.add_line('p1-r1-3', (22, 30), (24, 9))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', closed=False)
        self.add_line('p2-r1-1', (5, 9), (8, 9))
        self.add_line('p2-r1-2', (8, 9), (12, 9))
        self.add_line('p2-r1-3', (12, 9), (20, 9))
        self.add_line('p2-r1-4', (20, 9), (24, 9))
        self.add_line('p2-r1-5', (24, 9), (27, 9))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', 'p2-r1-5', closed=False)
        self.add_line('p3-r1-1', (12, 9), (12, 5))
        self.add_arc('p3-r1-2', (12, 5), (15, 2), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('p3-r1-3', (15, 2), (17, 2))
        self.add_arc('p3-r1-4', (17, 2), (20, 5), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('p3-r1-5', (20, 5), (20, 9))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', 'p3-r1-3', 'p3-r1-4', 'p3-r1-5', closed=False)
        self.relate('connect', 'p1-r1-1', 'p2-r1-1')
        self.relate('connect', 'p1-r1-1', 'p2-r1-2')
        self.relate('connect', 'p1-r1-3', 'p2-r1-4')
        self.relate('connect', 'p1-r1-3', 'p2-r1-5')
        self.relate('connect', 'p2-r1-2', 'p3-r1-1')
        self.relate('connect', 'p2-r1-3', 'p3-r1-1')
        self.relate('connect', 'p2-r1-3', 'p3-r1-5')
        self.relate('connect', 'p2-r1-4', 'p3-r1-5')
