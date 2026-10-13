"""Independent 32px profile of geometric-three-toed-paw.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = '52860099-ee8d-46b2-84ff-237a2c5f681c'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/paw print_52860099-ee8d-46b2-84ff-237a2c5f681c.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('52860099-ee8d-46b2-84ff-237a2c5f681c', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/paw print_52860099-ee8d-46b2-84ff-237a2c5f681c.svg'),)
PROFILE_SOURCE_KEYS = ('solo/geometric-three-toed-paw',)
SOLO_SOURCE_ICON_IDS = ('geometric-three-toed-paw',)
REFERENCE_EXPORT_SHA256 = '39b268cd29b8fe180b12d9648e587752d662b0b77bb4626884bab91668a81a4f'

class DrawingContainerSymbol(Sub32):
    icon_id = 'geometric-three-toed-paw-sub32-symbol'
    related_origin_icon_id = 'geometric-three-toed-paw-sub32'
    variant_label = 'Independent container symbol'
    usage_category = 'symbol'
    related_group = 'sub-origin/geometric-three-toed-paw-sub32'
    counterpart_icon_id = 'geometric-three-toed-paw-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives-generate'
    categories = ('symbol', 'state', 'other', 'primitives-generate')
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_arc('p1-r1-1', (13, 5), (16, 2), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_arc('p1-r1-2', (16, 2), (19, 5), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_arc('p1-r1-3', (19, 5), (16, 8), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_arc('p1-r1-4', (16, 8), (13, 5), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', closed=False)
        self.add_arc('p2-r1-1', (2, 16), (5, 13), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_arc('p2-r1-2', (5, 13), (8, 16), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_arc('p2-r1-3', (8, 16), (5, 20), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_bezier('p2-r1-4', (5, 20), ((4, 20), (3, 19), (3, 19)))
        self.add_bezier('p2-r1-5', (3, 19), ((2, 18), (2, 17), (2, 16)))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', 'p2-r1-5', closed=False)
        self.add_arc('p3-r1-1', (24, 16), (27, 13), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_arc('p3-r1-2', (27, 13), (30, 16), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_bezier('p3-r1-3', (30, 16), ((30, 17), (30, 18), (29, 19)))
        self.add_bezier('p3-r1-4', (29, 19), ((29, 19), (28, 20), (27, 20)))
        self.add_arc('p3-r1-5', (27, 20), (24, 16), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', 'p3-r1-3', 'p3-r1-4', 'p3-r1-5', closed=False)
        self.add_line('p4-r1-1', (16, 21), (9, 30))
        self.add_line('p4-r1-2', (9, 30), (23, 30))
        self.add_line('p4-r1-3', (23, 30), (16, 21))
        self.add_contour('path-4-1', 'p4-r1-1', 'p4-r1-2', 'p4-r1-3', closed=False)
