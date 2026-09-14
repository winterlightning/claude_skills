"""Obstruction (transportation), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '77ce8c19-d748-4677-9097-15486e0a1c5b'
SOURCE_PATH = 'icons-json/transportation/obstruction_77ce8c19-d748-4677-9097-15486e0a1c5b.json'
AUTHOR = 'json_to_solo'

class Obstruction(Solo48):
    icon_id = 'obstruction'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'transportation'
    aliases = ()
    keywords = ('obstruction', 'transportation')

    def build(self):
        self.add_line('e0', (33, 27), (33, 40))
        self.add_line('e1', (31, 42), (17, 42))
        self.add_line('e2', (15, 40), (15, 27))
        self.add_line('e3', (33, 27), (26, 27))
        self.add_line('e4', (33, 27), (41, 27))
        self.add_line('e5', (42, 26), (42, 15))
        self.add_line('e6', (42, 15), (34, 15))
        self.add_line('e7', (33, 16), (29, 22))
        self.add_line('e8', (29, 22), (26, 27))
        self.add_line('e9', (15, 27), (26, 27))
        self.add_line('e10', (15, 27), (13, 27))
        self.add_line('e11', (13, 27), (21, 15))
        self.add_line('e12', (13, 27), (7, 27))
        self.add_line('e13', (6, 26), (6, 17))
        self.add_line('e14', (7, 15), (15, 15))
        self.add_line('e15', (21, 15), (33, 15))
        self.add_line('e16', (33, 15), (33, 8))
        self.add_line('e17', (31, 6), (17, 6))
        self.add_line('e18', (15, 8), (15, 15))
        self.add_line('e19', (21, 15), (15, 15))
        self.add_arc('e20', (33, 40), (31, 42), radius_x=2)
        self.add_arc('e21', (17, 42), (15, 40), radius_x=2)
        self.add_line('e22', (41, 27), (42, 26))
        self.add_arc('e23', (34, 15), (33, 16), radius_x=15, sweep=False)
        self.add_arc('e24', (7, 27), (6, 26), radius_x=1)
        self.add_line('e25', (6, 17), (7, 15))
        self.add_arc('e26', (33, 8), (31, 6), radius_x=2, sweep=False)
        self.add_arc('e27', (17, 6), (15, 8), radius_x=2, sweep=False)
        self.add_contour('c0', 'e0', 'e20', 'e1', 'e21', 'e2')
        self.add_contour('c1', 'e3')
        self.add_contour('c2', 'e4', 'e22', 'e5', 'e6', 'e23', 'e7', 'e8')
        self.add_contour('c3', 'e9')
        self.add_contour('c4', 'e10')
        self.add_contour('c5', 'e11')
        self.add_contour('c6', 'e12', 'e24', 'e13', 'e25', 'e14')
        self.add_contour('c7', 'e15', 'e16', 'e26', 'e17', 'e27', 'e18')
        self.add_contour('c8', 'e19')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c0', 'c3')
        self.relate('connect', 'c0', 'c4')
        self.relate('connect', 'c3', 'c4')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c1', 'c3')
        self.relate('connect', 'c2', 'c3')
        self.relate('connect', 'c4', 'c5')
        self.relate('connect', 'c4', 'c6')
        self.relate('connect', 'c5', 'c6')
        self.relate('connect', 'c5', 'c7')
        self.relate('connect', 'c5', 'c8')
        self.relate('connect', 'c7', 'c8')
        self.relate('connect', 'c6', 'c7')
        self.relate('connect', 'c6', 'c8')
        self.relate('connect', 'c7', 'c8')
