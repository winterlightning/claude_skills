"""Ship (transportation), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '8d5fe550-1dfa-4180-b3f3-18aa73106ce5'
SOURCE_PATH = 'icons-json/transportation/ship_8d5fe550-1dfa-4180-b3f3-18aa73106ce5.json'
AUTHOR = 'json_to_solo'

class Ship8d5fe550(Solo48):
    icon_id = 'ship-8d5fe550'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'transportation'
    aliases = ()
    keywords = ('ship', 'transportation')

    def build(self):
        self.add_line('e0', (39, 28), (9, 28))
        self.add_line('e1', (29, 39), (32, 37))
        self.add_line('e2', (13, 37), (9, 40))
        self.add_line('e3', (19, 28), (27, 27))
        self.add_arc('e4', (33, 37), (39, 28), radius_x=22, sweep=False)
        self.add_arc('e5', (9, 28), (13, 37), radius_x=16, sweep=False)
        self.add_line('e6-1', (13, 37), (17, 37))
        self.add_line('e6-2', (17, 37), (26, 40))
        self.add_line('e6-3', (26, 40), (29, 39))
        self.add_arc('e7', (9, 40), (4, 40), radius_x=20, sweep=False)
        self.add_line('e8-1', (32, 37), (36, 37))
        self.add_line('e8-2', (36, 37), (44, 40))
        self.add_arc('e9-1', (27, 27), (35, 22), radius_x=26, sweep=False)
        self.add_arc('e9-2', (35, 22), (36, 20), radius_x=2, sweep=False)
        self.add_arc('e9-3', (36, 20), (19, 8), radius_x=19, sweep=False)
        self.add_arc('e9-4', (19, 8), (19, 28), radius_x=34)
        self.add_contour('c0', 'e4', 'e0', 'e5')
        self.add_contour('c1', 'e6-1', 'e6-2', 'e6-3', 'e1')
        self.add_contour('c2', 'e2', 'e7')
        self.add_contour('c3', 'e8-1', 'e8-2')
        self.add_contour('c4', 'e3', 'e9-1', 'e9-2', 'e9-3', 'e9-4', closed=True)
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c4', 'c0')
