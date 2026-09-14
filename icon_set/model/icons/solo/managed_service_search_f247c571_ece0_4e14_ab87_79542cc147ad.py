"""Managed service search (business), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'f247c571-ece0-4e14-ab87-79542cc147ad'
SOURCE_PATH = 'icons-json/business/managed service search_f247c571-ece0-4e14-ab87-79542cc147ad.json'
AUTHOR = 'gpt-6'

class ManagedServiceSearch(Solo48):
    icon_id = 'managed-service-search'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'business'
    aliases = ()
    keywords = ('managed', 'service', 'search', 'business')

    def build(self) -> None:
        # Symbol plan: preserve the subject, contour topology and curve types.
        # Rebalance whole parts on the SOLO48 integer grid; keep real shared contacts.
        self.add_line('e0', (42, 42), (32, 33))
        self.add_line('e1', (32, 20), (30, 20))
        self.add_line('e2', (30, 20), (26, 30))
        self.add_line('e3', (26, 30), (21, 12))
        self.add_line('e4', (21, 12), (16, 28))
        self.add_line('e5', (16, 28), (13, 22))
        self.add_line('e6', (13, 22), (6, 22))
        self.add_arc('e7-top', (6, 22), (38, 22), radius_x=16, radius_y=16, large_arc=False, sweep=True)
        self.add_arc('e7-bottom', (38, 22), (6, 22), radius_x=16, radius_y=16, large_arc=False, sweep=True)
        self.add_contour('c0', *('e0',), closed=False)
        self.add_contour('c1', *('e1', 'e2', 'e3', 'e4', 'e5', 'e6'), closed=False)
        self.add_contour('e7', *('e7-top', 'e7-bottom'), closed=True)
        self.relate('connect', *('c0', 'e7'))
        self.relate('connect', *('c1', 'e7'))
