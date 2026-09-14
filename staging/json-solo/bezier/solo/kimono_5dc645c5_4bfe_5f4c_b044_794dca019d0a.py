"""Kimono (sports), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '5dc645c5-4bfe-5f4c-b044-794dca019d0a'
SOURCE_PATH = 'icons-json/sports/kimono_5dc645c5-4bfe-5f4c-b044-794dca019d0a.json'
AUTHOR = 'json_to_solo'

class KimonoSports(Solo48):
    icon_id = 'kimono-sports'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'sports'
    aliases = ()
    keywords = ('kimono', 'sports')

    def build(self):
        self.add_line('e0', (33, 28), (15, 28))
        self.add_line('e1', (26, 35), (24, 28))
        self.add_line('e2', (19, 35), (30, 6))
        self.add_line('e3', (30, 6), (42, 16))
        self.add_line('e4', (42, 16), (38, 22))
        self.add_line('e5', (38, 22), (33, 17))
        self.add_line('e6', (33, 17), (33, 25))
        self.add_line('e7', (33, 25), (33, 29))
        self.add_line('e8', (33, 29), (35, 42))
        self.add_line('e9', (35, 42), (13, 42))
        self.add_line('e10', (13, 42), (14, 31))
        self.add_line('e11', (14, 31), (15, 26))
        self.add_line('e12', (15, 26), (15, 18))
        self.add_line('e13', (15, 18), (11, 22))
        self.add_line('e14', (11, 22), (6, 16))
        self.add_line('e15', (6, 16), (18, 6))
        self.add_line('e16', (30, 6), (18, 6))
        self.add_line('e17', (24, 22), (18, 6))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2')
        self.add_contour('c3', 'e3', 'e4', 'e5', 'e6', 'e7', 'e8', 'e9', 'e10', 'e11', 'e12', 'e13', 'e14', 'e15')
        self.add_contour('c4', 'e16')
        self.add_contour('c5', 'e17')
        self.relate('connect', 'c2', 'c3')
        self.relate('connect', 'c2', 'c4')
        self.relate('connect', 'c3', 'c4')
        self.relate('connect', 'c3', 'c4')
        self.relate('connect', 'c3', 'c5')
        self.relate('connect', 'c4', 'c5')
        self.relate('connect', 'c0', 'c3')
        self.relate('connect', 'c0', 'c3')
        self.relate('connect', 'c1', 'c0')
        self.relate('connect', 'c5', 'c2')
