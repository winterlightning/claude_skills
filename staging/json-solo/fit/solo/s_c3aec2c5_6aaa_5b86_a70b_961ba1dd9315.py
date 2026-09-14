"""S (typeface), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'c3aec2c5-6aaa-5b86-a70b-961ba1dd9315'
SOURCE_PATH = 'icons-json/typeface/S_c3aec2c5-6aaa-5b86-a70b-961ba1dd9315.json'
AUTHOR = 'json_to_solo'

class SC3aec2c5(Solo48):
    icon_id = 's-c3aec2c5'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'typeface'
    aliases = ()
    keywords = ('s', 'typeface')

    def build(self):
        self.add_line('e0', (28, 24), (18, 21))
        self.add_line('e1', (34, 7), (39, 9))
        self.add_line('e2-1', (8, 39), (17, 43))
        self.add_arc('e2-2', (17, 43), (24, 44), radius_x=25, sweep=False)
        self.add_line('e2-3', (24, 44), (32, 43))
        self.add_line('e2-4', (32, 43), (36, 41))
        self.add_arc('e2-5', (36, 41), (39, 38), radius_x=10, sweep=False)
        self.add_line('e2-6', (39, 38), (40, 34))
        self.add_arc('e2-7', (40, 34), (28, 24), radius_x=13, sweep=False)
        self.add_arc('e3-1', (18, 21), (10, 16), radius_x=15)
        self.add_arc('e3-2', (10, 16), (13, 7), radius_x=7)
        self.add_arc('e3-3', (13, 7), (17, 5), radius_x=14)
        self.add_line('e3-4', (17, 5), (23, 4))
        self.add_arc('e3-5', (23, 4), (34, 7), radius_x=24)
        self.add_contour('c0', 'e2-1', 'e2-2', 'e2-3', 'e2-4', 'e2-5', 'e2-6', 'e2-7', 'e0', 'e3-1', 'e3-2', 'e3-3', 'e3-4', 'e3-5', 'e1')
