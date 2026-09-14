"""Cashew (_uncategorized), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '80256a3b-3f6e-45e8-a830-db484f4197ff'
SOURCE_PATH = 'icons-json/_uncategorized_10/cashew_80256a3b-3f6e-45e8-a830-db484f4197ff.json'
AUTHOR = 'json_to_solo'

class CashewUncategorized(Solo48):
    icon_id = 'cashew-uncategorized'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = '_uncategorized'
    aliases = ()
    keywords = ('cashew', '_uncategorized')

    def build(self):
        self.add_arc('e0-1', (23, 25), (20, 26), radius_x=10)
        self.add_arc('e0-2', (20, 26), (12, 25), radius_x=14)
        self.add_arc('e0-3', (12, 25), (9, 26), radius_x=7, sweep=False)
        self.add_arc('e0-4', (9, 26), (6, 31), radius_x=6, sweep=False)
        self.add_arc('e0-5', (6, 31), (12, 40), radius_x=10, sweep=False)
        self.add_arc('e0-6', (12, 40), (20, 42), radius_x=18, sweep=False)
        self.add_arc('e0-7', (20, 42), (42, 20), radius_x=22, sweep=False)
        self.add_line('e0-8', (42, 20), (40, 11))
        self.add_arc('e0-9', (40, 11), (32, 6), radius_x=9, sweep=False)
        self.add_arc('e0-10', (32, 6), (26, 10), radius_x=7, sweep=False)
        self.add_line('e0-11', (26, 10), (26, 21))
        self.add_arc('e0-12', (26, 21), (23, 25), radius_x=8)
        self.add_contour('c0', 'e0-1', 'e0-2', 'e0-3', 'e0-4', 'e0-5', 'e0-6', 'e0-7', 'e0-8', 'e0-9', 'e0-10', 'e0-11', 'e0-12', closed=True)
