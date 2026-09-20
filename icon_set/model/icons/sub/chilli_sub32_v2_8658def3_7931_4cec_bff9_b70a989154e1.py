# Independent repair; parent preserved.
"""Independent 32px profile of chilli.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = '8658def3-7931-4cec-bff9-b70a989154e1'
SOURCE_PATH = 'pictographic-primitives/symbol/chilli_8658def3-7931-4cec-bff9-b70a989154e1.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('8658def3-7931-4cec-bff9-b70a989154e1', 'pictographic-primitives/symbol/chilli_8658def3-7931-4cec-bff9-b70a989154e1.svg'),)
PROFILE_SOURCE_KEYS = ('solo/chilli',)
SOLO_SOURCE_ICON_IDS = ('chilli',)
REFERENCE_EXPORT_SHA256 = 'e38aa7e61051b5c25c0f65421c0853c0d50362b6ce2d9bd3fe13b1c6c772f65b'

class RepairVariant(Sub32):
    variant_label = 'Centerline and source fidelity repair'
    variant_of = 'chilli-sub32'
    icon_id = 'chilli-sub32-v2'
    keyshape = Keyshape.HRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'symbol'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_bezier('p1-r1-1', (2, 16), ((4, 16), (5, 17), (7, 17)))
        self.add_bezier('p1-r1-2', (7, 17), ((15, 17), (21, 10), (25, 10)))
        self.add_bezier('p1-r1-4', (25, 10), ((26, 10), (27, 11), (27, 13)))
        self.add_bezier('p1-r1-5', (27, 13), ((27, 14), (28, 15), (28, 16)))
        self.add_bezier('p1-r1-6', (28, 16), ((28, 21), (22, 28), (15, 28)))
        self.add_bezier('p1-r1-7', (15, 28), ((8, 28), (4, 21), (2, 16)))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', closed=False)
        self.add_bezier('p2-r1-1', (27, 13), ((29, 12), (30, 10), (30, 8)))
        self.add_bezier('p2-r1-2', (30, 8), ((30, 6), (29, 4), (27, 4)))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', closed=False)
        self.relate('connect', 'p1-r1-4', 'p2-r1-1')
        self.relate('connect', 'p1-r1-5', 'p2-r1-1')
REPAIR_PLAN = 'Restore exact top and bottom envelope, align stalk junction tangent.'
CONSTRUCTION_REFERENCE = 'none'
