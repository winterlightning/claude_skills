# Repair: shared short-axis extrema retain the full source composition on the legal SUB32 envelope.
"""Independent 32px profile of octagon-up-arrow-content.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = '1d212fbb-810b-4031-893b-526296e01048'
SOURCE_PATH = 'icon_set/dist/gallery/combination-originals/1d212fbb-810b-4031-893b-526296e01048.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('1d212fbb-810b-4031-893b-526296e01048', 'icon_set/dist/gallery/combination-originals/1d212fbb-810b-4031-893b-526296e01048.svg'),)
PROFILE_SOURCE_KEYS = ('solo/octagon-up-arrow-content',)
SOLO_SOURCE_ICON_IDS = ('octagon-up-arrow-content',)
REFERENCE_EXPORT_SHA256 = '410829c823d717317547a5aaa7617e44d1cad625afd9f3790423649b53de8e39'

class DrawingVariant2(Sub32):
    icon_id = 'octagon-up-arrow-content-sub32-v2'
    variant_of = 'octagon-up-arrow-content-sub32'
    variant_label = 'Repair 32px envelope'
    keyshape = Keyshape.VRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'symbol'
    categories = ('symbol',)
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        short_axis = 16
        short_half_span = 12
        (short_low, short_high) = (short_axis - short_half_span, short_axis + short_half_span)
        self.add_line('p1-r1-1', (10, 16), (22, 16))
        self.add_line('p1-r1-2', (22, 16), (short_high, 22))
        self.add_line('p1-r1-3', (short_high, 22), (short_high, 24))
        self.add_line('p1-r1-4', (short_high, 24), (22, 30))
        self.add_line('p1-r1-5', (22, 30), (10, 30))
        self.add_line('p1-r1-6', (10, 30), (short_low, 24))
        self.add_line('p1-r1-7', (short_low, 24), (short_low, 22))
        self.add_line('p1-r1-8', (short_low, 22), (10, 16))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', 'p1-r1-8', closed=False)
        self.add_line('p2-r1-1', (10, 8), (16, 2))
        self.add_line('p2-r1-2', (16, 2), (22, 8))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', closed=False)
        self.add_line('p3-r1-1', (16, 2), (16, 10))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.relate('connect', 'p2-r1-1', 'p3-r1-1')
        self.relate('connect', 'p2-r1-2', 'p3-r1-1')
