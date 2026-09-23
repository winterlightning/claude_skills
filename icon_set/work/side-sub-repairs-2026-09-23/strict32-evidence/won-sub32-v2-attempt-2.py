"""Independent 32px profile of won.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '18f047b9-f81e-571a-a3ea-2c4af962bcb7'
SOURCE_PATH = 'pictographic-primitives/money/won_18f047b9-f81e-571a-a3ea-2c4af962bcb7.svg'
AUTHOR = 'gpt-6'
SOURCE_PARTS = ('W strokes', 'horizontal bar')
REPAIR_PLAN = {'concept': 'won', 'core_parts': ('W strokes', 'horizontal bar'), 'flexible_parts': 'Only minor curves and spacing may be simplified for 32px clearance', 'ladder': 'Rebalance and redraw on the strict SUB32 canvas'}

SOURCE_REFERENCES = (('18f047b9-f81e-571a-a3ea-2c4af962bcb7', 'pictographic-primitives/money/won_18f047b9-f81e-571a-a3ea-2c4af962bcb7.svg'),)
PROFILE_SOURCE_KEYS = ('solo/won',)
SOLO_SOURCE_ICON_IDS = ('won',)
REFERENCE_EXPORT_SHA256 = 'de0fbfba3c299a969fc32ad65dc01421b6802e8876ad59f63f4e61aaf4b08c9c'

class DrawingVariant2(Sub32):
    icon_id = 'won-sub32-v2'
    variant_of = 'won-sub32'
    variant_label = "Strict 32x32 repair draft"
    keyshape = Keyshape.HRECT_XL
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'money'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (30, 4), (24, 28))
        self.add_line('p1-r1-2', (24, 28), (16, 4))
        self.add_line('p1-r1-3', (16, 4), (8, 28))
        self.add_line('p1-r1-4', (8, 28), (2, 4))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', closed=False)
        self.add_line('p2-r1-1', (30, 20), (2, 20))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
