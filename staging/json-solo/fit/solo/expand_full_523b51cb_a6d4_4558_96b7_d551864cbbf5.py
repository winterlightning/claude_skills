"""Expand full (interface-essential), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '523b51cb-a6d4-4558-96b7-d551864cbbf5'
SOURCE_PATH = 'icons-json/interface-essential/expand full_523b51cb-a6d4-4558-96b7-d551864cbbf5.json'
AUTHOR = 'json_to_solo'

class ExpandFullInterfaceEssential(Solo48):
    icon_id = 'expand-full-interface-essential'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('expand', 'full', 'interface-essential')

    def build(self):
        self.add_line('e0', (6, 14), (6, 8))
        self.add_line('e1', (8, 6), (14, 6))
        self.add_line('e2', (34, 6), (40, 6))
        self.add_line('e3', (42, 8), (42, 14))
        self.add_line('e4', (6, 35), (6, 40))
        self.add_line('e5', (8, 42), (14, 42))
        self.add_line('e6', (34, 42), (40, 42))
        self.add_line('e7', (42, 40), (42, 35))
        self.add_line('e8', (31, 30), (16, 30))
        self.add_line('e9', (15, 28), (15, 20))
        self.add_line('e10', (17, 18), (31, 18))
        self.add_line('e11', (33, 20), (33, 28))
        self.add_arc('e12', (6, 8), (8, 6), radius_x=2)
        self.add_arc('e13', (40, 6), (42, 8), radius_x=2)
        self.add_arc('e14', (6, 40), (8, 42), radius_x=2, sweep=False)
        self.add_arc('e15', (40, 42), (42, 40), radius_x=2, sweep=False)
        self.add_line('e16', (16, 30), (15, 28))
        self.add_line('e17', (15, 20), (17, 18))
        self.add_line('e18', (31, 18), (33, 20))
        self.add_line('e19', (33, 28), (31, 30))
        self.add_contour('c0', 'e0', 'e12', 'e1')
        self.add_contour('c1', 'e2', 'e13', 'e3')
        self.add_contour('c2', 'e4', 'e14', 'e5')
        self.add_contour('c3', 'e6', 'e15', 'e7')
        self.add_contour('c4', 'e8', 'e16', 'e9', 'e17', 'e10', 'e18', 'e11', 'e19', closed=True)
