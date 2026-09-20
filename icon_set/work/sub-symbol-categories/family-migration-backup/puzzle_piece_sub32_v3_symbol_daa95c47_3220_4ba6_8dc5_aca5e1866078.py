# Independent container symbol; edit separately from linked side sub-icon.
"""Independent 32px profile of puzzle-piece.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = 'daa95c47-3220-4ba6-8dc5-aca5e1866078'
SOURCE_PATH = 'pictographic-primitives/symbol/puzzle piece_daa95c47-3220-4ba6-8dc5-aca5e1866078.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('daa95c47-3220-4ba6-8dc5-aca5e1866078', 'pictographic-primitives/symbol/puzzle piece_daa95c47-3220-4ba6-8dc5-aca5e1866078.svg'),)
PROFILE_SOURCE_KEYS = ('solo/puzzle-piece',)
SOLO_SOURCE_ICON_IDS = ('puzzle-piece',)
REFERENCE_EXPORT_SHA256 = '69bb0742c20688dfc2cb2726d56da61a0bfb102e3c45bc787f4a18a4046c689c'

class DrawingVariant3ContainerSymbol(Sub32):
    icon_id = 'puzzle-piece-sub32-v3-symbol'
    variant_of = 'puzzle-piece-sub32-v3'
    variant_label = 'Independent container symbol'
    usage_category = 'symbol'
    related_group = 'sub-origin/puzzle-piece-sub32-v3'
    counterpart_icon_id = 'puzzle-piece-sub32-v3'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'symbol'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_arc('tab', (11, 8), (21, 8), radius_x=5, radius_y=6, sweep=True)
        self.add_line('top-right', (21, 8), (30, 8))
        self.add_line('right-upper', (30, 8), (30, 15))
        self.add_arc('right-socket', (30, 15), (30, 23), radius_x=5, radius_y=4, sweep=False)
        self.add_line('right-lower', (30, 23), (30, 30))
        self.add_line('base', (30, 30), (2, 30))
        self.add_line('left-lower', (2, 30), (2, 23))
        self.add_arc('left-socket', (2, 23), (2, 15), radius_x=5, radius_y=4, sweep=False)
        self.add_line('left-upper', (2, 15), (2, 8))
        self.add_line('top-left', (2, 8), (11, 8))
        self.add_contour('piece', 'tab', 'top-right', 'right-upper', 'right-socket', 'right-lower', 'base', 'left-lower', 'left-socket', 'left-upper', 'top-left', closed=True)
