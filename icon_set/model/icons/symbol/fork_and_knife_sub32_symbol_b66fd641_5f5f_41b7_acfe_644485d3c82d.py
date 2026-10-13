"""Independent 32px profile of fork-and-knife.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = 'b66fd641-5f5f-41b7-acfe-644485d3c82d'
SOURCE_PATH = 'pictographic-primitives/symbol/fork and knife_b66fd641-5f5f-41b7-acfe-644485d3c82d.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('b66fd641-5f5f-41b7-acfe-644485d3c82d', 'pictographic-primitives/symbol/fork and knife_b66fd641-5f5f-41b7-acfe-644485d3c82d.svg'),)
PROFILE_SOURCE_KEYS = ('solo/fork-and-knife',)
SOLO_SOURCE_ICON_IDS = ('fork-and-knife',)
REFERENCE_EXPORT_SHA256 = '0e3c5c399b5f2ffcfea4b2559f8efaddc39b23d60f0d07af3ea3404d9a17f070'

class DrawingContainerSymbol(Sub32):
    icon_id = 'fork-and-knife-sub32-symbol'
    related_origin_icon_id = 'fork-and-knife-sub32'
    variant_label = 'Independent container symbol'
    usage_category = 'symbol'
    related_group = 'sub-origin/fork-and-knife-sub32'
    counterpart_icon_id = 'fork-and-knife-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'symbol'
    categories = ('symbol', 'state')
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        # Fork (two tines, rounded head) and knife (8-unit blade), 4 units apart.
        self.add_line('tine-l', (2, 2), (2, 11))
        self.add_arc('head', (2, 11), (14, 11), radius_x=6, radius_y=6, large_arc=False, sweep=False)
        self.add_line('tine-r', (14, 11), (14, 2))
        self.add_contour('fork', 'tine-l', 'head', 'tine-r')
        self.add_line('fork-handle', (8, 17), (8, 30))
        self.add_polyline('knife', (22, 30), (22, 2), (30, 2), (30, 20), (22, 20))
        self.relate('connect', 'fork', 'fork-handle')
