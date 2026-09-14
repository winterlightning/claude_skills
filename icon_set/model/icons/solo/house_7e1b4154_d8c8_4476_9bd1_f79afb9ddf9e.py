"""House (interface-essential), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '7e1b4154-d8c8-4476-9bd1-f79afb9ddf9e'
SOURCE_PATH = 'icons-json/interface-essential/house_7e1b4154-d8c8-4476-9bd1-f79afb9ddf9e.json'
AUTHOR = 'json_to_solo'

class House7e1b4154(Solo48):
    icon_id = 'house-7e1b4154'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('house', 'interface-essential')

    def build(self):
        self.add_line('e0', (6, 25), (10, 21))
        self.add_line('e1', (42, 24), (39, 21))
        self.add_line('e2', (20, 34), (20, 42))
        self.add_line('e3', (20, 42), (13, 42))
        self.add_line('e4', (10, 38), (10, 21))
        self.add_line('e5', (10, 21), (24, 6))
        self.add_line('e6', (24, 6), (39, 21))
        self.add_line('e7', (39, 21), (39, 39))
        self.add_line('e8', (37, 42), (29, 42))
        self.add_line('e9', (29, 42), (29, 33))
        self.add_arc('e10-1', (29, 33), (23, 29), radius_x=5, sweep=False)
        self.add_arc('e10-2', (23, 29), (20, 34), radius_x=4, sweep=False)
        self.add_arc('e11', (13, 42), (10, 38), radius_x=4)
        self.add_arc('e12', (39, 39), (37, 42), radius_x=3)
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e10-1', 'e10-2', 'e2', 'e3', 'e11', 'e4', 'e5', 'e6', 'e7', 'e12', 'e8', 'e9', closed=True)
        self.relate('connect', 'c0', 'c2')
