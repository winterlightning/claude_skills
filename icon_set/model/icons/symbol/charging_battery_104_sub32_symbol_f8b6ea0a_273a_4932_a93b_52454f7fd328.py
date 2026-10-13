"""Independent 32px profile of charging-battery-104-solo.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = 'f8b6ea0a-273a-4932-a93b-52454f7fd328'
SOURCE_PATH = 'icon_set/dist/gallery/combination-originals/f8b6ea0a-273a-4932-a93b-52454f7fd328.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('f8b6ea0a-273a-4932-a93b-52454f7fd328', 'icon_set/dist/gallery/combination-originals/f8b6ea0a-273a-4932-a93b-52454f7fd328.svg'),)
PROFILE_SOURCE_KEYS = ('solo/charging-battery-104-solo',)
SOLO_SOURCE_ICON_IDS = ('charging-battery-104-solo',)
REFERENCE_EXPORT_SHA256 = 'bce7e3dc67e2bbf7ede8ce6ed99985ce7ae0e0bf332ad8f331136f953845b2fe'

class DrawingContainerSymbol(Sub32):
    icon_id = 'charging-battery-104-sub32-symbol'
    related_origin_icon_id = 'charging-battery-104-sub32'
    variant_label = 'Independent container symbol'
    usage_category = 'symbol'
    related_group = 'sub-origin/charging-battery-104-sub32'
    counterpart_icon_id = 'charging-battery-104-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives-generate'
    categories = ('symbol', 'state', 'other', 'primitives-generate')
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        # Battery with a terminal stub beside a lightning bolt (the bolt cannot fit inside the battery).
        self.add_line('p1-r1-1', (2, 6), (12, 6))
        self.add_line('p1-r1-2', (12, 6), (12, 30))
        self.add_line('p1-r1-3', (12, 30), (2, 30))
        self.add_line('p1-r1-4', (2, 30), (2, 6))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', closed=True)
        self.add_line('p2-r1-1', (7, 2), (7, 6))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p3-r1-1', (30, 2), (20, 16))
        self.add_line('p3-r1-2', (20, 16), (30, 16))
        self.add_line('p3-r1-3', (30, 16), (20, 30))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', 'p3-r1-3', closed=False)
        self.relate('connect', 'p1-r1-1', 'p2-r1-1')
