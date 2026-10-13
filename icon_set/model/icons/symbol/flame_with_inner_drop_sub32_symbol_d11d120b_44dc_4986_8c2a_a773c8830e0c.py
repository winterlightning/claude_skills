"""Independent 32px profile of flame-with-inner-drop.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = 'd11d120b-44dc-4986-8c2a-a773c8830e0c'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/fire/flame_d11d120b-44dc-4986-8c2a-a773c8830e0c.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('d11d120b-44dc-4986-8c2a-a773c8830e0c', '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/fire/flame_d11d120b-44dc-4986-8c2a-a773c8830e0c.svg'),)
PROFILE_SOURCE_KEYS = ('solo/flame-with-inner-drop',)
SOLO_SOURCE_ICON_IDS = ('flame-with-inner-drop',)
REFERENCE_EXPORT_SHA256 = '6480a8274acccf6a7f1325e9837658e0827c5d5b5d6b54a54acbb3a1bddf168a'

class DrawingContainerSymbol(Sub32):
    icon_id = 'flame-with-inner-drop-sub32-symbol'
    related_origin_icon_id = 'flame-with-inner-drop-sub32'
    variant_label = 'Independent container symbol'
    usage_category = 'symbol'
    related_group = 'sub-origin/flame-with-inner-drop-sub32'
    counterpart_icon_id = 'flame-with-inner-drop-sub32'
    keyshape = Keyshape.VRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'fire'
    categories = ('fire', 'state')
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        # Flame with an inner drop, the drop 4 units clear of the flame.
        self.add_bezier('f-l', (4, 18), ((4, 10), (12, 8), (16, 2)))
        self.add_bezier('f-r', (16, 2), ((20, 8), (28, 10), (28, 18)))
        self.add_arc('f-b', (28, 18), (4, 18), radius_x=12, radius_y=12, large_arc=False, sweep=True)
        self.add_contour('flame', 'f-l', 'f-r', 'f-b', closed=True)
        self.add_line('d-1', (16, 14), (20, 18))
        self.add_arc('d-2', (20, 18), (12, 18), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_line('d-3', (12, 18), (16, 14))
        self.add_contour('drop', 'd-1', 'd-2', 'd-3', closed=True)
