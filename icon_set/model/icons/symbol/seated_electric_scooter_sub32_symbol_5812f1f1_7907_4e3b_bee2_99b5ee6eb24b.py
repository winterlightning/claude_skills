"""Independent 32px profile of seated-electric-scooter.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = '5812f1f1-7907-4e3b-bee2-99b5ee6eb24b'
SOURCE_PATH = 'pictographic-primitives/transportation/scooter_5812f1f1-7907-4e3b-bee2-99b5ee6eb24b.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('5812f1f1-7907-4e3b-bee2-99b5ee6eb24b', 'pictographic-primitives/transportation/scooter_5812f1f1-7907-4e3b-bee2-99b5ee6eb24b.svg'),)
PROFILE_SOURCE_KEYS = ('solo/seated-electric-scooter',)
SOLO_SOURCE_ICON_IDS = ('seated-electric-scooter',)
REFERENCE_EXPORT_SHA256 = '6d9e39f55b062cd667d346f1fd91bafc3e674d4168b6f5979154ec0d22408440'

class DrawingContainerSymbol(Sub32):
    icon_id = 'seated-electric-scooter-sub32-symbol'
    related_origin_icon_id = 'seated-electric-scooter-sub32'
    variant_label = 'Independent container symbol'
    usage_category = 'symbol'
    related_group = 'sub-origin/seated-electric-scooter-sub32'
    counterpart_icon_id = 'seated-electric-scooter-sub32'
    keyshape = Keyshape.HRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'transportation'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_bezier('p1-r1-1', (6, 20), ((7, 20), (9, 22), (9, 24)))
        self.add_bezier('p1-r1-2', (9, 24), ((9, 26), (7, 27), (6, 27)))
        self.add_bezier('p1-r1-3', (6, 27), ((4, 27), (2, 26), (2, 24)))
        self.add_bezier('p1-r1-4', (2, 24), ((2, 22), (4, 20), (6, 20)))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', closed=False)
        self.add_bezier('p2-r1-1', (26, 20), ((28, 20), (30, 22), (30, 24)))
        self.add_bezier('p2-r1-2', (30, 24), ((30, 26), (28, 27), (26, 27)))
        self.add_bezier('p2-r1-3', (26, 27), ((25, 27), (23, 26), (23, 24)))
        self.add_bezier('p2-r1-4', (23, 24), ((23, 22), (25, 20), (26, 20)))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', closed=False)
        self.add_line('p3-r1-1', (17, 5), (21, 5))
        self.add_line('p3-r1-2', (21, 5), (24, 13))
        self.add_line('p3-r1-3', (24, 13), (27, 20))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', 'p3-r1-3', closed=False)
        self.add_line('p4-r1-1', (6, 20), (14, 20))
        self.add_line('p4-r1-2', (14, 20), (18, 20))
        self.add_contour('path-4-1', 'p4-r1-1', 'p4-r1-2', closed=False)
        self.add_bezier('p5-r1-1', (18, 20), ((20, 20), (21, 20), (22, 19)))
        self.add_bezier('p5-r1-2', (22, 19), ((23, 18), (24, 16), (24, 15)))
        self.add_line('p5-r1-3', (24, 15), (24, 13))
        self.add_contour('path-5-1', 'p5-r1-1', 'p5-r1-2', 'p5-r1-3', closed=False)
        self.add_line('p6-r1-1', (8, 13), (11, 13))
        self.add_line('p6-r1-2', (11, 13), (15, 13))
        self.add_contour('path-6-1', 'p6-r1-1', 'p6-r1-2', closed=False)
        self.add_line('p7-r1-1', (11, 13), (14, 20))
        self.add_contour('path-7-1', 'p7-r1-1', closed=False)
        self.relate('connect', 'p1-r1-1', 'p4-r1-1')
        self.relate('connect', 'p1-r1-4', 'p4-r1-1')
        self.relate('connect', 'p3-r1-2', 'p5-r1-3')
        self.relate('connect', 'p3-r1-3', 'p5-r1-3')
        self.relate('connect', 'p4-r1-1', 'p7-r1-1')
        self.relate('connect', 'p4-r1-2', 'p5-r1-1')
        self.relate('connect', 'p4-r1-2', 'p7-r1-1')
        self.relate('connect', 'p6-r1-1', 'p7-r1-1')
        self.relate('connect', 'p6-r1-2', 'p7-r1-1')
