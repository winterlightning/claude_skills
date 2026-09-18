"""Independent 32px profile of book-open-1421392c.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = '1421392c-5884-4c7e-bf5c-1082165dfba9'
SOURCE_PATH = 'pictographic-primitives/content/book open_1421392c-5884-4c7e-bf5c-1082165dfba9.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('1421392c-5884-4c7e-bf5c-1082165dfba9', 'pictographic-primitives/content/book open_1421392c-5884-4c7e-bf5c-1082165dfba9.svg'), ('df25e3f8-0308-43ac-83b9-5a03a38cf7f5', 'pictographic-primitives/content/book open 1_df25e3f8-0308-43ac-83b9-5a03a38cf7f5.svg'), ('a147931e-057f-4518-b391-cf08f66084de', 'pictographic-primitives/content/book open_a147931e-057f-4518-b391-cf08f66084de.svg'))
PROFILE_SOURCE_KEYS = ('solo/book-open-1421392c', 'solo/book-open-1-df25e3f8', 'solo/book-open-a147931e')
SOLO_SOURCE_ICON_IDS = ('book-open-1421392c', 'book-open-1-df25e3f8', 'book-open-a147931e')
REFERENCE_EXPORT_SHA256 = '1bae9a15dc9fe7fdec94acae5090512df80fbbba3b114ec69ff3eeeda1a1eec5'

class DrawingContainerSymbol(Sub32):
    icon_id = 'book-open-1421392c-sub32-symbol'
    related_origin_icon_id = 'book-open-1421392c-sub32'
    variant_label = 'Independent container symbol'
    usage_category = 'symbol'
    related_group = 'sub-origin/book-open-1421392c-sub32'
    counterpart_icon_id = 'book-open-1421392c-sub32'
    keyshape = Keyshape.HRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'content'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (16, 10), (9, 5))
        self.add_line('p1-r1-2', (9, 5), (2, 8))
        self.add_line('p1-r1-3', (2, 8), (2, 23))
        self.add_line('p1-r1-4', (2, 23), (9, 22))
        self.add_line('p1-r1-5', (9, 22), (16, 27))
        self.add_bezier('p1-r1-6', (16, 27), ((20, 23), (26, 23), (30, 23)))
        self.add_line('p1-r1-7', (30, 23), (30, 6))
        self.add_bezier('p1-r1-8', (30, 6), ((26, 6), (20, 6), (16, 10)))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', 'p1-r1-8', closed=False)
        self.add_line('p2-r1-1', (16, 10), (16, 27))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p3-r1-1', (9, 5), (9, 22))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.relate('connect', 'p1-r1-1', 'p2-r1-1')
        self.relate('connect', 'p1-r1-1', 'p3-r1-1')
        self.relate('connect', 'p1-r1-2', 'p3-r1-1')
        self.relate('connect', 'p1-r1-4', 'p3-r1-1')
        self.relate('connect', 'p1-r1-5', 'p2-r1-1')
        self.relate('connect', 'p1-r1-5', 'p3-r1-1')
        self.relate('connect', 'p1-r1-6', 'p2-r1-1')
        self.relate('connect', 'p1-r1-8', 'p2-r1-1')
