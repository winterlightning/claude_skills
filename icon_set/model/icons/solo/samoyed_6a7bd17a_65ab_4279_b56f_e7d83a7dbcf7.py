"""Samoyed (pets), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '6a7bd17a-65ab-4279-b56f-e7d83a7dbcf7'
SOURCE_PATH = 'icons-json/pets/samoyed_6a7bd17a-65ab-4279-b56f-e7d83a7dbcf7.json'
AUTHOR = 'json_to_solo'

class Samoyed(Solo48):
    icon_id = 'samoyed'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'pets'
    aliases = ()
    keywords = ('samoyed', 'pets')

    def build(self):
        self.add_arc('e0', (4, 40), (7, 33), radius_x=17)
        self.add_arc('e1', (11, 38), (7, 33), radius_x=24)
        self.add_arc('e2', (37, 38), (41, 33), radius_x=24, sweep=False)
        self.add_arc('e3', (44, 40), (41, 33), radius_x=13, sweep=False)
        self.add_arc('e4-1', (7, 33), (5, 22), radius_x=15)
        self.add_arc('e4-2', (5, 22), (8, 16), radius_x=15)
        self.add_line('e4-3', (8, 16), (7, 12))
        self.add_arc('e4-4', (7, 12), (11, 8), radius_x=4)
        self.add_arc('e4-5', (11, 8), (17, 11), radius_x=9)
        self.add_arc('e4-6', (17, 11), (31, 11), radius_x=25)
        self.add_arc('e4-7', (31, 11), (37, 8), radius_x=8)
        self.add_arc('e4-8', (37, 8), (41, 12), radius_x=4)
        self.add_line('e4-9', (41, 12), (40, 16))
        self.add_arc('e4-10', (40, 16), (43, 22), radius_x=15)
        self.add_arc('e4-11', (43, 22), (41, 33), radius_x=15)
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2')
        self.add_contour('c3', 'e3')
        self.add_contour('c4', 'e4-1', 'e4-2', 'e4-3', 'e4-4', 'e4-5', 'e4-6', 'e4-7', 'e4-8', 'e4-9', 'e4-10', 'e4-11')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c4')
        self.relate('connect', 'c1', 'c4')
        self.relate('connect', 'c2', 'c3')
        self.relate('connect', 'c2', 'c4')
        self.relate('connect', 'c3', 'c4')
