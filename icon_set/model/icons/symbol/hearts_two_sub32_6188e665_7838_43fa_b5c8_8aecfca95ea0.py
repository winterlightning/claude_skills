"""Independent 32px profile of hearts-two.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = '6188e665-7838-43fa-b5c8-8aecfca95ea0'
SOURCE_PATH = 'pictographic-primitives/symbol/three hearts_6188e665-7838-43fa-b5c8-8aecfca95ea0.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('6188e665-7838-43fa-b5c8-8aecfca95ea0', 'pictographic-primitives/symbol/three hearts_6188e665-7838-43fa-b5c8-8aecfca95ea0.svg'), ('76a3aff2-7ce1-498f-ac39-f41016299ef6', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/heart and hook_76a3aff2-7ce1-498f-ac39-f41016299ef6.svg'))
PROFILE_SOURCE_KEYS = ('solo/hearts-two',)
SOLO_SOURCE_ICON_IDS = ('hearts-two',)
REFERENCE_EXPORT_SHA256 = 'd408f25c383ec471baf828ab37194cc4b23c104e28e2f454b338d53a6a0cd02e'

class Drawing(Sub32):
    icon_id = 'hearts-two-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'symbol'
    categories = ('symbol',)
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        # Two hearts: a full heart in front (top right) and the heart behind it showing its left lobe, side and tip, 4 units clear of the front heart.
        self.add_arc('front-1', (10, 7), (20, 7), radius_x=5, radius_y=5, large_arc=False, sweep=True)
        self.add_arc('front-2', (20, 7), (30, 7), radius_x=5, radius_y=5, large_arc=False, sweep=True)
        self.add_line('front-3', (30, 7), (20, 21))
        self.add_line('front-4', (20, 21), (10, 7))
        self.add_contour('front', 'front-1', 'front-2', 'front-3', 'front-4', closed=True)
        self.add_arc('back-1', (3, 13), (2, 16), radius_x=5, radius_y=5, large_arc=False, sweep=False)
        self.add_line('back-2', (2, 16), (12, 30))
        self.add_line('back-3', (12, 30), (14, 27))
        self.add_contour('back', 'back-1', 'back-2', 'back-3')
