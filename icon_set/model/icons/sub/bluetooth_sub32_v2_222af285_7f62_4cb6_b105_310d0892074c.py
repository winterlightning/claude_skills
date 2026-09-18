# Repair: shared short-axis extrema retain the full source composition on the legal SUB32 envelope.
"""Independent 32px profile of bluetooth.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = '222af285-7f62-4cb6-b105-310d0892074c'
SOURCE_PATH = 'pictographic-primitives/networks/bluetooth_222af285-7f62-4cb6-b105-310d0892074c.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('222af285-7f62-4cb6-b105-310d0892074c', 'pictographic-primitives/networks/bluetooth_222af285-7f62-4cb6-b105-310d0892074c.svg'),)
PROFILE_SOURCE_KEYS = ('solo/bluetooth',)
SOLO_SOURCE_ICON_IDS = ('bluetooth',)
REFERENCE_EXPORT_SHA256 = 'aaf017c74fdd180a64b6da389d39ede24e91377fffa10d9fb5aa323f2fc48f69'

class DrawingVariant2(Sub32):
    icon_id = 'bluetooth-sub32-v2'
    variant_of = 'bluetooth-sub32'
    variant_label = 'Repair 32px envelope'
    keyshape = Keyshape.VRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'networks'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        short_axis = 16
        short_half_span = 12
        (short_low, short_high) = (short_axis - short_half_span, short_axis + short_half_span)
        self.add_line('p1-r1-1', (short_low, 11), (14, 16))
        self.add_contour('path-1-1', 'p1-r1-1', closed=False)
        self.add_line('p2-r1-1', (short_low, 21), (14, 16))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p3-r1-1', (14, 16), (short_high, 23))
        self.add_line('p3-r1-2', (short_high, 23), (14, 30))
        self.add_line('p3-r1-3', (14, 30), (14, 16))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', 'p3-r1-3', closed=False)
        self.add_line('p4-r1-1', (14, 16), (14, 2))
        self.add_line('p4-r1-2', (14, 2), (short_high, 9))
        self.add_line('p4-r1-3', (short_high, 9), (14, 16))
        self.add_contour('path-4-1', 'p4-r1-1', 'p4-r1-2', 'p4-r1-3', closed=False)
        self.relate('connect', 'p1-r1-1', 'p2-r1-1')
        self.relate('connect', 'p1-r1-1', 'p3-r1-1')
        self.relate('connect', 'p1-r1-1', 'p3-r1-3')
        self.relate('connect', 'p1-r1-1', 'p4-r1-1')
        self.relate('connect', 'p1-r1-1', 'p4-r1-3')
        self.relate('connect', 'p2-r1-1', 'p3-r1-1')
        self.relate('connect', 'p2-r1-1', 'p3-r1-3')
        self.relate('connect', 'p2-r1-1', 'p4-r1-1')
        self.relate('connect', 'p2-r1-1', 'p4-r1-3')
        self.relate('connect', 'p3-r1-1', 'p4-r1-1')
        self.relate('connect', 'p3-r1-1', 'p4-r1-3')
        self.relate('connect', 'p3-r1-3', 'p4-r1-1')
        self.relate('connect', 'p3-r1-3', 'p4-r1-3')
