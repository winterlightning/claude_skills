"""Nagras (money), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '84618b8f-5dee-4f44-9380-893ba067f0b2'
SOURCE_PATH = 'icons-json/money/nagras_84618b8f-5dee-4f44-9380-893ba067f0b2.json'
AUTHOR = 'json_to_solo'

class Nagras84618b8f(Solo48):
    icon_id = 'nagras-84618b8f'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'money'
    aliases = ()
    keywords = ('nagras', 'money')

    def build(self):
        self.add_line('e0', (8, 23), (13, 23))
        self.add_line('e1', (13, 23), (13, 44))
        self.add_line('e2', (13, 23), (24, 23))
        self.add_line('e3', (24, 23), (28, 30))
        self.add_line('e4', (28, 30), (8, 30))
        self.add_line('e5', (13, 23), (13, 4))
        self.add_line('e6', (13, 4), (24, 23))
        self.add_line('e7', (24, 23), (35, 23))
        self.add_line('e8', (40, 30), (35, 30))
        self.add_line('e9', (35, 30), (35, 23))
        self.add_line('e10', (35, 23), (40, 23))
        self.add_line('e11', (35, 23), (35, 4))
        self.add_line('e12', (35, 44), (28, 30))
        self.add_line('e13', (28, 30), (35, 30))
        self.add_line('e14', (35, 30), (35, 44))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2', 'e3', 'e4')
        self.add_contour('c3', 'e5', 'e6', 'e7')
        self.add_contour('c4', 'e8', 'e9')
        self.add_contour('c5', 'e10')
        self.add_contour('c6', 'e11')
        self.add_contour('c7', 'e12', 'e13', 'e14', closed=True)
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c0', 'c3')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c1', 'c3')
        self.relate('connect', 'c2', 'c3')
        self.relate('connect', 'c2', 'c3')
        self.relate('connect', 'c2', 'c7')
        self.relate('connect', 'c3', 'c4')
        self.relate('connect', 'c3', 'c5')
        self.relate('connect', 'c3', 'c6')
        self.relate('connect', 'c4', 'c5')
        self.relate('connect', 'c4', 'c6')
        self.relate('connect', 'c5', 'c6')
        self.relate('connect', 'c4', 'c7')
