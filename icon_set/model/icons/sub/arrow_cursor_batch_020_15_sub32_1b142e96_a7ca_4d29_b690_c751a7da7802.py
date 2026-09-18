"""Independent 32px profile of arrow-cursor-batch-020-15.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '1b142e96-a7ca-4d29-b690-c751a7da7802'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/cursor left 2_1b142e96-a7ca-4d29-b690-c751a7da7802.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('1b142e96-a7ca-4d29-b690-c751a7da7802', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/cursor left 2_1b142e96-a7ca-4d29-b690-c751a7da7802.svg'),)
PROFILE_SOURCE_KEYS = ('solo/arrow-cursor-batch-020-15',)
SOLO_SOURCE_ICON_IDS = ('arrow-cursor-batch-020-15',)
REFERENCE_EXPORT_SHA256 = '7aba1b24d85456c2b09ab7b5dcea534f1ab71d99c2828dcbfaccaf2a2d903495'

class Drawing(Sub32):
    icon_id = 'arrow-cursor-batch-020-15-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'objects'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (2, 2), (30, 11))
        self.add_line('p1-r1-2', (30, 11), (21, 16))
        self.add_line('p1-r1-3', (21, 16), (30, 25))
        self.add_line('p1-r1-4', (30, 25), (25, 30))
        self.add_line('p1-r1-5', (25, 30), (16, 21))
        self.add_line('p1-r1-6', (16, 21), (11, 30))
        self.add_line('p1-r1-7', (11, 30), (2, 2))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', closed=False)
