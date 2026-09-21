"""Id (symbol), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '844a6cca-9183-43b4-8e32-4dbb2c81a21f'
SOURCE_PATH = 'icons-json/symbol/Id_844a6cca-9183-43b4-8e32-4dbb2c81a21f.json'
AUTHOR = 'json_to_solo'

class Id(Solo48):
    icon_id = 'id'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('id', 'symbol')

    def build(self):
        self.add_line('e0', (15, 8), (4, 8))
        self.add_line('e1', (9, 8), (9, 40))
        self.add_line('e2', (4, 40), (15, 40))
        self.add_line('e3', (44, 8), (44, 35))
        self.add_arc('e4-1', (44, 35), (41, 39), radius_x=6)
        self.add_line('e4-2', (41, 39), (36, 40))
        self.add_arc('e4-3', (36, 40), (31, 21), radius_x=11)
        self.add_arc('e4-4', (31, 21), (44, 23), radius_x=9)
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2')
        self.add_contour('c3', 'e3', 'e4-1', 'e4-2', 'e4-3', 'e4-4')
        self.relate('connect', 'c1', 'c0')
        self.relate('connect', 'c1', 'c2')
