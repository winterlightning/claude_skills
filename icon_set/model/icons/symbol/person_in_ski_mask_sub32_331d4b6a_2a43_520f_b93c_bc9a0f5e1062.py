"""Independent 32px profile of person-in-ski-mask.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = '331d4b6a-2a43-520f-b93c-bc9a0f5e1062'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/crime/tools criminal mask_331d4b6a-2a43-520f-b93c-bc9a0f5e1062.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('331d4b6a-2a43-520f-b93c-bc9a0f5e1062', '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/crime/tools criminal mask_331d4b6a-2a43-520f-b93c-bc9a0f5e1062.svg'), ('8a4bd6ce-492d-5b6a-a9ab-d8e814463361', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/criminal mask_8a4bd6ce-492d-5b6a-a9ab-d8e814463361.svg'))
PROFILE_SOURCE_KEYS = ('solo/person-in-ski-mask',)
SOLO_SOURCE_ICON_IDS = ('person-in-ski-mask',)
REFERENCE_EXPORT_SHA256 = 'df33f305561ba572d7f80e793823491af34e165cf8a2685bd93ca84d7d70b4a0'

class Drawing(Sub32):
    icon_id = 'person-in-ski-mask-sub32'
    keyshape = Keyshape.VRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'objects/crime'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_arc('p1-r1-1', (5, 30), (9, 26), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_line('p1-r1-2', (9, 26), (9, 24))
        self.add_arc('p1-r1-3', (9, 24), (5, 20), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_line('p1-r1-4', (5, 20), (5, 13))
        self.add_arc('p1-r1-5', (5, 13), (16, 2), radius_x=11, radius_y=11, large_arc=False, sweep=True)
        self.add_arc('p1-r1-6', (16, 2), (27, 13), radius_x=11, radius_y=11, large_arc=False, sweep=True)
        self.add_line('p1-r1-7', (27, 13), (27, 20))
        self.add_arc('p1-r1-8', (27, 20), (23, 24), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_line('p1-r1-9', (23, 24), (23, 26))
        self.add_arc('p1-r1-10', (23, 26), (27, 30), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', 'p1-r1-8', 'p1-r1-9', 'p1-r1-10', closed=False)
        self.add_line('p2-r1-1', (14, 9), (18, 9))
        self.add_arc('p2-r1-2', (18, 9), (18, 15), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('p2-r1-3', (18, 15), (14, 15))
        self.add_arc('p2-r1-4', (14, 15), (14, 9), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', closed=False)
        self.add_line('p3-r1-1', (15, 22), (17, 22))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
