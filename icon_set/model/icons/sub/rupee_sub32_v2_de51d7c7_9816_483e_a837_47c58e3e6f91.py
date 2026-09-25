"""Independent 32px profile of rupee.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = 'de51d7c7-9816-483e-a837-47c58e3e6f91'
SOURCE_PATH = 'pictographic-primitives/money/rupee_de51d7c7-9816-483e-a837-47c58e3e6f91.svg'
AUTHOR = 'gpt-6'
SOURCE_PARTS = ('two horizontal bars', 'rupee hook', 'descending diagonal')
REPAIR_PLAN = {'concept': 'Indian Rupee Currency Symbol', 'core_parts': ('two horizontal bars', 'rupee hook', 'descending diagonal'), 'flexible_parts': 'minor keyshape fit', 'ladder': 'Corrected VRECT_XL bounds and stroke spacing'}
SOURCE_REFERENCES = (('de51d7c7-9816-483e-a837-47c58e3e6f91', 'pictographic-primitives/money/rupee_de51d7c7-9816-483e-a837-47c58e3e6f91.svg'),)
PROFILE_SOURCE_KEYS = ('solo/rupee',)
SOLO_SOURCE_ICON_IDS = ('rupee',)
REFERENCE_EXPORT_SHA256 = 'd536f4e4b92b12d08bb5b92748218d185264fe9015b95befd0da3660c8abd9fc'

class DrawingVariant2(Sub32):
    icon_id = 'rupee-sub32-v2'
    variant_label = 'Complete source with corrected 32px geometry'
    keyshape = Keyshape.VRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'money'
    categories = ('money', 'state')
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_arc('p1-r1-1', (4, 17), (17, 15), radius_x=22, radius_y=22, large_arc=False, sweep=False)
        self.add_arc('p1-r1-2', (17, 15), (20, 10), radius_x=8, radius_y=8, large_arc=False, sweep=False)
        self.add_line('p1-r1-3', (20, 10), (28, 10))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', closed=False)
        self.add_line('p2-r1-1', (28, 2), (6, 2))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p3-r1-1', (15, 2), (19, 6))
        self.add_line('p3-r1-2', (19, 6), (20, 10))
        self.add_line('p3-r1-3', (20, 10), (4, 10))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', 'p3-r1-3', closed=False)
        self.add_line('p4-r1-1', (19, 30), (4, 17))
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
        self.relate('connect', 'p1-r1-1', 'p4-r1-1')
        self.relate('connect', 'p1-r1-2', 'p3-r1-2')
        self.relate('connect', 'p1-r1-2', 'p3-r1-3')
        self.relate('connect', 'p1-r1-3', 'p3-r1-2')
        self.relate('connect', 'p1-r1-3', 'p3-r1-3')
