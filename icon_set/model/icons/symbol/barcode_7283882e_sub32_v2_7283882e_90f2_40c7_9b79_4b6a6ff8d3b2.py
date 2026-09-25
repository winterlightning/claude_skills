"""Independent 32px profile of barcode-7283882e.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = '7283882e-90f2-40c7-9b79-4b6a6ff8d3b2'
SOURCE_PATH = 'pictographic-primitives/shopping/barcode_7283882e-90f2-40c7-9b79-4b6a6ff8d3b2.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('7283882e-90f2-40c7-9b79-4b6a6ff8d3b2', 'pictographic-primitives/shopping/barcode_7283882e-90f2-40c7-9b79-4b6a6ff8d3b2.svg'), ('d7b4657c-3734-40c1-a4f9-684f4d61861b', 'pictographic-primitives/shopping/barcode_d7b4657c-3734-40c1-a4f9-684f4d61861b.svg'), ('e7b1e1e5-d8dd-49d8-91d5-f83818d726c9', 'pictographic-primitives/shopping/barcode_e7b1e1e5-d8dd-49d8-91d5-f83818d726c9.svg'))
PROFILE_SOURCE_KEYS = ('solo/barcode-7283882e', 'solo/barcode-d7b4657c', 'solo/barcode-e7b1e1e5')
SOLO_SOURCE_ICON_IDS = ('barcode-7283882e', 'barcode-d7b4657c', 'barcode-e7b1e1e5')
REFERENCE_EXPORT_SHA256 = '167c77e172e7147ec6bc74c4fe00adeb787f921caa9817d9b1656061b12a2d18'

class DrawingVariant2(Sub32):
    icon_id = 'barcode-7283882e-sub32-v2'
    related_origin_icon_id = 'barcode-7283882e-sub32'
    variant_label = 'Repair 32px envelope'
    keyshape = Keyshape.HRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'shopping'
    categories = ('shopping', 'primitives')
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        short_axis = 16
        short_half_span = 12
        short_low, short_high = (short_axis - short_half_span, short_axis + short_half_span)
        self.add_line('p1-r1-1', (2, short_high), (2, short_low))
        self.add_contour('path-1-1', 'p1-r1-1', closed=False)
        self.add_line('p2-r1-1', (21, short_high), (21, short_low))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p3-r1-1', (11, short_high), (11, short_low))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_line('p4-r1-1', (30, short_high), (30, short_low))
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
