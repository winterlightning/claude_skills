"""Independent 32px profile of prescription-px.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = '75d310c2-6d65-443d-b092-89dae29f9457'
SOURCE_PATH = 'pictographic-primitives/health/prescription px_75d310c2-6d65-443d-b092-89dae29f9457.svg'
AUTHOR = 'gpt-6'
SOURCE_PARTS = ('Rx upright and rounded bowl', 'crossed prescription diagonals')
REPAIR_PLAN = {'concept': 'Medical Prescription Symbol', 'core_parts': ('Rx upright and rounded bowl', 'crossed prescription diagonals'), 'flexible_parts': 'minor keyshape fit', 'ladder': 'Corrected VRECT_XL bounds while preserving the Rx glyph'}
SOURCE_REFERENCES = (('75d310c2-6d65-443d-b092-89dae29f9457', 'pictographic-primitives/health/prescription px_75d310c2-6d65-443d-b092-89dae29f9457.svg'),)
PROFILE_SOURCE_KEYS = ('solo/prescription-px',)
SOLO_SOURCE_ICON_IDS = ('prescription-px',)
REFERENCE_EXPORT_SHA256 = 'bc4bb7535cfbc24db8f065e65ca4baffab987de25ff769d0bb1fcc5995da839f'

class DrawingVariant2(Sub32):
    icon_id = 'prescription-px-sub32-v2'
    variant_label = 'Complete source with corrected 32px geometry'
    keyshape = Keyshape.VRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'health'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (4, 25), (4, 2))
        self.add_line('p1-r1-2', (4, 2), (14, 2))
        self.add_arc('p1-r1-3', (14, 2), (19, 5), radius_x=6, radius_y=6, large_arc=False, sweep=True)
        self.add_arc('p1-r1-4', (19, 5), (14, 14), radius_x=6, radius_y=6, large_arc=False, sweep=True)
        self.add_line('p1-r1-5', (14, 14), (4, 14))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', closed=False)
        self.add_line('p2-r1-1', (14, 30), (21, 24))
        self.add_line('p2-r1-2', (21, 24), (28, 30))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', closed=False)
        self.add_line('p3-r1-1', (28, 17), (21, 24))
        self.add_line('p3-r1-2', (21, 24), (11, 14))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', closed=False)
        self.relate('connect', 'p2-r1-1', 'p3-r1-1')
        self.relate('connect', 'p2-r1-1', 'p3-r1-2')
        self.relate('connect', 'p2-r1-2', 'p3-r1-1')
        self.relate('connect', 'p2-r1-2', 'p3-r1-2')
