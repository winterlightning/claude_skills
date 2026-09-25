"""Taxi van (transportation), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'ada3205c-5d9e-5462-aa70-12c4111a8115'
SOURCE_PATH = 'pictographic-primitives/transportation/taxi van_ada3205c-5d9e-5462-aa70-12c4111a8115.svg'
AUTHOR = 'gpt-6'

class TaxiVan(Solo48):
    icon_id = 'taxi-van'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'transportation'
    categories = ('transportation', 'primitives')
    aliases = ()
    keywords = ('taxi', 'van', 'transportation')

    def build(self) -> None:
        # Symbol plan: preserve the subject, contour topology and curve types.
        # Rebalance whole parts on the SOLO48 integer grid; keep real shared contacts.
        self.add_line('e0', (44, 31), (44, 25))
        self.add_line('e1', (44, 25), (41, 25))
        self.add_line('e2', (31, 34), (17, 34))
        self.add_line('e3', (4, 30), (4, 12))
        self.add_line('e4', (8, 8), (29, 8))
        self.add_line('e5', (33, 10), (40, 19))
        self.add_line('e6', (38, 20), (4, 20))
        self.add_line('e7', (25, 8), (25, 19))
        self.add_arc('e8-top', (31, 34), (41, 34), radius_x=5, radius_y=6, large_arc=False, sweep=True)
        self.add_arc('e8-bottom', (41, 34), (31, 34), radius_x=5, radius_y=6, large_arc=False, sweep=True)
        self.add_arc('e9-top', (7, 34), (17, 34), radius_x=5, radius_y=6, large_arc=False, sweep=True)
        self.add_arc('e9-bottom', (17, 34), (7, 34), radius_x=5, radius_y=6, large_arc=False, sweep=True)
        self.add_line('e10-1', (40, 34), (43, 34))
        self.add_line('e10-2', (43, 34), (44, 31))
        self.add_arc('e11-1', (8, 34), (4, 32), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_arc('e11-2', (4, 32), (4, 30), radius_x=13, radius_y=13, large_arc=False, sweep=False)
        self.add_line('e12-1', (4, 12), (5, 9))
        self.add_arc('e12-2', (5, 9), (7, 8), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_arc('e12-3', (7, 8), (8, 8), radius_x=8, radius_y=8, large_arc=False, sweep=False)
        self.add_line('e13', (29, 8), (33, 10))
        self.add_arc('e14-1', (44, 25), (42, 21), radius_x=8, radius_y=8, large_arc=False, sweep=False)
        self.add_arc('e14-2', (42, 21), (38, 20), radius_x=4, radius_y=4, large_arc=False, sweep=False)
        self.add_contour('c0', *('e10-1', 'e10-2', 'e0', 'e1'), closed=False)
        self.add_contour('c1', *('e2',), closed=False)
        self.add_contour('c2', *('e11-1', 'e11-2', 'e3', 'e12-1', 'e12-2', 'e12-3', 'e4', 'e13', 'e5'), closed=False)
        self.add_contour('c3', *('e14-1', 'e14-2', 'e6'), closed=False)
        self.add_contour('c4', *('e7',), closed=False)
        self.add_contour('e9', *('e9-top', 'e9-bottom'), closed=True)
        self.add_contour('e8', *('e8-top', 'e8-bottom'), closed=True)
        self.relate('connect', *('c0', 'e8'))
        self.relate('connect', *('c1', 'e8'))
        self.relate('connect', *('c1', 'e9'))
        self.relate('connect', *('c2', 'e9'))
        self.relate('connect', *('c2', 'c3'))
        self.relate('connect', *('c4', 'c2'))
        self.relate('connect', *('c4', 'c3'))
