"""Independent 32px profile of liras.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = '986af714-6fb8-449a-ad31-d5271f278137'
SOURCE_PATH = 'pictographic-primitives/money/liras_986af714-6fb8-449a-ad31-d5271f278137.svg'
AUTHOR = 'gpt-6'
SOURCE_PARTS = ('sterling curve', 'two crossbars', 'baseline')
REPAIR_PLAN = {'concept': 'Pound Sterling Currency Symbol', 'core_parts': ('sterling curve', 'two crossbars', 'baseline'), 'flexible_parts': 'minor keyshape fit', 'ladder': 'Corrected VRECT_XL bounds while preserving the sterling mark'}
SOURCE_REFERENCES = (('986af714-6fb8-449a-ad31-d5271f278137', 'pictographic-primitives/money/liras_986af714-6fb8-449a-ad31-d5271f278137.svg'),)
PROFILE_SOURCE_KEYS = ('solo/liras',)
SOLO_SOURCE_ICON_IDS = ('liras',)
REFERENCE_EXPORT_SHA256 = 'e40bd69750f4eb3147f9a383eb2bc20ab3339d4b8dabc691afe542e24fafce2a'

class DrawingVariant2(Sub32):
    icon_id = 'liras-sub32-v2'
    variant_label = 'Complete source with corrected 32px geometry'
    keyshape = Keyshape.VRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'money'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_bezier('p1-r1-1', (28, 8), ((28, 4), (24, 2), (20, 2)))
        self.add_bezier('p1-r1-2', (20, 2), ((15, 2), (12, 4), (12, 8)))
        self.add_line('p1-r1-3', (12, 8), (12, 23))
        self.add_bezier('p1-r1-4', (12, 23), ((12, 27), (9, 30), (4, 30)))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', closed=False)
        self.add_line('p2-r1-1', (4, 30), (28, 30))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p3-r1-1', (6, 13), (20, 13))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_line('p4-r1-1', (6, 22), (20, 22))
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
        self.relate('connect', 'p1-r1-4', 'p2-r1-1')
