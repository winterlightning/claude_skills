"""Shredder (office), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '30f4b322-da9b-44a5-9a9b-6fc5c8dfef67'
SOURCE_PATH = 'icons-json/office/shredder_30f4b322-da9b-44a5-9a9b-6fc5c8dfef67.json'
AUTHOR = 'json_to_solo'

class ShredderOffice(Solo48):
    icon_id = 'shredder-office'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'office'
    aliases = ()
    keywords = ('shredder', 'office')

    def build(self):
        self.add_line('e0', (9, 35), (6, 35))
        self.add_line('e1', (4, 33), (4, 24))
        self.add_line('e2', (6, 22), (12, 22))
        self.add_line('e3', (39, 35), (42, 35))
        self.add_line('e4', (44, 33), (44, 24))
        self.add_line('e5', (42, 22), (36, 22))
        self.add_line('e6', (12, 22), (12, 10))
        self.add_line('e7', (14, 8), (31, 8))
        self.add_line('e8', (32, 8), (35, 12))
        self.add_line('e9', (36, 13), (36, 22))
        self.add_line('e10', (12, 22), (36, 22))
        self.add_line('e11', (18, 40), (18, 28))
        self.add_line('e12', (30, 40), (30, 29))
        self.add_arc('e13', (6, 35), (4, 33), radius_x=3)
        self.add_arc('e14', (4, 24), (6, 22), radius_x=3)
        self.add_arc('e15', (42, 35), (44, 33), radius_x=3, sweep=False)
        self.add_arc('e16', (44, 24), (42, 22), radius_x=3, sweep=False)
        self.add_arc('e17', (12, 10), (14, 8), radius_x=3)
        self.add_line('e18', (31, 8), (32, 8))
        self.add_arc('e19', (35, 12), (36, 13), radius_x=7, sweep=False)
        self.add_contour('c0', 'e0', 'e13', 'e1', 'e14', 'e2')
        self.add_contour('c1', 'e3', 'e15', 'e4', 'e16', 'e5')
        self.add_contour('c2', 'e6', 'e17', 'e7', 'e18', 'e8', 'e19', 'e9')
        self.add_contour('c3', 'e10')
        self.add_contour('c4', 'e11')
        self.add_contour('c5', 'e12')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c0', 'c3')
        self.relate('connect', 'c2', 'c3')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c1', 'c3')
        self.relate('connect', 'c2', 'c3')
