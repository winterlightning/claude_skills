"""Managed service search (programing), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '3fccb59a-1af7-5cab-a3db-98e5a8fc10cd'
SOURCE_PATH = 'pictographic-primitives/programing/managed service search_3fccb59a-1af7-5cab-a3db-98e5a8fc10cd.svg'
AUTHOR = 'gpt-6'

class ManagedServiceSearchPrograming(Solo48):
    icon_id = 'managed-service-search-programing'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'programing'
    categories = ('programing', 'primitives')
    aliases = ()
    keywords = ('managed', 'service', 'search', 'programing')

    def build(self) -> None:
        # Symbol plan: preserve the subject, contour topology and curve types.
        # Rebalance whole parts on the SOLO48 integer grid; keep real shared contacts.
        self.add_line('e0', (43, 22), (35, 22))
        self.add_line('e1', (34, 21), (33, 20))
        self.add_line('e2', (33, 20), (29, 30))
        self.add_line('e3', (29, 30), (24, 13))
        self.add_line('e4', (24, 13), (19, 27))
        self.add_line('e5', (19, 27), (17, 22))
        self.add_line('e6', (17, 22), (4, 22))
        self.add_line('e7', (44, 40), (36, 33))
        self.add_arc('e8-top', (11, 22), (41, 22), radius_x=15, radius_y=14, large_arc=False, sweep=True)
        self.add_arc('e8-bottom', (41, 22), (11, 22), radius_x=15, radius_y=14, large_arc=False, sweep=True)
        self.add_line('e9', (35, 22), (34, 21))
        self.add_contour('c0', *('e0', 'e9', 'e1', 'e2', 'e3', 'e4', 'e5', 'e6'), closed=False)
        self.add_contour('c1', *('e7',), closed=False)
        self.add_contour('e8', *('e8-top', 'e8-bottom'), closed=True)
        self.relate('connect', *('c1', 'e8'))
