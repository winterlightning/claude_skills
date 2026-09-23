"""Independent 32px profile of kips.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = '53a2b4a3-1baf-47dc-a7f6-5760e32d3d59'
SOURCE_PATH = 'pictographic-primitives/money/kips_53a2b4a3-1baf-47dc-a7f6-5760e32d3d59.svg'
AUTHOR = 'gpt-6'
SOURCE_PARTS = ('upright K stem', 'middle bar', 'upper and lower diagonals')
REPAIR_PLAN = {'concept': 'Kip Unit Measurement Symbol', 'core_parts': ('upright K stem', 'middle bar', 'upper and lower diagonals'), 'flexible_parts': 'minor keyshape fit', 'ladder': 'Corrected VRECT_XL bounds while preserving the kip symbol'}
SOURCE_REFERENCES = (('53a2b4a3-1baf-47dc-a7f6-5760e32d3d59', 'pictographic-primitives/money/kips_53a2b4a3-1baf-47dc-a7f6-5760e32d3d59.svg'),)
PROFILE_SOURCE_KEYS = ('solo/kips',)
SOLO_SOURCE_ICON_IDS = ('kips',)
REFERENCE_EXPORT_SHA256 = '82cb25dba3107a4eb4ff98100e292dc7d27f165f3e51479e119c93d7391716e9'

class DrawingVariant2(Sub32):
    icon_id = 'kips-sub32-v2'
    variant_of = 'kips-sub32'
    variant_label = 'Complete source with corrected 32px geometry'
    keyshape = Keyshape.VRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'money'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (26, 16), (4, 16))
        self.add_contour('path-1-1', 'p1-r1-1', closed=False)
        self.add_line('p2-r1-1', (28, 30), (14, 16))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p3-r1-1', (26, 3), (14, 16))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_line('p4-r1-1', (10, 2), (10, 30))
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
        self.relate('connect', 'p2-r1-1', 'p3-r1-1')
