"""Independent 32px profile of wheelchair-accessible.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = 'da29f68e-5632-431d-92e7-4ee9f999acb8'
SOURCE_PATH = 'pictographic-primitives/symbol/wheelchair_da29f68e-5632-431d-92e7-4ee9f999acb8.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('da29f68e-5632-431d-92e7-4ee9f999acb8', 'pictographic-primitives/symbol/wheelchair_da29f68e-5632-431d-92e7-4ee9f999acb8.svg'),)
PROFILE_SOURCE_KEYS = ('solo/wheelchair-accessible',)
SOLO_SOURCE_ICON_IDS = ('wheelchair-accessible',)
REFERENCE_EXPORT_SHA256 = '628c4b176c82ac2974b34469f9b2489870b6ccc915ab01b84fda940c9fb63018'

class DrawingContainerSymbol(Sub32):
    icon_id = 'wheelchair-accessible-sub32-symbol'
    related_origin_icon_id = 'wheelchair-accessible-sub32'
    variant_label = 'Independent container symbol'
    usage_category = 'symbol'
    related_group = 'sub-origin/wheelchair-accessible-sub32'
    counterpart_icon_id = 'wheelchair-accessible-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'objects/symbols'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_arc('p1-r1-1', (13, 5), (19, 5), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_arc('p1-r1-2', (19, 5), (13, 5), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', closed=False)
        self.add_line('p2-r1-1', (16, 8), (16, 13))
        self.add_line('p2-r1-2', (16, 13), (16, 19))
        self.add_line('p2-r1-3', (16, 19), (24, 19))
        self.add_line('p2-r1-4', (24, 19), (28, 28))
        self.add_line('p2-r1-5', (28, 28), (30, 28))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', 'p2-r1-5', closed=False)
        self.add_line('p3-r1-1', (16, 13), (24, 13))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_bezier('p4-r1-1', (5, 16), ((3, 18), (2, 20), (2, 22)))
        self.add_bezier('p4-r1-2', (2, 22), ((2, 24), (3, 26), (4, 28)))
        self.add_bezier('p4-r1-3', (4, 28), ((6, 29), (8, 30), (10, 30)))
        self.add_bezier('p4-r1-4', (10, 30), ((12, 30), (14, 29), (16, 27)))
        self.add_contour('path-4-1', 'p4-r1-1', 'p4-r1-2', 'p4-r1-3', 'p4-r1-4', closed=False)
        self.relate('connect', 'p2-r1-1', 'p3-r1-1')
        self.relate('connect', 'p2-r1-2', 'p3-r1-1')
