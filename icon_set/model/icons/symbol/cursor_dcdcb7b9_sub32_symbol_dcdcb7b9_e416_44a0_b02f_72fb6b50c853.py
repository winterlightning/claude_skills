"""Independent 32px profile of cursor-dcdcb7b9.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = 'dcdcb7b9-e416-44a0-b02f-72fb6b50c853'
SOURCE_PATH = 'pictographic-primitives/interface-essential/cursor_dcdcb7b9-e416-44a0-b02f-72fb6b50c853.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('dcdcb7b9-e416-44a0-b02f-72fb6b50c853', 'pictographic-primitives/interface-essential/cursor_dcdcb7b9-e416-44a0-b02f-72fb6b50c853.svg'), ('4b8a1949-3e5f-4bab-9f8a-db37b07f0bc0', 'pictographic-primitives/interface-essential/cursor_4b8a1949-3e5f-4bab-9f8a-db37b07f0bc0.svg'))
PROFILE_SOURCE_KEYS = ('solo/cursor-dcdcb7b9', 'solo/cursor-interface-essential')
SOLO_SOURCE_ICON_IDS = ('cursor-dcdcb7b9', 'cursor-interface-essential')
REFERENCE_EXPORT_SHA256 = 'b2f7caa79c084db2816252fc019798c1e4aa6caa19931029a55142aba3bdd03e'

class DrawingContainerSymbol(Sub32):
    icon_id = 'cursor-dcdcb7b9-sub32-symbol'
    related_origin_icon_id = 'cursor-dcdcb7b9-sub32'
    variant_label = 'Independent container symbol'
    usage_category = 'symbol'
    related_group = 'sub-origin/cursor-dcdcb7b9-sub32'
    counterpart_icon_id = 'cursor-dcdcb7b9-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'interface-essential'
    categories = ('interface-essential', 'primitives')
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (30, 30), (16, 2))
        self.add_line('p1-r1-2', (16, 2), (2, 30))
        self.add_line('p1-r1-3', (2, 30), (16, 21))
        self.add_line('p1-r1-4', (16, 21), (30, 30))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', closed=False)
