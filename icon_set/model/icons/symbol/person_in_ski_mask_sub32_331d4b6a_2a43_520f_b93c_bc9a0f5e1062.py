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
    category = 'crime'
    categories = ('crime', 'primitives')
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        # Person in a ski mask: hooded head, one round eye opening, a mouth slit.
        self.add_line('m-1', (4, 30), (4, 14))
        self.add_arc('m-2', (4, 14), (28, 14), radius_x=12, radius_y=12, large_arc=False, sweep=True)
        self.add_line('m-3', (28, 14), (28, 30))
        self.add_contour('mask', 'm-1', 'm-2', 'm-3')
        self.add_arc('eye-1', (12, 14), (20, 14), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_arc('eye-2', (20, 14), (12, 14), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_contour('eyes', 'eye-1', 'eye-2', closed=True)
        self.add_line('mouth', (14, 26), (18, 26))
