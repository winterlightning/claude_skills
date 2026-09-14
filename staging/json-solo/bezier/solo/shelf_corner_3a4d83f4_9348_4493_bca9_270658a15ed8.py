"""Shelf corner (office), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '3a4d83f4-9348-4493-bca9-270658a15ed8'
SOURCE_PATH = 'icons-json/office/shelf corner_3a4d83f4-9348-4493-bca9-270658a15ed8.json'
AUTHOR = 'json_to_solo'

class ShelfCornerOffice(Solo48):
    icon_id = 'shelf-corner-office'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'office'
    aliases = ()
    keywords = ('shelf', 'corner', 'office')

    def build(self):
        self.add_line('e0', (8, 4), (8, 9))
        self.add_line('e1', (8, 44), (8, 39))
        self.add_line('e2', (40, 44), (40, 39))
        self.add_line('e3', (40, 4), (40, 9))
        self.add_line('e4', (8, 29), (40, 29))
        self.add_line('e5', (8, 29), (8, 39))
        self.add_line('e6', (8, 29), (8, 19))
        self.add_line('e7', (40, 29), (40, 39))
        self.add_line('e8', (40, 29), (40, 19))
        self.add_line('e9', (8, 39), (40, 39))
        self.add_line('e10', (8, 19), (40, 19))
        self.add_line('e11', (8, 19), (8, 9))
        self.add_line('e12', (40, 19), (40, 9))
        self.add_line('e13', (8, 9), (40, 9))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2')
        self.add_contour('c3', 'e3')
        self.add_contour('c4', 'e4')
        self.add_contour('c5', 'e5')
        self.add_contour('c6', 'e6')
        self.add_contour('c7', 'e7')
        self.add_contour('c8', 'e8')
        self.add_contour('c9', 'e9')
        self.add_contour('c10', 'e10')
        self.add_contour('c11', 'e11')
        self.add_contour('c12', 'e12')
        self.add_contour('c13', 'e13')
        self.relate('connect', 'c0', 'c11')
        self.relate('connect', 'c0', 'c13')
        self.relate('connect', 'c11', 'c13')
        self.relate('connect', 'c1', 'c5')
        self.relate('connect', 'c1', 'c9')
        self.relate('connect', 'c5', 'c9')
        self.relate('connect', 'c2', 'c7')
        self.relate('connect', 'c2', 'c9')
        self.relate('connect', 'c7', 'c9')
        self.relate('connect', 'c12', 'c13')
        self.relate('connect', 'c12', 'c3')
        self.relate('connect', 'c13', 'c3')
        self.relate('connect', 'c4', 'c5')
        self.relate('connect', 'c4', 'c6')
        self.relate('connect', 'c5', 'c6')
        self.relate('connect', 'c4', 'c7')
        self.relate('connect', 'c4', 'c8')
        self.relate('connect', 'c7', 'c8')
        self.relate('connect', 'c10', 'c11')
        self.relate('connect', 'c10', 'c6')
        self.relate('connect', 'c11', 'c6')
        self.relate('connect', 'c10', 'c12')
        self.relate('connect', 'c10', 'c8')
        self.relate('connect', 'c12', 'c8')
