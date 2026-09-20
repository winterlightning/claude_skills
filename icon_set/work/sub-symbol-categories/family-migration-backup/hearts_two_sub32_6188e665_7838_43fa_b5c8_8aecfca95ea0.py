"""Independent 32px profile of hearts-two.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

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
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'objects/symbols'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_arc('p1-r1-1', (14, 16), (2, 16), radius_x=6, radius_y=6, large_arc=False, sweep=False)
        self.add_arc('p1-r1-2', (2, 16), (7, 22), radius_x=9, radius_y=9, large_arc=False, sweep=False)
        self.add_line('p1-r1-3', (7, 22), (16, 30))
        self.add_line('p1-r1-4', (16, 30), (24, 22))
        self.add_arc('p1-r1-5', (24, 22), (25, 19), radius_x=9, radius_y=9, large_arc=False, sweep=False)
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', closed=False)
        self.add_arc('p2-r1-1', (24, 5), (18, 5), radius_x=3, radius_y=3, large_arc=False, sweep=False)
        self.add_line('p2-r1-2', (18, 5), (19, 8))
        self.add_line('p2-r1-3', (19, 8), (24, 13))
        self.add_line('p2-r1-4', (24, 13), (28, 8))
        self.add_line('p2-r1-5', (28, 8), (30, 5))
        self.add_arc('p2-r1-6', (30, 5), (24, 5), radius_x=3, radius_y=3, large_arc=False, sweep=False)
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', 'p2-r1-5', 'p2-r1-6', closed=False)
