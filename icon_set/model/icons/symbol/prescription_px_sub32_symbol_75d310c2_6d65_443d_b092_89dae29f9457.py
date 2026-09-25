"""Independent 32px profile of prescription-px.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = '75d310c2-6d65-443d-b092-89dae29f9457'
SOURCE_PATH = 'pictographic-primitives/health/prescription px_75d310c2-6d65-443d-b092-89dae29f9457.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('75d310c2-6d65-443d-b092-89dae29f9457', 'pictographic-primitives/health/prescription px_75d310c2-6d65-443d-b092-89dae29f9457.svg'),)
PROFILE_SOURCE_KEYS = ('solo/prescription-px',)
SOLO_SOURCE_ICON_IDS = ('prescription-px',)
REFERENCE_EXPORT_SHA256 = 'bc4bb7535cfbc24db8f065e65ca4baffab987de25ff769d0bb1fcc5995da839f'

class DrawingContainerSymbol(Sub32):
    icon_id = 'prescription-px-sub32-symbol'
    related_origin_icon_id = 'prescription-px-sub32'
    variant_label = 'Independent container symbol'
    usage_category = 'symbol'
    related_group = 'sub-origin/prescription-px-sub32'
    counterpart_icon_id = 'prescription-px-sub32'
    keyshape = Keyshape.VRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'health'
    categories = ('health', 'state')
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (5, 25), (5, 2))
        self.add_line('p1-r1-2', (5, 2), (14, 2))
        self.add_arc('p1-r1-3', (14, 2), (19, 5), radius_x=6, radius_y=6, large_arc=False, sweep=True)
        self.add_arc('p1-r1-4', (19, 5), (14, 14), radius_x=6, radius_y=6, large_arc=False, sweep=True)
        self.add_line('p1-r1-5', (14, 14), (5, 14))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', closed=False)
        self.add_line('p2-r1-1', (14, 30), (21, 24))
        self.add_line('p2-r1-2', (21, 24), (27, 30))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', closed=False)
        self.add_line('p3-r1-1', (27, 17), (21, 24))
        self.add_line('p3-r1-2', (21, 24), (11, 14))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', closed=False)
        self.relate('connect', 'p2-r1-1', 'p3-r1-1')
        self.relate('connect', 'p2-r1-1', 'p3-r1-2')
        self.relate('connect', 'p2-r1-2', 'p3-r1-1')
        self.relate('connect', 'p2-r1-2', 'p3-r1-2')
