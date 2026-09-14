"""Graduation cap (symbol), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e5ae7651-62d6-4c05-b34e-faf818f521bc'
SOURCE_PATH = 'icons-json/symbol/graduation cap_e5ae7651-62d6-4c05-b34e-faf818f521bc.json'
AUTHOR = 'json_to_solo'

class GraduationCapE5ae7651(Solo48):
    icon_id = 'graduation-cap-e5ae7651'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('graduation', 'cap', 'symbol')

    def build(self):
        self.add_line('e0', (38, 21), (38, 33))
        self.add_line('e1', (10, 35), (10, 21))
        self.add_line('e2', (38, 21), (25, 27))
        self.add_line('e3', (23, 27), (10, 21))
        self.add_line('e4', (38, 21), (44, 18))
        self.add_line('e5', (44, 18), (24, 8))
        self.add_line('e6', (23, 8), (4, 18))
        self.add_line('e7', (4, 18), (10, 21))
        self.add_bezier('e8', (38, 33), ((38, 34.86), (36.373, 35.83), (35.064, 36.69)), ((32.036, 38.68), (28.245, 39.99), (24.7, 39.99)), ((24.521, 39.99), (24.351, 40), (24.172, 40)), ((24.169, 40), (24.166, 40), (24.164, 40)), ((23.991, 40), (23.809, 39.99), (23.636, 39.99)), ((18.8, 39.99), (13.945, 37.91), (10, 35)))
        self.add_bezier('e9', (25, 27), ((24.345, 27.06), (23.655, 27.06), (23, 27)))
        self.add_bezier('e10', (24, 8), ((23.7, 8), (23.3, 8), (23, 8)))
        self.add_contour('c0', 'e0', 'e8', 'e1')
        self.add_contour('c1', 'e2', 'e9', 'e3')
        self.add_contour('c2', 'e4', 'e5', 'e10', 'e6', 'e7')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
