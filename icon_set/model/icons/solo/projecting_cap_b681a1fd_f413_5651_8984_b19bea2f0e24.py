"""Projecting cap (construction), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b681a1fd-f413-5651-8984-b19bea2f0e24'
SOURCE_PATH = 'icons-json/construction/projecting cap_b681a1fd-f413-5651-8984-b19bea2f0e24.json'
AUTHOR = 'gpt-6'

class ProjectingCap(Solo48):
    icon_id = 'projecting-cap'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'construction'
    aliases = ()
    keywords = ('projecting', 'cap', 'construction')

    def build(self) -> None:
        # Symbol plan: preserve the subject, contour topology and curve types.
        # Rebalance whole parts on the SOLO48 integer grid; keep real shared contacts.
        self.add_line('e0', (44, 8), (4, 8))
        self.add_line('e1', (4, 8), (4, 40))
        self.add_line('e2', (4, 40), (44, 40))
        self.add_line('e3', (43, 24), (20, 24))
        self.add_arc('e4-top', (13, 24), (20, 24), radius_x=4, radius_y=5, large_arc=False, sweep=True)
        self.add_arc('e4-bottom', (20, 24), (13, 24), radius_x=4, radius_y=5, large_arc=False, sweep=True)
        self.add_contour('c0', *('e0', 'e1', 'e2'), closed=False)
        self.add_contour('c1', *('e3',), closed=False)
        self.add_contour('e4', *('e4-top', 'e4-bottom'), closed=True)
        self.relate('connect', *('c1', 'e4'))
