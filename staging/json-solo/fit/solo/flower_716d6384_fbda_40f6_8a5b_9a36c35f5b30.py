"""Flower (nature), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '716d6384-fbda-40f6-8a5b-9a36c35f5b30'
SOURCE_PATH = 'icons-json/nature/flower_716d6384-fbda-40f6-8a5b-9a36c35f5b30.json'
AUTHOR = 'json_to_solo'

class Flower716d6384(Solo48):
    icon_id = 'flower-716d6384'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'nature'
    aliases = ()
    keywords = ('flower', 'nature')

    def build(self):
        self.add_line('e0', (31, 11), (33, 15))
        self.add_arc('e1-top', (19, 25), (29, 25), radius_x=5, radius_y=4)
        self.add_arc('e1-bottom', (29, 25), (19, 25), radius_x=5, radius_y=4)
        self.add_arc('e2-1', (33, 15), (44, 22), radius_x=8)
        self.add_arc('e2-2', (44, 22), (39, 29), radius_x=9)
        self.add_arc('e2-3', (39, 29), (39, 36), radius_x=7)
        self.add_arc('e2-4', (39, 36), (35, 39), radius_x=8)
        self.add_arc('e2-5', (35, 39), (31, 40), radius_x=9)
        self.add_arc('e2-6', (31, 40), (25, 38), radius_x=10)
        self.add_arc('e2-7', (25, 38), (24, 37), radius_x=5)
        self.add_arc('e2-8', (24, 37), (17, 40), radius_x=10)
        self.add_line('e2-9', (17, 40), (12, 39))
        self.add_line('e2-10', (12, 39), (10, 37))
        self.add_arc('e2-11', (10, 37), (9, 29), radius_x=7)
        self.add_arc('e2-12', (9, 29), (4, 22), radius_x=9)
        self.add_line('e2-13', (4, 22), (6, 17))
        self.add_arc('e2-14', (6, 17), (15, 15), radius_x=9)
        self.add_arc('e2-15', (15, 15), (18, 10), radius_x=9)
        self.add_line('e2-16', (18, 10), (24, 8))
        self.add_arc('e2-17', (24, 8), (31, 11), radius_x=10)
        self.add_contour('c0', 'e0', 'e2-1', 'e2-2', 'e2-3', 'e2-4', 'e2-5', 'e2-6', 'e2-7', 'e2-8', 'e2-9', 'e2-10', 'e2-11', 'e2-12', 'e2-13', 'e2-14', 'e2-15', 'e2-16', 'e2-17', closed=True)
        self.add_contour('e1', 'e1-top', 'e1-bottom', closed=True)
