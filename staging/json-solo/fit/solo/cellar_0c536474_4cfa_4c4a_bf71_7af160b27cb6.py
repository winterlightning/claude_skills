"""Cellar (building), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '0c536474-4cfa-4c4a-bf71-7af160b27cb6'
SOURCE_PATH = 'icons-json/building/cellar_0c536474-4cfa-4c4a-bf71-7af160b27cb6.json'
AUTHOR = 'json_to_solo'

class CellarBuilding(Solo48):
    icon_id = 'cellar-building'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'building'
    aliases = ()
    keywords = ('cellar', 'building')

    def build(self):
        self.add_line('e0', (24, 6), (24, 42))
        self.add_line('e1', (42, 42), (42, 22))
        self.add_line('e2', (6, 22), (6, 42))
        self.add_line('e3', (6, 42), (42, 42))
        self.add_arc('e4', (15, 26), (15, 27), radius_x=32, sweep=False)
        self.add_arc('e5', (31, 26), (31, 27), radius_x=28, sweep=False)
        self.add_arc('e6-1', (42, 22), (38, 12), radius_x=16, sweep=False)
        self.add_arc('e6-2', (38, 12), (30, 7), radius_x=19, sweep=False)
        self.add_line('e6-3', (30, 7), (24, 6))
        self.add_arc('e6-4', (24, 6), (7, 17), radius_x=19, sweep=False)
        self.add_line('e6-5', (7, 17), (6, 22))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e4')
        self.add_contour('c2', 'e5')
        self.add_contour('c3', 'e1', 'e6-1', 'e6-2', 'e6-3', 'e6-4', 'e6-5', 'e2', 'e3', closed=True)
        self.relate('connect', 'c0', 'c3')
        self.relate('connect', 'c0', 'c3')
