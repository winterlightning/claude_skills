"""Independent 32px profile of geometric-three-toed-paw.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '52860099-ee8d-46b2-84ff-237a2c5f681c'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/paw print_52860099-ee8d-46b2-84ff-237a2c5f681c.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('52860099-ee8d-46b2-84ff-237a2c5f681c', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/paw print_52860099-ee8d-46b2-84ff-237a2c5f681c.svg'),)
PROFILE_SOURCE_KEYS = ('solo/geometric-three-toed-paw',)
SOLO_SOURCE_ICON_IDS = ('geometric-three-toed-paw',)
REFERENCE_EXPORT_SHA256 = '39b268cd29b8fe180b12d9648e587752d662b0b77bb4626884bab91668a81a4f'

class Drawing(Sub32):
    icon_id = 'geometric-three-toed-paw-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'objects/container-components'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_arc('p1-r1-1', (13, 5), (16, 2), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_arc('p1-r1-2', (16, 2), (19, 5), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_arc('p1-r1-3', (19, 5), (16, 8), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_arc('p1-r1-4', (16, 8), (13, 5), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', closed=False)
        self.add_arc('p2-r1-1', (2, 14), (5, 11), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_arc('p2-r1-2', (5, 11), (8, 14), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_arc('p2-r1-3', (8, 14), (5, 18), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_bezier('p2-r1-4', (5, 18), ((4, 18), (3, 17), (3, 17)))
        self.add_bezier('p2-r1-5', (3, 17), ((2, 16), (2, 15), (2, 14)))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', 'p2-r1-5', closed=False)
        self.add_arc('p3-r1-1', (24, 14), (27, 11), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_arc('p3-r1-2', (27, 11), (30, 14), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_bezier('p3-r1-3', (30, 14), ((30, 15), (30, 16), (29, 17)))
        self.add_bezier('p3-r1-4', (29, 17), ((29, 17), (28, 18), (27, 18)))
        self.add_arc('p3-r1-5', (27, 18), (24, 14), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', 'p3-r1-3', 'p3-r1-4', 'p3-r1-5', closed=False)
        self.add_line('p4-r1-1', (16, 18), (7, 30))
        self.add_line('p4-r1-2', (7, 30), (25, 30))
        self.add_line('p4-r1-3', (25, 30), (16, 18))
        self.add_contour('path-4-1', 'p4-r1-1', 'p4-r1-2', 'p4-r1-3', closed=False)
