"""Cog (interface-essential), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '4c6e5052-015f-4d2d-9e75-eb3bcb5b5dcf'
SOURCE_PATH = 'icons-json/interface-essential/cog_4c6e5052-015f-4d2d-9e75-eb3bcb5b5dcf.json'
AUTHOR = 'json_to_solo'

class Cog(Solo48):
    icon_id = 'cog'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('cog', 'interface-essential')

    def build(self):
        self.add_line('e0', (28, 6), (20, 6))
        self.add_line('e1', (20, 6), (20, 10))
        self.add_line('e2', (20, 10), (16, 12))
        self.add_line('e3', (16, 12), (13, 10))
        self.add_line('e4', (13, 10), (8, 16))
        self.add_line('e5', (8, 16), (11, 19))
        self.add_line('e6', (11, 19), (10, 23))
        self.add_line('e7', (10, 23), (6, 25))
        self.add_line('e8', (6, 25), (8, 32))
        self.add_line('e9', (8, 32), (12, 31))
        self.add_line('e10', (12, 31), (15, 35))
        self.add_line('e11', (15, 35), (13, 39))
        self.add_line('e12', (13, 39), (21, 42))
        self.add_line('e13', (21, 42), (22, 39))
        self.add_line('e14', (22, 39), (26, 39))
        self.add_line('e15', (26, 39), (27, 42))
        self.add_line('e16', (27, 42), (35, 39))
        self.add_line('e17', (35, 39), (33, 35))
        self.add_line('e18', (33, 35), (36, 31))
        self.add_line('e19', (36, 31), (40, 32))
        self.add_line('e20', (40, 32), (42, 25))
        self.add_line('e21', (42, 25), (38, 23))
        self.add_line('e22', (38, 23), (37, 19))
        self.add_line('e23', (37, 19), (40, 16))
        self.add_line('e24', (40, 16), (35, 10))
        self.add_line('e25', (35, 10), (32, 12))
        self.add_line('e26', (32, 12), (28, 10))
        self.add_line('e27', (28, 10), (28, 6))
        self.add_contour('c0', 'e0', 'e1', 'e2', 'e3', 'e4', 'e5', 'e6', 'e7', 'e8', 'e9', 'e10', 'e11', 'e12', 'e13', 'e14', 'e15', 'e16', 'e17', 'e18', 'e19', 'e20', 'e21', 'e22', 'e23', 'e24', 'e25', 'e26', 'e27', closed=True)
