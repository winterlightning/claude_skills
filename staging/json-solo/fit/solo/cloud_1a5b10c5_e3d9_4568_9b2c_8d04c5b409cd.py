"""Cloud (internet), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '1a5b10c5-e3d9-4568-9b2c-8d04c5b409cd'
SOURCE_PATH = 'icons-json/internet/cloud_1a5b10c5-e3d9-4568-9b2c-8d04c5b409cd.json'
AUTHOR = 'json_to_solo'

class Cloud1a5b10c5(Solo48):
    icon_id = 'cloud-1a5b10c5'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'internet'
    aliases = ()
    keywords = ('cloud', 'internet')

    def build(self):
        self.add_line('e0', (11, 40), (36, 40))
        self.add_arc('e1-1', (36, 40), (43, 35), radius_x=9, sweep=False)
        self.add_line('e1-2', (43, 35), (44, 30))
        self.add_line('e1-3', (44, 30), (43, 25))
        self.add_arc('e1-4', (43, 25), (37, 20), radius_x=8, sweep=False)
        self.add_line('e1-5', (37, 20), (33, 13))
        self.add_arc('e1-6', (33, 13), (25, 8), radius_x=11, sweep=False)
        self.add_line('e1-7', (25, 8), (24, 8))
        self.add_line('e1-8', (24, 8), (23, 8))
        self.add_arc('e1-9', (23, 8), (14, 14), radius_x=13, sweep=False)
        self.add_line('e1-10', (14, 14), (11, 20))
        self.add_arc('e1-11', (11, 20), (5, 25), radius_x=9, sweep=False)
        self.add_line('e1-12', (5, 25), (4, 30))
        self.add_line('e1-13', (4, 30), (5, 35))
        self.add_arc('e1-14', (5, 35), (11, 40), radius_x=8, sweep=False)
        self.add_contour('c0', 'e0', 'e1-1', 'e1-2', 'e1-3', 'e1-4', 'e1-5', 'e1-6', 'e1-7', 'e1-8', 'e1-9', 'e1-10', 'e1-11', 'e1-12', 'e1-13', 'e1-14', closed=True)
