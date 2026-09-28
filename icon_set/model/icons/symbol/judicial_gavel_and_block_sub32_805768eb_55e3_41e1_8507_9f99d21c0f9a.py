"""Independent 32px profile of judicial-gavel-and-block.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = '805768eb-55e3-41e1-8507-9f99d21c0f9a'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/judge_805768eb-55e3-41e1-8507-9f99d21c0f9a.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('805768eb-55e3-41e1-8507-9f99d21c0f9a', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/judge_805768eb-55e3-41e1-8507-9f99d21c0f9a.svg'),)
PROFILE_SOURCE_KEYS = ('solo/judicial-gavel-and-block',)
SOLO_SOURCE_ICON_IDS = ('judicial-gavel-and-block',)
REFERENCE_EXPORT_SHA256 = '2079fa264414f5d54cf86309d12e6d3db75d53b1ed5ffe2232831777e539cead'

class Drawing(Sub32):
    icon_id = 'judicial-gavel-and-block-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives-generate'
    categories = ('symbol', 'other', 'primitives-generate')
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (2, 11), (11, 2))
        self.add_line('p1-r1-2', (11, 2), (21, 11))
        self.add_line('p1-r1-3', (21, 11), (16, 16))
        self.add_line('p1-r1-4', (16, 16), (11, 21))
        self.add_line('p1-r1-5', (11, 21), (2, 11))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', closed=False)
        self.add_line('p2-r1-1', (16, 16), (30, 30))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p3-r1-1', (2, 30), (2, 27))
        self.add_line('p3-r1-2', (2, 27), (13, 27))
        self.add_line('p3-r1-3', (13, 27), (13, 30))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', 'p3-r1-3', closed=False)
        self.relate('connect', 'p1-r1-3', 'p2-r1-1')
        self.relate('connect', 'p1-r1-4', 'p2-r1-1')
