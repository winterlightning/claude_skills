"""Bread (symbol), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '8ddeed7d-559d-4b14-9b46-092f255cb54a'
SOURCE_PATH = 'icons-json/symbol/bread_8ddeed7d-559d-4b14-9b46-092f255cb54a.json'
AUTHOR = 'json_to_solo'

class BreadSymbol(Solo48):
    icon_id = 'bread-symbol'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('bread', 'symbol')

    def build(self):
        self.add_line('e0', (39, 18), (41, 17))
        self.add_line('e1', (33, 6), (18, 6))
        self.add_line('e2', (8, 17), (9, 18))
        self.add_line('e3', (9, 18), (9, 42))
        self.add_line('e4', (9, 42), (11, 42))
        self.add_line('e5', (11, 42), (34, 42))
        self.add_line('e6', (34, 42), (39, 42))
        self.add_line('e7', (39, 42), (39, 18))
        self.add_line('e8-1', (41, 17), (42, 13))
        self.add_arc('e8-2', (42, 13), (34, 6), radius_x=9, sweep=False)
        self.add_line('e8-3', (34, 6), (33, 6))
        self.add_line('e9-1', (18, 6), (11, 7))
        self.add_arc('e9-2', (11, 7), (6, 13), radius_x=7, sweep=False)
        self.add_line('e9-3', (6, 13), (8, 17))
        self.add_contour('c0', 'e0', 'e8-1', 'e8-2', 'e8-3', 'e1', 'e9-1', 'e9-2', 'e9-3', 'e2', 'e3', 'e4', 'e5', 'e6', 'e7', closed=True)
