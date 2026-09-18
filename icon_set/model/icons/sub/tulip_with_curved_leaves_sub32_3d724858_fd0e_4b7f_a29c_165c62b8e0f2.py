"""Independent 32px profile of tulip-with-curved-leaves.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '3d724858-fd0e-4b7f-a29c-165c62b8e0f2'
SOURCE_PATH = 'pictographic-primitives/nature/flower_3d724858-fd0e-4b7f-a29c-165c62b8e0f2.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('3d724858-fd0e-4b7f-a29c-165c62b8e0f2', 'pictographic-primitives/nature/flower_3d724858-fd0e-4b7f-a29c-165c62b8e0f2.svg'), ('3e0aa5f5-7bc6-4864-acd6-4434c86246fe', 'pictographic-primitives/nature/flower_3e0aa5f5-7bc6-4864-acd6-4434c86246fe.svg'))
PROFILE_SOURCE_KEYS = ('solo/tulip-with-curved-leaves', 'solo/tulip-with-curved-leaves-alternate')
SOLO_SOURCE_ICON_IDS = ('tulip-with-curved-leaves', 'tulip-with-curved-leaves-alternate')
REFERENCE_EXPORT_SHA256 = '4464cc32a8460746dc9d4f9a337855db876c96b747153fcec5d7c6e817cd92dc'

class Drawing(Sub32):
    icon_id = 'tulip-with-curved-leaves-sub32'
    keyshape = Keyshape.VRECT_XL
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'nature/batch-01'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (8, 10), (8, 2))
        self.add_line('p1-r1-2', (8, 2), (16, 8))
        self.add_line('p1-r1-3', (16, 8), (24, 2))
        self.add_line('p1-r1-4', (24, 2), (24, 10))
        self.add_arc('p1-r1-5', (24, 10), (16, 19), radius_x=8, radius_y=8, large_arc=False, sweep=True)
        self.add_arc('p1-r1-6', (16, 19), (8, 10), radius_x=8, radius_y=8, large_arc=False, sweep=True)
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', closed=False)
        self.add_line('p2-r1-1', (16, 19), (16, 30))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_arc('p3-r1-1', (5, 23), (16, 30), radius_x=11, radius_y=7, large_arc=False, sweep=True)
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_arc('p4-r1-1', (16, 30), (27, 23), radius_x=11, radius_y=7, large_arc=False, sweep=True)
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
        self.relate("connect", 'p1-r1-5', 'p2-r1-1')
        self.relate("connect", 'p1-r1-6', 'p2-r1-1')
        self.relate("connect", 'p2-r1-1', 'p3-r1-1')
        self.relate("connect", 'p2-r1-1', 'p4-r1-1')
        self.relate("connect", 'p3-r1-1', 'p4-r1-1')
