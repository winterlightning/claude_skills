# Independent container symbol; edit separately from linked side sub-icon.
"""Independent 32px profile of charging-battery-104-solo.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = 'f8b6ea0a-273a-4932-a93b-52454f7fd328'
SOURCE_PATH = 'icon_set/dist/gallery/combination-originals/f8b6ea0a-273a-4932-a93b-52454f7fd328.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('f8b6ea0a-273a-4932-a93b-52454f7fd328', 'icon_set/dist/gallery/combination-originals/f8b6ea0a-273a-4932-a93b-52454f7fd328.svg'),)
PROFILE_SOURCE_KEYS = ('solo/charging-battery-104-solo',)
SOLO_SOURCE_ICON_IDS = ('charging-battery-104-solo',)
REFERENCE_EXPORT_SHA256 = 'bce7e3dc67e2bbf7ede8ce6ed99985ce7ae0e0bf332ad8f331136f953845b2fe'

class DrawingContainerSymbol(Sub32):
    icon_id = 'charging-battery-104-sub32-symbol'
    variant_of = 'charging-battery-104-sub32'
    variant_label = 'Independent container symbol'
    usage_category = 'symbol'
    related_group = 'sub-origin/charging-battery-104-sub32'
    counterpart_icon_id = 'charging-battery-104-sub32'
    keyshape = Keyshape.HRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'objects/interface-essential'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (9, 5), (5, 5))
        self.add_arc('p1-r1-2', (5, 5), (2, 8), radius_x=3, radius_y=3, large_arc=False, sweep=False)
        self.add_line('p1-r1-3', (2, 8), (2, 24))
        self.add_arc('p1-r1-4', (2, 24), (5, 27), radius_x=3, radius_y=3, large_arc=False, sweep=False)
        self.add_line('p1-r1-5', (5, 27), (7, 27))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', closed=False)
        self.add_line('p2-r1-1', (24, 9), (24, 24))
        self.add_arc('p2-r1-2', (24, 24), (22, 27), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('p2-r1-3', (22, 27), (21, 27))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', closed=False)
        self.add_line('p3-r1-1', (30, 13), (30, 19))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_line('p4-r1-1', (17, 5), (10, 17))
        self.add_line('p4-r1-2', (10, 17), (17, 17))
        self.add_line('p4-r1-3', (17, 17), (13, 27))
        self.add_contour('path-4-1', 'p4-r1-1', 'p4-r1-2', 'p4-r1-3', closed=False)
