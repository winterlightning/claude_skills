"""Drawer (office), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '69cdd7db-2798-4d20-afc9-176097689ca1'
SOURCE_PATH = 'icons-json/office/drawer_69cdd7db-2798-4d20-afc9-176097689ca1.json'
AUTHOR = 'json_to_solo'

class Drawer69cdd7db(Solo48):
    icon_id = 'drawer-69cdd7db'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'office'
    aliases = ()
    keywords = ('drawer', 'office')

    def build(self):
        self.add_line('e0', (8, 29), (14, 29))
        self.add_line('e1', (21, 34), (37, 34))
        self.add_line('e2', (42, 37), (42, 40))
        self.add_line('e3', (40, 42), (8, 42))
        self.add_line('e4', (6, 40), (6, 31))
        self.add_line('e5', (8, 29), (8, 8))
        self.add_line('e6', (10, 6), (17, 6))
        self.add_line('e7', (20, 7), (23, 9))
        self.add_line('e8', (26, 11), (38, 11))
        self.add_line('e9', (39, 13), (39, 34))
        self.add_line('e10', (14, 29), (21, 34))
        self.add_arc('e11-1', (37, 34), (42, 35), radius_x=4)
        self.add_arc('e11-2', (42, 35), (42, 37), radius_x=14, sweep=False)
        self.add_arc('e12', (42, 40), (40, 42), radius_x=2)
        self.add_arc('e13', (8, 42), (6, 40), radius_x=2)
        self.add_arc('e14', (6, 31), (8, 29), radius_x=2)
        self.add_line('e15', (8, 8), (10, 6))
        self.add_line('e16', (17, 6), (20, 7))
        self.add_arc('e17', (23, 9), (26, 11), radius_x=3, sweep=False)
        self.add_line('e18', (38, 11), (39, 13))
        self.add_contour('c0', 'e0', 'e10', 'e1', 'e11-1', 'e11-2', 'e2', 'e12', 'e3', 'e13', 'e4', 'e14')
        self.add_contour('c1', 'e5', 'e15', 'e6', 'e16', 'e7', 'e17', 'e8', 'e18', 'e9')
        self.relate('connect', 'c1', 'c0')
