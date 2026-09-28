"""Independent 32px profile of earth.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = '1faa3a74-7dec-436a-b945-ba1bb83aadd7'
SOURCE_PATH = 'pictographic-primitives/maps/earth_1faa3a74-7dec-436a-b945-ba1bb83aadd7.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('1faa3a74-7dec-436a-b945-ba1bb83aadd7', 'pictographic-primitives/maps/earth_1faa3a74-7dec-436a-b945-ba1bb83aadd7.svg'), ('89744ee7-77df-4bf2-a24f-f1af9e4d239b', 'pictographic-primitives/maps/earth_89744ee7-77df-4bf2-a24f-f1af9e4d239b.svg'), ('d015ebfd-28ea-4f8e-ae85-82a0c2e8077c', 'pictographic-primitives/maps/earth_d015ebfd-28ea-4f8e-ae85-82a0c2e8077c.svg'), ('862e1938-ba92-42a6-be54-909eda881f11', 'pictographic-primitives/maps/earth_862e1938-ba92-42a6-be54-909eda881f11.svg'))
PROFILE_SOURCE_KEYS = ('solo/earth', 'solo/earth-89744ee7', 'solo/earth-d015ebfd', 'solo/earth-maps')
SOLO_SOURCE_ICON_IDS = ('earth', 'earth-89744ee7', 'earth-d015ebfd', 'earth-maps')
REFERENCE_EXPORT_SHA256 = 'dea57a0698906bb56251e1f848f1f819d91c2d1b1829c8436ec191b3e1377c19'

class DrawingContainerSymbol(Sub32):
    icon_id = 'earth-sub32-symbol'
    related_origin_icon_id = 'earth-sub32'
    variant_label = 'Independent container symbol'
    usage_category = 'symbol'
    related_group = 'sub-origin/earth-sub32'
    counterpart_icon_id = 'earth-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'maps'
    categories = ('maps', 'primitives')
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_arc('p1-r1-1', (5, 8), (16, 2), radius_x=14, radius_y=14, large_arc=False, sweep=True)
        self.add_arc('p1-r1-2', (16, 2), (24, 5), radius_x=14, radius_y=14, large_arc=False, sweep=True)
        self.add_arc('p1-r1-3', (24, 5), (30, 16), radius_x=14, radius_y=14, large_arc=False, sweep=True)
        self.add_arc('p1-r1-4', (30, 16), (27, 24), radius_x=14, radius_y=14, large_arc=False, sweep=True)
        self.add_arc('p1-r1-5', (27, 24), (16, 30), radius_x=14, radius_y=14, large_arc=False, sweep=True)
        self.add_arc('p1-r1-6', (16, 30), (8, 27), radius_x=14, radius_y=14, large_arc=False, sweep=True)
        self.add_arc('p1-r1-7', (8, 27), (2, 16), radius_x=14, radius_y=14, large_arc=False, sweep=True)
        self.add_arc('p1-r1-8', (2, 16), (5, 8), radius_x=14, radius_y=14, large_arc=False, sweep=True)
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', 'p1-r1-8', closed=False)
        self.add_bezier('p2-r1-1', (5, 8), ((6, 8), (8, 9), (10, 10)))
        self.add_line('p2-r1-2', (10, 10), (8, 16))
        self.add_bezier('p2-r1-3', (8, 16), ((8, 17), (12, 18), (14, 19)))
        self.add_bezier('p2-r1-4', (14, 19), ((14, 23), (12, 26), (8, 27)))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', closed=False)
        self.add_bezier('p3-r1-1', (24, 5), ((20, 6), (18, 8), (18, 10)))
        self.add_bezier('p3-r1-2', (18, 10), ((18, 12), (21, 13), (22, 15)))
        self.add_line('p3-r1-3', (22, 15), (23, 20))
        self.add_bezier('p3-r1-4', (23, 20), ((24, 22), (25, 24), (27, 24)))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', 'p3-r1-3', 'p3-r1-4', closed=False)
        self.relate('connect', 'p1-r1-1', 'p2-r1-1')
        self.relate('connect', 'p1-r1-2', 'p3-r1-1')
        self.relate('connect', 'p1-r1-3', 'p3-r1-1')
        self.relate('connect', 'p1-r1-4', 'p3-r1-4')
        self.relate('connect', 'p1-r1-5', 'p3-r1-4')
        self.relate('connect', 'p1-r1-6', 'p2-r1-4')
        self.relate('connect', 'p1-r1-7', 'p2-r1-4')
        self.relate('connect', 'p1-r1-8', 'p2-r1-1')
