"""Dress (clothes), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '00ccbf9d-32e5-579a-8960-b7860777882d'
SOURCE_PATH = 'icons-json/clothes/dress_00ccbf9d-32e5-579a-8960-b7860777882d.json'
AUTHOR = 'json_to_solo'

class Dress(Solo48):
    icon_id = 'dress'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'clothes'
    aliases = ()
    keywords = ('dress', 'clothes')

    def build(self):
        self.add_line('e0', (32, 8), (33, 12))
        self.add_line('e1', (17, 19), (15, 13))
        self.add_line('e2', (15, 11), (16, 8))
        self.add_line('e3', (16, 8), (16, 4))
        self.add_line('e4', (32, 8), (24, 13))
        self.add_line('e5', (24, 13), (16, 8))
        self.add_line('e6', (32, 8), (32, 4))
        self.add_line('e7-1', (33, 12), (31, 20))
        self.add_line('e7-2', (31, 20), (40, 41))
        self.add_arc('e7-3', (40, 41), (25, 44), radius_x=39)
        self.add_line('e7-4', (25, 44), (15, 43))
        self.add_arc('e7-5', (15, 43), (8, 41), radius_x=51, sweep=False)
        self.add_line('e7-6', (8, 41), (17, 19))
        self.add_arc('e8', (15, 13), (15, 11), radius_x=4)
        self.add_contour('c0', 'e0', 'e7-1', 'e7-2', 'e7-3', 'e7-4', 'e7-5', 'e7-6', 'e1', 'e8', 'e2', 'e3')
        self.add_contour('c1', 'e4', 'e5')
        self.add_contour('c2', 'e6')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
