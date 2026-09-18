"""Independent 32px profile of diamond-money.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = '5d9db826-3f1d-489d-b7b6-bf5b50bbe949'
SOURCE_PATH = 'pictographic-primitives/money/diamond_5d9db826-3f1d-489d-b7b6-bf5b50bbe949.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('5d9db826-3f1d-489d-b7b6-bf5b50bbe949', 'pictographic-primitives/money/diamond_5d9db826-3f1d-489d-b7b6-bf5b50bbe949.svg'),)
PROFILE_SOURCE_KEYS = ('solo/diamond-money',)
SOLO_SOURCE_ICON_IDS = ('diamond-money',)
REFERENCE_EXPORT_SHA256 = '2a0c5306cbdd87ab938391e3c8e1d687d04e1fed025b6426bc4ed454a87a9ae0'

class DrawingContainerSymbol(Sub32):
    icon_id = 'diamond-money-sub32-symbol'
    related_origin_icon_id = 'diamond-money-sub32'
    variant_label = 'Independent container symbol'
    usage_category = 'symbol'
    related_group = 'sub-origin/diamond-money-sub32'
    counterpart_icon_id = 'diamond-money-sub32'
    keyshape = Keyshape.HRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'money'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (9, 5), (23, 5))
        self.add_line('p1-r1-2', (23, 5), (30, 15))
        self.add_line('p1-r1-3', (30, 15), (16, 27))
        self.add_line('p1-r1-4', (16, 27), (2, 15))
        self.add_line('p1-r1-5', (2, 15), (9, 5))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', closed=False)
        self.add_line('p2-r1-1', (2, 15), (12, 15))
        self.add_line('p2-r1-2', (12, 15), (20, 15))
        self.add_line('p2-r1-3', (20, 15), (30, 15))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', closed=False)
        self.add_line('p3-r1-1', (9, 5), (12, 15))
        self.add_line('p3-r1-2', (12, 15), (16, 27))
        self.add_line('p3-r1-3', (16, 27), (20, 15))
        self.add_line('p3-r1-4', (20, 15), (23, 5))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', 'p3-r1-3', 'p3-r1-4', closed=False)
        self.relate('connect', 'p1-r1-1', 'p3-r1-1')
        self.relate('connect', 'p1-r1-1', 'p3-r1-4')
        self.relate('connect', 'p1-r1-2', 'p2-r1-3')
        self.relate('connect', 'p1-r1-2', 'p3-r1-4')
        self.relate('connect', 'p1-r1-3', 'p2-r1-3')
        self.relate('connect', 'p1-r1-3', 'p3-r1-2')
        self.relate('connect', 'p1-r1-3', 'p3-r1-3')
        self.relate('connect', 'p1-r1-4', 'p2-r1-1')
        self.relate('connect', 'p1-r1-4', 'p3-r1-2')
        self.relate('connect', 'p1-r1-4', 'p3-r1-3')
        self.relate('connect', 'p1-r1-5', 'p2-r1-1')
        self.relate('connect', 'p1-r1-5', 'p3-r1-1')
        self.relate('connect', 'p2-r1-1', 'p3-r1-1')
        self.relate('connect', 'p2-r1-1', 'p3-r1-2')
        self.relate('connect', 'p2-r1-2', 'p3-r1-1')
        self.relate('connect', 'p2-r1-2', 'p3-r1-2')
        self.relate('connect', 'p2-r1-2', 'p3-r1-3')
        self.relate('connect', 'p2-r1-2', 'p3-r1-4')
        self.relate('connect', 'p2-r1-3', 'p3-r1-3')
        self.relate('connect', 'p2-r1-3', 'p3-r1-4')
