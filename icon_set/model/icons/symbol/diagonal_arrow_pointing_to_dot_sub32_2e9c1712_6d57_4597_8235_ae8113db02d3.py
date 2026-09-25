"""Independent 32px profile of diagonal-arrow-pointing-to-dot.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = '2e9c1712-6d57-4597-8235-ae8113db02d3'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/mark point_2e9c1712-6d57-4597-8235-ae8113db02d3.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('2e9c1712-6d57-4597-8235-ae8113db02d3', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/mark point_2e9c1712-6d57-4597-8235-ae8113db02d3.svg'),)
PROFILE_SOURCE_KEYS = ('solo/diagonal-arrow-pointing-to-dot',)
SOLO_SOURCE_ICON_IDS = ('diagonal-arrow-pointing-to-dot',)
REFERENCE_EXPORT_SHA256 = '7e041c6075eb00b207c62310b12fd6697258f1f00b62887966ff28801193b1cc'

class Drawing(Sub32):
    icon_id = 'diagonal-arrow-pointing-to-dot-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives-generate'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (30, 2), (9, 23))
        self.add_contour('path-1-1', 'p1-r1-1', closed=False)
        self.add_line('p2-r1-1', (9, 14), (9, 23))
        self.add_line('p2-r1-2', (9, 23), (18, 23))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', closed=False)
        self.add_line('p3-r1-1', (2, 30), (2, 30))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.relate('connect', 'p1-r1-1', 'p2-r1-1')
        self.relate('connect', 'p1-r1-1', 'p2-r1-2')
