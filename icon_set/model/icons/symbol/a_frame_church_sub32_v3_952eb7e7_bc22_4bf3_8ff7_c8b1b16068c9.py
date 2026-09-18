"""Independent 32px profile of a-frame-church.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = '952eb7e7-bc22-4bf3-8ff7-c8b1b16068c9'
SOURCE_PATH = 'pictographic-primitives/landmarks/batch-01/church_952eb7e7-bc22-4bf3-8ff7-c8b1b16068c9.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('952eb7e7-bc22-4bf3-8ff7-c8b1b16068c9', 'pictographic-primitives/landmarks/batch-01/church_952eb7e7-bc22-4bf3-8ff7-c8b1b16068c9.svg'),)
PROFILE_SOURCE_KEYS = ('solo/a-frame-church',)
SOLO_SOURCE_ICON_IDS = ('a-frame-church',)
REFERENCE_EXPORT_SHA256 = '389f1feab393c4b42bcc9f7cd09b67143016e7cd21c72d05a8565642e893ea45'

class DrawingVariant3(Sub32):
    icon_id = 'a-frame-church-sub32-v3'
    related_origin_icon_id = 'a-frame-church-sub32-v2'
    variant_label = 'Straight roof centerlines'
    keyshape = Keyshape.VRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'places/landmarks'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        short_axis = 16
        short_half_span = 12
        apex_y = 10
        roof_apex = (short_axis, apex_y)
        wall_left = (8, apex_y + short_axis - 8)
        wall_right = (24, apex_y + 24 - short_axis)
        roof_left = (short_axis - short_half_span, apex_y + short_half_span)
        roof_right = (short_axis + short_half_span, apex_y + short_half_span)
        short_low, short_high = (short_axis - short_half_span, short_axis + short_half_span)
        self.add_line('p1-r1-1', roof_left, wall_left)
        self.add_line('p1-r1-2', wall_left, roof_apex)
        self.add_line('p1-r1-3', roof_apex, wall_right)
        self.add_line('p1-r1-4', wall_right, roof_right)
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', closed=False)
        self.add_line('p2-r1-1', wall_left, (8, 30))
        self.add_line('p2-r1-2', (8, 30), (16, 30))
        self.add_line('p2-r1-3', (16, 30), (24, 30))
        self.add_line('p2-r1-4', (24, 30), wall_right)
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', closed=False)
        self.add_line('p3-r1-1', (16, 2), (16, 5))
        self.add_line('p3-r1-2', (16, 5), roof_apex)
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', closed=False)
        self.add_line('p4-r1-1', (14, 5), (16, 5))
        self.add_line('p4-r1-2', (16, 5), (18, 5))
        self.add_contour('path-4-1', 'p4-r1-1', 'p4-r1-2', closed=False)
        self.add_line('p5-r1-1', (16, 30), (16, 23))
        self.add_contour('path-5-1', 'p5-r1-1', closed=False)
        self.relate('connect', 'p1-r1-1', 'p2-r1-1')
        self.relate('connect', 'p1-r1-2', 'p2-r1-1')
        self.relate('connect', 'p1-r1-2', 'p3-r1-2')
        self.relate('connect', 'p1-r1-3', 'p2-r1-4')
        self.relate('connect', 'p1-r1-3', 'p3-r1-2')
        self.relate('connect', 'p1-r1-4', 'p2-r1-4')
        self.relate('connect', 'p2-r1-2', 'p5-r1-1')
        self.relate('connect', 'p2-r1-3', 'p5-r1-1')
        self.relate('connect', 'p3-r1-1', 'p4-r1-1')
        self.relate('connect', 'p3-r1-1', 'p4-r1-2')
        self.relate('connect', 'p3-r1-2', 'p4-r1-1')
        self.relate('connect', 'p3-r1-2', 'p4-r1-2')
