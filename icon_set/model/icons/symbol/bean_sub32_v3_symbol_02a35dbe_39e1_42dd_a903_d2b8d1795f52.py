"""Independent 32px profile of bean.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = '02a35dbe-39e1-42dd-a903-d2b8d1795f52'
SOURCE_PATH = 'pictographic-primitives/symbol/peanut_02a35dbe-39e1-42dd-a903-d2b8d1795f52.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('02a35dbe-39e1-42dd-a903-d2b8d1795f52', 'pictographic-primitives/symbol/peanut_02a35dbe-39e1-42dd-a903-d2b8d1795f52.svg'),)
PROFILE_SOURCE_KEYS = ('solo/bean',)
SOLO_SOURCE_ICON_IDS = ('bean',)
REFERENCE_EXPORT_SHA256 = 'cc97f838ced67d583ecd052ba174121fc94dcdac494ec5a0cbb8ddeb2076bc10'

class DrawingVariant3ContainerSymbol(Sub32):
    icon_id = 'bean-sub32-v3-symbol'
    related_origin_icon_id = 'bean-sub32-v3'
    variant_label = 'Independent container symbol'
    usage_category = 'symbol'
    related_group = 'sub-origin/bean-sub32-v3'
    counterpart_icon_id = 'bean-sub32-v3'
    keyshape = Keyshape.HRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'symbol'
    categories = ('symbol', 'state')
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        # Adopted from the production stroke edit (Browser Edit by hina).
        self.add_bezier('p1-r1-1', (16, 10), ((16, 7), (19, 4), (23, 4)))
        self.add_bezier('p1-r1-2', (23, 4), ((27, 4), (30, 6), (30, 10)))
        self.add_bezier('p1-r1-3', (30, 10), ((30, 11.338912), (30, 12.677824), (30, 14)), ((30, 17.607306), (29.444444, 21.077626), (25, 24)))
        self.add_bezier('p1-r1-4', (25, 24), ((20, 28), (14, 28), (8, 28)))
        self.add_bezier('p1-r1-5', (8, 28), ((4, 28), (2, 25), (2, 22)))
        self.add_bezier('p1-r1-6', (2, 22), ((2, 19), (5, 16), (8, 16)))
        self.add_bezier('p1-r1-7', (8, 16), ((10, 16), (13, 15), (14, 14)))
        self.add_bezier('p1-r1-8', (14, 14), ((15, 13), (16, 12), (16, 10)))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', 'p1-r1-8', closed=False)
