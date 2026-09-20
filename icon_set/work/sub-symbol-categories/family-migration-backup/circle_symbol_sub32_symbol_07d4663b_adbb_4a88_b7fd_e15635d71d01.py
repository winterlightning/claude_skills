# Independent container symbol; edit separately from linked side sub-icon.
"""Grid-aligned SUB32 sibling preserving all source parts.
Exact proportional reuse requested for combination subs; fixed 4px stroke.
Keyshape: CIRCLE; no node snapping or feature removal.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = '07d4663b-adbb-4a88-b7fd-e15635d71d01'
SOURCE_PATH = 'pictographic-primitives/symbol/circle_07d4663b-adbb-4a88-b7fd-e15635d71d01.svg'
SOURCE_REFERENCES = ()
AUTHOR = 'gpt-6'
SOLO_SOURCE_ICON_ID = 'circle-symbol'

class GridAlignedSubContainerSymbol(Sub32):
    icon_id = 'circle-symbol-sub32-symbol'
    variant_of = 'circle-symbol-sub32'
    variant_label = 'Independent container symbol'
    usage_category = 'symbol'
    related_group = 'sub-origin/circle-symbol-sub32'
    counterpart_icon_id = 'circle-symbol-sub32'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'

    def build(self):
        self.add_arc('e0-top', (2, 16), (30, 16), radius_x=14, radius_y=14, large_arc=False, sweep=True)
        self.add_arc('e0-bottom', (30, 16), (2, 16), radius_x=14, radius_y=14, large_arc=False, sweep=True)
        self.add_contour('e0', *['e0-top', 'e0-bottom'], closed=True)
