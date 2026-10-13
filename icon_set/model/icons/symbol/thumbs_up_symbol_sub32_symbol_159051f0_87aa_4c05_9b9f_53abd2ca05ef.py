"""Independent 32px profile of thumbs-up-symbol.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = '159051f0-87aa-4c05-9b9f-53abd2ca05ef'
SOURCE_PATH = 'pictographic-primitives/symbol/thumbs up_159051f0-87aa-4c05-9b9f-53abd2ca05ef.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('159051f0-87aa-4c05-9b9f-53abd2ca05ef', 'pictographic-primitives/symbol/thumbs up_159051f0-87aa-4c05-9b9f-53abd2ca05ef.svg'), ('5680cb28-5cf7-4d7c-98be-ae372bac6440', 'pictographic-primitives/symbol/thumbs up_5680cb28-5cf7-4d7c-98be-ae372bac6440.svg'))
PROFILE_SOURCE_KEYS = ('solo/thumbs-up-symbol', 'solo/thumbs-up-5680cb28')
SOLO_SOURCE_ICON_IDS = ('thumbs-up-symbol', 'thumbs-up-5680cb28')
REFERENCE_EXPORT_SHA256 = 'fef39793b900339390a7f350b1a8d2cf9da5c5ce4dded16bb603b2155ee5e562'

class DrawingContainerSymbol(Sub32):
    icon_id = 'thumbs-up-symbol-sub32-symbol'
    related_origin_icon_id = 'thumbs-up-symbol-sub32'
    variant_label = 'Independent container symbol'
    usage_category = 'symbol'
    related_group = 'sub-origin/thumbs-up-symbol-sub32'
    counterpart_icon_id = 'thumbs-up-symbol-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'symbol'
    categories = ('symbol', 'state')
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        # Thumbs up: cuff on the left, fist with a rounded thumb raised.
        self.add_polyline('cuff', (2, 14), (10, 14), (10, 30), (2, 30), closed=True)
        self.add_line('h-1', (10, 14), (12, 6))
        self.add_arc('h-2', (12, 6), (20, 6), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_line('h-3', (20, 6), (20, 14))
        self.add_line('h-4', (20, 14), (26, 14))
        self.add_arc('h-5', (26, 14), (30, 18), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_line('h-6', (30, 18), (30, 26))
        self.add_arc('h-7', (30, 26), (26, 30), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_line('h-8', (26, 30), (10, 30))
        self.add_contour('hand', 'h-1', 'h-2', 'h-3', 'h-4', 'h-5', 'h-6', 'h-7', 'h-8')
        self.relate('connect', 'cuff', 'hand')
