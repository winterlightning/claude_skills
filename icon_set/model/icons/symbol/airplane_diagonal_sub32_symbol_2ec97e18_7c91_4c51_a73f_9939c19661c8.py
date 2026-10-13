"""Independent 32px profile of airplane-diagonal.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = '2ec97e18-7c91-4c51-a73f-9939c19661c8'
SOURCE_PATH = 'pictographic-primitives/symbol/airplane_2ec97e18-7c91-4c51-a73f-9939c19661c8.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('2ec97e18-7c91-4c51-a73f-9939c19661c8', 'pictographic-primitives/symbol/airplane_2ec97e18-7c91-4c51-a73f-9939c19661c8.svg'), ('995ca841-d25b-4135-bff1-8fefd083a02d', 'pictographic-primitives/travel/plane_995ca841-d25b-4135-bff1-8fefd083a02d.svg'), ('b476e384-418f-4620-b003-0fd2cce07768', 'pictographic-primitives/travel/plane_b476e384-418f-4620-b003-0fd2cce07768.svg'))
PROFILE_SOURCE_KEYS = ('solo/airplane-diagonal', 'solo/diagonal-airplane-outline', 'solo/diagonal-airplane-pointed-wings')
SOLO_SOURCE_ICON_IDS = ('airplane-diagonal', 'diagonal-airplane-outline', 'diagonal-airplane-pointed-wings')
REFERENCE_EXPORT_SHA256 = 'fa4f6cf64f6dde13cf077a5be1fdf25b18812cf2e218238376c7ef860085eeb8'

class DrawingContainerSymbol(Sub32):
    icon_id = 'airplane-diagonal-sub32-symbol'
    related_origin_icon_id = 'airplane-diagonal-sub32'
    variant_label = 'Independent container symbol'
    usage_category = 'symbol'
    related_group = 'sub-origin/airplane-diagonal-sub32'
    counterpart_icon_id = 'airplane-diagonal-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'symbol'
    categories = ('symbol', 'state')
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        # Line airplane on the diagonal: fuselage from tail to nose, swept wings, small tail fins.
        self.add_line('p1-r1-1', (4, 28), (16, 16))
        self.add_line('p1-r1-2', (16, 16), (30, 2))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', closed=False)
        self.add_line('p2-r1-1', (16, 16), (4, 10))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p3-r1-1', (16, 16), (22, 28))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_line('p4-r1-1', (6, 26), (2, 24))
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
        self.add_line('p5-r1-1', (6, 26), (8, 30))
        self.add_contour('path-5-1', 'p5-r1-1', closed=False)
        self.relate('connect', 'p1-r1-1', 'p2-r1-1')
        self.relate('connect', 'p1-r1-2', 'p2-r1-1')
        self.relate('connect', 'p1-r1-1', 'p3-r1-1')
        self.relate('connect', 'p1-r1-2', 'p3-r1-1')
        self.relate('connect', 'p1-r1-1', 'p4-r1-1')
        self.relate('connect', 'p1-r1-1', 'p5-r1-1')
