"""Independent 32px profile of skull-1.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = '43ebe571-7748-45bd-9b7e-bba72b5f6a14'
SOURCE_PATH = 'pictographic-primitives/interface-essential/skull 1_43ebe571-7748-45bd-9b7e-bba72b5f6a14.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('43ebe571-7748-45bd-9b7e-bba72b5f6a14', 'pictographic-primitives/interface-essential/skull 1_43ebe571-7748-45bd-9b7e-bba72b5f6a14.svg'), ('b6589244-b5a7-49bf-bf40-d9b773c9d505', 'pictographic-primitives/interface-essential/skull_b6589244-b5a7-49bf-bf40-d9b773c9d505.svg'))
PROFILE_SOURCE_KEYS = ('solo/skull-1', 'solo/skull-b6589244')
SOLO_SOURCE_ICON_IDS = ('skull-1', 'skull-b6589244')
REFERENCE_EXPORT_SHA256 = '9a19ed7d7844278ce16ea59f45ebc1cddf3d27fe12a9273c5bd5d4701a6dee52'

class DrawingContainerSymbol(Sub32):
    icon_id = 'skull-1-sub32-symbol'
    related_origin_icon_id = 'skull-1-sub32'
    variant_label = 'Independent container symbol'
    usage_category = 'symbol'
    related_group = 'sub-origin/skull-1-sub32'
    counterpart_icon_id = 'skull-1-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'interface-essential'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (20, 16), (23, 14))
        self.add_contour('path-1-1', 'p1-r1-1', closed=False)
        self.add_line('p2-r1-1', (12, 16), (9, 14))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p3-r1-1', (23, 30), (23, 26))
        self.add_bezier('p3-r1-2', (23, 26), ((25, 25), (29, 25), (30, 19)))
        self.add_bezier('p3-r1-3', (30, 19), ((30, 18), (30, 17), (30, 16)))
        self.add_bezier('p3-r1-4', (30, 16), ((30, 11), (28, 8), (26, 6)))
        self.add_bezier('p3-r1-5', (26, 6), ((23, 3), (20, 2), (16, 2)))
        self.add_bezier('p3-r1-6', (16, 2), ((12, 2), (9, 3), (6, 6)))
        self.add_bezier('p3-r1-7', (6, 6), ((4, 8), (2, 11), (2, 16)))
        self.add_bezier('p3-r1-8', (2, 16), ((2, 17), (2, 18), (2, 19)))
        self.add_bezier('p3-r1-9', (2, 19), ((3, 25), (7, 25), (9, 26)))
        self.add_line('p3-r1-10', (9, 26), (9, 30))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', 'p3-r1-3', 'p3-r1-4', 'p3-r1-5', 'p3-r1-6', 'p3-r1-7', 'p3-r1-8', 'p3-r1-9', 'p3-r1-10', closed=False)
        self.add_line('p4-r1-1', (16, 30), (16, 28))
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
