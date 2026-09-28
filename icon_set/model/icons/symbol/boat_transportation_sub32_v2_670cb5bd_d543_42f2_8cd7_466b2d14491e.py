"""Independent 32px profile of boat-transportation.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = '670cb5bd-d543-42f2-8cd7-466b2d14491e'
SOURCE_PATH = 'pictographic-primitives/transportation/boat_670cb5bd-d543-42f2-8cd7-466b2d14491e.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('670cb5bd-d543-42f2-8cd7-466b2d14491e', 'pictographic-primitives/transportation/boat_670cb5bd-d543-42f2-8cd7-466b2d14491e.svg'),)
PROFILE_SOURCE_KEYS = ('solo/boat-transportation',)
SOLO_SOURCE_ICON_IDS = ('boat-transportation',)
REFERENCE_EXPORT_SHA256 = '0c699973b78d2abc46f1c6c27d8fc95afd0c414a354eb52ad8f4e7fb79cafeb1'

class DrawingVariant2(Sub32):
    icon_id = 'boat-transportation-sub32-v2'
    related_origin_icon_id = 'boat-transportation-sub32'
    variant_label = 'Repair 32px envelope'
    keyshape = Keyshape.HRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'transportation'
    categories = ('transportation', 'other', 'primitives-generate')
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        short_axis = 16
        short_half_span = 12
        short_low, short_high = (short_axis - short_half_span, short_axis + short_half_span)
        self.add_line('p1-r1-1', (8, 16), (10, short_low))
        self.add_line('p1-r1-2', (10, short_low), (22, short_low))
        self.add_line('p1-r1-3', (22, short_low), (24, 16))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', closed=False)
        self.add_line('p2-r1-1', (2, 16), (8, 16))
        self.add_line('p2-r1-2', (8, 16), (24, 16))
        self.add_line('p2-r1-3', (24, 16), (30, 16))
        self.add_line('p2-r1-4', (30, 16), (26, short_high))
        self.add_bezier('p2-r1-5', (26, short_high), ((23, short_high), (22, 25), (20, 25)))
        self.add_bezier('p2-r1-6', (20, 25), ((19, 25), (18, 26), (16, short_high)))
        self.add_bezier('p2-r1-7', (16, short_high), ((14, 26), (13, 25), (12, 25)))
        self.add_bezier('p2-r1-8', (12, 25), ((10, 25), (9, short_high), (6, short_high)))
        self.add_line('p2-r1-9', (6, short_high), (2, 16))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', 'p2-r1-5', 'p2-r1-6', 'p2-r1-7', 'p2-r1-8', 'p2-r1-9', closed=False)
        self.relate('connect', 'p1-r1-1', 'p2-r1-1')
        self.relate('connect', 'p1-r1-1', 'p2-r1-2')
        self.relate('connect', 'p1-r1-3', 'p2-r1-2')
        self.relate('connect', 'p1-r1-3', 'p2-r1-3')
