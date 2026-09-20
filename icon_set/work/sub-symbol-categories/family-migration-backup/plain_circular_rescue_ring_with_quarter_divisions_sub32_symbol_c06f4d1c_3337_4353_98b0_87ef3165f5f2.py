# Independent container symbol; edit separately from linked side sub-icon.
"""Grid-aligned SUB32 sibling preserving all source parts.
Exact proportional reuse requested for combination subs; fixed 4px stroke.
Keyshape: CIRCLE; no node snapping or feature removal.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = 'c06f4d1c-3337-4353-98b0-87ef3165f5f2'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/entertainment/casino chip_c06f4d1c-3337-4353-98b0-87ef3165f5f2.svg'
SOURCE_REFERENCES = ()
AUTHOR = 'gpt-6'
SOLO_SOURCE_ICON_ID = 'plain-circular-rescue-ring-with-quarter-divisions'

class GridAlignedSubContainerSymbol(Sub32):
    icon_id = 'plain-circular-rescue-ring-with-quarter-divisions-sub32-symbol'
    variant_of = 'plain-circular-rescue-ring-with-quarter-divisions-sub32'
    variant_label = 'Independent container symbol'
    usage_category = 'symbol'
    related_group = 'sub-origin/plain-circular-rescue-ring-with-quarter-divisions-sub32'
    counterpart_icon_id = 'plain-circular-rescue-ring-with-quarter-divisions-sub32'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/recreation'

    def build(self):
        self.add_arc('outer-0', (16, 2), (30, 16), radius_x=14, radius_y=14, large_arc=False, sweep=True)
        self.add_arc('outer-1', (30, 16), (16, 30), radius_x=14, radius_y=14, large_arc=False, sweep=True)
        self.add_arc('outer-2', (16, 30), (2, 16), radius_x=14, radius_y=14, large_arc=False, sweep=True)
        self.add_arc('outer-3', (2, 16), (16, 2), radius_x=14, radius_y=14, large_arc=False, sweep=True)
        self.add_arc('inner-0', (16, 9), (23, 16), radius_x=7, radius_y=7, large_arc=False, sweep=True)
        self.add_arc('inner-1', (23, 16), (16, 23), radius_x=7, radius_y=7, large_arc=False, sweep=True)
        self.add_arc('inner-2', (16, 23), (9, 16), radius_x=7, radius_y=7, large_arc=False, sweep=True)
        self.add_arc('inner-3', (9, 16), (16, 9), radius_x=7, radius_y=7, large_arc=False, sweep=True)
        self.add_line('band-0', (16, 2), (16, 9))
        self.add_line('band-1', (30, 16), (23, 16))
        self.add_line('band-2', (16, 30), (16, 23))
        self.add_line('band-3', (2, 16), (9, 16))
        self.add_contour('outer', *['outer-0', 'outer-1', 'outer-2', 'outer-3'], closed=True)
        self.add_contour('inner', *['inner-0', 'inner-1', 'inner-2', 'inner-3'], closed=True)
        self.relate('connect', *['band-0', 'outer'])
        self.relate('connect', *['band-0', 'inner'])
        self.relate('connect', *['band-1', 'outer'])
        self.relate('connect', *['band-1', 'inner'])
        self.relate('connect', *['band-2', 'outer'])
        self.relate('connect', *['band-2', 'inner'])
        self.relate('connect', *['band-3', 'outer'])
        self.relate('connect', *['band-3', 'inner'])
