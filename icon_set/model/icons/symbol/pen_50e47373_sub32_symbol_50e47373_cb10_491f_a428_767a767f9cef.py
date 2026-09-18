"""Independent 32px profile of pen-50e47373.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = '50e47373-cb10-491f-a428-767a767f9cef'
SOURCE_PATH = 'pictographic-primitives/design/pen_50e47373-cb10-491f-a428-767a767f9cef.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('50e47373-cb10-491f-a428-767a767f9cef', 'pictographic-primitives/design/pen_50e47373-cb10-491f-a428-767a767f9cef.svg'), ('7ee2f930-e642-4295-aaa3-5150e3fc91e5', 'pictographic-primitives/design/pen_7ee2f930-e642-4295-aaa3-5150e3fc91e5.svg'))
PROFILE_SOURCE_KEYS = ('solo/pen-50e47373', 'solo/pen-7ee2f930')
SOLO_SOURCE_ICON_IDS = ('pen-50e47373', 'pen-7ee2f930')
REFERENCE_EXPORT_SHA256 = '4ed27c71c7372ed32ce2a47ac5f724620e282c674712c89a5fa989db8f2253d6'

class DrawingContainerSymbol(Sub32):
    icon_id = 'pen-50e47373-sub32-symbol'
    related_origin_icon_id = 'pen-50e47373-sub32'
    variant_label = 'Independent container symbol'
    usage_category = 'symbol'
    related_group = 'sub-origin/pen-50e47373-sub32'
    counterpart_icon_id = 'pen-50e47373-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'design'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (7, 19), (21, 5))
        self.add_bezier('p1-r1-2', (21, 5), ((22, 4), (23, 2), (25, 2)))
        self.add_arc('p1-r1-3', (25, 2), (30, 7), radius_x=5, radius_y=5, large_arc=False, sweep=True)
        self.add_bezier('p1-r1-4', (30, 7), ((30, 9), (28, 10), (27, 11)))
        self.add_line('p1-r1-5', (27, 11), (13, 25))
        self.add_line('p1-r1-6', (13, 25), (2, 30))
        self.add_line('p1-r1-7', (2, 30), (7, 19))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', closed=False)
        self.add_line('p2-r1-1', (18, 8), (24, 14))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p3-r1-1', (7, 19), (13, 25))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.relate('connect', 'p1-r1-1', 'p3-r1-1')
        self.relate('connect', 'p1-r1-5', 'p3-r1-1')
        self.relate('connect', 'p1-r1-6', 'p3-r1-1')
        self.relate('connect', 'p1-r1-7', 'p3-r1-1')
