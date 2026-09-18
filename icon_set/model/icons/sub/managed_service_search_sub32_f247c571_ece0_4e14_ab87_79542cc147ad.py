"""Independent 32px profile of managed-service-search.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = 'f247c571-ece0-4e14-ab87-79542cc147ad'
SOURCE_PATH = 'pictographic-primitives/business/managed service search_f247c571-ece0-4e14-ab87-79542cc147ad.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('f247c571-ece0-4e14-ab87-79542cc147ad', 'pictographic-primitives/business/managed service search_f247c571-ece0-4e14-ab87-79542cc147ad.svg'),)
PROFILE_SOURCE_KEYS = ('solo/managed-service-search',)
SOLO_SOURCE_ICON_IDS = ('managed-service-search',)
REFERENCE_EXPORT_SHA256 = '656440a3f26cdafe16d3d8195de80e8a5e75427797efdd258be0621b11e7783f'

class Drawing(Sub32):
    icon_id = 'managed-service-search-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'business'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (30, 30), (22, 23))
        self.add_contour('path-1-1', 'p1-r1-1', closed=False)
        self.add_line('p2-r1-1', (22, 13), (21, 13))
        self.add_line('p2-r1-2', (21, 13), (18, 21))
        self.add_line('p2-r1-3', (18, 21), (14, 7))
        self.add_line('p2-r1-4', (14, 7), (10, 19))
        self.add_line('p2-r1-5', (10, 19), (7, 14))
        self.add_line('p2-r1-6', (7, 14), (2, 14))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', 'p2-r1-5', 'p2-r1-6', closed=False)
        self.add_bezier('p3-r1-1', (2, 14), ((2, 8), (8, 2), (14, 2)))
        self.add_bezier('p3-r1-2', (14, 2), ((21, 2), (27, 8), (27, 14)))
        self.add_arc('p3-r1-3', (27, 14), (2, 14), radius_x=12.5, radius_y=12.5, large_arc=False, sweep=True)
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', 'p3-r1-3', closed=False)
        self.relate("connect", 'p2-r1-6', 'p3-r1-1')
        self.relate("connect", 'p2-r1-6', 'p3-r1-3')
