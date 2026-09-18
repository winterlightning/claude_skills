"""Independent 32px profile of lines.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = '70edbe92-e5a7-4163-82c3-c5891c1950fd'
SOURCE_PATH = 'pictographic-primitives/symbol/lines_70edbe92-e5a7-4163-82c3-c5891c1950fd.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('70edbe92-e5a7-4163-82c3-c5891c1950fd', 'pictographic-primitives/symbol/lines_70edbe92-e5a7-4163-82c3-c5891c1950fd.svg'),)
PROFILE_SOURCE_KEYS = ('solo/lines',)
SOLO_SOURCE_ICON_IDS = ('lines',)
REFERENCE_EXPORT_SHA256 = '291e1867663e7bfaa7272952faa75a50328447a7bca1b4037b97e74378de7a3e'

class DrawingVariant2(Sub32):
    icon_id = 'lines-sub32-v2'
    variant_of = 'lines-sub32'
    variant_label = 'Repair 32px envelope'
    keyshape = Keyshape.HRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'symbol'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        short_axis = 16
        short_half_span = 12
        (short_low, short_high) = (short_axis - short_half_span, short_axis + short_half_span)
        self.add_line('p1-r1-1', (2, 4), (8, 4))
        self.add_bezier('p1-r1-2', (8, 4), ((10, 4), (10, 7), (12, 10)))
        self.add_line('p1-r1-3', (12, 10), (20, 22))
        self.add_bezier('p1-r1-4', (20, 22), ((22, 25), (22, 28), (24, 28)))
        self.add_line('p1-r1-5', (24, short_high), (30, short_high))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', closed=False)
