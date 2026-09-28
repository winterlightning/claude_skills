"""Independent 32px profile of database-servers.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = '7226fb36-c110-4033-9d0b-3e66cfa5b027'
SOURCE_PATH = 'pictographic-primitives/servers/database_7226fb36-c110-4033-9d0b-3e66cfa5b027.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('7226fb36-c110-4033-9d0b-3e66cfa5b027', 'pictographic-primitives/servers/database_7226fb36-c110-4033-9d0b-3e66cfa5b027.svg'), ('b3ea511d-2f05-474a-944e-587c5423980b', 'pictographic-primitives/diagrams/database_b3ea511d-2f05-474a-944e-587c5423980b.svg'))
PROFILE_SOURCE_KEYS = ('solo/database-servers', 'solo/database-diagrams')
SOLO_SOURCE_ICON_IDS = ('database-servers', 'database-diagrams')
REFERENCE_EXPORT_SHA256 = 'ad9ac229eddcd969e40d210b27eeed7f66ff8c9a2e5a743bbaf9796892935d26'

class DrawingContainerSymbol(Sub32):
    icon_id = 'database-servers-sub32-symbol'
    related_origin_icon_id = 'database-servers-sub32'
    variant_label = 'Independent container symbol'
    usage_category = 'symbol'
    related_group = 'sub-origin/database-servers-sub32'
    counterpart_icon_id = 'database-servers-sub32'
    keyshape = Keyshape.VRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'servers'
    categories = ('servers', 'state')
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_arc('p1-r1-1', (5, 6), (27, 6), radius_x=11, radius_y=4, large_arc=False, sweep=True)
        self.add_arc('p1-r1-2', (27, 6), (5, 6), radius_x=11, radius_y=4, large_arc=False, sweep=True)
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', closed=False)
        self.add_line('p2-r1-1', (5, 6), (5, 26))
        self.add_arc('p2-r1-2', (5, 26), (27, 26), radius_x=11, radius_y=4, large_arc=False, sweep=False)
        self.add_line('p2-r1-3', (27, 26), (27, 6))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', closed=False)
        self.add_arc('p3-r1-1', (5, 17), (27, 17), radius_x=11, radius_y=4, large_arc=False, sweep=False)
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.relate('connect', 'p1-r1-1', 'p2-r1-1')
        self.relate('connect', 'p1-r1-1', 'p2-r1-3')
        self.relate('connect', 'p1-r1-2', 'p2-r1-1')
        self.relate('connect', 'p1-r1-2', 'p2-r1-3')
