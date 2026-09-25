"""Grid-aligned SUB32 sibling preserving all source parts.
Exact proportional reuse requested for combination subs; fixed 4px stroke.
Keyshape: CIRCLE; no node snapping or feature removal.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = 'c4d23011-c558-4522-931b-0d558dad4995'
SOURCE_PATH = 'pictographic-primitives/other/circle add_c4d23011-c558-4522-931b-0d558dad4995.svg'
SOURCE_REFERENCES = ()
AUTHOR = 'gpt-6'
SOLO_SOURCE_ICON_ID = 'circle-add'

class GridAlignedSubContainerSymbol(Sub32):
    icon_id = 'circle-add-sub32-symbol'
    related_origin_icon_id = 'circle-add-sub32'
    variant_label = 'Independent container symbol'
    usage_category = 'symbol'
    related_group = 'sub-origin/circle-add-sub32'
    counterpart_icon_id = 'circle-add-sub32'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'

    def build(self):
        self.add_arc('sym-e0', (2, 16), (30, 16), radius_x=14, radius_y=14, large_arc=False, sweep=True)
        self.add_arc('sym-e1', (30, 16), (2, 16), radius_x=14, radius_y=14, large_arc=False, sweep=True)
        self.add_line('sym-e2', (16, 16), (16, 23))
        self.add_line('sym-e3', (9, 16), (23, 16))
        self.add_line('sym-e5', (16, 9), (16, 16))
        self.add_contour('sym-c0', *['sym-e0', 'sym-e1'], closed=True)
        self.add_contour('sym-c1', *['sym-e2'], closed=False)
        self.add_contour('sym-c2', *['sym-e3'], closed=False)
        self.add_contour('sym-c3', *['sym-e5'], closed=False)
        self.relate('connect', *['sym-c1', 'sym-c2', 'sym-c3'])
