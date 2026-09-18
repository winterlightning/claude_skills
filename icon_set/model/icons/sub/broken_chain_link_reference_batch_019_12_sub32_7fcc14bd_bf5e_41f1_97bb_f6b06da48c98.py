"""Independent 32px profile of broken-chain-link-reference-batch-019-12.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '7fcc14bd-bf5e-41f1-97bb-f6b06da48c98'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/disconnect_7fcc14bd-bf5e-41f1-97bb-f6b06da48c98.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('7fcc14bd-bf5e-41f1-97bb-f6b06da48c98', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/disconnect_7fcc14bd-bf5e-41f1-97bb-f6b06da48c98.svg'),)
PROFILE_SOURCE_KEYS = ('solo/broken-chain-link-reference-batch-019-12',)
SOLO_SOURCE_ICON_IDS = ('broken-chain-link-reference-batch-019-12',)
REFERENCE_EXPORT_SHA256 = '3fa6d2713325b3262e53c246fd830b88d9224a1235cf27990b29cff86b44fecf'

class Drawing(Sub32):
    icon_id = 'broken-chain-link-reference-batch-019-12-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'objects'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (10, 16), (2, 24))
        self.add_line('p1-r1-2', (2, 24), (2, 27))
        self.add_line('p1-r1-3', (2, 27), (5, 30))
        self.add_line('p1-r1-4', (5, 30), (10, 30))
        self.add_line('p1-r1-5', (10, 30), (18, 22))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', closed=False)
        self.add_line('p2-r1-1', (16, 10), (24, 2))
        self.add_line('p2-r1-2', (24, 2), (27, 2))
        self.add_line('p2-r1-3', (27, 2), (30, 5))
        self.add_line('p2-r1-4', (30, 5), (30, 10))
        self.add_line('p2-r1-5', (30, 10), (22, 18))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', 'p2-r1-5', closed=False)
        self.add_line('p3-r1-1', (2, 10), (5, 10))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_line('p4-r1-1', (10, 2), (10, 5))
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
