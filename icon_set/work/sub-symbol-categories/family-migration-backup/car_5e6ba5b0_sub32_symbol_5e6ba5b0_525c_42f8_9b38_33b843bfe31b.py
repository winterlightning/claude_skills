# Independent container symbol; edit separately from linked side sub-icon.
"""Independent 32px profile of car-5e6ba5b0.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = '5e6ba5b0-525c-42f8-9b38-33b843bfe31b'
SOURCE_PATH = 'pictographic-primitives/transportation/car_5e6ba5b0-525c-42f8-9b38-33b843bfe31b.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('5e6ba5b0-525c-42f8-9b38-33b843bfe31b', 'pictographic-primitives/transportation/car_5e6ba5b0-525c-42f8-9b38-33b843bfe31b.svg'), ('796e3289-99b8-4ef8-bce0-4e8fa2bfefc8', 'pictographic-primitives/transportation/car_796e3289-99b8-4ef8-bce0-4e8fa2bfefc8.svg'), ('eaa7f06c-57de-4d21-aaa7-d89d24b33193', 'pictographic-primitives/transportation/car_eaa7f06c-57de-4d21-aaa7-d89d24b33193.svg'), ('edd4874e-4e76-4ead-a51d-24426b253623', 'pictographic-primitives/transportation/car_edd4874e-4e76-4ead-a51d-24426b253623.svg'))
PROFILE_SOURCE_KEYS = ('solo/car-5e6ba5b0', 'solo/car-796e3289', 'solo/car-eaa7f06c', 'solo/car-edd4874e')
SOLO_SOURCE_ICON_IDS = ('car-5e6ba5b0', 'car-796e3289', 'car-eaa7f06c', 'car-edd4874e')
REFERENCE_EXPORT_SHA256 = '74c0ff8439a2ad60f72d38cffa5d6783aeb36217329f66101bd7a6a604bc8cf1'

class DrawingContainerSymbol(Sub32):
    icon_id = 'car-5e6ba5b0-sub32-symbol'
    variant_of = 'car-5e6ba5b0-sub32'
    variant_label = 'Independent container symbol'
    usage_category = 'symbol'
    related_group = 'sub-origin/car-5e6ba5b0-sub32'
    counterpart_icon_id = 'car-5e6ba5b0-sub32'
    keyshape = Keyshape.HRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'transportation'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (8, 13), (11, 6))
        self.add_bezier('p1-r1-2', (11, 6), ((12, 5), (13, 5), (16, 5)))
        self.add_bezier('p1-r1-3', (16, 5), ((19, 5), (20, 5), (21, 6)))
        self.add_line('p1-r1-4', (21, 6), (24, 13))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', closed=False)
        self.add_bezier('p2-r1-1', (5, 23), ((3, 23), (2, 20), (2, 18)))
        self.add_line('p2-r1-2', (2, 18), (2, 16))
        self.add_bezier('p2-r1-3', (2, 16), ((2, 14), (4, 12), (8, 13)))
        self.add_line('p2-r1-4', (8, 13), (24, 13))
        self.add_bezier('p2-r1-5', (24, 13), ((28, 13), (30, 14), (30, 16)))
        self.add_line('p2-r1-6', (30, 16), (30, 18))
        self.add_bezier('p2-r1-7', (30, 18), ((30, 20), (29, 23), (27, 23)))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', 'p2-r1-5', 'p2-r1-6', 'p2-r1-7', closed=False)
        self.add_arc('p3-r1-1', (5, 23), (9, 19), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_arc('p3-r1-2', (9, 19), (13, 23), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_arc('p3-r1-3', (13, 23), (9, 27), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_arc('p3-r1-4', (9, 27), (5, 23), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', 'p3-r1-3', 'p3-r1-4', closed=False)
        self.add_arc('p4-r1-1', (19, 23), (23, 19), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_arc('p4-r1-2', (23, 19), (27, 23), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_arc('p4-r1-3', (27, 23), (23, 27), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_arc('p4-r1-4', (23, 27), (19, 23), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_contour('path-4-1', 'p4-r1-1', 'p4-r1-2', 'p4-r1-3', 'p4-r1-4', closed=False)
        self.add_line('p5-r1-1', (13, 23), (19, 23))
        self.add_contour('path-5-1', 'p5-r1-1', closed=False)
        self.relate('connect', 'p1-r1-1', 'p2-r1-3')
        self.relate('connect', 'p1-r1-1', 'p2-r1-4')
        self.relate('connect', 'p1-r1-4', 'p2-r1-4')
        self.relate('connect', 'p1-r1-4', 'p2-r1-5')
        self.relate('connect', 'p2-r1-1', 'p3-r1-1')
        self.relate('connect', 'p2-r1-1', 'p3-r1-4')
        self.relate('connect', 'p2-r1-7', 'p4-r1-2')
        self.relate('connect', 'p2-r1-7', 'p4-r1-3')
        self.relate('connect', 'p3-r1-2', 'p5-r1-1')
        self.relate('connect', 'p3-r1-3', 'p5-r1-1')
        self.relate('connect', 'p4-r1-1', 'p5-r1-1')
        self.relate('connect', 'p4-r1-4', 'p5-r1-1')
