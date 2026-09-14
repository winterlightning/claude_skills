"""Pomeranian (pets), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '4413e747-cf76-4c47-8e61-cd932ec2a846'
SOURCE_PATH = 'icons-json/pets/pomeranian_4413e747-cf76-4c47-8e61-cd932ec2a846.json'
AUTHOR = 'json_to_solo'

class PomeranianPets(Solo48):
    icon_id = 'pomeranian-pets'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'pets'
    aliases = ()
    keywords = ('pomeranian', 'pets')

    def build(self):
        self.add_arc('e0-1', (4, 40), (7, 34), radius_x=12)
        self.add_line('e0-2', (7, 34), (11, 38))
        self.add_arc('e1', (37, 39), (41, 34), radius_x=27, sweep=False)
        self.add_arc('e2', (44, 40), (41, 34), radius_x=15, sweep=False)
        self.add_arc('e3-1', (7, 34), (4, 26), radius_x=14)
        self.add_line('e3-2', (4, 26), (5, 21))
        self.add_line('e3-3', (5, 21), (8, 16))
        self.add_arc('e3-4', (8, 16), (7, 11), radius_x=7)
        self.add_arc('e3-5', (7, 11), (9, 9), radius_x=4)
        self.add_arc('e3-6', (9, 9), (12, 8), radius_x=5)
        self.add_arc('e3-7', (12, 8), (17, 11), radius_x=6)
        self.add_arc('e3-8', (17, 11), (29, 11), radius_x=19)
        self.add_arc('e3-9', (29, 11), (31, 11), radius_x=2, sweep=False)
        self.add_arc('e3-10', (31, 11), (36, 8), radius_x=6)
        self.add_arc('e3-11', (36, 8), (39, 9), radius_x=5)
        self.add_arc('e3-12', (39, 9), (41, 12), radius_x=4)
        self.add_arc('e3-13', (41, 12), (40, 16), radius_x=7)
        self.add_line('e3-14', (40, 16), (43, 21))
        self.add_line('e3-15', (43, 21), (44, 26))
        self.add_arc('e3-16', (44, 26), (41, 34), radius_x=14)
        self.add_contour('c0', 'e0-1', 'e0-2')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2')
        self.add_contour('c3', 'e3-1', 'e3-2', 'e3-3', 'e3-4', 'e3-5', 'e3-6', 'e3-7', 'e3-8', 'e3-9', 'e3-10', 'e3-11', 'e3-12', 'e3-13', 'e3-14', 'e3-15', 'e3-16')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c1', 'c3')
        self.relate('connect', 'c2', 'c3')
        self.relate('connect', 'c3', 'c0')
