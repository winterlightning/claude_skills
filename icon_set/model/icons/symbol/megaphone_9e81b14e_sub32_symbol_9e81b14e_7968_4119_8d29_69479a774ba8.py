"""Independent 32px profile of megaphone-9e81b14e.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = '9e81b14e-7968-4119-8d29-69479a774ba8'
SOURCE_PATH = 'pictographic-primitives/interface-essential/megaphone_9e81b14e-7968-4119-8d29-69479a774ba8.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('9e81b14e-7968-4119-8d29-69479a774ba8', 'pictographic-primitives/interface-essential/megaphone_9e81b14e-7968-4119-8d29-69479a774ba8.svg'), ('419cefd4-6e8d-4c3c-8b36-3566f3fa846b', 'pictographic-primitives/interface-essential/megaphone_419cefd4-6e8d-4c3c-8b36-3566f3fa846b.svg'))
PROFILE_SOURCE_KEYS = ('solo/megaphone-9e81b14e', 'solo/megaphone-interface-essential')
SOLO_SOURCE_ICON_IDS = ('megaphone-9e81b14e', 'megaphone-interface-essential')
REFERENCE_EXPORT_SHA256 = '0c17287a95bf13d28f521e0d9d93ccbfb1b446831e6760dfa4b90635ad542d26'

class DrawingContainerSymbol(Sub32):
    icon_id = 'megaphone-9e81b14e-sub32-symbol'
    related_origin_icon_id = 'megaphone-9e81b14e-sub32'
    variant_label = 'Independent container symbol'
    usage_category = 'symbol'
    related_group = 'sub-origin/megaphone-9e81b14e-sub32'
    counterpart_icon_id = 'megaphone-9e81b14e-sub32'
    keyshape = Keyshape.HRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'interface-essential'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (6, 15), (12, 15))
        self.add_bezier('p1-r1-2', (12, 15), ((17, 13), (22, 8), (27, 5)))
        self.add_line('p1-r1-3', (27, 5), (30, 22))
        self.add_bezier('p1-r1-4', (30, 22), ((27, 21), (24, 20), (22, 20)))
        self.add_bezier('p1-r1-5', (22, 20), ((18, 20), (15, 21), (12, 22)))
        self.add_line('p1-r1-6', (12, 22), (9, 22))
        self.add_line('p1-r1-7', (9, 22), (6, 22))
        self.add_bezier('p1-r1-8', (6, 22), ((4, 22), (2, 20), (2, 18)))
        self.add_bezier('p1-r1-9', (2, 18), ((2, 16), (4, 15), (6, 15)))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', 'p1-r1-8', 'p1-r1-9', closed=False)
        self.add_line('p2-r1-1', (12, 15), (12, 22))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_bezier('p3-r1-1', (9, 22), ((10, 24), (12, 27), (14, 27)))
        self.add_line('p3-r1-2', (14, 27), (17, 26))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', closed=False)
        self.relate('connect', 'p1-r1-1', 'p2-r1-1')
        self.relate('connect', 'p1-r1-2', 'p2-r1-1')
        self.relate('connect', 'p1-r1-5', 'p2-r1-1')
        self.relate('connect', 'p1-r1-6', 'p2-r1-1')
        self.relate('connect', 'p1-r1-6', 'p3-r1-1')
        self.relate('connect', 'p1-r1-7', 'p3-r1-1')
