# Independent container symbol; edit separately from linked side sub-icon.
"""Grid-aligned SUB32 sibling preserving all source parts.
Exact proportional reuse requested for combination subs; fixed 4px stroke.
Keyshape: CIRCLE; no node snapping or feature removal.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = '4be75ff3-2cc9-4492-a406-ef7c11b29925'
SOURCE_PATH = 'pictographic-primitives/sports/ball_4be75ff3-2cc9-4492-a406-ef7c11b29925.svg'
SOURCE_REFERENCES = ()
AUTHOR = 'gpt-6'
SOLO_SOURCE_ICON_ID = 'ball'

class GridAlignedSubContainerSymbol(Sub32):
    icon_id = 'ball-sub32-symbol'
    variant_of = 'ball-sub32'
    variant_label = 'Independent container symbol'
    usage_category = 'symbol'
    related_group = 'sub-origin/ball-sub32'
    counterpart_icon_id = 'ball-sub32'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'sports'

    def build(self):
        self.add_arc('outline-0', (2, 16), (16, 2), radius_x=14, radius_y=14, large_arc=False, sweep=True)
        self.add_arc('outline-1', (16, 2), (30, 16), radius_x=14, radius_y=14, large_arc=False, sweep=True)
        self.add_arc('outline-2', (30, 16), (16, 30), radius_x=14, radius_y=14, large_arc=False, sweep=True)
        self.add_arc('outline-3', (16, 30), (2, 16), radius_x=14, radius_y=14, large_arc=False, sweep=True)
        self.add_bezier('seam-top-0', (16, 2), *[[[16.0, 9.7], [22.3, 16.0], [30.0, 16.0]]])
        self.add_bezier('seam-bottom-0', (2, 16), *[[[9.7, 16.0], [16.0, 22.3], [16.0, 30.0]]])
        self.add_contour('outline', *['outline-0', 'outline-1', 'outline-2', 'outline-3'], closed=True)
        self.add_contour('seam-top', *['seam-top-0'], closed=False)
        self.add_contour('seam-bottom', *['seam-bottom-0'], closed=False)
        self.relate('connect', *['seam-top', 'outline'])
        self.relate('connect', *['seam-bottom', 'outline'])
