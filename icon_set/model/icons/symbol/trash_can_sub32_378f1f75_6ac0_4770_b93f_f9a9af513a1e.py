"""Independent 32px profile of trash-can.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = '378f1f75-6ac0-4770-b93f-f9a9af513a1e'
SOURCE_PATH = 'pictographic-primitives/symbol/trash_378f1f75-6ac0-4770-b93f-f9a9af513a1e.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('378f1f75-6ac0-4770-b93f-f9a9af513a1e', 'pictographic-primitives/symbol/trash_378f1f75-6ac0-4770-b93f-f9a9af513a1e.svg'),)
PROFILE_SOURCE_KEYS = ('solo/trash-can',)
SOLO_SOURCE_ICON_IDS = ('trash-can',)
REFERENCE_EXPORT_SHA256 = 'd5d2eb7e84014e9c7a9022175cf3f110a0efbe6ce7e8caebcd858ee66bad37d2'

class Drawing(Sub32):
    icon_id = 'trash-can-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'objects/symbols'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (2, 8), (5, 8))
        self.add_line('p1-r1-2', (5, 8), (8, 8))
        self.add_line('p1-r1-3', (8, 8), (24, 8))
        self.add_line('p1-r1-4', (24, 8), (27, 8))
        self.add_line('p1-r1-5', (27, 8), (30, 8))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', closed=False)
        self.add_arc('p2-r1-1', (8, 8), (24, 8), radius_x=8, radius_y=6, large_arc=False, sweep=True)
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p3-r1-1', (5, 8), (7, 25))
        self.add_line('p3-r1-2', (7, 25), (10, 30))
        self.add_line('p3-r1-3', (10, 30), (22, 30))
        self.add_line('p3-r1-4', (22, 30), (25, 25))
        self.add_line('p3-r1-5', (25, 25), (27, 8))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', 'p3-r1-3', 'p3-r1-4', 'p3-r1-5', closed=False)
        self.add_line('p4-r1-1', (16, 16), (16, 22))
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
        self.relate('connect', 'p1-r1-1', 'p3-r1-1')
        self.relate('connect', 'p1-r1-2', 'p2-r1-1')
        self.relate('connect', 'p1-r1-2', 'p3-r1-1')
        self.relate('connect', 'p1-r1-3', 'p2-r1-1')
        self.relate('connect', 'p1-r1-4', 'p2-r1-1')
        self.relate('connect', 'p1-r1-4', 'p3-r1-5')
        self.relate('connect', 'p1-r1-5', 'p3-r1-5')
