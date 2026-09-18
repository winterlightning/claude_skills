"""Independent 32px profile of seven-pointed-cannabis-leaf-solo-b003-02.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '219ceabe-349a-4492-b9c9-eae240f9d5c9'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/cannabis/cannabis_219ceabe-349a-4492-b9c9-eae240f9d5c9.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('219ceabe-349a-4492-b9c9-eae240f9d5c9', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/cannabis/cannabis_219ceabe-349a-4492-b9c9-eae240f9d5c9.svg'),)
PROFILE_SOURCE_KEYS = ('solo/seven-pointed-cannabis-leaf-solo-b003-02',)
SOLO_SOURCE_ICON_IDS = ('seven-pointed-cannabis-leaf-solo-b003-02',)
REFERENCE_EXPORT_SHA256 = '5e7b84f622641b9283b7e8cd5b94507bf087955dfb0771cd57742899172a118d'

class Drawing(Sub32):
    icon_id = 'seven-pointed-cannabis-leaf-solo-b003-02-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'objects'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (16, 2), (21, 14))
        self.add_line('p1-r1-2', (21, 14), (28, 8))
        self.add_line('p1-r1-3', (28, 8), (24, 19))
        self.add_line('p1-r1-4', (24, 19), (30, 22))
        self.add_line('p1-r1-5', (30, 22), (22, 25))
        self.add_line('p1-r1-6', (22, 25), (16, 24))
        self.add_line('p1-r1-7', (16, 24), (10, 25))
        self.add_line('p1-r1-8', (10, 25), (2, 22))
        self.add_line('p1-r1-9', (2, 22), (8, 19))
        self.add_line('p1-r1-10', (8, 19), (4, 8))
        self.add_line('p1-r1-11', (4, 8), (11, 14))
        self.add_line('p1-r1-12', (11, 14), (16, 2))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', 'p1-r1-8', 'p1-r1-9', 'p1-r1-10', 'p1-r1-11', 'p1-r1-12', closed=False)
        self.add_line('p2-r1-1', (16, 24), (13, 30))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.relate("connect", 'p1-r1-6', 'p2-r1-1')
        self.relate("connect", 'p1-r1-7', 'p2-r1-1')
