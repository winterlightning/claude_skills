"""Arrow square (combination), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '5daad2a0-1899-447f-a4db-7072ef776e5c'
SOURCE_PATH = 'icons-json/combination/arrow square_5daad2a0-1899-447f-a4db-7072ef776e5c.json'
AUTHOR = 'json_to_solo'

class ArrowSquare(Solo48):
    icon_id = 'arrow-square'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'combination'
    aliases = ()
    keywords = ('arrow', 'square', 'combination')

    def build(self):
        self.add_line('e0', (32, 4), (37, 9))
        self.add_line('e1', (8, 31), (8, 13))
        self.add_line('e2', (11, 9), (37, 9))
        self.add_line('e3', (32, 15), (37, 9))
        self.add_line('e4', (40, 17), (40, 35))
        self.add_line('e5', (37, 39), (11, 39))
        self.add_line('e6', (16, 33), (11, 39))
        self.add_line('e7', (16, 44), (11, 39))
        self.add_line('e8', (8, 13), (11, 9))
        self.add_line('e9', (40, 35), (37, 39))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1', 'e8', 'e2')
        self.add_contour('c2', 'e3')
        self.add_contour('c3', 'e4', 'e9', 'e5')
        self.add_contour('c4', 'e6')
        self.add_contour('c5', 'e7')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c3', 'c4')
        self.relate('connect', 'c3', 'c5')
        self.relate('connect', 'c4', 'c5')
