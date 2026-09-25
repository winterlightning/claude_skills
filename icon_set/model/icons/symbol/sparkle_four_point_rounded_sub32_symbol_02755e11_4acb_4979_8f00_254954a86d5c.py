"""Grid-aligned SUB32 sibling preserving all source parts.
Exact proportional reuse requested for combination subs; fixed 4px stroke.
Keyshape: SQUARE; no node snapping or feature removal.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = '02755e11-4acb-4979-8f00-254954a86d5c'
SOURCE_PATH = 'pictographic-primitives/symbol/spark_02755e11-4acb-4979-8f00-254954a86d5c.svg'
SOURCE_REFERENCES = ()
AUTHOR = 'gpt-6'
SOLO_SOURCE_ICON_ID = 'sparkle-four-point-rounded'

class GridAlignedSubContainerSymbol(Sub32):
    icon_id = 'sparkle-four-point-rounded-sub32-symbol'
    related_origin_icon_id = 'sparkle-four-point-rounded-sub32'
    variant_label = 'Independent container symbol'
    usage_category = 'symbol'
    related_group = 'sub-origin/sparkle-four-point-rounded-sub32'
    counterpart_icon_id = 'sparkle-four-point-rounded-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    categories = ('symbol', 'state')

    def build(self):
        self.add_arc('side-0', (16, 2), (30, 16), radius_x=14, radius_y=14, large_arc=False, sweep=False)
        self.add_arc('side-1', (30, 16), (16, 30), radius_x=14, radius_y=14, large_arc=False, sweep=False)
        self.add_arc('side-2', (16, 30), (2, 16), radius_x=14, radius_y=14, large_arc=False, sweep=False)
        self.add_arc('side-3', (2, 16), (16, 2), radius_x=14, radius_y=14, large_arc=False, sweep=False)
        self.add_contour('sparkle', *['side-0', 'side-1', 'side-2', 'side-3'], closed=True)
