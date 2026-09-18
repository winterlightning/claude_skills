"""Independent 32px profile of qr-code-shopping.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = 'c718dafa-f70c-4dd4-a8fd-0d77a06c599f'
SOURCE_PATH = 'pictographic-primitives/shopping/qr code_c718dafa-f70c-4dd4-a8fd-0d77a06c599f.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('c718dafa-f70c-4dd4-a8fd-0d77a06c599f', 'pictographic-primitives/shopping/qr code_c718dafa-f70c-4dd4-a8fd-0d77a06c599f.svg'),)
PROFILE_SOURCE_KEYS = ('solo/qr-code-shopping',)
SOLO_SOURCE_ICON_IDS = ('qr-code-shopping',)
REFERENCE_EXPORT_SHA256 = '4ebb324eca5b0018182929aa1c8a60de851f06ea10b6bad2cfd4b61abdb23d5d'

class DrawingVariant2(Sub32):
    icon_id = 'qr-code-shopping-sub32-v2'
    related_origin_icon_id = 'qr-code-shopping-sub32'
    variant_label = 'Repair 32px envelope'
    keyshape = Keyshape.HRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'shopping'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        short_axis = 16
        short_half_span = 12
        short_low, short_high = (short_axis - short_half_span, short_axis + short_half_span)
        self.add_line('p1-r1-1', (2, short_high), (2, short_low))
        self.add_contour('path-1-1', 'p1-r1-1', closed=False)
        self.add_line('p2-r1-1', (12, short_low), (12, 18))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p3-r1-1', (20, short_low), (20, 18))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_line('p4-r1-1', (30, short_low), (30, short_high))
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
        self.add_line('p5-r1-1', (12, 26), (12, short_high))
        self.add_contour('path-5-1', 'p5-r1-1', closed=False)
        self.add_line('p6-r1-1', (20, 26), (20, short_high))
        self.add_contour('path-6-1', 'p6-r1-1', closed=False)
