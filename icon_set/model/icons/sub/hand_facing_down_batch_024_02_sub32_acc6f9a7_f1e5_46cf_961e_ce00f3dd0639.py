"""Independent 32px profile of hand-facing-down-batch-024-02.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = 'acc6f9a7-f1e5-46cf-961e-ce00f3dd0639'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/hand down_acc6f9a7-f1e5-46cf-961e-ce00f3dd0639.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('acc6f9a7-f1e5-46cf-961e-ce00f3dd0639', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/hand down_acc6f9a7-f1e5-46cf-961e-ce00f3dd0639.svg'),)
PROFILE_SOURCE_KEYS = ('solo/hand-facing-down-batch-024-02',)
SOLO_SOURCE_ICON_IDS = ('hand-facing-down-batch-024-02',)
REFERENCE_EXPORT_SHA256 = '4dddd68c6deae8b1da888156e045acf44bce0593d79272c733520d08034f8636'

class Drawing(Sub32):
    icon_id = 'hand-facing-down-batch-024-02-sub32'
    keyshape = Keyshape.HRECT_L
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'primitives-generate'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_bezier('p1-r1-1', (2, 10), ((3, 11), (3, 11), (4, 11)))
        self.add_bezier('p1-r1-2', (4, 11), ((10, 11), (12, 6), (16, 6)))
        self.add_bezier('p1-r1-3', (16, 6), ((20, 6), (24, 11), (29, 15)))
        self.add_bezier('p1-r1-4', (29, 15), ((29, 16), (30, 17), (30, 18)))
        self.add_bezier('p1-r1-5', (30, 18), ((30, 20), (29, 22), (27, 22)))
        self.add_bezier('p1-r1-6', (27, 22), ((26, 22), (25, 22), (24, 21)))
        self.add_line('p1-r1-7', (24, 21), (18, 16))
        self.add_bezier('p1-r1-8', (18, 16), ((16, 22), (13, 26), (9, 26)))
        self.add_line('p1-r1-9', (9, 26), (2, 24))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', 'p1-r1-8', 'p1-r1-9', closed=False)
