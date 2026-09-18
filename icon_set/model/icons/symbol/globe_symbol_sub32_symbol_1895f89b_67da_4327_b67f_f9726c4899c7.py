"""Independent 32px profile of globe-symbol.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = '1895f89b-67da-4327-b67f-f9726c4899c7'
SOURCE_PATH = 'pictographic-primitives/symbol/globe_1895f89b-67da-4327-b67f-f9726c4899c7.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('1895f89b-67da-4327-b67f-f9726c4899c7', 'pictographic-primitives/symbol/globe_1895f89b-67da-4327-b67f-f9726c4899c7.svg'), ('c71b55db-b3c3-429a-ae0f-378e045b24c3', 'pictographic-primitives/maps/earth_c71b55db-b3c3-429a-ae0f-378e045b24c3.svg'))
PROFILE_SOURCE_KEYS = ('solo/globe-symbol', 'solo/earth-c71b55db')
SOLO_SOURCE_ICON_IDS = ('globe-symbol', 'earth-c71b55db')
REFERENCE_EXPORT_SHA256 = '79c1bab50d0da22962d8f6ef8575e63e3d61674f33f9307fcf1320ff8a8f6c30'

class DrawingContainerSymbol(Sub32):
    icon_id = 'globe-symbol-sub32-symbol'
    related_origin_icon_id = 'globe-symbol-sub32'
    variant_label = 'Independent container symbol'
    usage_category = 'symbol'
    related_group = 'sub-origin/globe-symbol-sub32'
    counterpart_icon_id = 'globe-symbol-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'symbol'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (28, 21), (4, 21))
        self.add_contour('path-1-1', 'p1-r1-1', closed=False)
        self.add_line('p2-r1-1', (16, 30), (16, 2))
        self.add_arc('p2-r1-2', (16, 2), (2, 16), radius_x=14, radius_y=14, large_arc=False, sweep=False)
        self.add_arc('p2-r1-3', (2, 16), (16, 30), radius_x=14, radius_y=14, large_arc=False, sweep=False)
        self.add_arc('p2-r1-4', (16, 30), (30, 16), radius_x=14, radius_y=14, large_arc=False, sweep=False)
        self.add_arc('p2-r1-5', (30, 16), (16, 2), radius_x=14, radius_y=14, large_arc=False, sweep=False)
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', 'p2-r1-5', closed=False)
        self.add_line('p3-r1-1', (28, 11), (4, 11))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
