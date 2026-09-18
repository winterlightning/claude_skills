"""Independent 32px profile of female-user-profile.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = 'b7558322-6681-447e-8b8a-0f4a588a3f0e'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/images/woman_b7558322-6681-447e-8b8a-0f4a588a3f0e.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('b7558322-6681-447e-8b8a-0f4a588a3f0e', '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/images/woman_b7558322-6681-447e-8b8a-0f4a588a3f0e.svg'),)
PROFILE_SOURCE_KEYS = ('solo/female-user-profile',)
SOLO_SOURCE_ICON_IDS = ('female-user-profile',)
REFERENCE_EXPORT_SHA256 = 'cdd959f1883528419a69f76da94dc1f58926781ccf68b19bd6e6a530f1de59f3'

class Drawing(Sub32):
    icon_id = 'female-user-profile-sub32'
    keyshape = Keyshape.VRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'objects/images'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_arc('p1-r1-1', (9, 9), (23, 9), radius_x=7, radius_y=7, large_arc=False, sweep=True)
        self.add_arc('p1-r1-2', (23, 9), (9, 9), radius_x=7, radius_y=7, large_arc=False, sweep=True)
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', closed=False)
        self.add_bezier('p2-r1-1', (9, 9), ((12, 9), (15, 8), (16, 6)))
        self.add_bezier('p2-r1-2', (16, 6), ((17, 8), (20, 9), (23, 9)))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', closed=False)
        self.add_arc('p3-r1-1', (5, 30), (16, 22), radius_x=11, radius_y=8, large_arc=False, sweep=True)
        self.add_arc('p3-r1-2', (16, 22), (27, 30), radius_x=11, radius_y=8, large_arc=False, sweep=True)
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', closed=False)
        self.relate('connect', 'p1-r1-1', 'p2-r1-1')
        self.relate('connect', 'p1-r1-1', 'p2-r1-2')
        self.relate('connect', 'p1-r1-2', 'p2-r1-1')
        self.relate('connect', 'p1-r1-2', 'p2-r1-2')
