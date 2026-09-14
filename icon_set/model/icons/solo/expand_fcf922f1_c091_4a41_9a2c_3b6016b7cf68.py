"""Expand (interface-essential), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'fcf922f1-c091-4a41-9a2c-3b6016b7cf68'
SOURCE_PATH = 'icons-json/interface-essential/expand_fcf922f1-c091-4a41-9a2c-3b6016b7cf68.json'
AUTHOR = 'gpt-6'

class Expand(Solo48):
    icon_id = 'expand'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('expand', 'interface-essential')

    def build(self) -> None:
        # Symbol plan: preserve the subject, contour topology and curve types.
        # Rebalance whole parts on the SOLO48 integer grid; keep real shared contacts.
        self.add_line('e0', (4, 17), (4, 9))
        self.add_line('e1', (5, 8), (15, 8))
        self.add_line('e2', (33, 8), (43, 8))
        self.add_line('e3', (44, 10), (44, 17))
        self.add_line('e4', (4, 31), (4, 39))
        self.add_line('e5', (6, 40), (15, 40))
        self.add_line('e6', (33, 40), (42, 40))
        self.add_line('e7', (44, 38), (44, 31))
        self.add_line('e8', (35, 31), (13, 31))
        self.add_line('e9', (12, 29), (12, 19))
        self.add_line('e10', (14, 17), (35, 17))
        self.add_line('e11', (36, 19), (36, 30))
        self.add_arc('e12', (4, 9), (5, 8), radius_x=1, radius_y=1, large_arc=False, sweep=True)
        self.add_arc('e13', (43, 8), (44, 10), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('e14', (4, 39), (6, 40))
        self.add_arc('e15', (42, 40), (44, 38), radius_x=2, radius_y=2, large_arc=False, sweep=False)
        self.add_line('e16', (13, 31), (12, 29))
        self.add_arc('e17', (12, 19), (14, 17), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('e18', (35, 17), (36, 19))
        self.add_line('e19', (36, 30), (35, 31))
        self.add_contour('c0', *('e0', 'e12', 'e1'), closed=False)
        self.add_contour('c1', *('e2', 'e13', 'e3'), closed=False)
        self.add_contour('c2', *('e4', 'e14', 'e5'), closed=False)
        self.add_contour('c3', *('e6', 'e15', 'e7'), closed=False)
        self.add_contour('c4', *('e8', 'e16', 'e9', 'e17', 'e10', 'e18', 'e11', 'e19'), closed=True)
