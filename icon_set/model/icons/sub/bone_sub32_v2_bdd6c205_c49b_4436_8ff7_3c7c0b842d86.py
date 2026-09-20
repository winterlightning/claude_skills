# Independent repair; parent preserved.
"""Independent 32px profile of bone.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = 'bdd6c205-c49b-4436-8ff7-3c7c0b842d86'
SOURCE_PATH = 'pictographic-primitives/symbol/bone_bdd6c205-c49b-4436-8ff7-3c7c0b842d86.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('bdd6c205-c49b-4436-8ff7-3c7c0b842d86', 'pictographic-primitives/symbol/bone_bdd6c205-c49b-4436-8ff7-3c7c0b842d86.svg'),)
PROFILE_SOURCE_KEYS = ('solo/bone',)
SOLO_SOURCE_ICON_IDS = ('bone',)
REFERENCE_EXPORT_SHA256 = 'b4447a8b1a1e7ec2fe4ad116519564eedeffd318035e6b576692675799e1e30b'

class RepairVariant(Sub32):
    variant_label = 'Centerline and source fidelity repair'
    variant_of = 'bone-sub32'
    icon_id = 'bone-sub32-v2'
    keyshape = Keyshape.HRECT_M
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'symbol'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_bezier('p1-r1-1', (9, 12), ((9, 10), (8, 8), (6, 8)))
        self.add_bezier('p1-r1-2', (6, 8), ((3, 8), (2, 9), (2, 11)))
        self.add_bezier('p1-r1-3', (2, 11), ((2, 14), (4, 14), (4, 16)))
        self.add_bezier('p1-r1-4', (4, 16), ((4, 18), (2, 18), (2, 21)))
        self.add_bezier('p1-r1-5', (2, 21), ((2, 23), (3, 24), (6, 24)))
        self.add_bezier('p1-r1-6', (6, 24), ((8, 24), (9, 22), (9, 20)))
        self.add_line('p1-r1-7', (9, 20), (23, 20))
        self.add_bezier('p1-r1-8', (23, 20), ((23, 22), (24, 24), (26, 24)))
        self.add_bezier('p1-r1-9', (26, 24), ((29, 24), (30, 23), (30, 21)))
        self.add_bezier('p1-r1-10', (30, 21), ((30, 18), (28, 18), (28, 16)))
        self.add_bezier('p1-r1-11', (28, 16), ((28, 14), (30, 14), (30, 11)))
        self.add_bezier('p1-r1-12', (30, 11), ((30, 9), (29, 8), (26, 8)))
        self.add_bezier('p1-r1-13', (26, 8), ((24, 8), (23, 10), (23, 12)))
        self.add_line('p1-r1-14', (23, 12), (9, 12))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', 'p1-r1-8', 'p1-r1-9', 'p1-r1-10', 'p1-r1-11', 'p1-r1-12', 'p1-r1-13', 'p1-r1-14', closed=False)
REPAIR_PLAN = 'Widen bone shaft symmetrically to eight units; retain four round lobes.'
CONSTRUCTION_REFERENCE = 'bone'
