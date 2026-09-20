# Independent container symbol; edit separately from linked side sub-icon.
"""Independent 32px profile of basket-shopping.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = '37404b45-6940-44fc-b7c8-3c963f7c35dd'
SOURCE_PATH = 'pictographic-primitives/symbol/basket_37404b45-6940-44fc-b7c8-3c963f7c35dd.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('37404b45-6940-44fc-b7c8-3c963f7c35dd', 'pictographic-primitives/symbol/basket_37404b45-6940-44fc-b7c8-3c963f7c35dd.svg'),)
PROFILE_SOURCE_KEYS = ('solo/basket-shopping',)
SOLO_SOURCE_ICON_IDS = ('basket-shopping',)
REFERENCE_EXPORT_SHA256 = 'c76a6ffc8a30ba2030673bb2a07e023e41005b45aedf2e50b87c517100a24006'

class DrawingContainerSymbol(Sub32):
    icon_id = 'basket-shopping-sub32-symbol'
    variant_of = 'basket-shopping-sub32'
    variant_label = 'Independent container symbol'
    usage_category = 'symbol'
    related_group = 'sub-origin/basket-shopping-sub32'
    counterpart_icon_id = 'basket-shopping-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'symbols/standalone'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (2, 14), (10, 14))
        self.add_line('p1-r1-2', (10, 14), (22, 14))
        self.add_line('p1-r1-3', (22, 14), (30, 14))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', closed=False)
        self.add_line('p2-r1-1', (2, 14), (5, 27))
        self.add_arc('p2-r1-2', (5, 27), (8, 30), radius_x=3, radius_y=3, large_arc=False, sweep=False)
        self.add_line('p2-r1-3', (8, 30), (24, 30))
        self.add_arc('p2-r1-4', (24, 30), (27, 27), radius_x=3, radius_y=3, large_arc=False, sweep=False)
        self.add_line('p2-r1-5', (27, 27), (30, 14))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', 'p2-r1-5', closed=False)
        self.add_arc('p3-r1-1', (10, 14), (22, 14), radius_x=6, radius_y=12, large_arc=False, sweep=True)
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.relate('connect', 'p1-r1-1', 'p2-r1-1')
        self.relate('connect', 'p1-r1-1', 'p3-r1-1')
        self.relate('connect', 'p1-r1-2', 'p3-r1-1')
        self.relate('connect', 'p1-r1-3', 'p2-r1-5')
        self.relate('connect', 'p1-r1-3', 'p3-r1-1')
