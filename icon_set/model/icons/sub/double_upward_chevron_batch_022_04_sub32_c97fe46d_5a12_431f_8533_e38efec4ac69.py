"""Independent 32px profile of double-upward-chevron-batch-022-04.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = 'c97fe46d-5a12-431f-8533-e38efec4ac69'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/double arrow up_c97fe46d-5a12-431f-8533-e38efec4ac69.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('c97fe46d-5a12-431f-8533-e38efec4ac69', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/double arrow up_c97fe46d-5a12-431f-8533-e38efec4ac69.svg'),)
PROFILE_SOURCE_KEYS = ('solo/double-upward-chevron-batch-022-04',)
SOLO_SOURCE_ICON_IDS = ('double-upward-chevron-batch-022-04',)
REFERENCE_EXPORT_SHA256 = '447bb78c99aaea9826b8cc5ba4f556b8e87c555966fc8d644c53d7ba6fd210bf'

class Drawing(Sub32):
    icon_id = 'double-upward-chevron-batch-022-04-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'primitives-generate'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (2, 14), (16, 2))
        self.add_line('p1-r1-2', (16, 2), (30, 14))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', closed=False)
        self.add_line('p2-r1-1', (2, 30), (16, 18))
        self.add_line('p2-r1-2', (16, 18), (30, 30))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', closed=False)
