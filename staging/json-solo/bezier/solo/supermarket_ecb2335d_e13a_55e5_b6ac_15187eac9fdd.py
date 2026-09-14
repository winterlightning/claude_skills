"""Supermarket (school-learning), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'ecb2335d-e13a-55e5-b6ac-15187eac9fdd'
SOURCE_PATH = 'icons-json/school-learning/supermarket_ecb2335d-e13a-55e5-b6ac-15187eac9fdd.json'
AUTHOR = 'json_to_solo'

class SupermarketSchoolLearning(Solo48):
    icon_id = 'supermarket-school-learning'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'school-learning'
    aliases = ()
    keywords = ('supermarket', 'school-learning')

    def build(self):
        self.add_line('e0', (28, 42), (28, 32))
        self.add_line('e1', (20, 35), (20, 42))
        self.add_line('e2', (34, 15), (14, 15))
        self.add_line('e3', (32, 15), (32, 24))
        self.add_line('e4', (32, 24), (42, 24))
        self.add_line('e5', (40, 24), (40, 42))
        self.add_line('e6', (40, 42), (8, 42))
        self.add_line('e7', (8, 42), (8, 24))
        self.add_line('e8', (6, 24), (16, 24))
        self.add_line('e9', (16, 24), (16, 15))
        self.add_line('e10', (24, 15), (24, 6))
        self.add_line('e11', (26, 7), (31, 7))
        self.add_bezier('e12', (28, 32), ((28, 28.703), (24.36, 26.332), (21.586, 28.68)), ((19.574, 30.382), (20, 32.627), (20, 35)))
        self.add_bezier('e13', (24, 6), ((24.548, 6.27), (25.452, 6.73), (26, 7)))
        self.add_contour('c0', 'e0', 'e12', 'e1')
        self.add_contour('c1', 'e2')
        self.add_contour('c2', 'e3', 'e4')
        self.add_contour('c3', 'e5', 'e6', 'e7')
        self.add_contour('c4', 'e8', 'e9')
        self.add_contour('c5', 'e10', 'e13', 'e11')
        self.relate('connect', 'c0', 'c3')
        self.relate('connect', 'c0', 'c3')
        self.relate('connect', 'c2', 'c1')
        self.relate('connect', 'c3', 'c2')
        self.relate('connect', 'c3', 'c4')
        self.relate('connect', 'c4', 'c1')
        self.relate('connect', 'c5', 'c1')
