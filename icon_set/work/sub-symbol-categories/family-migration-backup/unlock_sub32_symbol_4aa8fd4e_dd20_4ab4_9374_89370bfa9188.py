# Independent container symbol; edit separately from linked side sub-icon.
"""Independent 32px profile of unlock.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = '4aa8fd4e-dd20-4ab4-9374-89370bfa9188'
SOURCE_PATH = 'pictographic-primitives/state/unlock_4aa8fd4e-dd20-4ab4-9374-89370bfa9188.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('4aa8fd4e-dd20-4ab4-9374-89370bfa9188', 'pictographic-primitives/state/unlock_4aa8fd4e-dd20-4ab4-9374-89370bfa9188.svg'), ('90a6ff07-21bc-47ed-b588-aacc1c25c397', 'pictographic-primitives/symbol/unlock_90a6ff07-21bc-47ed-b588-aacc1c25c397.svg'))
PROFILE_SOURCE_KEYS = ('solo/unlock', 'solo/unlock-90a6ff07')
SOLO_SOURCE_ICON_IDS = ('unlock', 'unlock-90a6ff07')
REFERENCE_EXPORT_SHA256 = '1aed9ece8daf9f853443f7683f46868886f3a263c274d74dfd3325a6c18aa711'

class DrawingContainerSymbol(Sub32):
    icon_id = 'unlock-sub32-symbol'
    variant_of = 'unlock-sub32'
    variant_label = 'Independent container symbol'
    usage_category = 'symbol'
    related_group = 'sub-origin/unlock-sub32'
    counterpart_icon_id = 'unlock-sub32'
    keyshape = Keyshape.VRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'state'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (8, 15), (24, 15))
        self.add_arc('p1-r1-2', (24, 15), (27, 17), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('p1-r1-3', (27, 17), (27, 27))
        self.add_arc('p1-r1-4', (27, 27), (24, 30), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('p1-r1-5', (24, 30), (8, 30))
        self.add_arc('p1-r1-6', (8, 30), (5, 27), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('p1-r1-7', (5, 27), (5, 17))
        self.add_arc('p1-r1-8', (5, 17), (8, 15), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', 'p1-r1-8', closed=False)
        self.add_line('p2-r1-1', (9, 15), (9, 9))
        self.add_arc('p2-r1-2', (9, 9), (23, 9), radius_x=7, radius_y=7, large_arc=False, sweep=True)
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', closed=False)
