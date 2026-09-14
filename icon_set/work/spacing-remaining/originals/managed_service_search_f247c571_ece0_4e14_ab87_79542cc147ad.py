"""Managed service search (business), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'f247c571-ece0-4e14-ab87-79542cc147ad'
SOURCE_PATH = 'icons-json/business/managed service search_f247c571-ece0-4e14-ab87-79542cc147ad.json'
AUTHOR = 'json_to_solo'

class ManagedServiceSearch(Solo48):
    icon_id = 'managed-service-search'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'business'
    aliases = ()
    keywords = ('managed', 'service', 'search', 'business')

    def build(self):
        self.add_line('e0', (42, 42), (32, 33))
        self.add_line('e1', (32, 21), (30, 21))
        self.add_line('e2', (30, 21), (26, 31))
        self.add_line('e3', (26, 31), (21, 13))
        self.add_line('e4', (21, 13), (16, 29))
        self.add_line('e5', (16, 29), (13, 23))
        self.add_line('e6', (13, 23), (6, 23))
        self.add_arc('e7-top', (6, 22), (38, 22), radius_x=16)
        self.add_arc('e7-bottom', (38, 22), (6, 22), radius_x=16)
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1', 'e2', 'e3', 'e4', 'e5', 'e6')
        self.add_contour('e7', 'e7-top', 'e7-bottom', closed=True)
        self.relate('connect', 'c0', 'e7')
        self.relate('connect', 'c1', 'e7')
