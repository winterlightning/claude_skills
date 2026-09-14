"""Batch-05/earring (accessories), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'bdcf8f0c-b460-5564-8495-792c693562c8'
SOURCE_PATH = 'icons-json/accessories/batch-05/earring_bdcf8f0c-b460-5564-8495-792c693562c8.json'
AUTHOR = 'json_to_solo'

class Batch05Earring(Solo48):
    icon_id = 'batch-05-earring'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'accessories'
    aliases = ()
    keywords = ('batch', 'earring', 'accessories')

    def build(self):
        self.add_line('e0', (24, 15), (24, 19))
        self.add_arc('e1-1', (13, 10), (15, 6), radius_x=3)
        self.add_line('e1-2', (15, 6), (23, 4))
        self.add_line('e1-3', (23, 4), (30, 5))
        self.add_arc('e1-4', (30, 5), (33, 7), radius_x=10)
        self.add_arc('e1-5', (33, 7), (33, 12), radius_x=3)
        self.add_arc('e1-6', (33, 12), (24, 15), radius_x=16)
        self.add_line('e2-1', (24, 19), (33, 26))
        self.add_arc('e2-2', (33, 26), (40, 36), radius_x=14)
        self.add_arc('e2-3', (40, 36), (36, 41), radius_x=6)
        self.add_arc('e2-4', (36, 41), (25, 44), radius_x=22)
        self.add_line('e2-5', (25, 44), (14, 42))
        self.add_arc('e2-6', (14, 42), (9, 39), radius_x=12)
        self.add_line('e2-7', (9, 39), (8, 35))
        self.add_arc('e2-8', (8, 35), (15, 26), radius_x=15)
        self.add_arc('e2-9', (15, 26), (24, 19), radius_x=67)
        self.add_contour('c0', 'e1-1', 'e1-2', 'e1-3', 'e1-4', 'e1-5', 'e1-6', 'e0')
        self.add_contour('c1', 'e2-1', 'e2-2', 'e2-3', 'e2-4', 'e2-5', 'e2-6', 'e2-7', 'e2-8', 'e2-9', closed=True)
        self.relate('connect', 'c0', 'c1')
