# Independent repair; parent preserved.
"""Independent 32px profile of child-face.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = '2126ca4d-f169-4065-8484-6a0bfd33fcd9'
SOURCE_PATH = 'pictographic-primitives/symbol/spicy head_2126ca4d-f169-4065-8484-6a0bfd33fcd9.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('2126ca4d-f169-4065-8484-6a0bfd33fcd9', 'pictographic-primitives/symbol/spicy head_2126ca4d-f169-4065-8484-6a0bfd33fcd9.svg'),)
PROFILE_SOURCE_KEYS = ('solo/child-face',)
SOLO_SOURCE_ICON_IDS = ('child-face',)
REFERENCE_EXPORT_SHA256 = '51c8125f9945ad93db6dfb25f2b1c0509a9a0671e06974d88073ca84698a9b13'

class RepairVariant(Sub32):
    variant_label = 'Centerline and source fidelity repair'
    icon_id = 'child-face-sub32-v2'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'symbol'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_arc('p1-r1-1', (2, 16), (30, 16), radius_x=14, radius_y=14, large_arc=False, sweep=True)
        self.add_arc('p1-r1-2', (30, 16), (2, 16), radius_x=14, radius_y=14, large_arc=False, sweep=True)
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', closed=False)
        self.add_arc('p2-r1-1', (2, 16), (19, 7), radius_x=17, radius_y=17, large_arc=False, sweep=False)
        self.add_arc('p2-r1-2', (19, 7), (30, 16), radius_x=13, radius_y=13, large_arc=False, sweep=False)
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', closed=False)
        self.add_line('p3-r1-1', (11, 22), (13, 23))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_line('p4-r1-1', (19, 23), (20, 22))
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
        self.relate('connect', 'p1-r1-1', 'p2-r1-1')
        self.relate('connect', 'p1-r1-1', 'p2-r1-2')
        self.relate('connect', 'p1-r1-2', 'p2-r1-1')
        self.relate('connect', 'p1-r1-2', 'p2-r1-2')
REPAIR_PLAN = 'Rebalance hair crest and short eye marks; circular head and original parts retained.'
CONSTRUCTION_REFERENCE = 'baby'
