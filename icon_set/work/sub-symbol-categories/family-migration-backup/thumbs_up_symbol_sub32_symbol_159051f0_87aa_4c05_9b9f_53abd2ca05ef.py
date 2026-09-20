# Independent container symbol; edit separately from linked side sub-icon.
"""Independent 32px profile of thumbs-up-symbol.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = '159051f0-87aa-4c05-9b9f-53abd2ca05ef'
SOURCE_PATH = 'pictographic-primitives/symbol/thumbs up_159051f0-87aa-4c05-9b9f-53abd2ca05ef.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('159051f0-87aa-4c05-9b9f-53abd2ca05ef', 'pictographic-primitives/symbol/thumbs up_159051f0-87aa-4c05-9b9f-53abd2ca05ef.svg'), ('5680cb28-5cf7-4d7c-98be-ae372bac6440', 'pictographic-primitives/symbol/thumbs up_5680cb28-5cf7-4d7c-98be-ae372bac6440.svg'))
PROFILE_SOURCE_KEYS = ('solo/thumbs-up-symbol', 'solo/thumbs-up-5680cb28')
SOLO_SOURCE_ICON_IDS = ('thumbs-up-symbol', 'thumbs-up-5680cb28')
REFERENCE_EXPORT_SHA256 = 'fef39793b900339390a7f350b1a8d2cf9da5c5ce4dded16bb603b2155ee5e562'

class DrawingContainerSymbol(Sub32):
    icon_id = 'thumbs-up-symbol-sub32-symbol'
    variant_of = 'thumbs-up-symbol-sub32'
    variant_label = 'Independent container symbol'
    usage_category = 'symbol'
    related_group = 'sub-origin/thumbs-up-symbol-sub32'
    counterpart_icon_id = 'thumbs-up-symbol-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'symbol'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (2, 16), (8, 16))
        self.add_line('p1-r1-2', (8, 16), (8, 30))
        self.add_line('p1-r1-3', (8, 30), (2, 30))
        self.add_line('p1-r1-4', (2, 30), (2, 16))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', closed=False)
        self.add_line('p2-r1-1', (8, 16), (14, 8))
        self.add_line('p2-r1-2', (14, 8), (14, 2))
        self.add_line('p2-r1-3', (14, 2), (22, 2))
        self.add_line('p2-r1-4', (22, 2), (24, 7))
        self.add_line('p2-r1-5', (24, 7), (21, 14))
        self.add_line('p2-r1-6', (21, 14), (25, 14))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', 'p2-r1-5', 'p2-r1-6', closed=False)
        self.add_arc('p3-r1-1', (25, 14), (30, 19), radius_x=5, radius_y=5, large_arc=False, sweep=True)
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_line('p4-r1-1', (30, 19), (30, 24))
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
        self.add_arc('p5-r1-1', (30, 24), (24, 30), radius_x=6, radius_y=6, large_arc=False, sweep=True)
        self.add_contour('path-5-1', 'p5-r1-1', closed=False)
        self.add_line('p6-r1-1', (24, 30), (8, 30))
        self.add_contour('path-6-1', 'p6-r1-1', closed=False)
        self.relate('connect', 'p1-r1-1', 'p2-r1-1')
        self.relate('connect', 'p1-r1-2', 'p2-r1-1')
        self.relate('connect', 'p1-r1-2', 'p6-r1-1')
        self.relate('connect', 'p1-r1-3', 'p6-r1-1')
        self.relate('connect', 'p2-r1-6', 'p3-r1-1')
        self.relate('connect', 'p3-r1-1', 'p4-r1-1')
        self.relate('connect', 'p4-r1-1', 'p5-r1-1')
        self.relate('connect', 'p5-r1-1', 'p6-r1-1')
