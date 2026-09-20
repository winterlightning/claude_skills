# Independent container symbol; edit separately from linked side sub-icon.
"""Independent 32px profile of fork-and-knife.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = 'b66fd641-5f5f-41b7-acfe-644485d3c82d'
SOURCE_PATH = 'pictographic-primitives/symbol/fork and knife_b66fd641-5f5f-41b7-acfe-644485d3c82d.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('b66fd641-5f5f-41b7-acfe-644485d3c82d', 'pictographic-primitives/symbol/fork and knife_b66fd641-5f5f-41b7-acfe-644485d3c82d.svg'),)
PROFILE_SOURCE_KEYS = ('solo/fork-and-knife',)
SOLO_SOURCE_ICON_IDS = ('fork-and-knife',)
REFERENCE_EXPORT_SHA256 = '0e3c5c399b5f2ffcfea4b2559f8efaddc39b23d60f0d07af3ea3404d9a17f070'

class DrawingContainerSymbol(Sub32):
    icon_id = 'fork-and-knife-sub32-symbol'
    variant_of = 'fork-and-knife-sub32'
    variant_label = 'Independent container symbol'
    usage_category = 'symbol'
    related_group = 'sub-origin/fork-and-knife-sub32'
    counterpart_icon_id = 'fork-and-knife-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'symbol'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (2, 2), (2, 11))
        self.add_bezier('p1-r1-2', (2, 11), ((2, 13), (3, 15), (4, 16)))
        self.add_bezier('p1-r1-3', (4, 16), ((5, 17), (7, 18), (8, 18)))
        self.add_bezier('p1-r1-4', (8, 18), ((8, 18), (8, 18), (8, 18)))
        self.add_arc('p1-r1-5', (8, 18), (14, 11), radius_x=6, radius_y=6, large_arc=False, sweep=False)
        self.add_line('p1-r1-6', (14, 11), (14, 2))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', closed=False)
        self.add_line('p2-r1-1', (8, 2), (8, 18))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p3-r1-1', (8, 18), (8, 30))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_line('p4-r1-1', (24, 30), (24, 2))
        self.add_line('p4-r1-2', (24, 2), (30, 14))
        self.add_line('p4-r1-3', (30, 14), (30, 21))
        self.add_line('p4-r1-4', (30, 21), (24, 21))
        self.add_contour('path-4-1', 'p4-r1-1', 'p4-r1-2', 'p4-r1-3', 'p4-r1-4', closed=False)
        self.relate('connect', 'p1-r1-3', 'p2-r1-1')
        self.relate('connect', 'p1-r1-3', 'p3-r1-1')
        self.relate('connect', 'p1-r1-4', 'p2-r1-1')
        self.relate('connect', 'p1-r1-4', 'p3-r1-1')
        self.relate('connect', 'p1-r1-5', 'p2-r1-1')
        self.relate('connect', 'p1-r1-5', 'p3-r1-1')
        self.relate('connect', 'p2-r1-1', 'p3-r1-1')
