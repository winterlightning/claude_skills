"""Terrier (pets), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'f1950074-4cd5-5fc7-9ef0-4b5f76445f3a'
SOURCE_PATH = 'icons-json/pets/terrier_f1950074-4cd5-5fc7-9ef0-4b5f76445f3a.json'
AUTHOR = 'json_to_solo'

class Terrier(Solo48):
    icon_id = 'terrier'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'pets'
    aliases = ()
    keywords = ('terrier', 'pets')

    def build(self):
        self.add_line('e0', (24, 44), (24, 35))
        self.add_line('e1', (20, 26), (20, 21))
        self.add_line('e2', (28, 26), (28, 21))
        self.add_line('e3', (18, 13), (9, 4))
        self.add_line('e4', (39, 4), (30, 13))
        self.add_arc('e5', (30, 13), (18, 13), radius_x=27, sweep=False)
        self.add_line('e6-1', (9, 4), (8, 9))
        self.add_arc('e6-2', (8, 9), (12, 20), radius_x=21, sweep=False)
        self.add_arc('e6-3', (12, 20), (14, 33), radius_x=33, sweep=False)
        self.add_arc('e6-4', (14, 33), (24, 44), radius_x=13, sweep=False)
        self.add_line('e6-5', (24, 44), (29, 42))
        self.add_arc('e6-6', (29, 42), (34, 33), radius_x=36, sweep=False)
        self.add_arc('e6-7', (34, 33), (36, 20), radius_x=33, sweep=False)
        self.add_arc('e6-8', (36, 20), (40, 8), radius_x=20, sweep=False)
        self.add_arc('e6-9', (40, 8), (39, 4), radius_x=10, sweep=False)
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2')
        self.add_contour('c3', 'e5', 'e3', 'e6-1', 'e6-2', 'e6-3', 'e6-4', 'e6-5', 'e6-6', 'e6-7', 'e6-8', 'e6-9', 'e4', closed=True)
        self.relate('connect', 'c0', 'c3')
