"""Independent 32px profile of bus-front.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = '6be3bbdd-720f-407c-af2d-59983752017d'
SOURCE_PATH = 'pictographic-primitives/transportation/bus_6be3bbdd-720f-407c-af2d-59983752017d.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('6be3bbdd-720f-407c-af2d-59983752017d', 'pictographic-primitives/transportation/bus_6be3bbdd-720f-407c-af2d-59983752017d.svg'),)
PROFILE_SOURCE_KEYS = ('solo/bus-front',)
SOLO_SOURCE_ICON_IDS = ('bus-front',)
REFERENCE_EXPORT_SHA256 = 'a515514d2accbf20d8e88d0f111e037fe0a3fb605e3b5591d47aaba7df81e861'

class DrawingContainerSymbol(Sub32):
    icon_id = 'bus-front-sub32-symbol'
    related_origin_icon_id = 'bus-front-sub32'
    variant_label = 'Independent container symbol'
    usage_category = 'symbol'
    related_group = 'sub-origin/bus-front-sub32'
    counterpart_icon_id = 'bus-front-sub32'
    keyshape = Keyshape.VRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'transportation'
    categories = ('transportation', 'other', 'primitives-generate')
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (7, 2), (25, 2))
        self.add_arc('p1-r1-2', (25, 2), (28, 5), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('p1-r1-3', (28, 5), (28, 10))
        self.add_line('p1-r1-4', (28, 10), (28, 23))
        self.add_arc('p1-r1-5', (28, 23), (25, 26), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('p1-r1-6', (25, 26), (23, 26))
        self.add_line('p1-r1-7', (23, 26), (9, 26))
        self.add_line('p1-r1-8', (9, 26), (7, 26))
        self.add_arc('p1-r1-9', (7, 26), (4, 23), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('p1-r1-10', (4, 23), (4, 10))
        self.add_line('p1-r1-11', (4, 10), (4, 5))
        self.add_arc('p1-r1-12', (4, 5), (7, 2), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', 'p1-r1-8', 'p1-r1-9', 'p1-r1-10', 'p1-r1-11', 'p1-r1-12', closed=False)
        self.add_line('p2-r1-1', (4, 10), (28, 10))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p3-r1-1', (9, 26), (9, 30))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_line('p4-r1-1', (23, 26), (23, 30))
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
        self.add_line('p5-r1-1', (12, 18), (12, 18))
        self.add_contour('path-5-1', 'p5-r1-1', closed=False)
        self.add_line('p6-r1-1', (20, 18), (20, 18))
        self.add_contour('path-6-1', 'p6-r1-1', closed=False)
        self.relate('connect', 'p1-r1-3', 'p2-r1-1')
        self.relate('connect', 'p1-r1-4', 'p2-r1-1')
        self.relate('connect', 'p1-r1-6', 'p4-r1-1')
        self.relate('connect', 'p1-r1-7', 'p3-r1-1')
        self.relate('connect', 'p1-r1-7', 'p4-r1-1')
        self.relate('connect', 'p1-r1-8', 'p3-r1-1')
        self.relate('connect', 'p1-r1-10', 'p2-r1-1')
        self.relate('connect', 'p1-r1-11', 'p2-r1-1')
