"""Independent 32px profile of move-left.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = '04363f1e-1843-48d2-b5d7-1bcba7668a99'
SOURCE_PATH = 'pictographic-primitives/interface-essential/move left_04363f1e-1843-48d2-b5d7-1bcba7668a99.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('04363f1e-1843-48d2-b5d7-1bcba7668a99', 'pictographic-primitives/interface-essential/move left_04363f1e-1843-48d2-b5d7-1bcba7668a99.svg'),)
PROFILE_SOURCE_KEYS = ('solo/move-left',)
SOLO_SOURCE_ICON_IDS = ('move-left',)
REFERENCE_EXPORT_SHA256 = '20ba605ef448c8c995ffc7c9e10c9b3217959ee9693d49fbd6a30a86c3c79978'

class DrawingVariant2(Sub32):
    icon_id = 'move-left-sub32-v2'
    related_origin_icon_id = 'move-left-sub32'
    variant_label = 'Repair 32px envelope'
    keyshape = Keyshape.VRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'interface-essential'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        short_axis = 16
        short_half_span = 12
        short_low, short_high = (short_axis - short_half_span, short_axis + short_half_span)
        self.add_line('p1-r1-1', (short_low, 30), (short_low, 2))
        self.add_contour('path-1-1', 'p1-r1-1', closed=False)
        self.add_line('p2-r1-1', (13, 16), (short_high, 16))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p3-r1-1', (13, 16), (18, 22))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_line('p4-r1-1', (13, 16), (18, 10))
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
        self.relate('connect', 'p2-r1-1', 'p3-r1-1')
        self.relate('connect', 'p2-r1-1', 'p4-r1-1')
        self.relate('connect', 'p3-r1-1', 'p4-r1-1')
