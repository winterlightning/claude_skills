"""Independent 32px profile of six-dot-drag-handle.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = 'b1a71762-cfed-4c31-8dc5-4cfaea8d5909'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/mark circle_b1a71762-cfed-4c31-8dc5-4cfaea8d5909.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('b1a71762-cfed-4c31-8dc5-4cfaea8d5909', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/mark circle_b1a71762-cfed-4c31-8dc5-4cfaea8d5909.svg'),)
PROFILE_SOURCE_KEYS = ('solo/six-dot-drag-handle',)
SOLO_SOURCE_ICON_IDS = ('six-dot-drag-handle',)
REFERENCE_EXPORT_SHA256 = 'a20d3c044cee70120a4ae9cac17ad7896068f68dff0565fa0154c24ac477b6c6'

class Drawing(Sub32):
    icon_id = 'six-dot-drag-handle-sub32'
    keyshape = Keyshape.HRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives-generate'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (2, 5), (2, 5))
        self.add_contour('path-1-1', 'p1-r1-1', closed=False)
        self.add_line('p2-r1-1', (16, 5), (16, 5))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p3-r1-1', (30, 5), (30, 5))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_line('p4-r1-1', (2, 27), (2, 27))
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
        self.add_line('p5-r1-1', (16, 27), (16, 27))
        self.add_contour('path-5-1', 'p5-r1-1', closed=False)
        self.add_line('p6-r1-1', (30, 27), (30, 27))
        self.add_contour('path-6-1', 'p6-r1-1', closed=False)
