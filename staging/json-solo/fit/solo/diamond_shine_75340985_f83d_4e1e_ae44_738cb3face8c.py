"""Diamond shine (money), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '75340985-f83d-4e1e-ae44-738cb3face8c'
SOURCE_PATH = 'icons-json/money/diamond shine_75340985-f83d-4e1e-ae44-738cb3face8c.json'
AUTHOR = 'json_to_solo'

class DiamondShineMoney(Solo48):
    icon_id = 'diamond-shine-money'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'money'
    aliases = ()
    keywords = ('diamond', 'shine', 'money')

    def build(self):
        self.add_line('e0', (16, 34), (24, 44))
        self.add_line('e1', (32, 33), (24, 37))
        self.add_line('e2', (32, 33), (29, 37))
        self.add_line('e3', (29, 37), (24, 44))
        self.add_line('e4', (32, 33), (32, 11))
        self.add_line('e5', (16, 11), (16, 33))
        self.add_line('e6', (16, 33), (24, 37))
        self.add_line('e7', (24, 37), (24, 14))
        self.add_line('e8', (24, 14), (16, 11))
        self.add_line('e9', (16, 11), (24, 4))
        self.add_line('e10', (24, 4), (32, 11))
        self.add_line('e11', (32, 11), (24, 14))
        self.add_line('e12', (8, 13), (11, 17))
        self.add_line('e13', (37, 17), (40, 14))
        self.add_line('e14', (10, 34), (11, 31))
        self.add_line('e15', (37, 31), (38, 34))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2', 'e3')
        self.add_contour('c3', 'e4')
        self.add_contour('c4', 'e5', 'e6')
        self.add_contour('c5', 'e7')
        self.add_contour('c6', 'e8', 'e9', 'e10', 'e11', closed=True)
        self.add_contour('c7', 'e12')
        self.add_contour('c8', 'e13')
        self.add_contour('c9', 'e14')
        self.add_contour('c10', 'e15')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c1', 'c3')
        self.relate('connect', 'c2', 'c3')
        self.relate('connect', 'c1', 'c4')
        self.relate('connect', 'c1', 'c5')
        self.relate('connect', 'c4', 'c5')
        self.relate('connect', 'c5', 'c6')
