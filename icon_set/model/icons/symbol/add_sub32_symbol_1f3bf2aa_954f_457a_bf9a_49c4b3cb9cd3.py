"""Grid-aligned SUB32 sibling preserving all source parts.
Exact proportional reuse requested for combination subs; fixed 4px stroke.
Keyshape: SQUARE; no node snapping or feature removal.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = '1f3bf2aa-954f-457a-bf9a-49c4b3cb9cd3'
SOURCE_PATH = 'pictographic-primitives/interface-essential/add_1f3bf2aa-954f-457a-bf9a-49c4b3cb9cd3.svg'
SOURCE_REFERENCES = ()
AUTHOR = 'gpt-6'
SOLO_SOURCE_ICON_ID = 'add'

class GridAlignedSubContainerSymbol(Sub32):
    icon_id = 'add-sub32-symbol'
    related_origin_icon_id = 'add-sub32'
    variant_label = 'Independent container symbol'
    usage_category = 'symbol'
    related_group = 'sub-origin/add-sub32'
    counterpart_icon_id = 'add-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'

    def build(self):
        self.add_line('e0', (16, 2), (16, 30))
        self.add_line('e1', (2, 16), (30, 16))
        self.add_contour('c0', *['e0'], closed=False)
        self.add_contour('c1', *['e1'], closed=False)
