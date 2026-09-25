"""Independent 32px profile of cannabis-plant-leaf-symbol-solo-b003-01.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '8be10246-6ae7-43c7-bc9e-c25a3d070fe3'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/cannabis/cannabis_8be10246-6ae7-43c7-bc9e-c25a3d070fe3.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('8be10246-6ae7-43c7-bc9e-c25a3d070fe3', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/cannabis/cannabis_8be10246-6ae7-43c7-bc9e-c25a3d070fe3.svg'),)
PROFILE_SOURCE_KEYS = ('solo/cannabis-plant-leaf-symbol-solo-b003-01',)
SOLO_SOURCE_ICON_IDS = ('cannabis-plant-leaf-symbol-solo-b003-01',)
REFERENCE_EXPORT_SHA256 = 'c1c338e378b8764f30dd0092cef2bf98454dd40f047c736f75bd8bdd5b340b26'

class Drawing(Sub32):
    icon_id = 'cannabis-plant-leaf-symbol-solo-b003-01-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'cannabis'
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
        self.add_line('p2-r1-1', (16, 24), (16, 30))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.relate("connect", 'p1-r1-6', 'p2-r1-1')
        self.relate("connect", 'p1-r1-7', 'p2-r1-1')
